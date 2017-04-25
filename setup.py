"""Setup file for easy installation"""
import os

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)


setup(
    name="django-pypayzen",
    version="0.2",
    description="Django app to manage payments with Payzen ETP",
    license='MIT',
    author="Felipe Ferreira",
    author_email="felipe.gomes.ferreira@gmail.com",
    url="https://github.com/samambaman/django-pypayzen",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Django"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Django",
        "Topic :: Software Development"],
)
