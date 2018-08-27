from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from tracker.models import Ticket
from pytz import UTC


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the ticket data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from ticket_data.csv into our ticket model"
    def handle(self, *args, **options):
        # if Ticket.objects.exists():
        #     print('Already loaded exiting')
        #     return
        print('Loading data...')
    
        for row in DictReader(open('incidentseed.csv')):
            ticket = Ticket()
            ticket.status = row['status']
            ticket.number = row['number']
            ticket.assigned = row['assigned']
            ticket.save()
