#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity """
# Import the necessary models
from models import *

# Creation of a State
state = state.State(name="California")
# Save the state object
state.save()

# Creation of a City
city = city.City(state_id=state.id, name="San Francisco")
# Save the city object
city.save()

# Creation of a User
user = user.User(email="john@snow.com", password="johnpwd",
            first_name='john', last_name='snow')
# Save the user object
user.save()

# Creation of 2 Places
place_1 = place.Place(user_id=user.id, city_id=city.id, name="House 1")
# Save the first place object
place_1.save()
place_2 = place.Place(user_id=user.id, city_id=city.id, name="House 2")
# Save the second place object
place_2.save()

# Creation of 3 various Amenity
amenity_1 = amenity.Amenity(name="Wifi")
# Save the first amenity object
amenity_1.save()
amenity_2 = amenity.Amenity(name="Cable")
# Save the second amenity object
amenity_2.save()
amenity_3 = amenity.Amenity(name="Oven")
# Save the third amenity object
amenity_3.save()

# Link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# Link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

# Save all the changes to the storage
storage.save()

# Print a success message
print("OK")
