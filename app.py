import streamlit as st

# Your braille_to_char and braille_word_to_str functions
# You can import them from your main code or paste here

# For now, a minimal example mapping:
braille_to_letter = {
    (1,): 'A', (1,2): 'B', (1,4): 'C', (1,4,5): 'D', (1,5): 'E',
    # add the rest...
}

def braille_to_char(braille_keys):
    mapping = {'Q': 1, 'W': 2, 'E': 3, 'D': 4, 'K': 5, 'O': 6, 'P': 7}
    dots = set()
    for key in braille_keys:
        if key in mapping:
            dots.add(mapping[key])
    return tuple(sorted(dots))

def braille_word_to_str(braille_word):
    result = ''
    for braille_char in braille_word:
        result += braille_to_letter.get(braille_char, '?')
    return result

st.title("Braille to Text Converter")

st.write("Enter Braille keys separated by spaces (e.g., Q W for dots 1 and 2).")

input_keys = st.text_input("Enter keys:")

if input_keys:
    keys_list = input_keys.strip().upper().split()
    braille_char = braille_to_char(keys_list)
    letter = braille_to_letter.get(braille_char, None)
    if letter:
        st.success(f"Braille dots {braille_char} → Letter: {letter}")
    else:
        st.error(f"Invalid Braille pattern: {braille_char}")
