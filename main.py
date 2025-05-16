import pyttsx3

# ========== CONFIGURATIONS ==========
DEBUG = True       # Set to False to disable debug logs
TTS_ENABLED = True # Set to False to disable text-to-speech

# ========== BRAILLE MAPPING ==========
def braille_to_char(braille_keys):
    # Map keys to correct Braille dot numbers (1 to 6)
    mapping = {'Q': 1, 'W': 2, 'E': 3, 'D': 4, 'K': 5, 'O': 6, 'P': 7}  # P maybe ignored or adjusted if needed
    dots = set()
    for key in braille_keys:
        if key in mapping:
            dots.add(mapping[key])
    return tuple(sorted(dots))


braille_to_letter = {
    (1,): 'A', (1,2): 'B', (1,4): 'C', (1,4,5): 'D', (1,5): 'E',
    (1,2,4): 'F', (1,2,4,5): 'G', (1,2,5): 'H', (2,4): 'I', (2,4,5): 'J',
    (1,3): 'K', (1,2,3): 'L', (1,3,4): 'M', (1,3,4,5): 'N', (1,3,5): 'O',
    (1,2,3,4): 'P', (1,2,3,4,5): 'Q', (1,2,3,5): 'R', (2,3,4): 'S', (2,3,4,5): 'T',
    (1,3,6): 'U', (1,2,3,6): 'V', (2,4,5,6): 'W', (1,3,4,6): 'X', (1,3,4,5,6): 'Y', (1,3,5,6): 'Z',
    (3,4,5,6): '#'
}

NUMBER_MAP = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
}

# ========== BRAILLE WORD CONVERTER ==========
def braille_word_to_str(braille_word):
    result = ''
    number_mode = False
    for braille_char in braille_word:
        letter = braille_to_letter.get(braille_char, '?')
        if letter == '#':
            number_mode = True
            continue
        if number_mode:
            digit = NUMBER_MAP.get(letter)
            if digit:
                result += digit
            else:
                number_mode = False
                result += letter
        else:
            result += letter
    return result

# ========== TEXT SUGGESTION ENGINE ==========
def levenshtein_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[m][n]

def load_dictionary(filename):
    dictionary = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().upper()
                if word:
                    dictionary.append(word)
    except FileNotFoundError:
        print("Dictionary file not found!")
    return dictionary

def suggest_words(input_word, dictionary, max_suggestions=5):
    distances = [(levenshtein_distance(input_word, word), word) for word in dictionary]
    distances.sort()
    return [w for _, w in distances[:max_suggestions]]

def speak(text):
    if TTS_ENABLED:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

# ========== MAIN INTERACTION ==========
def main():
    dictionary = load_dictionary('dictionary.txt')
    braille_sentence = []
    print("Braille-to-Text Converter with Suggestions")
    print("Enter keys (Q W E D K O P). Type 'END' to end word, 'DONE' to end sentence.")

    while True:
        user_input = input(">> ").strip().upper()
        if user_input == 'DONE':
            break
        elif user_input == 'END':
            if not braille_sentence or not braille_sentence[-1]:
                print("No letters in current word.")
                continue
            word_chars = braille_sentence.pop()
            interpreted = braille_word_to_str(word_chars).upper()

            if DEBUG:
                print(f"[DEBUG] Interpreted word: {interpreted}")

            print("You entered:", interpreted)
            speak(interpreted)

            if interpreted in dictionary:
                print("✔ Word found in dictionary.")
            else:
                print("❌ Word not found in dictionary.")
                suggestions = suggest_words(interpreted, dictionary)
                print("🔍 Suggested closest words:")
                for i, word in enumerate(suggestions, 1):
                    print(f"{i}. {word}")

                choice = input("Would you like to add this word to the dictionary? (y/n): ").strip().lower()
                if choice == 'y':
                    with open('dictionary.txt', 'a') as f:
                        f.write(interpreted + '\n')
                    dictionary.append(interpreted)
                    print("✅ Word added to dictionary.")

            braille_sentence.append([])  # prepare for next word
        else:
            keys = user_input.split()
            valid_keys = {'D', 'W', 'Q', 'K', 'O', 'P', 'E'}
            if not all(k in valid_keys for k in keys):
                print("⚠ Invalid keys. Use only Q W E D K O P.")
                continue
            braille_char = braille_to_char(keys)
            if DEBUG:
                print(f"[DEBUG] Braille keys {keys} → {braille_char}")
            if not braille_sentence:
                braille_sentence.append([])
            braille_sentence[-1].append(braille_char)

    # Print full interpreted sentence
    full_words = [braille_word_to_str(word) for word in braille_sentence if word]
    final_output = ' '.join(full_words)
    print("\n📝 Final interpreted sentence:", final_output)
    speak(final_output)

if __name__ == "__main__":
    main()
