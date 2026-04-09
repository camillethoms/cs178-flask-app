# dbCode.py
# Author: Camille Thoms
# Helper functions for database connection and queries

# tools for a) python to mysql connection and b) keeps login info 
import pymysql
import creds

# actually makes the connection that the tools do of connecting the database. logs in basically by using creds and sends off connection. 
# used from lab work. (also the 'connect' is like crossed out and idk why)
def get_conn():
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

# used from lab work and used Claude for what the hell 'args' is and how to use it
def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    cur = get_conn().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

# get all animals function - feels self-explanitory, gets every animal's data and combines them with their topics into one part
# The following function was generated with help from Claude Sonnet 4.6 for joining and grouping the topics right, specifically the GROUP_CONCAT and | usage 
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

# i did this cause i thought i was gonna make a search funciton. is this function even applicable now? The following function was generated with help from Claude Sonnet 4.6, same reasoning as get all animals function
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

# this shit aint even done. what do i do with it now? do i have to finish it and the delete and update version? i didn't think so tho 
def add_animal(name, species, species_class, sex, birthday, arrivaldate, conservationstatus, topics):
    """to add a new animal and their ambassador topics"""
    conn = get_conn()
    cursor = conn.cursor()
    