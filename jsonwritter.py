#NOTE READ DATA
a_file = open("asd.json", "r")
json_obj = json.load(a_file)
a_file.close()

print(json_obj)

#NOTE Write Data

json_obj["studium"] = "WI"
a_file = open("asd.json", "w")
json.dump(json_obj, a_file)
a_file.close()

