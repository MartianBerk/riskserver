from mylib.webapi import request, response, route


@route("/newtest", methods=["GET"])
def test():
    return "New Test"
