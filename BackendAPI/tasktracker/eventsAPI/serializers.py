from rest_framework import serializers
from .models import Tasks, CurrentTime


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class CurrentTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CurrentTime
        fields = ['seconds','minutes','hours']


    def save(self,):
        current_time = CurrentTime(
            seconds = self.validated_data['seconds'],
            minutes = self.validated_data['minutes'],
            hours = self.validated_data['hours'],
        )
        current_time.save()
        return current_time
