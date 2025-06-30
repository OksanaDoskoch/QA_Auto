class Rhombus:
    def __init__(self, side_a, angle_a):
        self._side_a = None
        self._angle_a = None
        self._angle_b = None
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side length must be greater than 0.")
            super().__setattr__("_side_a", value)

        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Angle A must be between 0 and 180 degrees.")
            super().__setattr__("_angle_a", value)
            super().__setattr__("_angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("Angle B is set automatically and cannot be changed directly.")

        else:
            super().__setattr__(name, value)

    def get_side_a(self):
        return self._side_a

    def get_angle_a(self):
        return self._angle_a

    def get_angle_b(self):
        return self._angle_b

    def __str__(self):
        return f"Rhombus: side = {self._side_a}, angle A = {self._angle_a}, angle B = {self._angle_b}"

rh = Rhombus(10, 60)
print(rh)
print(rh.get_side_a())
print(rh.get_angle_b())