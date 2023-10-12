import os
from datetime import datetime

import requests
from django.core.exceptions import ObjectDoesNotExist

from habits.models import Habit
from users.models import Users

TELEGRAM_TOKEN = os.getenv('TOKEN_TELEGRAM_BOT')


def habit_scheduler() -> None:
    '''check time / day for habit and send notification to user'''
    current_time = datetime.now()
    for habit in Habit.object.filter(is_pleasant=False):
        print(habit)
        # DAILY HABIT
        if habit.frequency == "DAYLI":
            if habit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                print(f'HABBIT INFORMATION: {habit}')
                chat_id = habit.owner.chat_id
                if habit.award:
                    message = (f"ACTION: {habit.action}\n"
                               f"PLACE: {habit.place}\n"
                               f"YOUR AWARD: {habit.award}\n"
                               f"DURATION: {habit.duration}")
                else:
                    message = (f"ACTION: {habit.action}\n"
                               f"PLACE: {habit.place}\n"
                               f"MAKE PLEASANT HABIT: {habit.link_pleasant.action}\n"
                               f"DURATION: {habit.duration}")
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                print(url)
                requests.get(url)
        # WEEK DAY HABIT
        else:
            today = ''
            # check current day
            if datetime.today().weekday() == 0:
                today = "MONDAY"
            elif datetime.today().weekday() == 1:
                today = "TUESDAY"
            elif datetime.today().weekday() == 2:
                today = "WEDNESDAY"
            elif datetime.today().weekday() == 3:
                today = "THURSDAY"
            elif datetime.today().weekday() == 4:
                today = "FRIDAY"
            elif datetime.today().weekday() == 5:
                today = "SATURDAY"
            elif datetime.today().weekday() == 6:
                today = "SUNDAY"

            if habit.frequency == today:
                if habit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                    print(f'HABIT INFORMATION: {habit}')
                    chat_id = habit.owner.chat_id
                    if habit.award:
                        message = (
                            f"ACTION: {habit.action}\n"
                            f"PLACE: {habit.place}\n"
                            f"YOUR AWARD: {habit.award}\n"
                            f"DURATION: "
                            f"{habit.duration}")
                    else:
                        message = (f"ACTION: {habit.action}\n"
                                   f"PLACE: {habit.place}\n"
                                   f"MAKE PLEASANT HABIT:"
                                   f" {habit.link_pleasant.action}\n"
                                   f"DURATION: {habit.duration}")

                    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                    print(url)
                    requests.get(url)


def telegram_check_updates() -> None:
    """ get information from telegram bot and add user telegram id to base"""
    url_get_updates = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates'
    response = requests.get(url_get_updates)
    print(response)
    print("200")
    if response.status_code == 200:
        for telegram_users in response.json()['result']:
            telegram_user_chat_id = telegram_users['message']['from']['id']
            telegram_user_name = telegram_users['message']['from']['usermane']

            try:
                user = Users.objects.get(telegram_user_name=telegram_user_name)
                if user.chat_id is None:
                    user.chat_id = telegram_user_chat_id
                    user.save()
            except ObjectDoesNotExist:
                print('No user in the bases')
