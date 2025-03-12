from random import choice
from string import ascii_letters, digits


class Token:
    @staticmethod
    def generate_token():
        """Generate a new token."""
        return "".join(choice(ascii_letters + digits) for _ in range(64))
