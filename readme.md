About:
A simple python/pygame pipline for rendering 3d objects. (Lighting has not been implemented yet)
<img width="686" height="634" alt="Screenshot from 2026-04-19 17-26-15" src="https://github.com/user-attachments/assets/35116e64-ca07-4603-89d6-20053b543d7d" />
Usage:
In your project, import the package and use:
from pythreedee import setup
setup.run()
This will create a blank window.
To add shapes use
setup.render.init_object("type", [args], "id")
In the base version of the package, there are 4 types of objects, 0(cube), 1(pyramid), 2(sphere), 3(polygon)
The arguments are formated with a list, identical for every shape except the polygon. [x, y, z, size, pitch, yaw] and the polygon has ,points, faces] added to it.
The id is just a string that can be used to refer to the object later. for example you can initialize an object with an id of "obj1",
then later run the init function again with different parameters and same ID, and "obj1" will take on the new parameters.
For polygons the points and faces arguments are two lists. Points is formated as such: [[x, y, z], [x, y, z], etc] where x, y, and z are relative to the center of the object.
Faces is another list formated as such: [(0, 1, 2), (2, 3, 4), etc] where each number is a point that will be connected into a face, and each tuple is one face.
Here is an example init:
setup.render.init_object("0", [0, 0, 200, 200, 45, 45], "obj1")
custom shapes:
Since this package currently only has 4 shapes, to add more shapes you can either:
create a polygon with the points and faces of your shape,
or locate the 'shapes.py' file in the package and create a new class named however you like with def __init__(self, size) in it,
and inside the __init__ function, have self.size = size, self.hs = size/2, hs = self.hs, self.points = [points here, you can use hs to make it relative to size], self.faces = [faces here]
example:
class Cube:
    def __init__(self, size):
        self.size = size
        self.hs = size / 2

        hs = self.hs  # local shortcut

        self.points = [
            [-hs,  hs, -hs],
            [-hs, -hs, -hs],
            [hs, -hs, -hs],
            [hs,  hs, -hs],
            [-hs,  hs,  hs],
            [-hs, -hs,  hs],
            [hs, -hs,  hs],
            [hs,  hs,  hs],
        ]

        self.faces = [
            (0, 1, 2), (0, 2, 3),  # back
            (4, 5, 6), (4, 6, 7),  # front
            (0, 1, 5), (0, 5, 4),  # left
            (2, 3, 7), (2, 7, 6),  # right
            (1, 2, 6), (1, 6, 5),  # bottom
            (0, 3, 7), (0, 7, 4)   # top
        ]

After this, find the render.py file and scroll to the bottom.
Add
elif objtype == "4":
        objects[id] = {"type": 4, "x": args[0], "y": args[1], "z": args[2], "size": args[3], "yaw": args[4], "pitch": args[5]}
to the def init_object() function.
Next find the def build_object_points() function at line 74
add
    elif obj["type"] == 4:
        shape = shapes.your object class name here(obj["size"])
And now you can initialize your object by using the setup.render.init_object function with the type being "4"
That was very complicated so I might add a .blend converter or smth so you can import .blend files directly or smth

instalation:
To install the package, click the green 'code' dropdown in the top right of the repo page, and click 'download zip'
once the zip file is downloaded, extract it. Once extracted open a terminal at your project directory, and if you have a virtual environment activate it.
Run: pip install "path/to/package/parent/directory/pythreedee_aw"
example, if it was installed in my Downloads directory (linux)
pip install "/home/<myusername>/Downloads/pythreedee_aw"


if you managed to read this without having a stroke, congratulations!
