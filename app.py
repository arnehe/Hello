
import web

urls = (
    #'/', 'home'
    '/(.*)', 'hello'

)
app = web.application(urls, globals())

# class home:
#     def GET(self):
#         return 'Hello, this is a GET'
#     def POST(self):
#         return 'Hello, this is a POST'

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
