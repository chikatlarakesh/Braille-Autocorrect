# 🔤 Braille-to-Text Converter with Auto-Correction

This Python-based project converts simulated Braille key combinations into English text and provides word suggestions based on Levenshtein distance. It also supports text-to-speech output using the `pyttsx3` library.

## Live Demo

Try the live web app here: [Braille-Autocorrect on Streamlit](https://braille-autocorrect.streamlit.app/)

## 📌 Features

- ⠿ Braille input using keys (Q, W, E, D, K, O, P)
- ✅ Auto-completion and word suggestions using Levenshtein distance
- 🔊 Text-to-Speech output
- 📖 Dictionary-based word matching
- ✏️ Real-time correction prompts

## 🛠️ Tech Stack

- Python 3.x
- `pyttsx3` (Text-to-Speech)
- Custom dictionary logic

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/chikatlarakesh/Braille-Autocorrect.git
cd Braille-Autocorrect
```

### 2. Create & Activate Virtual Environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pyttsx3
```

### 4.  Run the Program

```bash
python3 main.py
```

## 📚 Dictionary

You can modify or add more words to `dictionary.txt` to expand the vocabulary.

---

## 🎯 Sample Usage

```bash
>> Q W
[DEBUG] Braille keys ['Q', 'W'] → (1, 2)
>> Q
[DEBUG] Braille keys ['Q'] → (1,)
>> Q D K
[DEBUG] Braille keys ['Q', 'D', 'K'] → (1, 4, 5)
>> END
Interpreted word: BAD
✔ Word found in dictionary.
```

## 🧠 Future Improvements

- Multilingual support  
- Image-to-Braille translation  
- Mobile-friendly interface  

---

**Author:** Rakesh Ch  
**GitHub:** [@chikatlarakesh](https://github.com/chikatlarakesh)  
**Project:** Part of a Braille Accessibility Initiative
