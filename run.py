from simba_framework.main import Framework
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = Framework(routes, fronts)
HOST= '127.0.0.1'
PORT = 8000

with make_server(HOST, PORT, application) as httpd:
    print("Запуск на порту 8000...")
    httpd.serve_forever()
