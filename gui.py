import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from OpenGL.GL import *
from OpenGL.GLU import *
import config


updating_slider = False


def run_gui():
    global updating_slider

    def update_zoom_factor():
        with config.lock:
            config.zoom_factor = float(entry2.get())

    def update_camera_speed():
        with config.lock:
            config.camera_speed = float(entry3.get())

    def update_multiplier(val, entry1):
        global updating_slider
        if not updating_slider:  
            with config.lock:
                if not config.paused:
                    config.time_multiplier = float(val)
                    entry1.delete(0, tk.END)
                    entry1.insert(0, str(config.time_multiplier))

    def set_multiplier():
        global updating_slider
        try:
            with config.lock:
                value = float(entry1.get())
                if 0.1 <= value <= 1000:
                    if not config.paused:
                        config.time_multiplier = value
                        updating_slider = True 
                        slider1.set(value) 
                        updating_slider = False 
                else:
                    print("Value out of range! Please enter a value between 0.1 and 1000.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def toggle_pause():
        with config.lock:
            config.paused = not config.paused
            if config.paused:
                pause_button.config(text="Resume")
                config.saved_time_multiplier = config.time_multiplier
                config.time_multiplier = 0
            else:
                config.time_multiplier = config.saved_time_multiplier
                pause_button.config(text="Pause")


    def on_closing():
        if config.simulationRunning:
            messagebox.showwarning("Warning", "SSimulation is still active. Turn it off to turn off the interface!")
        else:
            root.destroy()

    def information():
        messagebox.showwarning("Information", "By holding the left mouse button and moving the mouse, the camera moves along the x and y axes.\n\nBy holding the right mouse button and moving the mouse, the camera rotates around the center of view.\n\nThe scroll wheel is used for zooming.")
       

    root = tk.Tk()
    root.title("User Interface")
    root.geometry("500x480")
    
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle the window close event

    slider_label1 = tk.Label(root, text="Time Multiplier (0.1 - 1000):")
    slider_label1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    entry1 = ttk.Entry(root) 
    entry1.insert(0, str(config.time_multiplier))

    slider1 = ttk.Scale(root, from_=0.1, to=1000, orient='horizontal', 
                        command=lambda val: update_multiplier(val, entry1))
    slider1.set(config.time_multiplier)
    slider1.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    entry_label1 = tk.Label(root, text="Set Exact Value of Time Multiplier:")
    entry_label1.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    entry1.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    confirm_button1 = ttk.Button(root, text="Confirm Time Multiplier", command=set_multiplier)
    confirm_button1.grid(row=1, column=2, padx=10, pady=10)

    entry_label2 = tk.Label(root, text="Set Value of Zoom Factor:")
    entry_label2.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    entry2 = ttk.Entry(root)
    entry2.insert(0, str(config.zoom_factor))
    entry2.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    confirm_button2 = ttk.Button(root, text="Confirm Zoom Factor", command=update_zoom_factor)
    confirm_button2.grid(row=2, column=2, padx=10, pady=10)

    entry_label3 = tk.Label(root, text="Set Value of Camera Speed:")
    entry_label3.grid(row=3, column=0, padx=10, pady=10, sticky='w')

    entry3 = ttk.Entry(root)
    entry3.insert(0, str(config.camera_speed))
    entry3.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    confirm_button3 = ttk.Button(root, text="Confirm Camera Speed", command=update_camera_speed)
    confirm_button3.grid(row=3, column=2, padx=10, pady=10)

    pause_button = ttk.Button(root, text="Pause", command=toggle_pause)
    pause_button.grid(row=4, column=0, padx=10, pady=10)

    information_button = ttk.Button(root, text="Information", command=information)
    information_button.grid(row=4, column=2, padx=10, pady=10)
    
    root.grid_columnconfigure(1, weight=1)
    root.mainloop()
