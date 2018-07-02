
class Blueprint_Handler():

    def __init__(self):

        # blueprint format is [shape, position, type]
        self.left_wall_blueprint = [
            ["vertical_wall", (-300, -200), "vertical"],
            ["right_lean_wall", (-300, -100), "roof"],
            ["vertical_wall", (-225, 0), "vertical"],
            ["left_lean_wall", (-225, 100), "floor"],
            ["vertical_wall", (-300, 200), "vertical"],
            ["right_lean_wall", (-300, 300), "roof"],
            ["vertical_wall", (-225, 400), "vertical"],
            ["left_lean_wall", (-225, 500), "floor"],
            ["vertical_wall", (-300, 400), "vertical"],
            ["right_lean_wall", (-300, 400), "roof"],
            ["vertical_wall", (-225, 400), "vertical"],
            ["left_lean_wall", (-225, 400), "floor"],
            ["vertical_wall", (-300, 400), "vertical"],
            ["right_lean_wall", (-300, 400), "roof"],
            ["vertical_wall", (-225, 400), "vertical"],
            ["left_lean_wall", (-225, 400), "floor"],
            ["vertical_wall", (-300, 400), "vertical"],
            ["right_lean_wall", (-300, 400), "roof"],
            ["vertical_wall", (-225, 400), "vertical"],
            ["left_lean_wall", (-225, 400), "floor"],
            ["vertical_wall", (-300, 400), "vertical"],
            ["right_lean_wall", (-300, 400), "roof"],
            ["vertical_wall", (-225, 400), "vertical"],
            ["left_lean_wall", (-225, 400), "floor"],
            ["vertical_wall", (-300, 400), "vertical"],
            ["right_lean_wall", (-300, 400), "roof"],
            ["right_lean_wall", (-225, 400), "roof"],
            ["right_lean_wall", (-150, 400), "roof"],

        ]

        # blueprint format is [shape, position, type]
        self.right_wall_blueprint = [
            ["vertical_wall", (220, -200), "vertical"],
            ["right_lean_wall", (220, -100), "floor"],
            ["vertical_wall", (295, 0), "vertical"],
            ["left_lean_wall", (295, 100), "roof"],
            ["vertical_wall", (220, 200), "vertical"],
            ["right_lean_wall", (220, 300), "floor"],
            ["vertical_wall", (295, 400), "vertical"],
            ["left_lean_wall", (295, 500), "roof"],
            ["vertical_wall", (220, 400), "vertical"],
            ["right_lean_wall", (220, 400), "floor"],
            ["vertical_wall", (295, 400), "vertical"],
            ["left_lean_wall", (295, 400), "roof"],
            ["vertical_wall", (220, 400), "vertical"],
            ["right_lean_wall", (220, 400), "floor"],
            ["vertical_wall", (295, 400), "vertical"],
            ["left_lean_wall", (295, 400), "roof"],
            ["vertical_wall", (220, 400), "vertical"],
            ["right_lean_wall", (220, 400), "floor"],
            ["vertical_wall", (295, 400), "vertical"],
            ["left_lean_wall", (295, 400), "roof"],
            ["vertical_wall", (220, 400), "vertical"],
            ["right_lean_wall", (220, 400), "floor"],
            ["vertical_wall", (295, 400), "vertical"],
            ["left_lean_wall", (295, 400), "roof"],
            ["left_lean_wall", (220, 400), "roof"],
            ["left_lean_wall", (145, 400), "roof"],

        ]
