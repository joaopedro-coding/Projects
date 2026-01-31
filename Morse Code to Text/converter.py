from morse_code import MORSE_CODE_DICT, REVERSE_MORSE_DICT
from morse_code_exception import MorseTranslationError
from unidecode import unidecode

class Converter:

    def normalize_text(self, text:str) -> str:
        """Remove any strange accent"""
        return unidecode(text).upper().strip()

    def encrypt(self, text_to_morse:str) -> str:
        """Converts a text into morse code string"""
        clean_text = self.normalize_text(text_to_morse)

        # Check for any invalid character
        invalid_chars = [char for char in clean_text if char not in MORSE_CODE_DICT]
        if invalid_chars:
            raise MorseTranslationError(f"Invalid characters: {' '.join(set(invalid_chars))}")

        # .strip() removes the space before and after the string
        words = clean_text.split(" ")

        # Translate each letter into morse
        encoded_words = [" ".join(MORSE_CODE_DICT.get(char, "") for char in word) for word in words]
        
        # Group the words with a / so the user know when there is a space
        return " / ".join(encoded_words)
    
    def decrypt(self, morse_to_text:str) -> str:
        """Converts a morse code into a text string"""

        clean_text = self.normalize_text(morse_to_text).strip()

        # .strip() removes the space before and after the string
        words = morse_to_text.split(" ")

        # Joins each letter returning a full word
        try:
            return "".join(REVERSE_MORSE_DICT.get(char, "") for char in words)
        except KeyError as e:
            raise MorseTranslationError(f"Invalid keyword or invalid morsecode {e}")