from django.shortcuts import render
from django.db import connections
from django.db.utils import OperationalError
from nutanix.settings import DATABASES



def index(request):
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
    else:
        connected = True
    context = {
            'connection': connected,
            'host': DATABASES['default']['HOST'],
            'port': DATABASES['default']['PORT']
        }
    return render(request, 'clusters/index.html', context)
