import web, json

urls = (
    '/(.*)', 'Home'
)

app = web.application(urls, globals())


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Home:
    def __init__(self):
        self.p = Person("Onbekend")

    def GET(self, var):
        web.header('Content-Type', 'application/json')
        if not var:
            return json.dumps({"Name": "unknown"})
        self.p.name = var
        return json.dumps({"Name": self.p.name})

    def POST(self, var):
        return 'Hello, this is the POST method'


if __name__ == "__main__":
    app.run() 