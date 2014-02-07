import cherrypy

songs = {
    '1' : {
        'title':'Can\'t hold us',
        'artist':'Mackelmore'
    },
    '2' : {
        'title':'I always love you',
        'artist':'Amaninho'
    },
    '3' : {
        'title':'Window to His love',
        'artist':'Azevedo'
    }
}

class Songs:
    exposed = True


    def GET(self,id=None):
        if id == None:
            return('Aqui estan todas las canciones que tenemos: %s' % songs)
        elif id in songs:
            song = songs[id]
            return('La cancion con el ID %s se llama %s y el artista que lo canta es %s' % (id,song['title'],song['artist']))
        else:
            return('No se encontro cancion con el ID %s :-(' % id)

    def POST(self,title,artist):
        id = str(max([int(_) for _ in songs.keys()]) + 1)
        songs[id] = {
            'title':title,
            'artist': artist
        }
        return ('Registraste una nueva cancion con el ID: %s' % id)

if __name__ == '__main__':
    cherrypy.tree.mount(
        Songs(),'/api/songs',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

