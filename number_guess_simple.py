#!/usr/bin/env python3
# number_guess_simple.py
# Simple Number Guessing Game
# Features: Difficulty, hints (high/low + hot/warm/cold), simple score system, play again

import random

DIFFICULTIES = {
    "1": ("Easy",   1, 20, 8, 1),   # name, low, high, attempts, multiplier
    "2": ("Medium", 1, 50, 6, 2),
    "3": ("Hard",   1, 100, 5, 4),
}

def get_choice(prompt, choices):
    while True:
        c = input(prompt).strip()
        if c in choices:
            return c
        print("Invalid choice. Try again.")

def choose_difficulty():
    print("Choose difficulty:")
    for k, v in DIFFICULTIES.items():
        name, low, high, attempts, _ = v
        print(f" {k}. {name} (range {low}-{high}, attempts {attempts})")
    sel = get_choice("Enter 1 / 2 / 3: ", DIFFICULTIES.keys())
    name, low, high, attempts, mult = DIFFICULTIES[sel]
    return {"name": name, "low": low, "high": high, "attempts": attempts, "mult": mult}

def proximity_hint(target, guess):
    d = abs(target - guess)
    if d == 0:
        return ""
    if d <= 2:
        return "🔥 Very hot!"
    if d <= 5:
        return "🌡️ Hot!"
    if d <= 10:
        return "🙂 Warm."
    return "❄️ Cold."

def calculate_score(multiplier, attempts_left):
    return 50 * multiplier + attempts_left * 10

def play_round():
    diff = choose_difficulty()
    hints_on = input("Turn hints ON? (y/n): ").strip().lower() in ("y", "yes")
    target = random.randint(diff["low"], diff["high"])
    attempts_left = diff["attempts"]

    print(f"\nI'm thinking of a number between {diff['low']} and {diff['high']}.")
    print(f"You have {attempts_left} attempts. Good luck!\n")

    while attempts_left > 0:
        print(f"Attempts left: {attempts_left}")
        guess_raw = input(f"Enter your guess ({diff['low']}-{diff['high']}): ").strip()
        if not guess_raw.lstrip("-").isdigit():
            print("Please enter a valid integer.\n")
            continue
        guess = int(guess_raw)

        if guess == target:
            score = calculate_score(diff["mult"], attempts_left)
            print(f"\n🎉 Correct! The number was {target}.")
            print(f"⭐ Difficulty: {diff['name']} — Your score: {score}\n")
            return

        attempts_left -= 1
        if guess < target:
            print("Too low!")
        else:
            print("Too high!")
        if hints_on:
            print(proximity_hint(target, guess))
        print()

    print(f"\n❌ Out of attempts! The number was {target}. Better luck next time.\n")

def main():
    print("=== Number Guessing Game ===\n")
    player = input("Enter your name (or press Enter to stay 'Player'): ").strip() or "Player"
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print(f"\nThanks for playing, {player}! Goodbye 👋")
            break
        print()

if __name__ == "__main__":
    main()
