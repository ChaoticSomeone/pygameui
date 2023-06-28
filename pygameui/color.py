
class Color:

    @staticmethod
    def colorRestrain(color):
        def clamp(x):
            if x < 0: x = 0
            if x > 255: x = 255
            return x

        red = int(round(color[0]))
        green = int(round(color[1]))
        blue = int(round(color[2]))

        return clamp(red), clamp(green), clamp(blue)