from converter import Converter
from morse_code_exception import MorseTranslationError

convert = Converter()

try:
    result = convert.encrypt("Helloçá> World")
    print(result)
    print(convert.decrypt(result))
except MorseTranslationError as e:
    print(e)
except Exception as e:
    print(e)