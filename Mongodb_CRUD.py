from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
x=input("Enter the database name: ",)
db=client[x]
y=input("Enter the collection name: ",)
mycol=db[y]


# 1. Insert a record into a collection
name = input("Enter the name:", )
number = input("Enter the number:", )
place = input("Enter the place:", )
mycol.insert_one({"Name": name, "Number": number, "Place": place})
for i in mycol.find():
    print(i)



# 2. Update_one
doc= mycol.find_one()
print('List of fields in the document', doc.keys())
Field_to_update = input("Enter the field name of the value to be changed:", )
Existing_name = input("Enter the existing value:", )
Update_name = input("Enter the update value:", )
query = {Field_to_update: Existing_name}
update = {"$set": {Field_to_update: Update_name}}
mycol.update_one(query, update)
for i in mycol.find():
    print(i)


# 3. Delete_one
doc= mycol.find_one()
print('List of fields in the document', doc.keys())
delete_doc_field = input("Enter the field name of the value to be deleted: ", )
delete_doc_value = input("Enter the value:", )
mycol.delete_one({delete_doc_field: delete_doc_value})
for i in mycol.find():
    print(i)
