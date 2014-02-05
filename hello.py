import cherrypy

class Root(object):
	def index(self):
		return "Hello World"

	index.exposed = True

cherrypy.quickstart(Root())