def get_num_of_characters(str_to_count):
    character = 0

    for character in range(len(str_to_count)):
        character = character + 1
    return character

def output_without_whitespace(str_to_count):
    return str_to_count.replace(" ", "")

if __name__ == '__main__':
    a = ''
    counts = 0
    number = 0
    str_to_count = str(input('Enter a sentence or phrase: \n'))

    print(f'\nYou entered: {str_to_count}')

    print(f'Number of characters: {get_num_of_characters(str_to_count)}')

    print(f'String with no whitespace: {output_without_whitespace(str_to_count)}')