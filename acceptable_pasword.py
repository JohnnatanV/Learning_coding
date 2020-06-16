"the length should be bigger than 6."

def is_acceptable_password(str):
    print(True) if (len(str) >= 6) is True else print(False)


if __name__ == '__main__':
    print("Example:")
    is_acceptable_password('short')

#    These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
