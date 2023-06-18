menu={"아메", "라떼", "차"}
print(menu, type(menu)) #{'아메', '라떼', '차'} <class 'set'>

menu=list(menu)
print(menu, type(menu)) #['아메', '라떼', '차'] <class 'list'>

menu = tuple(menu)
print(menu,type(menu)) #('아메', '차', '라떼') <class 'tuple'>

menu=set(menu)
print(menu, type(menu)) #{'라떼', '차', '아메'} <class 'set'>