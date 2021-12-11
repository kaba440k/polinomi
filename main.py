def main():
    degree = int(input())
    polinom = ''
    mas_monoms = []
    for i in range(degree + 1):
        mas_monoms.append(input())
        ready_monom = monom(mas_monoms[0], degree)
        if ready_monom is not None:
            polinom += monom(mas_monoms[0], degree)
        del mas_monoms[0]
        degree -= 1
        if i == 0 and ready_monom[0] == "+":
            ready_monom.replace("+", "")

    print(polinom)


def monom(factor, degree_copy):
    degree_copy = str(degree_copy)
    if factor == '1':
        if degree_copy == '1':
            return "x "
        elif degree_copy == '0':
            return "1 "
        elif degree_copy != '0' and degree_copy != '1':
            return "x^" + degree_copy + " "

    elif factor == '0':
        return None

    elif factor != '0' and factor != '1':
        if degree_copy == '1' and factor[0] != "-":
            return "+" + factor + " * x "
        elif degree_copy == '1' and factor[0] == "":
            return factor + " * x "
        if degree_copy == '0':
            return factor
        if degree_copy != '0' and degree_copy != '1':
            return factor + " * x^" + degree_copy + " "


if __name__ == "__main__":
    main()
