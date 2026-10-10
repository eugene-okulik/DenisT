PRICE_LIST = """тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р"""

new_list = PRICE_LIST.split()
keys = [x for x in new_list[0::2]]
values = [int(x.strip("р")) for x in new_list[1::2]]
new_dict = dict(zip(keys, values))
print(new_dict)
