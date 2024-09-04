# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje:
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def average_word_len(file_text: str) -> float:
    lines = []
    lines.append(file_text)
    words_packed = []
    word_len = []
    for line in file_text:
        words_packed.append(line.split())

    unpack_word = [" ".join(packs) for packs in words_packed]

    for word in unpack_word:
        word_len.append(len(word))

    return sum(word_len) / word_counter(file_text)


def most_used_word(file_text: str) -> int:
    words_list: list[str] = []

    for line in file_text:
        words_list += line.split()

    counter = 0
    characters = words_list[0]

    for i in words_list:
        curr_frequency = words_list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            characters = i

    return counter, characters


def word_counter(file_text: str) -> int:
    word_count = 0
    for line in file_text:
        word_count += len(line.split())
    return word_count


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def main():
    sentences = read_from_file(
        "en_resa_genom_svenska_skogen.txt"
    )  # Här har du nu en lista av strängar från den inlästa filen.

    print(word_counter(sentences))
    print(most_used_word(sentences))
    print(average_word_len(sentences))


if __name__ == "__main__":
    main()
