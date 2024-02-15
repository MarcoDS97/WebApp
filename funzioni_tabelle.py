from funzioni_connessioni import *

def create_table():
    query_squadra = """
        CREATE TABLE IF NOT EXISTS squadra(
        id_squadra INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(255) UNIQUE
        );
        """
    execute_query_insert(query_squadra)
    
    query_risultati = """
        CREATE TABLE IF NOT EXISTS risultati(
        id_risultato INT PRIMARY KEY AUTO_INCREMENT,
        gs1 INT,
        gs2 INT,
        giornata INT,
        id_s1 INT,
        id_s2 INT
        );
        """
    execute_query_insert(query_risultati)

    query_giocatori = """
        CREATE TABLE IF NOT EXISTS giocatori(
        id_giocatore INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(255),
        cognome VARCHAR(255),
        nazionalita VARCHAR(255),
        ruolo VARCHAR(255),
        numero_maglia INT,
        eta INT,
        id_squadra INT
        );
        """
    execute_query_insert(query_giocatori)

    try:
        fk_giocatori = """
            ALTER TABLE giocatori
            ADD CONSTRAINT fk_squadra FOREIGN KEY (id_squadra) REFERENCES squadra(id_squadra);
            """
        execute_query_insert(fk_giocatori)
    except:
        pass

    try:
        fk_risultati = """
            ALTER TABLE risultati
            ADD CONSTRAINT fk_id_s1 FOREIGN KEY (id_s1) REFERENCES squadra(id_squadra)
            ADD CONSTRAINT fk_id_s2 FOREIGN KEY (id_s2) REFERENCES squadra(id_squadra);
            """
        execute_query_insert(fk_giocatori)
    except:
        pass

