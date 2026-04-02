# dbCode.py
# Author: Camille Thoms
# Helper functions for database connection and queries

import pymysql
import creds

def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    cur = get_conn().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

# The following function was generated with help from Claude Sonnet 4.6
def get_all_animals():
    """Returns all animals with their ambassador topics."""
    query = """
        SELECT a.id, a.name, a.species, a.species_class, a.sex, 
               a.birthday, a.arrivaldate, a.conservationstatus,
               GROUP_CONCAT(t.topic SEPARATOR '|') AS topics
        FROM animals a
        LEFT JOIN ambassador_topics t ON a.id = t.animal_id
        GROUP BY a.id
    """
    return execute_query(query)

# The following function was generated with help from Claude Sonnet 4.6
def get_animal_by_id(animal_id):
    """Returns a single animal and their topics by ID."""
    query = """
        SELECT a.id, a.name, a.species, a.species_class, a.sex,
               a.birthday, a.arrivaldate, a.conservationstatus,
               GROUP_CONCAT(t.topic SEPARATOR '|') AS topics
        FROM animals a
        LEFT JOIN ambassador_topics t ON a.id = t.animal_id
        WHERE a.id = %s
        GROUP BY a.id
    """
    results = execute_query(query, (animal_id,))
    return results[0] if results else None
