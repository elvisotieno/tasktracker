from django.shortcuts import render
import random
import requests
from .models import Tasks, CurrentTime
from .serializers import TasksSerializers, CurrentTimeSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#periodically post current time
@api_view(['POST',])
def current_time(request, null=None):
    if request.method == 'POST':
        serializer = CurrentTimeSerializers(data=request.data)
        data={}

        if serializer.is_valid():
            current_time= serializer.save()
            data['seconds'] = current_time.seconds
            data['minutes'] = current_time.minutes
            data['hours'] = current_time.hours
            program_time = f'{current_time.hours}:{current_time.minutes}:{current_time.seconds}'

            # Determining which given task should be carried out
            time = current_time.seconds + (current_time.minutes*60) + (current_time.hours*3600)
            if time%30 == 0:
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "START","message": generate.integerN(),"program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z","wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

            elif time%40 == 0:
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "STOP", "message": generate.n_kintegers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

            elif time%50 == 0:
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "REPORT", "message": generate.running_servers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

            elif time%30 == 0 and time%40 == 0:
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "START", "message": generate.integerN(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "STOP", "message": generate.n_kintegers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)
            elif time%30 == 0 and time%50 == 0:
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "START", "message": generate.integerN(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "REPORT", "message": generate.running_servers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)
            elif time%50 == 0 and time%40 == 0:
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "STOP", "message": generate.n_kintegers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "REPORT", "message": generate.running_servers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)
            elif time%50 == 0 and time%40 == 0 and time%30 ==0 :
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "START", "message": generate.integerN(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)
                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "STOP", "message": generate.n_kintegers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)

                url = 'http://127.0.0.1:8000/tasks/'
                payload = {"events": "REPORT", "message": generate.running_servers(), "program_time": program_time,
                           "actual_time": "2021-10-11T13:38:25.579041Z", "wall_color": generate.wall_color(),
                           "clock_color": generate.clock_color(), "hourhand_color": generate.hourhand_color()}
                requests.post(url, data=payload)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Creating Tasks and Retrieving Running Tasks.
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method =='GET':
        all_products= Tasks.objects.all()
        serializer=TasksSerializers(all_products, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = TasksSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Task Details

@api_view(['GET','PUT','DELETE'])
def detail(requst, pk):
    # First let's check if the Task exist
    try:
        task = Tasks.objects.get(pk=pk)

    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if requst.method =='GET':
        serializer = TasksSerializers(task)
        return Response(serializer.data)

    elif requst.method =='PUT':
        serializer = TasksSerializers(data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif requst.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Get the current task
@api_view(['GET'])
def current_task(request):
    if request.method =='GET':
        current_event = Tasks.objects.all().order_by('-actual_time')[0]
        serializer=TasksSerializers(current_event, many=False)
        return Response(serializer.data)
#Generate random number and Hex colorcode
# keep track of the events
class Generate:
    def __init__(self):
        self.running=0
    def integerN(self):
        N = random.randint(10, 20)
        self.running += N
        return f'Start {N} servers'

    def running_servers(self):
        k=self.running
        return f'Report {k} servers running'

    def n_kintegers(self):

        n = random.randint(5,self.running)
        self.running -= n
        return f'Stop {n} servers'

    def wall_color(self):
        generate = "%06x" % random.randint(0, 0xFFFFFF)
        wall_color=str(f'#{generate}')
        return wall_color

    def clock_color(self):
        generate = "%06x" % random.randint(0, 0xFFFFFF)
        clock_color=str(f'#{generate}')
        return clock_color

    def hourhand_color(self):
        generate = "%06x" % random.randint(0, 0xFFFFFF)
        hourhand_color=str(f'#{generate}')
        return hourhand_color


generate = Generate()
