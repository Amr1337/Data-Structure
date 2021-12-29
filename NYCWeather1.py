import os

#print(os.getcwd())
weather_dict= {}

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(",")
        date = tokens[0]
        try:
            temp = int(tokens[1])
            weather_dict[date] = temp
        except:
            "Invalid, Ignore row"

print(weather_dict)
print(weather_dict["Jan 9"])
print(weather_dict["Jan 4"])