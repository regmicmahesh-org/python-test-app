#!/usr/bin/python
import sys
import site

#this enables python to access installed packages from global python
site.addsitedir("/home/asdf/env/lib/python3.9/site-packages/")

#this was needed to make sure i can import app i guess
#i was right
#if i remove this, i cant import stuffs
site.addsitedir("/home/asdf/FlaskApp/")

#setting up app which is executable by WSGI Directly.
from app import app as application
