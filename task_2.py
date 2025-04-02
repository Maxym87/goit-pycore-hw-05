
def generator_numbers(text: str):
    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            continue

        