import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(data)

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

dict_data = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "count": [grey_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

data_fr = pd.DataFrame(dict_data)

print(data_fr.to_csv("count_of_color.csv"))
