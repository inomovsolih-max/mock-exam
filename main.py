def sort_keys_by_value(my_dict):
    saralangan = sorted(my_dict.items(), key=lambda x: x[1])
    return [kalit for kalit, _ in saralangan]



my_dict = {
    "t": 3,
    "p": 1,
    "y": 2,
    "o": 5,
    "h": 4,
    "n": 6,
}

for k in sort_keys_by_value(my_dict): 
    print(k)

print("salom dunyo")
