from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ serializer for habit and validation"""

    def create(self, validated_data):

        duration = validated_data.get("duration")
        is_pleasant = validated_data.get("is_pleasant")
        award = validated_data.get("award")
        link_pleasant = validated_data.get("link_pleasant")

        # check duration
        if duration > 120:
            raise serializers.ValidationError("Duration greater than 120 second!")

        # check usual habit
        if is_pleasant is False:
            if not award:
                if not link_pleasant:
                    raise serializers.ValidationError("Usual habit must has award or pleasant habit!")
            else:
                if link_pleasant:
                    raise serializers.ValidationError(
                        "Usual habit must not has award and pleasant habit simultaneously!")


            new_habit = Habit.objects.create(**validated_data)

            return new_habit

        # check pleasant habit
        else:
            if award:
                raise serializers.ValidationError("Pleasant habit can not has award!")

            if link_pleasant:
                raise serializers.ValidationError("A good habit cannot have associated habits!")

            new_habit = Habit.objects.create(**validated_data)

            return new_habit

    class Meta:
        model = Habit
        fields = "__all__"
