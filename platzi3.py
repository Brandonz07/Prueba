def palindromo(p):
    p = p.replace(" ", "")
    p = p.lower()
    p_inver = p[::-1]
    if p == p_inver:
        return True
    else:
        return False

def run():
    p = input("introduzca una palabra: ")
    es_palindromo = palindromo(p)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")


if __name__ == "__main__":
    run()