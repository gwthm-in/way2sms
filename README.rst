pytest-pspec
==============

.. image:: https://travis-ci.org/gowtham-sai/way2sms.svg?branch=master
    :target: https://travis-ci.org/gowtham-sai/way2sms

.. image:: https://codecov.io/gh/gowtham-sai/pytest-pspec/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/gowtham-sai/way2sms


Install
-------

::

    pip install waytwo



way2sms
-------

This python code to send messages to the people in the list automatically based on the time.

Way2SMS.py - This file handels the login and message sending part. It takes number and password as inputs
and then returns boolean values as result

Perf.py - This file handles helps to craft a beautiful message grabbed from way2sms website. Randomly picks one
messages and appends wishs to that message and returns

auto.py - This file automates the entire tasks. You need to run auto.py to initiate the tasks

to.py - This is file contains mobile number of recievers. Keep all the recievers numbers in this file.
