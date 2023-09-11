contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter username'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Invalid input'

    return inner


@input_error
def add_contact(user_input):
    _, name, phone = user_input.split()
    contacts[name] = phone
    return f'Contact {name} added with phone {phone}'


@input_error
def change_number(user_input):
    _, name, phone = user_input.split()
    if name in contacts:
        contacts[name] = phone
        return f'Changed phone number for {name} to {phone}'
    else:
        return f'Contact {name} not found'


@input_error
def get_contact(user_input):
    _, name = user_input.split()
    if name in contacts:
        return f'Phone number for {name} is {contacts[name]}'
    else:
        return f'Contact {name} not found'


@input_error
def show_all_contacts(user_input):
    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    else:
        return 'No contacts'


@input_error
def main():
    print('How can I help you?')

    while True:
        user_input = input().lower()

        if user_input == 'good bye' or user_input == 'exit' or user_input == 'close':
            print('Good bye!')
            break
        elif user_input == 'hello':
            print('How can I help you?')
        elif user_input.startswith('add'):
            print(add_contact(user_input))
        elif user_input.startswith('change'):
            print(change_number(user_input))
        elif user_input.startswith('phone'):
            print(get_contact(user_input))
        elif user_input == 'show all':
            print(show_all_contacts(user_input))
        else:
            print('Invalid command, try again')


if __name__ == '__main__':
    main()
