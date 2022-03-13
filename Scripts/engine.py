import tkinter
import random
#Window Geometry is X: 300, Y: 275

class PlaceObject:
    """A basic Class used to make placing tkinter objects more easy for me."""
    def __init__(self, objectData, x, y, anchor):

        self.x = x
        self.y = y
        self.anchor = anchor
        

        self.objectData = objectData
        # I think this converts all the place data of an instance into one single dictionary so it's usable by gui.py
        self.objectData = {
            "x": x,
            "y": y,
            'anchor': anchor
        }

# Template Setup: labelClass(placeData, x, y, anchor)
# Make sure to leave PlaceData as None

# "placeGT" means: place Greeting Text.
placeGT = PlaceObject(None, 150, 0, anchor=tkinter.N)
# "PlaceHT" means: place Help Text.
placeHT = PlaceObject(None, 150, 50, anchor=tkinter.N)
# "placeCT" means: place Credits Text.
placeCT = PlaceObject(None, 0, 275, anchor=tkinter.SW)

# "placeLS" means: place Less Than Symbol
placeLS = PlaceObject(None, 140, 175, anchor=tkinter.CENTER)

# "placeCB" means: place Calculate Button
placeCB = PlaceObject(None, 140, 230, anchor=tkinter.CENTER)

# "placeRN" means: place Result Number
placeRN = PlaceObject(None, 140, 125, anchor=tkinter.CENTER)

# "placeminIE" means: place Minimum Integer Entry Box
placeminIE = PlaceObject(None, 75, 175, anchor=tkinter.CENTER)
# "placemaxIE" means: place Maximum Integer Entry Box
placemaxIE = PlaceObject(None, 210, 175, anchor=tkinter.CENTER)



#Just some debug messages to test if engine.py isn't funtioning.
uiList = [placeGT, placeCT, placeHT, placeLS, placemaxIE, placeminIE, placeCB, placeRN]

for x in uiList:
    print("DEBUG:", x, "- placedata: ", x.objectData)

print("\nThe Engine is working without fail!")