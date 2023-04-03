from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["Telephone_directory"]
mycol=db["Telephone_numbers_collection"]


# 1. Insert one record into a collection

mycol.insert_one({"Name": 'Rio', "Number": 9654892, "Place": 'Sweden', "Postal": 1145})
for i in mycol.find():
    print(i)


# Insert many records into a collection
mycol.insert_many([{"Name":"aimee Zank","Number": 123582456, 'Place': 'Italy', 'Postal': 60214}, {"Name":"Aurelia Menendez","Number": 97852456, 'Place': 'Paris', 'Postal': 6084},
                   {"Name":"Bao Ziglar","Number": 875201656, 'Place': 'Korea', 'Postal': 52014}, {"Name":"Zachary Langlais","Number": 76695256, 'Place': 'Italy', 'Postal': 60214},
                   {"Name":"Salena Olmos","Number": 99955224, 'Place': 'Germany', 'Postal': 6994}, {"Name":"Daphne Zheng","Number": 85425224, 'Place': 'Canada', 'Postal': 9714}])
for i in mycol.find():
    print(i)


# 2. Reading document in a collection

# find all documents in the collection
for i in mycol.find():
    print(i)

# find only specific collection
for i in mycol.find({'Name': 'Salena Olmos'}):
    print(i)


# 3. Update document in a collection

# update one documents in the collection

query = {'Place': 'Canada'}
update = {"$set": {'Postal': 8000}}
mycol.update_one(query, update)
for i in mycol.find():
    print(i)

# update many documents in the collection
query= {"Place": "Italy"}
new_values= {"$set": {'Postal': 78520}}
mycol.update_many(query, new_values)
for i in mycol.find():
    print(i)



# 4. Delete document in a collection

# Delete one document in a collection
mycol.delete_one({"Name": "Bao Ziglar"})
for i in mycol.find():
    print(i)

# Delete multiple document in a collection}
mycol.delete_many({"Place": "Italy"})
for i in mycol.find():
    print(i)
