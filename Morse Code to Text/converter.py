from morse_code import MORSE_CODE_DICT, REVERSE_MORSE_DICT

class Converter:

    def encrypt(self, text_to_morse:str) -> str:
        """Converts a text into morse code string"""

        # .strip() removes the space before and after the string
        words = text_to_morse.upper().strip().split(" ")

        # Translate each letter into morse
        encoded_words = [" ".join(MORSE_CODE_DICT.get(char, "") for char in word) for word in words]
        
        # Group the words with a / so the user know when there is a space
        return " / ".join(encoded_words)
    
    def decrypt(self, morse_to_text:str) -> str:
        """Converts a morse code into a text string"""

        # .strip() removes the space before and after the string
        words = morse_to_text.strip().split(" ")

        # Joins each letter returning a full word
        return "".join(REVERSE_MORSE_DICT.get(char, "") for char in words)