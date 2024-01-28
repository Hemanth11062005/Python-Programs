#dictionary comphrehensive

cities_in_F = {"New Yord":32, "Boston":75, "Los Angles":100, "Chicago":50}

cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

print(cities_in_C)

desc_cities = {key: ("Warm" if value>=40 else "Cold") for (key,value) in cities_in_F.items()}
print(desc_cities)