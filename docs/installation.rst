Installation
============

1. Install django-pypayzen package.

::

    pip install django-pypayzen


2. Add django_pypayzen in your INSTALLED_APPS

Edit your django settings.py and add django_pypayzen in your INSTALLED_APPS.

2. Configure your :doc:`django-pypayzen settings </settings>` .

In your settings.py file, add the settings specific to django-pypayzen.

3. Include "django_pypayzen.urls" in your urls.py

::

    url(r'^payment/', include("django_pypayzen.urls")),
