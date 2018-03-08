
import web

urls = (
    '/(.*)', 'home'
    '/(.*)', 'hello'

)
app = web.application(urls, globals())

class home:
    def GET(self, name):
        if not name: 
            name = 'world'
        return 'Hello, ' + name + '!'
    def POST(self, name):
        if not name:
            name = 'world'
        return 'Hello, ' + name + '!'

class hello:
    def GET(self, name):
        if not name:
            name = 'world'
        return 'Hello, ' + name + '!'
    def POST(self, name):
        if not name:
            name = 'world'
        return 'Hello, ' + name + '!'


if __name__ == "__main__":
    app.run()
