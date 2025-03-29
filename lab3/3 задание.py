list1 = input("Введите первый список через пробел:").split()
list2 = input("Введите второй список через пробел:").split()

num1 = [x for x in list1 if x.isdigit()]
num2 = [y for y in list2 if y.isdigit()]

if not num1 or not num2:
    print("Один или оба списка не содержат чисел.")
else:
    set1 = set(num1)
    set2 = set(num2)

    set3 = set1 & set2
    set4 = set1.intersection(set2)

    set3_str = ' '.join(set3) if set3 else "нет общих элементов"
    set4_str = ' '.join(set4) if set4 else "нет общих элементов"

    print("Общие элементы '&':", set3_str)
    print("Общие элементы '.intersection()':", set4_str)
