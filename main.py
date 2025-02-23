mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

count = 0
for names in mission_names:
  count = len(mission_names)
print("Total number of missions:", count)

total = 0
for word in mission_success:
  if word == True:
    total = total + 1
print("Number of successful missions:", total)

count = 0
sum = 0
for things in mission_success:
  count = count + 1
  sum = int(sum + things)
print("Success rate: " + str(round(sum / count * 100, 2)) + "%")

print("Missions launched before the year 2000:")

for years in mission_years:
  if years < 2000:
    print("-", mission_names[mission_years.index(years)])