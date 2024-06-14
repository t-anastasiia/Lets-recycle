import sqlite3

def fetch_cities_from_db():
    conn = sqlite3.connect('Data/Location/Cities.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM cities;")
    cities_data = cursor.fetchall()
    conn.close()
    return [city[0] for city in cities_data]

cities = fetch_cities_from_db()
