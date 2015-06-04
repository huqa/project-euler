
def base10_to_base2_string(n):
    return bin(n)[2:]

def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    db_palindromes = []
    for n in range(1,1000000):
        if is_palindrome(str(n)) and is_palindrome(base10_to_base2_string(n)):
            db_palindromes.append(n)

    print(db_palindromes)
    print(sum(db_palindromes))
