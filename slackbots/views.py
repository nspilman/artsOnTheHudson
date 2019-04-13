from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient                               #1
from rtmbot.core import Plugin
from django.contrib.auth.models import User
from people.models import Profile
from .timeparse import TimeParse
from timelog.models import Timelog
import datetime

SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,                          #2
'SLACK_BOT_USER_TOKEN', None)                                     #
Client = SlackClient(SLACK_BOT_USER_TOKEN)                        #3

today = datetime.date.today()

class Events(APIView):
    def post(self, request, *args, **kwargs):

            slack_message = request.data
        # if Client.rtm_connect(with_team_state=False):
        
            # verification challenge
            if slack_message.get('type') == 'url_verification':
                return Response(data=slack_message,
                                status=status.HTTP_200_OK)
            # greet bot
            if 'event' in slack_message:                              #4
                event_message = slack_message.get('event')            #
                
                # ignore bot's own message
                if event_message.get('subtype') == 'bot_message':     #5
                    return Response(status=status.HTTP_200_OK)        #
                
                # process user's message                      #6
                text = event_message.get('text')                      #
                channel = event_message.get('channel')
                user_id = event_message.get('user')   
                user_profile = Profile.objects.get(slack_id = user_id)
                user = user_profile.user
                
                Client.api_call(method='chat.postMessage',        #8
                                    channel=channel,                  #
                                    text=bot_text)                    #
                return Response(status=status.HTTP_200_OK)        #9


                time_obj =  TimeParse(text)

                timelog = Timelog()
                timelog.person = user
                timelog.logdate = today
                timelog.minutes = time_obj.minutes
                timelog.description = time_obj.description
                timelog.work_day = time_obj.day

                timelog.save()
                             #
                bot_text = 'Thanks, {}. You logged {} to "{}" on {}.'.format(user.username, timelog.minutes, timelog.description, timelog.work_day)             #                              #7
                Client.api_call(method='chat.postMessage',        #8
                                    channel=channel,                  #
                                    text=bot_text)                    #
                return Response(status=status.HTTP_200_OK)        #9

            return Response(status=status.HTTP_200_OK)

def test(request):
    user_id = 'U97G8HY69'
    user_profile = Profile.objects.get(slack_id = user_id)
    user = user_profile.user
                
    text = '140 this is taking forever'
    time_obj =  TimeParse(text)
    timelog = Timelog()
    timelog.person = user
    timelog.logdate = today
    timelog.minutes = time_obj.minutes
    timelog.description = time_obj.description
    timelog.work_day = time_obj.day
                
    timelog.save()

    return "Did it work?"       #9




""" 
def timelog(request):
    slack_client = SlackClient('xoxb-350748077316-lWaMjFvNFf48tI4U9dnNHBKJ')
    timelog_bot = Timelog_Bot()
    if slack_client.rtm_connect(with_team_state=False):
        send_mail('We have a hit on our hands', 'wasgood',
                           ['nate.spilman@gmail.com'], fail_silently=True)
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]

        command, channel = timelog_bot.parse_bot_commands(slack_client.rtm_read())
        if command:
            timelog_bot.handle_command(command, channel)
        else:
            print("Connection failed. Exception traceback printed above.")
    
    return request
"""
