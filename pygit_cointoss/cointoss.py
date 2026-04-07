import tkinter as tk
from PIL import Image, ImageTk
import random

class CustomCoinFlipper:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Texture Coin Toss")
        self.root.geometry("400x450")

        # --- LOAD YOUR IMAGES HERE ---
        # Adjust the (200, 200) to whatever size you want the coin to be
        self.heads_img = self.load_and_resize("heads.png", (200, 200))
        self.tails_img = self.load_and_resize("tails.png", (200, 200))
        
        self.images = [self.heads_img, self.tails_img]

        # UI Setup
        self.coin_display = tk.Label(root, image=self.heads_img)
        self.coin_display.pack(pady=30)

        self.flip_button = tk.Button(root, text="Flip Coin", font=("Arial", 14), 
                                    command=self.start_animation)
        self.flip_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Ready to flip!", font=("Arial", 12))
        self.status_label.pack()

    def load_and_resize(self, path, size):
        # Helper to load image, resize it, and convert for tkinter
        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def start_animation(self):
        self.flip_button.config(state="disabled")
        self.animate(0)

    def animate(self, count):
        # Rapidly swap images 12 times to simulate a spin
        if count < 12:
            current_img = self.images[count % 2]
            self.coin_display.config(image=current_img)
            # Schedule next frame in 80ms
            self.root.after(80, lambda: self.animate(count + 1))
        else:
            self.show_final_result()

    def show_final_result(self):
        # The actual 50/50 logic
        result = random.choice(["Heads", "Tails"])
        final_img = self.heads_img if result == "Heads" else self.tails_img
        
        self.coin_display.config(image=final_img)
        self.status_label.config(text=f"Result: {result}!")
        self.flip_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomCoinFlipper(root)
    root.mainloop()