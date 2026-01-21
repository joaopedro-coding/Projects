from converter import Converter

converter = Converter()

result = converter.encrypt("Hello World")
print(result)
print(converter.decrypt(result))