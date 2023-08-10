""" Coordinator"""
import math

from logger import Logger
from converter import Angle, Line, Point


class Coordinator:
    """ Uses converted objects and properties to create coordinates for objects. """

    @staticmethod
    def create_coordinates(objects, properties):  # started working, not a completed module
        """ Creates coordinates for all points using data provided by converter, """
        Logger.log("Started coordinator", "coordinator")
        coordinates = []
        for obj in objects:
            if isinstance(obj, Point):  # processing points
                Logger.log(f"Found point {obj.name}", "coord")
                angles = []
                for prop in properties:  # gathering angles
                    if isinstance(prop, Angle):
                        angles.append(prop)
                Logger.log(f"Found angles {angles}", "coord")
                for angle in angles:
                    if angle.p_2 == obj.name[0]:  # gathering angles in which the point appears
                        inp = angle.p_2  # inp = initial point
                        cp1 = angle.p_1  # cp = connection point, cp1 will be the one under inp
                        cp2 = angle.p_3
                        Logger.log([inp, cp1, cp2], "coord")
                        # cp1_angle = 180  # gathering angles
                        # cp2_angle = 180-angle.value

                        angle_lines = []
                        for line in objects:
                            if isinstance(line, Line):  # gathering distances for points
                                if inp in [line.p_1, line.p_2] and any([cp1 in [line.p_1, line.p_2],
                                                                      cp2 in [line.p_1, line.p_2]]):
                                    angle_lines.append(line)
                        Logger.log(angle_lines, "coord")
                        cp1_line = None
                        cp2_line = None
                        for line in angle_lines:  # determining which line found is which
                            if cp1 in [line.p_1, line.p_2]:
                                cp1_line = line
                            else:
                                cp2_line = line

                        # TODO: make sure signs of offsets are correct
                        angle_sin = math.sin(math.radians(int(angle.value)))  # getting x offset
                        x_offset = angle_sin*int(cp2_line.length)  # to line length ratio
                        angle_cos = math.cos(math.radians(int(angle.value)))  # getting y offset
                        y_offset = angle_cos*int(cp2_line.length)  # to line length ratio
                        coordinates.append(Point(0, 0, obj.name))
                        coordinates.append(Point(0, -int(cp1_line.length), cp1))
                        coordinates.append(Point(-x_offset, -y_offset, cp2))

            if obj is Line:
                pass

        printable_ccordinates = []
        for point in coordinates:
            printable_ccordinates.append(point)
        Logger.log(f"Coordinator finished, {printable_ccordinates}", "coordinator")
        return coordinates
