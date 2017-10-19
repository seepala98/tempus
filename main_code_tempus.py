from __future__ import print_function
from tkinter import *
import webbrowser
import time
import tkinter.messagebox as mes
import requests
from tkinter import *
from tkinter import simpledialog
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime
import winsound

#Function definitions

def mainfunction():
    time1=time_from_user.get()
    url1=url_from_user.get()
    if(url1==""):
        mes.showinfo("Error",'Please enter the URL')
    time3=int(time1)
    time.sleep(time3)
    webbrowser.open(url1)
    freq=500
    dur=500
    winsound.Beep(freq,dur)
    
def clear_text():
    url_from_user.delete(0,END)
    time_from_user.delete(0,END)
def message1():
    mes.showinfo("MEMBERS",'Sharanya\nVardhan\nPavan')
def message2():
    mes.showinfo("Project",'TEMPUS\nReminder and Planner\nThis is mainly developed for the people to remind tasks.')
def message3():
    mes.showinfo("College",'SIR M VISVESWARAYA INSTITUTE OF TECHNOLOGY')
#def message4():
   # mes.showinfo("Information",'Hello')
def message5():
    mes.showinfo("Version",'1.0.1')
def question():
    answer=mes.askquestion("Confirmation","Proceed?")
    if(answer=='yes'):
        mainfunction()
def terms():
    #from tkinter import *
    root = Tk()
    Label(root,text="1->Please make sure your default browser has no windows open").pack(fill=X)
    Label(root,text="2->Please do not minimise this program after requesting particular URL to open.Access your programs from main menu (START in windows)").pack(fill=X)
    Label(root,text="3->You cannot remove the request once it is set so please make sure before requesting particular URL to open").pack(fill=X)
    Label(root,text="4->Thank you .").pack(fill=X)
    Button(root,text="Quit",bg='red',fg='white',command=root.destroy).pack()
    root.mainloop()

#WEATHER FUNCTION
    
def weatherfunction():
    #pavan=200
    city=simpledialog.askstring("Area","Enter the Area?")
#city=input("enter the city name:")
    bp='https://maps.googleapis.com/maps/api/geocode/json?address='+city
    response=requests.get(bp)
    data=response.json()
    #formatted address
    address=data['results'][0]['formatted_address']
    ## print('you entered')
    ## print(address)
    lat=str(data['results'][0]['geometry']['location']['lat'])
    lng=str(data['results'][0]['geometry']['location']['lng'])


     #lat=input("latitude")
         #lon=input("longitude")
    api='https://darksky.net/forecast/'+lat+','+lng+'/si24/en.json'
    response = requests.get(api)
    data=response.json()
      #print('\n')
     #print("In",address)
            #currently summary
    ##print("currently summary is:",data['currently']['summary'])

                           #hourly summary
    ##print("hourly summary is :",data['hourly']['summary'])

                      #temperature
    p1=float(data["currently"]["temperature"])
    p2=str(address)
    p3='\n'+p2
    mes.showinfo("Weather Report",'The temperature is : %.2f °C at %s'%(p1,p3))
             # Humidity
    p=int(data["currently"]['humidity']*100)
    #print("humidity is :",p,'%')

#Event Creation

def eventcreation():
    summary_user=simpledialog.askstring("Summary","Enter the Event Summary?")
    #if(ans=='OK'):
    sdate=simpledialog.askstring("Date","Enter the Event start date(YYYY-MM-DD)?")
    edate=simpledialog.askstring("Date","Enter the Event end date(YYYY-MM-DD)?")
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)
    CAL = build('calendar', 'v3', http=creds.authorize(Http()))

    GMT_OFF = '-07:00'      # PDT/MST/GMT-7
    EVENT = {
        'summary': summary_user,
        'start':  {'dateTime': sdate+'T19:00:00%s' % GMT_OFF},
        'end':    {'dateTime': edate+'T22:00:00%s' % GMT_OFF},
        'attendees': [
            {'email': 'friend1@example.com'},
            {'email': 'friend2@example.com'},
        ],
    }

    e = CAL.events().insert(calendarId='primary',
            sendNotifications=True, body=EVENT).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (e['summary'].encode('utf-8'),
            e['start']['dateTime'], e['end']['dateTime']))
    mes.showinfo("Event Created",'%r %s %s'%(e['summary'].encode('utf-8'),
            e['start']['dateTime'], e['end']['dateTime']))
#EVENT LIST
def showcalendar():
    mes.showinfo('Calendar','June calendar')
def showevents():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/calendar-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Calendar API Python Quickstart'


    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def main():
        """Shows basic usage of the Google Calendar API.

        Creates a Google Calendar API service object and outputs a list of the next
        10 events on the user's calendar.
        """
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])
        
        if not events:
            p1='No upcoming events found.'
            mes.showinfo("Event List",p1)
        p3=[]
        i=0
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            p3.append(start+ "   <--->  "+event['summary']+'\n')
            #blank= Entry(top1,width=60).pack(ipady=3)
        mes.showinfo("Event list",p3)
        
        

    if __name__ == '__main__':
        main()
#GUI
        
root = Tk()
root.configure()
menu=Menu(root)
root.config(menu=menu)
#project heading
root.wm_title("Project _TEMPUS_")
#File bar
submenu=Menu(menu)
menu.add_cascade(label="OPTIONS",menu=submenu)
submenu.add_command(label="Members",command=message1)
submenu.add_command(label="Project",command=message2)
#submenu.add_command(label="Weather",command=messagew)

submenu.add_separator()

submenu.add_command(label="College",command=message3)
#submenu.add_command(label="Pre-requisites",command=terms)

submenu.add_separator()

submenu.add_command(label="Version",command=message5)
submenu.add_separator()
submenu.add_command(label="Exit",command=root.destroy)
#WEATHER  bar

submenu=Menu(menu)
menu.add_cascade(label="Weather",menu=submenu)
submenu.add_command(label="Show Weather",command=weatherfunction)

#CALENDAR BAR
submenu=Menu(menu)
menu.add_cascade(label="Calendar",menu=submenu)
submenu.add_command(label="Create Event",command=eventcreation)
submenu.add_command(label="Show Events",command=showevents)
submenu.add_command(label="Show Calendar",command=showcalendar)
#MAIN HEADING

#image

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file="C:\\Users\\SEEPALA\\Desktop\\tempus\\rainclock.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
#image ends here

top=Frame(root)
top.pack(side=LEFT,anchor=W)
D = Canvas(top, bg="blue", height=250, width=300)
filename1 = PhotoImage(file="C:\\Users\\SEEPALA\\Desktop\\tempus\\rainclk3.png")
background_label = Label(top, image=filename1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

D.pack()

button1=Label(top,text="URL / Local Disk files",fg="#383864")
button1.pack()
button1.config(font=("Courier",15))
url_from_user = Entry(top)
url_from_user.pack()

button2=Label(top,text="TIME(in seconds)",fg="#383839")
button2.pack()
button2.config(font=("Courier",15))
time_from_user=Entry(top)
time_from_user.pack()

b = Button(top,text='Enter',command=question)
b.pack()
b.config(font=("Courier",15))
b2=Button(top,text="Clear",command=clear_text)
b2.pack()
b2.config(font=("Courier",15))

root.mainloop()

