from logger import Logger
from converter import Angle, Line, Point


class Coordinator:
    """ Uses converted objects and properties to create coordinates for objects. """

    @staticmethod
    def create_coordinates(objects, properties):  # started working, code doesn't work (don't attempt to uncomment)
        """for obj in objects:
            coordinates = []
            if obj is Point:
                angles = []
                for prop in properties:
                    if prop is Angle:
                        angles.append(prop)
                for angle in angles:
                    if angle.p2 == obj.name:
                        cp1 = angle.p1
                        cp2 = angle.p3

                        cp1_angle = 180
                        cp2_angle = 180-angle.value

                        for line in :

                        coordinates.append([obj.name, (0,0)], [cp1, ], [])


            if obj is Line:
                pass
"""