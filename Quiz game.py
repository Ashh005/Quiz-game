import tkinter as tk
from tkinter import messagebox, simpledialog

# Questions data
questions = [
    {
        "question": "Who is the first Prime Minister of India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhash Chandra Bose", "Sardar Patel"],
        "answer": "Jawaharlal Nehru"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Canberra", "Melbourne", "Perth"],
        "answer": "Canberra"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Jupiter", "Mars", "Mercury"],
        "answer": "Mars"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["Ag", "Au", "Gd", "Go"],
        "answer": "Au"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["Rabindranath Tagore", "Bankim Chandra", "Subramania Bharati", "Sarojini Naidu"],
        "answer": "Rabindranath Tagore"
    }
]

prize_money = [1000, 5000, 10000, 20000, 50000]

# Function to save the score
def save_score(name, score):
    with open("scores.txt", "a") as f:
        f.write(f"{name} - Rs. {score}\n")

# Main Game Class
class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("KBC Quiz Game")
        self.root.geometry("500x400")
        self.score = 0
        self.q_index = 0

        self.player_name = simpledialog.askstring("Welcome", "Enter your name:")

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=480)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", font=("Arial", 12), variable=self.var, value="", wraplength=400)
            btn.pack(anchor="w", padx=50, pady=2)
            self.options.append(btn)

        self.submit_btn = tk.Button(root, text="Submit", font=("Arial", 12), command=self.check_answer)
        self.submit_btn.pack(pady=20)

        self.status_label = tk.Label(root, text="Prize: Rs. 0", font=("Arial", 12))
        self.status_label.pack()

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            q = questions[self.q_index]
            self.question_label.config(text=q["question"])
            self.var.set(None)
            for i, opt in enumerate(q["options"]):
                self.options[i].config(text=opt, value=opt)
        else:
            messagebox.showinfo("Game Over", f"Congratulations {self.player_name}!\nYou won Rs. {self.score}")
            save_score(self.player_name, self.score)
            self.root.destroy()

    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an answer!")
            return

        correct = questions[self.q_index]["answer"]
        if selected == correct:
            self.score += prize_money[self.q_index]
            self.status_label.config(text=f"Prize: Rs. {self.score}")
            self.q_index += 1
            self.load_question()
        else:
            messagebox.showerror("Wrong Answer", f"Wrong answer!\n{self.player_name}, you won Rs. {self.score}")
            save_score(self.player_name, self.score)
            self.root.destroy()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = KBCGame(root)
    root.mainloop()
