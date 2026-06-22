import random
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# Secret Number
secret_number = random.randint(1, 100)
attempts = 0

# Title
title = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="#00ffd5"
)
title.pack(pady=20)

# Instructions
instruction = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="white"
)
instruction.pack(pady=10)

# Entry Box
guess_entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center",
    width=10,
    bd=5
)
guess_entry.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="Start guessing...",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="#ffd166"
)
result_label.pack(pady=10)

# Attempts Label
attempt_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
attempt_label.pack()

# Check Function
def check_guess():
    global attempts

    try:
        user_guess = int(guess_entry.get())

        if user_guess < 1 or user_guess > 100:
            result_label.config(
                text="❌ Enter a number between 1 and 100",
                fg="red"
            )
            return

        attempts += 1
        attempt_label.config(text=f"Attempts: {attempts}")

        if user_guess == secret_number:
            result_label.config(
                text="🎉 Correct Guess!",
                fg="#00ff88"
            )

            if attempts <= 5:
                msg = "Outstanding! You're a guessing master 😎"
            elif attempts <= 10:
                msg = "Great Job! 👏"
            else:
                msg = "Nice! Keep practicing 👍"

            messagebox.showinfo(
                "You Won!",
                f"You guessed the number in {attempts} attempts!\n\n{msg}"
            )

        elif user_guess < secret_number:
            result_label.config(
                text="📉 Too Low! Try Higher",
                fg="#ffb703"
            )

        else:
            result_label.config(
                text="📈 Too High! Try Lower",
                fg="#ffb703"
            )

    except ValueError:
        result_label.config(
            text="⚠ Please enter a valid number",
            fg="red"
        )

# Guess Button
guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 14, "bold"),
    bg="#00adb5",
    fg="white",
    padx=15,
    pady=8,
    command=check_guess
)
guess_button.pack(pady=20)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    bg="#ff4d4d",
    fg="white",
    padx=10,
    pady=5,
    command=root.destroy
)
exit_button.pack()

# Run App
root.mainloop()