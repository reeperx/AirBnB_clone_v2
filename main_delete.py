#!/usr/bin/python3
""" Test delete feature
"""
# Import necessary modules
from models.engine.file_storage import FileStorage
from models.state import State

# Create an instance of FileStorage
fs = FileStorage()

# Get all State objects from the FileStorage instance
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State object
new_state = State()
new_state.name = "California"
# Add the new State object to the FileStorage instance
fs.new(new_state)
# Save the FileStorage instance to a file
fs.save()
print("New State: {}".format(new_state))

# Get all State objects from the FileStorage instance again
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State object
another_state = State()
another_state.name = "Nevada"
# Add the new State object to the FileStorage instance
fs.new(another_state)
# Save the FileStorage instance to a file
fs.save()
print("Another State: {}".format(another_state))

# Get all State objects from the FileStorage instance again
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete the first State object from the FileStorage instance
fs.delete(new_state)

# Get all State objects from the FileStorage instance again
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
