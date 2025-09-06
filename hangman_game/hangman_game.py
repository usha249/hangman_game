import random

# Hangman diagrams for each wrong guess
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

# Word list
WORDS = [
    "python", "developer", "hangman", "keyboard",
    "function", "terminal", "syntax", "variable", "computer"
]

# Choose a word
word = random.choice(WORDS)
guessed_letters = []
wrong_guesses = 0
max_wrong = len(HANGMAN_PICS) - 1

print("🎯 Welcome to the Hangman Game!")
print("🕹️ Guess the word one letter at a time.\n")

# Game loop
while wrong_guesses <= max_wrong:
    print(HANGMAN_PICS[wrong_guesses])
    
    # Show word progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("📌 Word:        ", display.strip())
    print("🔠 Guessed:     ", ' '.join(guessed_letters))
    print("❌ Wrong Left:  ", max_wrong - wrong_guesses)
    print("👀 Actual Word: ", word)  # For learning/demo

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 YOU WON! 🎊 The word was:", word)
        break

    # Get input
    guess = input("\n👉 Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter one valid letter.\n")
        continue
    if guess in guessed_letters:
        print("⚠️ Already guessed. Try a different letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!\n")
    else:
        print("❌ Incorrect!\n")
        wrong_guesses += 1

    # After guess: Show diagram again after step (✅ as you asked)
    print("\n📍 Updated Game State:")
    print(HANGMAN_PICS[wrong_guesses if wrong_guesses <= max_wrong else max_wrong])
    print("📌 Word:        ", ''.join([l + ' ' if l in guessed_letters else "_ " for l in word]))
    print("=" * 40 + "\n")

    # Check loss
    if wrong_guesses == max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("\n💀 GAME OVER! The correct word was:", word)
        break
