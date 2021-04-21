fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
        make_pie(4)
    except:
        fruit = fruits[index-2]
        print(fruit + " pie")
        


make_pie(4)


