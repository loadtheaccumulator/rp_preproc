# Copyright 2019 Red Hat QE CCIT
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software. If not, see <http://www.gnu.org/licenses/>.
#
"""RP PreProc Package for importing test result files into ReportPortal"""
from setuptools import setup, find_packages

setup(
    name='rp-preproc',
    version='0.1',
    description=('REST API and client for pre-processing XML data before '
                 'import into ReportPortal'),
    url='https://github.com/loadtheaccumulator/rp-preproc',
    author='Jonathan D. Holloway',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='reportportal rest api xml xunit junit',

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rp_preproc = rp_preproc.main:main',
            ]
                },
    install_requires=['flask-restplus==0.9.2', 'gunicorn==19.8.*',
                      'xmltodict', 'reportportal_client',
                      ('glusto@git+git://github.com/loadtheaccumulator/'
                       'glusto.git@python3_port4#egg=glusto')],
)
