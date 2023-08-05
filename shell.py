import Govayk

while True:
    text = input('Govayk > ')
    result, error = Govayk.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)