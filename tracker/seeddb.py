#seed the tickets database
import csv
import os

path =  "../" # Set path of new directory here
os.chdir(path)
from models import Ticket # imports the model
with open('incidentseed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                p = Ticket(status=row[0], number=row[1], assigned=row[2])
                p.save()