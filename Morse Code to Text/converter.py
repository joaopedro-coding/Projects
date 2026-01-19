from morse_code import MORSE_CODE_DICT, REVERSE_MORSE_DICT

class Converter:

    def encrypt(self, text_to_morse:str) -> str:
        """Converts a text into morse code"""
        return "".join(MORSE_CODE_DICT.get(char.upper(), "") for char in text_to_morse)