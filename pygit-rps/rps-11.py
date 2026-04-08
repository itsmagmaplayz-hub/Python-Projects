import tkinter as tk
import random
import math

class RPS11CircleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS-11 Circular")
        self.root.geometry("700x750")
        self.root.configure(bg="#2c3e50")

        # Game State (Order matters!)
        self.options = [
            "rock", "fire", "scissors", "snake", "human", 
            "wolf", "sponge", "paper", "air", "water", "dragon"
        ]
        self.emojis = {
            "rock": "🪨", "fire": "🔥", "scissors": "✂️", "snake": "🐍", "human": "🧍",
            "wolf": "🐺", "sponge": "🧽", "paper": "📄", "air": "💨", "water": "💧", "dragon": "🐲"
        }
        
        self.canvas_size = 600
        self.center = self.canvas_size / 2
        self.radius = 220  # Distance of buttons from center

        # UI Setup
        self.label_title = tk.Label(root, text="RPS-11: Choose Your Move", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
        self.label_title.pack(pady=10)

        # Canvas for drawing arrows
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="#2c3e50", highlightthickness=0)
        self.canvas.pack()

        self.label_result = tk.Label(root, text="Click a button to start!", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
        self.label_result.pack(pady=20)

        self.buttons = {}
        self.create_circular_layout()

    def create_circular_layout(self):
        angle_step = 360 / len(self.options)

        for i, opt in enumerate(self.options):
            # Calculate angle in radians
            angle_rad = math.radians(i * angle_step - 90) # -90 to start at the top
            
            x = self.center + self.radius * math.cos(angle_rad)
            y = self.center + self.radius * math.sin(angle_rad)

            btn = tk.Button(
                self.root, 
                text=f"{self.emojis[opt]}\n{opt.capitalize()}",
                font=("Arial", 9, "bold"),
                width=8, height=3,
                command=lambda o=opt: self.play(o)
            )
            # Place button on top of canvas
            btn.place(in_=self.canvas, x=x, y=y, anchor="center")
            self.buttons[opt] = (x, y)

    def draw_arrows(self, winner_opt):
        self.canvas.delete("arrow") # Clear old arrows
        
        start_x, start_y = self.buttons[winner_opt]
        winner_idx = self.options.index(winner_opt)
        
        # In RPS-11, you beat the NEXT 5 items
        for i in range(1, 6):
            loser_idx = (winner_idx + i) % 11
            loser_opt = self.options[loser_idx]
            end_x, end_y = self.buttons[loser_opt]
            
            # Draw line with arrow head
            self.canvas.create_line(
                start_x, start_y, end_x, end_y,
                arrow=tk.LAST, fill="#f1c40f", width=2, tags="arrow",
                arrowshape=(16, 20, 6)
            )

    def play(self, user_choice):
        computer_choice = random.choice(self.options)
        
        user_idx = self.options.index(user_choice)
        comp_idx = self.options.index(computer_choice)
        
        # Logic to find the winner
        win_indices = [(user_idx + i) % 11 for i in range(1, 6)]
        
        if user_choice == computer_choice:
            result_text = f"Both chose {self.emojis[user_choice]} {user_choice.upper()}\nIt's a Tie!"
            self.canvas.delete("arrow")
        elif comp_idx in win_indices:
            result_text = f"Computer chose {self.emojis[computer_choice]} {computer_choice}\nYOU WIN! 🎉"
            self.draw_arrows(user_choice) # Show what you beat
        else:
            result_text = f"Computer chose {self.emojis[computer_choice]} {computer_choice}\nYOU LOSE! 🤖"
            self.draw_arrows(computer_choice) # Show what the computer beat

        self.label_result.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = RPS11CircleUI(root)
    root.mainloop()