

import secrets
import string


class ID:
    
    @staticmethod
    def upper_case_alpha(length: int) -> str:
        alphabet = string.ascii_letters.upper()

        result = ''
        for count in range(length):
            result += ''.join(secrets.choice(alphabet))

        return result