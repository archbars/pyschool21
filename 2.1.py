import os


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


def get_ingredients_from_string(reciept):
    ingridients = {}
    list = []
    for i in range(int(reciept[1])):
        list.append({'ingridient_name': reciept[2 + i].split(' | ')[0].lower(),'quantity': int(reciept[2 + i].split(' | ')[1].lower()),'measure': reciept[2 + i].split(' | ')[2].lower()})
        ingridients.update({reciept[0].lower(): list})
    return ingridients


def get_from_file():
    script_dir = os.path.dirname(__file__)
    reciepts = open(script_dir+'/reciept.txt','r')
    ingred=[]
    for line in reciepts:
        if not line=="\n":
            ingred.append(line.replace('\n', ''))
        else:
            cook_book.update(get_ingredients_from_string(ingred))
            ingred.clear()
    create_shop_list()


cook_book = {}
get_from_file()
