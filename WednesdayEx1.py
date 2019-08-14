## Lists

# name = 'hayley'
# level = 5
# awesomeness = 95.5
# is_raining = True


# backpack = []
# # print()


# backpack = [
#     'drink bottle',
#     'yoghurt',
#     'headphones',
#     'laptop',
# ]
# # print (backpack)

# backpack.append('blueberries')
# backpack.append('book')
# backpack.append('pythons')

# # print (backpack)

# # print (backpack[0])

# backpack[0] = 'lunchbox'

# print (backpack)

# print ()
# name = 'emma'
# print(name[1])

# for index, item in enumerate(backpack):
#     print(index, item)

# counter = 0
# for item in backpack:
#     print(counter, item)
#     counter += 1

# counter = 0
# while counter < len(backpack):
#     print(counter, backpack[counter])
#     counter += 1

# for numbers in range(1,11):
#     print(numbers)
# print('end of for loop')

# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 1
# print('end of while loop 1')


# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1
# print('end of while loop 2')


## Tuples
# person = ('emma', 'awesome')
# print(person)




## Example 1


def card_flip():
    five_by_five_grid = [
        ['X','0','X','X','X'],
        ['X','X','0','0','0'],
        ['X','0','X','0','X'],
        ['0','X','X','X','X'],
        ['X','0','0','X','X'],
    ]

card_flip()

# #user input coordinates
# coordinate = input('Enter a coordinate in the format (x,y)') 

# for row in five_by_five_grid:
#     xcounter = 0
#     for char in row:
#         if char == 'X':
#             xcounter += 1
#         if xcounter % 2 == 0:
#             five_by_five_grid.append('0')
#         else:
#             five_by_five_grid.append('X')
    

#what are the coordinates (x, y)
#user input translated to list indexes
#if coords= x, replace with y. Else y replace with x.


