from parser import validate_file, get_language


print(validate_file("calculator.py"))
print(get_language("calculator.py"))

print(validate_file("app.js"))
print(get_language("app.js"))

print(validate_file("Main.java"))
print(get_language("Main.java"))

print(validate_file("image.jpg"))