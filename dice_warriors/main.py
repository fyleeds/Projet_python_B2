import builder

def main():
    char1 = builder.builder_characters()
    char1.json_save()
    char2 = builder.builder_characters()
    char2.json_save()
    print(char1)
    print(char2)

    while char1.is_alive() and char2.is_alive():
        char1.attack(char2)
        char2.attack(char1)

main()