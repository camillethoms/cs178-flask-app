from dbCode import *

conn = get_conn()
cursor = conn.cursor()

# Insert new animals
animals = [
    (15, 'Kasi', 'Leptailurus serval', 'Mammals', 'Male', '2024-01-01', '2026-04-01', 'Least Concern'),
    (16, 'Nolie', 'Dromaius novaehollandiae', 'Birds', 'Female', '2020-01-01', '2025-09-12', 'Least Concern'),
    (17, 'Oliver', 'Gallus gallus domesticus', 'Birds', 'Male', '2021-01-01', '2021-06-01', 'Not Evaluated'),
    (18, 'Nugget', 'Gallus gallus domesticus', 'Birds', 'Female', '2019-01-01', '2021-04-01', 'Not Evaluated'),
    (19, 'Henrique', 'Gallus gallus domesticus', 'Birds', 'Female', '2020-01-01', '2022-08-01', 'Not Evaluated'),
    (20, 'Polly', 'Gallus gallus domesticus', 'Birds', 'Female', '2020-01-01', '2023-11-01', 'Not Evaluated'),
    (21, 'Noodle', 'Morelia spilota mcdowelli', 'Reptiles & Amphibians', 'Female', '2015-01-01', '2021-04-01', 'Least Concern'),
    (22, 'Marty', 'Armadillidium maculatum', 'Invertebrates', 'Unknown', '2022-01-01', '2022-01-01', 'Not Evaluated'),
    (23, 'Toaster Strudel', 'Tiliqua scincoides intermedia', 'Reptiles & Amphibians', 'Unknown', '2022-07-04', '2022-11-01', 'Least Concern'),
    (24, 'Tortellini', 'Pandinus imperator', 'Invertebrates', 'Male', '2022-10-01', '2022-11-01', 'Not Evaluated'),
    (25, 'Tipsy', 'Psittacus erithacus', 'Birds', 'Male', '1995-01-01', '2026-03-10', 'Endangered'),
]

topics = [
    (15, 'Exotic pet trade'),
    (16, 'Exotic meat trade'),
    (16, 'Traditional medicine'),
    (16, 'Animal products in cosmetics'),
    (17, 'Agricultural industry'),
    (17, 'Consumer choice and environment'),
    (18, 'Agricultural industry'),
    (18, 'Consumer choice and environment'),
    (19, 'Agricultural industry'),
    (19, 'Consumer choice and environment'),
    (20, 'Agricultural industry'),
    (20, 'Consumer choice and environment'),
    (21, 'Pet trade'),
    (21, 'Habitat loss'),
    (22, 'Importance of invertebrates'),
    (22, 'Misconceptions about invertebrates'),
    (23, 'Human development'),
    (23, 'Invasive species'),
    (24, 'Importance of invertebrates'),
    (24, 'Misconceptions about invertebrates'),
    (25, 'Pet trade'),
    (25, 'Habitat loss'),
]

for a in animals:
    cursor.execute("""
        INSERT INTO animals (id, name, species, species_class, sex, birthday, arrivaldate, conservationstatus)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, a)

for t in topics:
    cursor.execute("""
        INSERT INTO ambassador_topics (animal_id, topic)
        VALUES (%s, %s)
    """, t)

conn.commit()
cursor.close()
conn.close()
print("Done! All animals added.")
