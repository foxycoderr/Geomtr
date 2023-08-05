import math

from logger import Logger
from converter import Angle, Line, Point


class Coordinator:
    """ Uses converted objects and properties to create coordinates for objects. """

    @staticmethod
    def create_coordinates(objects, properties):  # started working, code doesn't work (don't attempt to uncomment)
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
                    if angle.p2 == obj.name[0]:  # gathering angles in which the point in question appears
                        inp = angle.p2  # inp = initial point
                        cp1 = angle.p1  # cp = connection point, cp1 will be the one directly under inp as defined in plan
                        cp2 = angle.p3
                        Logger.log([inp, cp1, cp2], "coord")
                        # cp1_angle = 180  # gathering angles
                        # cp2_angle = 180-angle.value

                        angle_lines = []
                        for line in objects:
                            if isinstance(line, Line):  # gathering distances for angles
                                if inp in [line.p1, line.p2] and any([cp1 in [line.p1, line.p2], cp2 in [line.p1, line.p2]]):  # found connection line
                                    angle_lines.append(line)
                        Logger.log(angle_lines, "coord")
                        cp1_line = None
                        cp2_line = None
                        for line in angle_lines:
                            if cp1 in [line.p1, line.p2]:
                                cp1_line = line
                            else:
                                cp2_line = line

                        # TODO: make sure signs of offsets are correct
                        angle_sin = math.sin(math.radians(int(angle.value)))  # getting x offset to line length ratio
                        x_offset = angle_sin*int(cp2_line.length)
                        angle_cos = math.cos(math.radians(int(angle.value)))  # getting y offset to line length ration
                        y_offset = angle_cos*int(cp2_line.length)
                        coordinates.append([obj.name, (0,0)])
                        coordinates.append([cp1, (0, -int(cp1_line.length))])
                        coordinates.append([cp2, (-x_offset, -y_offset)])

            if obj is Line:
                pass

        Logger.log(f"Coordinator finished, {coordinates}", "coordinator")
        return coordinates
