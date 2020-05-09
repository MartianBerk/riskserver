from contextlib import suppress

from mylib.webapi import request, response, route

from mb.risk.engine import RiskEngine
from mb.risk.model import Colour, MissionCard
from mb.risk.service.cardservice import CardService
from mb.risk.service.colourservice import ColourService


@route("/meta", methods=["GET"])
def meta():
    # collect all mission cards
    missions = []
    card_service = CardService.deal()
    while True:
        try:
            missions.append(card_service.mission_card.dict())
        except AttributeError:
            break

    body = {"colours": [c.dict() for c in ColourService().list_colours()],
            "missions": missions}

    return response(body)


@route("/newgame", methods=["POST"])
def new_game():
    body = request.json

    players = []

    try:
        for player in body["players"]:
            players.append({
                "name": player["name"],
                "colour": Colour(**player["colour"]),
                "mission": MissionCard(**player["mission"])
            })

    except (AttributeError, KeyError) as e:
        raise Exception(f"invalid payload: {str(e)}")  # TODO: HTTPError, extend mylib.webapi

    players = RiskEngine().new_game().register_players(players)

    return "TODO"
