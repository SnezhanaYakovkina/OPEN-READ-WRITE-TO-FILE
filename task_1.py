from pprint import pprint

# task_1
cook_book = {}

with open('recipes.txt', encoding='utf-8') as file:
    for string in file:
        # print(string)
        name = string.strip()
        # print(name)
        quantity = int(file.readline().strip())
        # print(name, quantity)
        food = []
        for ingredients in range(quantity):
            ingr_dict = {}
            ingr = file.readline().split('|')
            ingr_dict['ingredient_name'] = ingr[0].strip()
            ingr_dict['quantity'] = ingr[1].strip()
            ingr_dict['measure'] = ingr[2].strip()
            # print(ingr)
            # print(ingr_dict)
            food.append(ingr_dict)
            # print(food)
        file.readline()
        cook_book[name] = food
# pprint(cook_book)

# task_2
    def get_shop_list_by_dishes(dishes, person_count):
        cooking_list = {}
        for dish in dishes:
            if dish in cook_book:
                # print(dish)
                for ingr in cook_book[dish]:
                    # print(ingr)
                    if ingr['ingredient_name'] not in cooking_list:
                        value = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
                        # print(cooking_list)
                        cooking_list[ingr['ingredient_name']] = value
                    else:
                        cooking_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count

        return cooking_list
    print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

# task_3

