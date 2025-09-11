import random

word_list = ['python', 'hangman', 'challenge', 'programming', 'openai', 'developer', 'algorithm']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ['_' for _ in chosen_word]

lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print(' '.join(display))

while '_' in display and lives > 0:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print(f"🔁 You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"❌ Wrong guess. You lose a life. Lives left: {lives}")

    print(' '.join(display))

if '_' not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over. The word was:", chosen_word)