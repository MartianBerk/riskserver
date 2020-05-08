import random

from mylib.globals import get_global
from mylib.myodbc import MyOdbc

from mb.risk.model.cards import MissionCard, TerritoryCard


class CardService:
    _db = "risk"

    def __init__(self, mission_cards, territory_cards):
        """Initialize a Card Service object.

        Args:
            mission_cards (list): List of MissionCard objects.
            territory_cards (list): List of TerritoryCard objects.
        """
        self._mission_cards = mission_cards
        self._territory_cards = territory_cards

    @staticmethod
    def _load_mission_cards(db):
        """Helper function to load mission cards from DB."""
        return [MissionCard(**card) for card in db.get("MISSIONS")]

    @staticmethod
    def _load_territory_cards(db):
        """Helper function to load territory cards from DB."""
        territories = [t["name"] for t in db.get("TERRITORIES")]
        territories = random.shuffle(territories)

        # 30 infantry, 14 cavalry, 6 artillery & 2 wild (TODO: check amounts)
        infantry_cards = [TerritoryCard(territory=territories.pop(0), troop="infantry") for _ in range(0, 24)]
        cavalry_cards = [TerritoryCard(territory=territories.pop(0), troop="cavalry") for _ in range(0, 12)]
        artillery_cards = [TerritoryCard(territory=territories.pop(0), troop="artillery") for _ in range(0, 6)]
        wild_cards = [TerritoryCard(territory="wild", troop="wild") for _ in range(0, 2)]

        return infantry_cards + cavalry_cards + artillery_cards + wild_cards

    def shuffle_deck(self, card_deck):
        """Shuffle one of the card decks.

        Args:
            card_deck (str): Name of the card deck (mission or territory).
        """
        if card_deck not in ["mission", "territory"]:
            raise ValueError("unknown card_deck")

        random.shuffle(getattr(self, f"_{card_deck}_cards"))

    @classmethod
    def deal(cls):
        """Load and shuffle fresh card decks.

        Returns:
            CardService.
        """
        db_settings = get_global("dbs", CardService._db)

        db = MyOdbc.connect(db_settings.get("driver"),
                            CardService._db,
                            db_settings.get("location"))

        mission_cards = CardService._load_mission_cards(db)
        territory_cards = CardService._load_territory_cards(db)

        service = CardService(mission_cards, territory_cards)
        service.shuffle_deck("mission")
        service.shuffle_deck("territory")

        return service

    @classmethod
    def load(cls, mission_cards, territory_cards):
        """Load and shuffle card decks, but remove cards in play.

        Args:
            mission_cards (list): List of MissionCard objects.
            territory_cards (list): List of TerritoryCard objects.

        Returns:
            CardService.
        """
        db_settings = get_global("dbs", CardService._db)

        db = MyOdbc.connect(db_settings.get("driver"),
                            CardService._db,
                            db_settings.get("location"))

        new_mission_cards = CardService._load_mission_cards(db)
        [new_mission_cards.remove(m) for m in mission_cards]

        new_territory_cards = CardService._load_territory_cards(db)
        [new_territory_cards.remove(t) for t in territory_cards]

        service = CardService(new_mission_cards, new_territory_cards)
        service.shuffle_deck("mission")
        service.shuffle_deck("territory")

        return service

    @property
    def mission_card(self):
        if not self._mission_cards:
            raise AttributeError("no mission cards")

        return self._mission_cards.pop(0)

    @property
    def territory_card(self):
        if not self._territory_cards:
            raise AttributeError("no territory cards")

        return self._territory_cards.pop(0)

    @territory_card.setter
    def territory_card(self, value):
        self._territory_cards.append(value)
