possible_words: list[str] = []


def open_file(file: str):
    global possible_words

    previous = ""
    with open(file, "r", encoding="utf-8") as file_handler:
        while True:
            try:
                line = file_handler.readline().lower().split()
                if (
                    line[-1] in ("imenica", "glagol", "pridjev")
                    and len(line[1]) > 2
                    and line[1] != previous
                ):
                    possible_words.append(line[1])
                    previous = line[1]
            except:
                break


def check_word(word: str):
    if len(word) <= 2:
        return 2
    if word not in possible_words:
        return 1
    if word[-2:] == "ka":
        return 3
    return 0


def get_word(input: str):
    possible_output = []
    for word in possible_words:
        if word[:2] == input[-2:]:
            possible_output.append(word)
            # return word
    return possible_output


if __name__ == "__main__":
    open_file("HR_Txt-624.txt")
    while True:
        inputed_word = input("Upiši riječ: ").lower()
        match check_word(inputed_word):
            case 1:
                print("Ova riječ nije u riječniku!")
                print("Svejedno se nastavlja")
            case 2:
                print("Riječ je prekratka!")
                print("Riječ mora imati više od 2 slova!")
                continue
            case 3:
                print("Kaladont!")
                continue

        output = get_word(inputed_word)
        print(f"Moguće riječi: {output}")
        print(f"Moguće riječi: {len(output)}")
