# # with open("weather_data.csv", mode="r") as file:
# #     data = file.readlines()
# #
# # print(data)
# #
# # import csv
# #
# #
# # with open("weather_data.csv", mode="r") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #
# #             temperatures.append(int(row[1]))
# #
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # temp_list = data["temp"].to_list()
# # print(data["temp"].mean())
#
# print(data.day[data.temp == data.temp.max()])
# temp = int((data.temp[data.day == "Monday"]))
#
# cel = (temp - 32) * 5/9
#
# print(f"{temp} temp in F and {cel} temp in celcius")

import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(df.columns)
colors = df["Primary Fur Color"].dropna().unique().tolist()
# count = df[]
print(colors)
print(type(colors[0]))

color_count = []

for color in colors:
    print("inside")
    count = df["Primary Fur Color"][df["Primary Fur Color"] == color].count()
    color_count.append(count)

dict = {"Colors": colors, "Count": color_count}
print(dict)
df = pd.DataFrame.from_dict(dict)
print(df)
df.to_csv("new_data")


# df = pd.DataFrame()