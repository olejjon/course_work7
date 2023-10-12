from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ serializer for habit and validation"""

    def create(self, validated_data):
        new_habit = Habit.objects.create(**validated_data)
        # check duration
        if new_habit.duration > 120:
            raise serializers.ValidationError("Duration greater than 120 second!")
        # check usual habit
        if new_habit.is_pleasant is False:
            if not new_habit.award:
                if not new_habit.link_pleasant:
                    raise serializers.ValidationError("Usual habit must has award or pleasant habit!")
            else:
                if new_habit.link_pleasant:
                    raise serializers.ValidationError("Usual habit must not has award and pleasant habit simultaneously!")

            return new_habit
        # check pleasant habit
        else:
            if new_habit.award:
                raise serializers.ValidationError("Pleasant habit can not has award!")
            return new_habit

    class Meta:
        model = Habit
        fields = "__all__"