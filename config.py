import threading

# Shared variables
zoom_factor = 1.0
time_multiplier = 1.0
saved_time_multiplier = 0
paused = False
camera_speed = 0.001
lock = threading.Lock()
simulationRunning = True
rotation_x, rotation_y = 0, 0
