def create_table():
    query_squadra_risultati = """
    CREATE TABLE IF NOT EXISTS squadra_risultati(
    id_squadra INT(11) PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) UNIQUE,
    vittorie INT(11),
    sconfitte INT(11),
    pareggi INT(11),
    punteggio INT(11)
    )
    """

    query_giocatori = """
    CREATE TABLE IF NOT EXISTS giocatori(
    id_giocatore INT(11) PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    cognome VARCHAR(255),
    eta INT(11),
    nazionalita VARCHAR(255),
    ruolo VARCHAR(255),
    numero_maglia INT(11),
    id_squadra INT(11)
    """

    fk_giocatori = """
    ALTER TABLE giocatori
    ADD CONSTRAINT fk_squadra FOREIGN KEY (id_squadra) REFERENCES squadra_risultati(id_squadra)
    """