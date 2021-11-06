#!/bin/python3
'''Serve radio station links using CherryPy with Jinja2 template.'''
from json import load
import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

# this module’s directory path
WORKING_DIR = os.path.dirname(__file__)
# initialize cherrypy environment
e = Environment(loader=FileSystemLoader(f'{WORKING_DIR}/templates'))

# render index template
class Index():
    '''Index page class.'''
    @cherrypy.expose()
    def index(self):
        '''Render index page template.'''
        template = e.get_template('index.html')
        return template.render(station_data=self.station_data())
    # radio station data
    def station_data(self):
        '''Get radio station data.'''
        with open(f'{WORKING_DIR}/json/stations.json') as json_file:
            return load(json_file)

# if web app runs as standalone
if __name__ == '__main__':
    cherrypy.quickstart(Index())
