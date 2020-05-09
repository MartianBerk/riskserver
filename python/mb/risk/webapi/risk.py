from mylib.webapi import request, response, route


@route("/new_game")
def new_game():
    body = request.json

    try:
        return "Hello World"
    except KeyError as e:
        pass


@route("/test")
def test():
    return "Test"
