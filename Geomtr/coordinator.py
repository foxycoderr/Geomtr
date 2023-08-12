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
                        Logger.log([str(inp), str(cp1), str(cp2)], "coord")
                        # cp1_angle = 180  # gathering angles
                        # cp2_angle = 180-angle.value

                        angle_lines = []
                        for line in objects:
                            if isinstance(line, Line):  # gathering distances for points
                                if inp in [line.p_1, line.p_2] and any([cp1 in [line.p_1, line.p_2],
                                                                        cp2 in [line.p_1,
                                                                                line.p_2]]):
                                    angle_lines.append(line)
                        Logger.log((line for line in angle_lines), "coord")
                        cp1_line = None
                        cp2_line = None
                        for line in angle_lines:  # determining which line found is which
                            if cp1 in [line.p_1, line.p_2]:
                                cp1_line = line
                            else:
                                cp2_line = line

                        point_object_cp1 = Point(0, -int(cp1_line.length), cp1)
                        point_object_inp = Point(0, 0, obj.name)

                        # look at coordinate calculation.png for variable names

                        angle_m = 90 - int(angle.value)
                        sin_m = math.sin(math.radians(angle_m))
                        cos_m = math.cos(math.radians(angle_m))
                        y_offset = -float(sin_m)*float(cp2_line.length)
                        x_offset = float(cos_m)*float(cp2_line.length)

                        coordinates.append(point_object_inp)
                        coordinates.append(point_object_cp1)
                        coordinates.append(Point(x_offset, y_offset, cp2))

            if obj is Line:
                pass

        printable_coordinates = []
        for point in coordinates:
            printable_coordinates.append(str(point))
        Logger.log(f"Coordinator finished, {printable_coordinates}", "coordinator")
        return coordinates
