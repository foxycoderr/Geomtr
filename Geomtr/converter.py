from logger import Logger


class Point:  # stores point information
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.p1 = None  # following fields exist only to ease a process later on
        self.p2 = None

    def __str__(self):
        return str("point " + self.name)


class Line:  # stores line information
    def __init__(self, p1, p2, visible=True, length=None):
        self.p1 = p1
        self.p2 = p2
        self.visible = visible
        self.length = length

    def __str__(self):
        if not self.length:
            return str("line " + self.p1 + "-" + self.p2)
        else:
            return str("line " + self.p1 + "-" + self.p2 + " " + self.length)


class Angle:  # stores angles
    def __init__(self, p1, p2, p3, value):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.value = value

    def __str__(self):
        return str("angle " + self.value + " " + self.p1 + self.p2 + self.p3)


class Converter:  # contains function to convert keywords to classes
    """ Converts data parsed from text into classes. """

    def __init__(self):
        pass

    @staticmethod
    def convert_objects(object_keywords, dbm):  # converts objects to classes
        Logger.log("Started object conversion", "converter")
        objects = []
        properties = []
        for obj in object_keywords:
            if obj[0] in ["rectangle", "triangle"]:  # converts rectangles and triangles
                points = list(obj[1])
                for point in points:  # adding points
                    if not any(added_obj.name == point for added_obj in objects):
                        objects.append(Point(0, 0, point))

                added_obj = None
                index = 0
                for point in points:  # adding lines
                    p1 = point
                    try:
                        p2 = points[index+1]
                    except IndexError:
                        p2 = points[0]

                    if not any(added_obj.p1 == p1 and added_obj.p2 == p2 or added_obj.p1 == p2 and added_obj.p2 == p1 for added_obj in objects):
                        objects.append(Line(p1, p2))
                    index += 1
                if obj[0] == "rectangle":  # adding right angles in case rectangle is registered
                    index = 0
                    for point in points:
                        angle = Angle(points[index % 4], points[(index+1) % 4], points[(index+2) % 4], "90")
                        properties.append(angle)
                        index += 1

            if obj[0] == "point":  # converts points
                point = list(obj[1])
                if not any(added_obj.name == point for added_obj in objects):
                    objects.append(Point(0, 0, point))

        printable_objects = []
        for obj in objects:  # creates a nice-looking printable and loggable list of converted objects
            printable_objects.append(str(obj))

        Logger.log(f"Objects converted {printable_objects}", "converter")

        return [objects, properties]

    @staticmethod  # TODO: create lines for angles
    def convert_properties(property_keywords, objects, properties, dbm):  # converts keywords to classes
        Logger.log("Started property conversion", "converter")
        properties = properties
        objects_local = objects
        for prop in property_keywords:
            if prop[0] == "side":  # converting sides
                points = list(prop[1])
                if any(obj.p1 == points[0] and obj.p2 == points[1] or obj.p1 == points[1] and obj.p2 == points[0] for obj in objects_local):
                    index = 0
                    for obj in objects_local:
                        if obj.p1 == points[0] and obj.p2 == points[1] or obj.p1 == points[1] and obj.p2 == points[0]:
                            objects_local[index].length = prop[2]
                        index += 1
                else:
                    objects_local.append(Line(points[0], points[1], False, prop[2]))

            if prop[0] == "angle":  # converting angles
                points = list(prop[1])
                if not any(added_prop.p2 == points[1] and (added_prop.p1 == points[2] and added_prop.p3 == points[0] or added_prop.p1 == points[0] and added_prop.p3 == points[2]) for added_prop in properties):
                    properties.append(Angle(points[0], points[1], points[2], prop[2]))

        printable_objects = []
        for obj in objects:  # making nice list of conversions
            printable_objects.append(str(obj))

        printable_properties = []
        for prop in properties:  # another nice list of conversions
            printable_properties.append(str(prop))
        Logger.log(f"Properties converted {printable_properties} and possibly updated objects {printable_objects}", "converter")

        return [properties, objects_local]

    @staticmethod
    def validate(object_keywords, property_keywords, dbm):  # carries out second logic validation
        if dbm: print("Validating problem logic.")
        obj_valid = True
        obj_errors = []
        for object_kw in object_keywords:  # checks number of points per object (4 for rectangle etc.)
            if object_kw[0] == "rectangle":
                if len(object_kw[1]) != 4:
                    obj_valid = False
                    obj_errors.append(f"- rectangle {object_kw[1]} seems to not have 4 points. ")
            elif object_kw[0] == "triangle":
                if len(object_kw[1]) != 3:
                    obj_valid = False
                    obj_errors.append(f"- triangle {object_kw[1]} seems to not have 3 points. ")
            elif object_kw[0] == "point":
                if len(object_kw[1]) != 1:
                    obj_valid = False
                    obj_errors.append(f"- point {object_kw[1]} seems to have an invalid name (only one-letter point names are allowed). ")

        prop_valid = True
        prop_errors = []
        for property_kw in property_keywords:  # checks number of points per property (2 for each side, 3 for each angle)
            if property_kw[0] == "side":
                if len(property_kw[1]) != 2:
                    prop_valid = False
                    prop_errors.append(f" - side {property_kw[1]} seems to not have 2 points.")

            elif property_kw[0] == "angle":
                if len(property_kw[1]) != 3:
                    prop_valid = False
                    prop_errors.append(f" - angle {property_kw[1]} seems to not have 3 associated points.")

        if obj_valid is True and prop_valid is True:  # checking no errors were found, if they were, printing them
            if dbm: print("Problem logic OK, proceeding to draw diagram.")
            Logger.log("Logic OK", "converter")
        else:
            print("Problem seems to have logic issues. Errors are outlined below:")
            for error in obj_errors:
                print(error)
            for error in prop_errors:
                print(error)

        return [obj_valid, prop_valid]
