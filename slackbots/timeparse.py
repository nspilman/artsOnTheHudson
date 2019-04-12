import re
import datetime

today = datetime.date.today()

class TimeParse():
    def __init__(self, message):
        self.message = message
        self.message_list = message.split('~')
        self.first_space = message.find(' ')
        self.description = ''
        
        #check to see if the first item in the list is an int
        try:
            self.minutes = int(self.message_list[0])
            worked_first = True

        #if it's not, try splitting after the space into a second item
        except:
            try:
                self.minutes = int(self.message_list[0][0:self.first_space])
                self.description = self.message_list[0][self.first_space:]
                worked_first = False
            except:
                print('the FUCK you tryna do?')
                return 
        
        if worked_first == True:
            self.description = self.message_list[1]
            try:
                self.day = self.message_list[2]
            except:
                self.day = datetime.date.today()
        else:
            try:
                self.day = self.message_list[1]
            except:
                self.day = datetime.date.today()
        if str(self.day).lower() == 'yesterday':
            self.day = datetime.date.today() - datetime.timedelta(1)
        
        if type(self.day) != datetime.date:
            try:
                self.day = self.day + '/' + str(today.year)
                self.day = datetime.datetime.strptime(self.day,'%m/%d').date()
            except:
                self.day = datetime.datetime.strptime(self.day,'%m/%d/%Y').date()
                





