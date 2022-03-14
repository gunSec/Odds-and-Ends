import os
from datetime import date

customer = input("Customer Name >>  ")

date = date.today().strftime("%b %m %Y").upper()
PWD = f"/mnt/c/Users/Gunnar/Desktop/Incidents/{date[-4:]}/{date[4:6:]} {date[:3:]}/"
template = f"""{customer}

POC:
Reporter:
Ticket
    RT:
    Remedy:


==QUICK NOTE==


==TIMELINE==


==CALL LOG==


"""
with open(f"{PWD}{customer} - Notes.txt", 'w') as f:
    f.write(template)
