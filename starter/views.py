# -*- coding: utf-8 -*-
"""pavement.py -- pavement for <Django Project Name>

Copyright 2011-2012 Plexical. See LICENCE for permissions.
"""

from django.http import HttpResponse

from annoying.decorators import render_to

@render_to('base.html')
def home(request):
    return {'marker': 'base template'}
