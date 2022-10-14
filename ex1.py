name = input("Введите имя: ")
sur = input("Введите фамилию: ")
date = int(input("Введите год рождения: "))
print(name, "_", sur, "_", date)

name, sur = sur, name

date_2 = date + 60

print(name, "_", sur, "_", date)