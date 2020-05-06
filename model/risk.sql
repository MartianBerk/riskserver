/*
 * SQLite DB for Risk! Game.
 */

CREATE TABLE GAMES (
    id INTEGER PRIMARY KEY,
    started TEXT NOT NULL,
    ended TEXT
);

CREATE TABLE MISSIONS (
    id INTEGER PRIMARY KEY,
    mission TEXT NOT NULL,
    criteria TEXT NOT NULL
);

CREATE TABLE COLOURS (
    id INTEGER PRIMARY KEY,
    colour TEXT NOT NULL
);

CREATE TABLE PLAYERS (
    name TEXT NOT NULL,
    game_id INTEGER NOT NULL,
    mission_id INTEGER NOT NULL,
    colour_id INTEGER NOT NULL,
    has_dice INTEGER NOT NULL,
    game_data BLOB NOT NULL  -- hold data such as number of armies, cards, army placement, etc.
);

CREATE TABLE CONTINENTS (
    id TEXT NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE TERRITORIES (
    name TEXT NOT NULL,
    continent_id TEXT NOT NULL
);


/*
 * Load Colours Data.
 */

INSERT INTO COLOURS (colour)
VALUES
    ("black"),
    ("blue"),
    ("green"),
    ("pink"),
    ("red"),
    ("yellow");

/*
 * Load Mission Data.
 */

INSERT INTO MISSIONS (mission, criteria)
VALUES
    ("Capture Europe, Australia and one other continent.", "EU,AU,OTHER"),
    ("Capture Europe, South America and one other continent.", "EU,SA,OTHER")
    ("Capture North America and Africa.", "NA,AF")
    ("Capture North America and Australia.", "NA,AU")
    ("Capture Asia and South America.", "AS,SA")
    ("Capture Asia and Africa.", "AS,AF")
    ("Capture 24 territories.", "24T")
    ("Capture 18 territories and occupy each with two troops.", "18T_2")
    ("Destroy all black armies or capture 24 territories.", "BLACK_24T")
    ("Destroy all blue armies or capture 24 territories.", "BLUE_24T")
    ("Destroy all green armies or capture 24 territories.", "GREEN_24T")
    ("Destroy all pink armies or capture 24 territories.", "PINK_24T")
    ("Destroy all red armies or capture 24 territories.", "RED_24T")
    ("Destroy all yellow armies or capture 24 territories.", "YELLOW_24T");

/*
 * Load Continents Data.
 */

INSERT INTO CONTINENTS (id, name)
VALUES
    ("AF", "Africa"),
    ("AS", "Asia"),
    ("AU", "Australia"),
    ("EU", "Europe"),
    ("NA", "North America"),
    ("SA", "South America");

 /*
  * Load Territories Data.
  */

INSERT INTO TERRITORIES (continent_id, name)
VALUES
    ("AF", "Congo"),
    ("AF", "East Africa"),
    ("AF", "Egypt"),
    ("AF", "Madagascar"),
    ("AF", "North Africa"),
    ("AF", "South Africa"),
    ("AS", "Afghanistan"),
    ("AS", "China"),
    ("AS", "India"),
    ("AS", "Irkutsk"),
    ("AS", "Japan"),
    ("AS", "Kamchatka"),
    ("AS", "Middle East"),
    ("AS", "Mongolia"),
    ("AS", "Siam"),
    ("AS", "Siberia"),
    ("AS", "Ural"),
    ("AS", "Yakutsk"),
    ("AU", "Eastern Australia"),
    ("AU", "Indonesia"),
    ("AU", "New Guinea"),
    ("AU", "Western Australia"),
    ("EU", "Great Britain"),
    ("EU", "Iceland"),
    ("EU", "Northern Europe"),
    ("EU", "Scandinavia"),
    ("EU", "Southern Europe"),
    ("EU", "Ukraine"),
    ("EU", "Western Europe"),
    ("NA", "Alaska"),
    ("NA", "Alberta"),
    ("NA", "Central America"),
    ("NA", "Eastern United States"),
    ("NA", "Greenland"),
    ("NA", "Northwest Territory"),
    ("NA", "Ontario"),
    ("NA", "Quebec"),
    ("NA", "Western United States"),
    ("SA", "Argentina"),
    ("SA", "Brazil"),
    ("SA", "Peru"),
    ("SA", "Venezuela");
