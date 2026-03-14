# 1-This is a Excercise for LIst in Python. 

expense=[
    {'January':1200},
    {'February':2000},
    {'March':2500},
    {'April':3000}
]


# 1- in Feb how much expense was xtra than January
xtra_expense=expense[1]['February']-expense[0]['January']
# print(xtra_expense)


# 1st quarter expenses
expenses = expense[0]['January']+expense[1]['February']+expense[2]['March']
# print(expenses)


# items() : method in Python returns a view object containing all key-value pairs of the dictionary as tuples
# for i in expense:
#     for key ,value in i.items():
#         if value ==2000:
            # print(f'In {key} month your expense was {value}')


# adding new month expense 
expense.append({'May':2500})
# print(expense)


# just returned an items and got 200 returned from February
expense[1]['February']=2000-200
print(expense)


# =========================================================================
# =========================================================================
# You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print('length of list: ',len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)



# 3. You realize that you need to add 'black panther' after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)


""" 4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code."""

heros[1:3]=['doctor strange']
print(heros,'\n')


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# print(dir([]))
heros.sort()
print('sorted LIST:')
print(heros)