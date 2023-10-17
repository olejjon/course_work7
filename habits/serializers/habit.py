from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ serializer for habit and validation"""

    def create(self, validated_data):
        # check duration
        if validated_data['duration'] > 120:
            raise serializers.ValidationError("Duration greater than 120 second!")
        # check usual habit
        if validated_data['is_pleasant'] is False:
            if not validated_data['award']:
                if not validated_data['link_pleasant']:
                    raise serializers.ValidationError("Usual habit must has award or pleasant habit!")

            new_habit = Habit.objects.create(**validated_data)
            return new_habit
        # check pleasant habit
        else:
            if validated_data['award']:
                raise serializers.ValidationError("Pleasant habit can not has award!")
            new_habit = Habit.objects.create(**validated_data)
            return new_habit

    class Meta:
        model = Habit
        fields = "__all__"
