def get_book_words(content_string):
    return f"Found {len(content_string.split())} total words"


def get_character_count(content_string):

    character_dictionary = {}

    for char in content_string:
        char = char.lower()
        if char not in character_dictionary:
            character_dictionary[char] = 1
        else:
            character_dictionary[char] += 1

    return character_dictionary
