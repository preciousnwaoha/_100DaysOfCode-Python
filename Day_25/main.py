# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))

# convert Pandas DataFrame to Dictionary
# data_dict = data.to_dict()
# print(data_dict)

# convert a Pandas Series to list
# temp_list = data['temp'].to_list()
# print(temp_list)

# stats are easy in pandas
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data["day"] == "Monday"])
# Challenge: get row where temp is max
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "store": [76, 56, 65],
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("squirrels_data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")