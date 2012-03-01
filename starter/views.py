# -*- coding: utf-8 -*-
"""pavement.py -- pavement for <Django Project Name>

Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""

from django.http import HttpResponse

def home(request):
    return HttpResponse('Starter app up')
