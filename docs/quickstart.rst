.. _quickstart-chapter:

=================
Quick Start Guide
=================

Requirements
============

* Python >=2.7
* virtualenv
* pip
* MySQL (alternatively sqlite or PostgreSQL should work)
* git


Set Up
======

::

    $ git clone https://github.com/rockawayhelp/friendsofrockaway.git
    $ cd friendsofrockaway
    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt


Running
=======

::

    $ cd friendsofrockaway/
    $ python manage.py runserver 

This will start a development server running on ``localhost:8000``.
