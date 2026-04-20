from . import shapes
import pygame
import math

objects = {}

drawpoint = False
drawface = True


def project(points, faces, window):
    f = 400
    projected = []

    for x, y, z in points:
        if z <= 0:
            projected.append(None)
            continue
        px = window.convertcanvas((x * f) / z)
        py = window.convertcanvas((y * f) / z)
        projected.append((px, py))

    if drawpoint:
        s = 6
        for p in projected:
            if p is not None:
                pygame.draw.rect(
                    window.SCREEN,
                    window.DARK_GREEN,
                    (p[0] - s / 2, p[1] - s / 2, s, s),
                )

    if drawface:
        face_depths = []

        for face in faces:
            z_avg = sum(points[i][2] for i in face) / len(face)
            face_depths.append((z_avg, face))

        # sort far → near
        face_depths.sort(reverse=True)

        for _, face in face_depths:
            pts = []
            skip = False

            for idx in face:
                if projected[idx] is None:
                    skip = True
                    break
                pts.append(projected[idx])

            if skip:
                continue

            pygame.draw.polygon(window.SCREEN, window.DARK_GREEN, pts)


def project_objects(camera, window):
    for obj_id in objects:
        obj = objects[obj_id]
        points, faces = build_object_points(obj, camera)
        project(points, faces, window)
    return points, faces

def center_points(points):
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    cz = sum(p[2] for p in points) / len(points)
    centered = [[x - cx, y - cy, z - cz] for x, y, z in points]
    return centered, (cx, cy, cz)


def build_object_points(obj, camera):
    # create base shape
    if obj["type"] == 0:
        shape = shapes.Cube(obj["size"])
    elif obj["type"] == 1:
        shape = shapes.Pyramid(obj["size"])
    elif obj["type"] == 2:
        shape = shapes.Sphere(obj["size"])
    elif obj["type"] == 3:
        points, faces = obj["points"], obj["faces"]
        shape = None

    if shape:
        points, faces = shape.points, shape.faces

    points, center = center_points(points)

    # object rotation
    points = rotate_xz(points, obj["yaw"])
    points = rotate_yz(points, obj["pitch"])

    # move back from center
    cx, cy, cz = center
    points = [[x + cx, y + cy, z + cz] for x, y, z in points]

    transformed = []

    for px, py, pz in points:
        # world transform
        world_x = px + obj["x"]
        world_y = py + obj["y"]
        world_z = pz + obj["z"]

        # camera translation
        rel_x = world_x - camera.cam_x
        rel_y = world_y - camera.cam_y
        rel_z = world_z - camera.cam_z

        transformed.append([rel_x, rel_y, rel_z])

    # camera rotation
    transformed = rotate_xz(transformed, -camera.yaw)
    transformed = rotate_yz(transformed, -camera.pitch)

    return transformed, faces


def rotate_xz(points, angle):
    new_points = []
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    for x, y, z in points:
        x1 = x * cos_a - z * sin_a
        z1 = x * sin_a + z * cos_a
        new_points.append([x1, y, z1])

    return new_points


def rotate_yz(points, angle):
    new_points = []
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    for x, y, z in points:
        y1 = y * cos_a - z * sin_a
        z1 = y * sin_a + z * cos_a
        new_points.append([x, y1, z1])

    return new_points


def init_object(objtype, args, id):
    if objtype == "0":
        objects[id] = {"type": 0, "x": args[0], "y": args[1], "z": args[2], "size": args[3], "yaw": args[4], "pitch": args[5]}
    elif objtype == "1":
        objects[id] = {"type": 1, "x": args[0], "y": args[1], "z": args[2], "size": args[3], "yaw": args[4], "pitch": args[5]}
    elif objtype == "2":
        objects[id] = {"type": 2, "x": args[0], "y": args[1], "z": args[2], "size": args[3], "yaw": args[4], "pitch": args[5]}
    elif objtype == "3":
        objects[id] = {"type": 3, "x": args[0], "y": args[1], "z": args[2], "size": args[3], "yaw": args[4], "pitch": args[5], "points": args[6], "faces": args[7]}