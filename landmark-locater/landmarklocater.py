#def class Landmark(Object):
    #GPS coordinate of place, name, description, builtdate, image

    #class var: GPS coordinate (set to input) <- is this necessary? probably not
    #class method 1: prettyprint place, name, description, builtdate, image
    #class method 2: pass sexagesimal coordinates of landmark to convert_to_decimal, store returned value as property on landmark instance
    #class method 3: take input of decimal coordinate
        # convert it to radians
        # compute the distance between landmark and input using the equirectangular approximation or haversine formula:
            # http://www.movable-type.co.uk/scripts/latlong.html
        # return that value

#function 1 (convert_to_decimal): convert degree/min/sec to decimal coordinates and return decimal value
#function 2 (sort_by_distance): sort all landmarks by their distance from you and return the nearest 3 in order from nearest to farthest

class Landmark:
    def __init__(self, name, coordinates_x, coordinates_y, description, built_date=None, image=None):
        self.name = name
        self.coordinates_x = coordinates_x
        self.coordinates_y = coordinates_y
        self.description = description
        self.built_date = built_date
        self.image = image

    def prettyprint(self):
        print self.name
        print "Built " + str(self.built_date)
        print self.description

    def get_sexagesimal():
        return self.sexagesimal

def convert_to_decimal(sexagesimal):
    # check if data is in the correct format to be interpreted, give error if not (using regex?)
    # regex interpretation of sexagesimal
    # mathematical conversion


    """ alex notes
    if you want to convert '123' --> 123, do:   int('123')  '123.123' --> 123.123 do: float('123.123.')

    '44_44_55'.split('_')
    import re
    re.match(r'\d{2}_\d{2}_\d{2}\.\d{2}_[NWES]', sexagesimal)
    """
    pass

def sort_by_distance(*args):
    # grab self.decimal_coordinates from each instance
    # for each loop them to calculate_distance
    pass



empirestatebuilding = Landmark("Empire State Building", "40_44_54.36_N", "73_59_08.36_W", "The Empire State Building is very tall.", 1931, "Image here")
brooklynbridge = Landmark("Brooklyn Bridge", "40.70569_N", "73.99639_W", "The Brooklyn Bridge connects Manhattan to Brooklyn and sucks to bike on.", 1883, "Image here")
chryslerbuilding = Landmark("Chrysler Building", "40_45_6.12_N", "73_58_31.08_W", "The Chrysler Building is in the Art Deco style and was designed by William Van Alen.", 1930, "Image here")
worldtradecenter = Landmark("One World Trade Center", "40_42_46.8_N", "74_0_48.6_W", "1 WTC used to be called the Freedom Tower until they realized that was dumb.", 2014, "Image here")

