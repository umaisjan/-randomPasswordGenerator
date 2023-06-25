import random
import string

# We want to generate a random password.
# Password should contain
#  - At least 1 upper case
#  - at least 1 lower case
#  - at least 1 digit
#  - at least 1 special character from (#$%^&*)
# Password should be 10 character long.

# create characters
SPECIAL_LETTERS = '#$%^&*'
ALL_CHARACTERS = string.ascii_letters + string.digits + SPECIAL_LETTERS
PASSWORD_LENGTH = 10


def generate_random_characters(characters: str, length: int) -> list[chr]:
    """
    Takes input as a list of possible characters and length of the list.
    Returns a list with random character and length match the input parameter length
    :param characters: a string containing all possible charactors
    :param length: length of the password
    :return: List of Characters
    """

    assert type(length) == int, "Length should be an Integer"
    seed = random.choices(characters, k=length)
    random.shuffle(seed)

    return seed


def validate_password(pwd: list[chr]) -> bool:
    """
    Applies different conditions and validates if the password is correct
    :param pwd: List of characters for password
    :return: a Boolean highlighting if password is correct or not
    """
    return any(x in pwd for x in string.ascii_letters) \
        and any(x in pwd for x in string.digits) \
        and any(x in pwd for x in SPECIAL_LETTERS) \
        and len(pwd) == 10


if __name__ == '__main__':
    password = generate_random_characters(characters=ALL_CHARACTERS, length=PASSWORD_LENGTH)
    while not validate_password(password):
        password = generate_random_characters(characters=ALL_CHARACTERS, length=PASSWORD_LENGTH)

    print(''.join(password))
