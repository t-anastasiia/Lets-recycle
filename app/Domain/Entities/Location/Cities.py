import sqlite3
from enum import Enum

# Connect to the database
conn = sqlite3.connect('../../Data/Location/Cities.db')
cursor = conn.cursor()

# Fetch all rows from the cities table
cursor.execute("SELECT name FROM cities;")
cities_data = cursor.fetchall()

# Close the connection
conn.close()

# Generate an enum with the list of cities
class Cities(Enum):
    "Enum for cities"
    "Dynamic enumeration for cities extracted from the Cities.db database."

    def __new__(cls, value):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

# Adding the cities dynamically to the enum
for i, (city,) in enumerate(cities_data):
    setattr(Cities, city.replace(' ', '_').replace('-', '_'), Cities(i + 1))

# Example usage
if __name__ == "__main__":
    for city in Cities:
        print(city.name, city.value)
