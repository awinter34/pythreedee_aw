from . import render
from . import camera
from . import window as w

def run(caption ="", wsize = (800, 800)):
    print("raaaaaan")
    window = w.Window(caption = caption, wsize = wsize)
    pygame = w.pygame
    clock = window.CLOCK
    c = camera.Camera()
    pygame.init()

    running = True
    while running:
        events = []
        for event in pygame.event.get():
            events.append(event)
            if event.type == pygame.QUIT:
                running = False

        c.update(events)
        window.clear()
        render.project_objects(c, window)
        pygame.display.flip()
        clock.tick(60)