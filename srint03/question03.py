def create_account(user_name: str, password: str, secret_words: list):
    def check(password_: str, secret_words_: list):
        if password != password_ or len(secret_words) != len(secret_words_):
            return False
        else:
            temp = secret_words_[:]
            for word in secret_words:
                if word not in temp:
                    continue
                del temp[temp.index(word)]

            if len(temp) > 1:
                return False
            else:
                return True

    if len(password) >= 6 and not password.islower() \
                          and not password.isupper() \
                          and not password.isalpha() \
                          and not password.isalnum():
        return check
    else:
        raise ValueError