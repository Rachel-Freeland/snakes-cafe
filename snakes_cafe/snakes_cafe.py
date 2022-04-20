from ast import Break


intro_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""
print(intro_message)

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Little Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print("""
Appetizers
----------""")
for appetizer in appetizers:
  print(appetizer)

print("""
Entrees
-------""")
for entree in entrees:
  print(entree)

print("""
Desserts
--------""")
for dessert in desserts:
  print(dessert)

print("""
Drinks
------""")
for drink in drinks:
  print(drink)

order_message = ("""
***********************************
** What would you like to order? **
***********************************
""")
print(order_message)

menu_item = input('> ')
order = []

while menu_item.title() != 'Quit':
  print('** 1 order of ' + menu_item.title() + ' have been added to your meal **')
  order.append(menu_item.title())
  menu_item = input('> ')

print('Order Summary: ' + ', '.join(str(item) for item in order))

