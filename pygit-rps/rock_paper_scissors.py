import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS Game")
        self.root.geometry("400x450")

        # Game State
        self.language = "EN"  # Default language
        self.options = ["rock", "paper", "scissors"]

        # Translations
        self.text_data = {
            "EN": {
                "title": "Choose your move!",
                "lang_btn": "Español",
                "rock": "Rock", "paper": "Paper", "scissors": "Scissors",
                "win": "You Win! 🎉", "lose": "You Lose! 🤖", "tie": "It's a Tie! 🤝",
                "result_fmt": "Computer chose: {cp}"
            },
            "ES": {
                "title": "¡Elige tu jugada!",
                "lang_btn": "English",
                "rock": "Piedra", "paper": "Papel", "scissors": "Tijera",
                "win": "¡Ganaste! 🎉", "lose": "¡Perdiste! 🤖", "tie": "¡Empate! 🤝",
                "result_fmt": "La PC eligió: {cp}"
            }
        }

        # UI Elements
        self.lang_button = tk.Button(root, text="Español", command=self.toggle_language)
        self.lang_button.pack(pady=10, padx=10, anchor="ne")

        self.label_title = tk.Label(root, text="Choose your move!", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        self.btn_rock = tk.Button(btn_frame, text="🪨\nRock", width=10, height=5, command=lambda: self.play("rock"))
        self.btn_rock.grid(row=0, column=0, padx=5)

        self.btn_paper = tk.Button(btn_frame, text="📄\nPaper", width=10, height=5, command=lambda: self.play("paper"))
        self.btn_paper.grid(row=0, column=1, padx=5)

        self.btn_scissors = tk.Button(btn_frame, text="✂️\nScissors", width=10, height=5,
                                      command=lambda: self.play("scissors"))
        self.btn_scissors.grid(row=0, column=2, padx=5)

        self.label_result = tk.Label(root, text="", font=("Arial", 12))
        self.label_result.pack(pady=20)

    def toggle_language(self):
        self.language = "ES" if self.language == "EN" else "EN"
        t = self.text_data[self.language]

        # Update UI Text
        self.lang_button.config(text=t["lang_btn"])
        self.label_title.config(text=t["title"])
        self.btn_rock.config(text=f"🪨\n{t['rock']}")
        self.btn_paper.config(text=f"📄\n{t['paper']}")
        self.btn_scissors.config(text=f"✂️\n{t['scissors']}")
        self.label_result.config(text="")

    def play(self, user_choice):
        computer_choice = random.choice(self.options)
        t = self.text_data[self.language]

        # Map internal choice to translated name for display
        cp_translated = t[computer_choice]
        result_msg = t["result_fmt"].format(cp=cp_translated)

        if user_choice == computer_choice:
            final_res = t["tie"]
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            final_res = t["win"]
        else:
            final_res = t["lose"]

        self.label_result.config(text=f"{result_msg}\n{final_res}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsUI(root)
    root.mainloop()