cook_book = {}
with open('recepies', 'rt', encoding='Utf-8') as file:
    for l in file:
        dish_name = l.strip()
        dish = []
        count_ingridients = file.readline()
        for ingridients in range(int(count_ingridients)):
            cons_dish = file.readline()
            name, quantity, measure = cons_dish.split(' | ')
            dish.append({'ingredient_name': name,
                          'quantity': quantity,
                          'measure': measure
                         })

        blank_line = file.readline()
        cook_book[dish_name] = dish

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    recipes = {}
    for dish, sources in cook_book.items():
        if dish in dishes:
            for ingr in sources:
                counter = 0
                name = ingr['ingredient_name']
                if name in recipes:
                    counter = int(ingr['quantity']) * person_count
                recipes[name] = {'measure': ingr['measure'], 'quantities': int(ingr['quantity']) * person_count + counter}
    return recipes

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4))

