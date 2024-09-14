hp = 150
Brona = 300
lvl = 100

print("Здоровье", hp, "Броня", Brona )
neme = input("Ведите имя персонажа: ")
print(f"Приветствую вас, {neme}!")

_class = input("Ввыберете роль: Мог, Повстанец, Д-класс, Учоный, SCP: ")

# if 5 > 10:
#     print("Это правда")
# elif 11 > 10:
#     print("Это тоже правда")

if _class == "Мог":
    hp = hp * 2
    Brona = Brona * 1

elif _class == "Учоный":
    hp = hp * 1
    Brona = Brona - 2

elif _class == "Повстанец":
    hp = hp * 2
    Brona = Brona - 2

elif _class == "Д-класс":
    hp = hp * 1
    Brona = Brona * 1

elif _class == "SCP":
    hp = hp * 2
    Brona = Brona * 2

    print(f"Ваш новый класс: {_class}, Новые характеристики:, \nЗдоровье {hp} \nБроня {Brona}")