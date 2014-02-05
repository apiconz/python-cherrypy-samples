import cherrypy

class Home:

	@cherrypy.expose
	def index(self): #/
		return "Home"

	@cherrypy.expose
	def links(self): #/links
		return "Links"

	@cherrypy.expose
	def contact(self): #/contact
		return "Contact"

	@cherrypy.expose
	def information(self): #/information
		return "Information"

class Gallerys:

	@cherrypy.expose
	def index(self): #/gallerys
		return "Gallerys"

	@cherrypy.expose
	def photography(self): #/gallerys/photography
		return "Photography"

	@cherrypy.expose
	def art(self): #/gallerys/art
		return "Art"

	@cherrypy.expose
	def others(self): #/gallerys/photography
		return "Others"

home = Home()
home.gallerys = Gallerys()

cherrypy.quickstart(home)