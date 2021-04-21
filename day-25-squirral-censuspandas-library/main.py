#fur color  Gray,Black,cinnamon

import pandas 

data = pandas.read_csv("squirrel_count.csv") # data frame
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])#
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])##series


data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count": [grey_squirrels, black_squirrels, red_squirrels]
}

df = pandas.DataFrame(data_dict)

df.to_csv("poor.csv")