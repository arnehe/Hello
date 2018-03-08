import web

urls = (
    '/arne', 'home'
    # '/(.*)', 'hello'

)
app = web.application(urls, globals())


class home:
    def GET(self):
        return 'Hello, this is a GET'

    def POST(self):
        return 'Hello, this is a POST'


class person():
    def __init__(self):
        self.name
    def getName(self):
        print("asd")


if __name__ == "__main__":
    app.run()
