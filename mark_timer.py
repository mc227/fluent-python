"""
chat gpt generated code
with mc timer requirements
"""
import time
import tkinter as tk
from PIL import Image, ImageTk

def timer(minutes):
    """
    docstring
    """
    seconds = minutes * 60
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, seconds - elapsed_time)

        if remaining_time == 0:
            break

        print(f"Time remaining: {int(remaining_time / 60)}:{int(remaining_time % 60)}", end='\r')
        time.sleep(1)

    display_gif()

def display_gif():
    """
    docstring
    """
    def update_gif():
        """
        docstring
        """
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

    gif_path = "./fluent-python/homer.gif"  # Change this path to the location of your GIF
    gif = Image.open(gif_path)

    photo = ImageTk.PhotoImage(gif)
    label = tk.Label(root, image=photo)
    label.pack()

    close_button = tk.Button(root, text="Close", command=close_app)
    close_button.pack()

    root.after(0, update_gif)
    root.mainloop()

if __name__ == "__main__":
    minutes = 1
    print("Countdown in progress...")
    timer(minutes)
