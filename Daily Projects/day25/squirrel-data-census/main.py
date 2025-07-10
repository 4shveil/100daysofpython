import pandas as pd

df = pd.read_csv("/Users/Dell/Documents/python-stuff/day 25/squirrel-data-census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

new_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [df["Primary Fur Color"].value_counts()["Gray"], 
              df["Primary Fur Color"].value_counts()["Cinnamon"], 
              df["Primary Fur Color"].value_counts()["Black"]],
}

new_df = pd.DataFrame(new_data)
new_df.to_csv("/Users/Dell/Documents/python-stuff/day 25/squirrel-data-census/squirrel_count.csv")
