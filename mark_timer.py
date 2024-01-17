"""
mark_timer.py
"""
import time
import tkinter as tk
from PIL import Image, ImageTk

def timer(minutes):
    seconds = minutes * 60
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, seconds - elapsed_time)

        if remaining_time == 0:
            break

        minutes_display = int(remaining_time / 60)
        seconds_display = int(remaining_time % 60)

        # Zero-fill the minute and second values
        display_str = f"Time remaining: {str(minutes_display).zfill(2)}:{str(seconds_display).zfill(2)}"
        print(display_str, end='\r')
        
        time.sleep(1)

    display_gif()

def display_gif():
    def update_gif():
        try:
            gif.seek(gif.tell() + 1)
            photo = ImageTk.PhotoImage(gif)
            label.config(image=photo)
            label.image = photo
            if not close_requested:
                root.after(100, update_gif)
        except EOFError:
            gif.seek(0)  # Reset to the beginning
            root.after(100, update_gif)

    def close_app():
        global close_requested
        close_requested = True
        root.destroy()

    global close_requested
    close_requested = False

    root = tk.Tk()
    root.title("GIF Display")

    # Make the window topmost
    root.attributes('-topmost', True)

    gif_path = "./fluent-python/toph.gif"  # Change this path to the location of your GIF
    gif = Image.open(gif_path)

    # Resize the image to be bigger
    resized_gif = gif.resize((400, 400), Image.LANCZOS)

    photo = ImageTk.PhotoImage(resized_gif)
    label = tk.Label(root, image=photo)
    label.config(width=800, height=600)  # Adjust the width and height as needed
    label.pack()

    close_button = tk.Button(root, text="Close", command=close_app)
    close_button.pack()

    root.after(0, update_gif)
    root.mainloop()

if __name__ == "__main__":
    MINUTES = 0.5
    print("Countdown in progress...")
    timer(MINUTES)
