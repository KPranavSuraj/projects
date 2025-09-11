import random

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

WORD_CATEGORIES = {
    "Animals": [
        {"word": "giraffe", "hint": "The tallest land animal."},
        {"word": "elephant", "hint": "The largest land animal."},
        {"word": "kangaroo", "hint": "It carries its baby in a pouch."},
    ],
    "Technology": [
        {"word": "python", "hint": "A popular programming language."},
        {"word": "robot", "hint": "A machine that can act like a human."},
        {"word": "internet", "hint": "Connects the world digitally."},
    ],
    "Space": [
        {"word": "astronaut", "hint": "Someone who travels to space."},
        {"word": "planet", "hint": "Orbits a star and may support life."},
        {"word": "galaxy", "hint": "A massive group of stars and planets."},
    ],
    "Objects": [
        {"word": "piano", "hint": "A large musical instrument with keys."},
        {"word": "umbrella", "hint": "Used to stay dry in the rain."},
        {"word": "backpack", "hint": "Used to carry books or supplies."}
    ]
}

def choose_word():
    category = random.choice(list(WORD_CATEGORIES.keys()))
    word_data = random.choice(WORD_CATEGORIES[category])
    return word_data["word"], word_data["hint"], category

def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_round():
    word, hint, category = choose_word()
    guessed_letters = set()
    wrong_letters = set()
    attempts = len(HANGMAN_PICS) - 1

    print("\n🎮 New Game Started!")
    print("📚 Category:", category)
    print("💡 Hint:", hint)

    while attempts > 0:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
        print("\nWord:", display_progress(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters | wrong_letters)))
        print("❌ Wrong guesses left:", attempts)

        guess = input("🔠 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single letter.\n")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("✅ Good guess!\n")
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You guessed the word:", word.upper())
                return True
        else:
            wrong_letters.add(guess)
            attempts -= 1
            print("❌ Wrong guess.\n")

    print(HANGMAN_PICS[-1])
    print("\n💀 Game over! The word was:", word.upper())
    return False

def main():
    score = 0
    rounds_played = 0
    print("===== Welcome to Enhanced Hangman! =====")

    while True:
        result = play_round()
        rounds_played += 1
        if result:
            score += 1

        print(f"\n🏆 Score: {score}/{rounds_played}")
        play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\n👋 Thanks for playing! Final Score:", score, "/", rounds_played)

if __name__ == "__main__":
    main()
