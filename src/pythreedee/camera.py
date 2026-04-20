
import math
import pygame
class Camera:
    def __init__(self):
        self.yaw = 0
        self.pitch = 0
        self.cam_x = 0
        self.cam_y = 0
        self.cam_z = -400
        self.right_mouse_held = False
        self.mouse_sensitivity = 0.005
        self.camera_speed = 1000
    def update(self, events):
        dt = 1/60
        #run every time an event is triggered
        for event in events:
            #exit when quit is called
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #region camera/mouse movement
            #change right_mouse_held when we press or release right mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # right click
                    self.right_mouse_held = True
        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.right_mouse_held = False
            #called whenever the mouse moves
            elif event.type == pygame.MOUSEMOTION:
                if self.right_mouse_held: #only move if rmb is down
                    #lock & hide mouse
                    pygame.mouse.set_visible(False)
                    pygame.event.set_grab(True)
                    dx, dy = event.rel #change x and y based on the amount moved
                    self.yaw += -dx * self.mouse_sensitivity #change pitch and yaw based on amount moved and mouse sensitivity
                    self.pitch += -dy * self.mouse_sensitivity
                    #clamp pitch so you cant look over yourself
                    self.pitch = max(-math.pi/2, min(math.pi/2, self.pitch))
                else:
                    #unlock & hide mouse
                    pygame.mouse.set_visible(True)
                    pygame.event.set_grab(False)
        # Calculate the forward vectors of the camera
        cam_forward_x = math.cos(self.pitch) * math.sin(self.yaw)
        cam_forward_y = math.sin(self.pitch)
        cam_forward_z = math.cos(self.pitch) * math.cos(self.yaw)

        # Check for keys
        keys = pygame.key.get_pressed()

        # forward/backward camera movement
        if keys[pygame.K_w]:
            self.cam_x -= cam_forward_x * self.camera_speed * dt
            self.cam_y -= cam_forward_y * self.camera_speed * dt
            self.cam_z += cam_forward_z * self.camera_speed * dt

        if keys[pygame.K_s]:
            self.cam_x += cam_forward_x * self.camera_speed * dt
            self.cam_y += cam_forward_y * self.camera_speed * dt
            self.cam_z -= cam_forward_z * self.camera_speed * dt

        # left/right camera movement
        right_x = math.sin(self.yaw - math.pi/2)
        right_z = math.cos(self.yaw - math.pi/2)

        if keys[pygame.K_d]:
            self.cam_x -= right_x * self.camera_speed * dt
            self.cam_z += right_z * self.camera_speed * dt

        if keys[pygame.K_a]:
            self.cam_x += right_x * self.camera_speed * dt
            self.cam_z -= right_z * self.camera_speed * dt
        # up/down camera movement
        if keys[pygame.K_SPACE]:
            self.cam_y -= self.camera_speed*dt
        if keys[pygame.K_LCTRL]:
            self.cam_y += self.camera_speed*dt