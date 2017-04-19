# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request=request, template_name='gbfgraph/index.html')
