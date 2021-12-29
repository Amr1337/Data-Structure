import os

#print(os.getcwd())

#class Weather:
#    def __init__(self):
#        self.MAX = 10
#        self.arr = [[] for i in range(self.MAX)]
temp_arr = []
nyc_weather = []

    def get_hash(self, key):
    h = 0
     for char in key:
        h += ord(char)
    return h % 10


with open('nyc_weather.csv', "r") as f:
    for line in f:
        tokens = line.split(",")
        date = tokens[0]
        try:
            temp = int(tokens[1])
            temp_arr.append(temp)
            nyc_weather.append([date, temp])
        except:
            print("Invalid temperature, Ignore row")

avg= sum(temp_arr) / len(temp_arr)

for element in nyc_weather:
    if element[0] == "Jan 9":
        print("The Temp on Jan 9 is :", element[1])





#print(nyc_weather)




#t = Weather()
#t.get_hash("Jan 11")
print(temp_arr)
print(avg)
print(max(temp_arr))
print(nyc_weather)