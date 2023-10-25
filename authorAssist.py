def print_menu():
    print("""MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit\n""")
def exec_menu(string, choice):
    if choice == 'c':
        get_num_of_non_WS_characters(string)
    elif choice == 'w':
        num_words(string)
    elif choice == 'f':
        fix_cap(string)
    elif choice == 'r':
        char_rep(string)
    elif choice == 's':
        fix_spaces(string)
def get_num_of_non_WS_characters(string):
    print('non-white space')
def num_words(string):
    print('number of words')
def fix_cap(string):
    print('fix cap')
def fix_spaces(string):
    print('fix spaces')
def char_rep(string):
    print('replace char')

if __name__ == '__main__':
    text = input('Enter text: ')

    print_menu()

    option = ''
    while option not in ['c', 'w', 'f', 'r', 's', 'q']:
        option = input('Give option: ')

    if option != 'q':
        exec_menu(text, option)