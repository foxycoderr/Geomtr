""" Converter"""
from logger import Logger


class Point:
    """ Stores point info (coords, name) """
    def __init__(self, x, y, name):
        self.x_coord = x
        self.y_coord = y
        self.name = name
        self.p_1 = None  # following fields exist only to ease a process later on
        self.p_2 = None

    def __str__(self):  # configures what should be returned when str()
        # is applied to the class instance
        return str("point " + str(self.name) + " at " + str(self.x_coord) + "," + str(self.y_coord))



class Line:
    """ Stores line info (visibility, length, points) """
    def __init__(self, p1, p2, visible=True, length=None):
        self.p_1 = p1  # points used by the line
        self.p_2 = p2
        self.visible = visible
        self.length = length

    def __str__(self):  # configures what the class should return when stringed
        if not self.length:  # in case length isn't yet defined
            return str("line " + self.p_1 + "-" + self.p_2)
        else:
            return str("line " + self.p_1 + "-" + self.p_2 + " " + self.length)


class Angle:
    """ Stores angle data (points, deg) """
    def __init__(self, p1, p2, p3, value):
        self.p_1 = p1  # 3 points used to define an angle
        self.p_2 = p2
        self.p_3 = p3
        self.value = value  # angle degree

    def __str__(self):  # what the class should return when stringed
        return str("angle " + self.value + " " + self.p_1 + self.p_2 + self.p_3)


class Converter:
    """ Converts data parsed from text into classes. """

    @staticmethod
    def convert_objects(object_keywords):
        """ Converts objects (rects, triangles, points etc to classes. """
        Logger.log("Started object conversion", "converter")
        objects = []
        properties = []
        for obj in object_keywords:
            if obj[0] in ["rectangle", "triangle"]:  # converts rectangles and triangles
                points = list(obj[1])  # save point data from obj datalist
                for point in points:  # adding points
                    if not any(added_obj.name == point for added_obj in objects):  # checking the
                        objects.append(Point(0, 0, point))                         # point doesn't
                        # already exist

                added_obj = None
                index = 0
                for point in points:  # adding lines
                    p1 = point
                    try:
                        p2 = points[index+1]  # finding next point
                    except IndexError:
                        p2 = points[0]

                    if not any(added_obj.p_1 == p1 and added_obj.p_2 == p2 or added_obj.p_1 == p2
                               and added_obj.p_2 == p1 for added_obj in objects):
                        objects.append(Line(p1, p2))  # making sure line doesn't exist
                    index += 1
                if obj[0] == "rectangle":  # adding right angles in case rectangle is registered
                    index = 0
                    for point in points:  # no check is neede das to whether these angles
                        # exist (forced to 90)
                        angle = Angle(points[index % 4], points[(index+1) % 4], points[(index+2) % 4],
                                      "90")
                        properties.append(angle)
                        index += 1

            if obj[0] == "point":  # converts points
                point = list(obj[1])
                if not any(added_obj.name == point for added_obj in objects):  # chcking point
                    # doesn't exist already
                    objects.append(Point(0, 0, point))

        printable_objects = []
        for obj in objects:  # creates a nice-looking printable and loggable list of converted objs.
            printable_objects.append(str(obj))

        Logger.log(f"Objects converted {printable_objects}", "converter")

        return [objects, properties]

    @staticmethod  # TODO: add check that all points used in properties exist, create them with
    def convert_properties(property_keywords, objects, properties):
        """ Converts property (angle, length etc) to classes. """
        Logger.log("Started property conversion", "converter")
        properties = properties  # saving given data into variables
        objects_local = objects
        for prop in property_keywords:
            if prop[0] == "side":  # converting sides
                points = list(prop[1])  # next line checks whether line exists
                if any(obj.p_1 == points[0] and obj.p_2 == points[1] or obj.p_1 == points[1]
                       and obj.p_2 == points[0] for obj in objects_local):
                    index = 0
                    for obj in objects_local:
                        if obj.p_1 == points[0] and obj.p_2 == points[1] or obj.p_1 == points[1]\
                                and obj.p_2 == points[0]:
                            objects_local[index].length = prop[2]  # if it exists, just
                            # add length data to it
                        index += 1
                else:
                    objects_local.append(Line(points[0], points[1], False, prop[2]))  # else create

            if prop[0] == "angle":  # converting angles
                points = list(prop[1])  # NL checks angle doesn't already exist
                if not any(added_prop.p_2 == points[1] and (added_prop.p_1 == points[2] and added_prop.p_3 == points[0]
                                                            or added_prop.p_1 == points[0] and added_prop.p_3 == points[2]) for added_prop in properties):
                    properties.append(Angle(points[0], points[1], points[2], prop[2]))  # create it
                    line_1 = None  # these are the angle lines; if we create an angle ABC,
                    line_2 = None  # the architecture later on requires line AB and BC

                    lines = []
                    for line in objects_local:  # finding all lines among objects
                        if isinstance(line, Line):
                            lines.append(line)

                    for line in lines:  # finding whether the list of lines contains
                        # both the lines given
                        if (line.p_1 and line.p_2) in [points[0], points[1]]:
                            line_1 = line
                        if (line.p_1 and line.p_2) in [points[1], points[2]]:
                            line_2 = line

                    index = 0
                    for line in [line_1, line_2]:
                        if line is None:  # create lines in case they don't exist
                            objects_local.append(Line(points[index], points[(index+1) % 3],
                                                      length="5"))
                        index += 1

        printable_objects = []
        for obj in objects:  # making nice list of conversions
            printable_objects.append(str(obj))

        printable_properties = []
        for prop in properties:  # another nice list of conversions
            printable_properties.append(str(prop))

        Logger.log(f"Properties converted {printable_properties} and possibly updated objects "
                   f"{printable_objects}", "converter")

        return [properties, objects_local]

    @staticmethod
    def validate(object_keywords, property_keywords, dbm):
        """ Carries out additional logic validation. """
        if dbm: print("Validating problem logic.")
        obj_valid = True
        obj_errors = []
        for object_kw in object_keywords:  # checks number of points per object
            # (4 for rectangle etc.)
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
                    obj_errors.append(f"- point {object_kw[1]} seems to have an invalid "
                                      f"name (only one-letter point names are allowed). ")

        prop_valid = True
        prop_errors = []
        for property_kw in property_keywords:  # checks number of points per
            if property_kw[0] == "side":       # property (2 for each side, 3 for each angle)
                if len(property_kw[1]) != 2:
                    prop_valid = False
                    prop_errors.append(f" - side {property_kw[1]} seems to not have 2 points.")

            elif property_kw[0] == "angle":
                if len(property_kw[1]) != 3:
                    prop_valid = False
                    prop_errors.append(f" - angle {property_kw[1]} seems to not have 3"
                                       f" associated points.")

        if obj_valid is True and prop_valid is True:  # checking no errors were found,
            # if they were, printing them
            if dbm:
                print("Problem logic OK, proceeding to draw diagram.")
            Logger.log("Logic OK", "converter")
        else:
            print("Problem seems to have logic issues. Errors are outlined below:")
            for error in obj_errors:
                print(error)
            for error in prop_errors:
                print(error)

        return [obj_valid, prop_valid]
