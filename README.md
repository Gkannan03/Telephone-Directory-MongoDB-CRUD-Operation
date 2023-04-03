# Telephone-Directory-MongoDB-CRUD-Operation
Objective:



Solution:

Create a mongodb document called "Telephone_directory" and a colletion name called "Telephone_numebers_collection"

    from pymongo import MongoClient
    client=MongoClient("mongodb://localhost:27017/")
    db=client["Telephone_directory"]
    mycol=db["Telephone_numbers_collection"]

CRUD Operation
# Creating dcuments into a colection
To insert many document in a collection, use insert_many() method.

      mycol.insert_many([{"Name":"aimee Zank","Number": 123582456, 'Place': 'Italy', 'Postal': 60214}, {"Name":"Aurelia Menendez","Number": 97852456, 'Place': 'Paris','Postal': 6084}, {"Name":"Bao Ziglar","Number": 875201656, 'Place': 'Korea', 'Postal': 52014},{"Name":"Zachary Langlais","Number": 76695256, 'Place': 'Italy','Postal': 60214}, {"Name":"Salena Olmos","Number": 99955224, 'Place': 'Germany', 'Postal': 6994}, {"Name":"Daphne Zheng","Number": 85425224, 'Place': 'Canada', 'Postal': 9714}]) 
      for i in mycol.find():
      print(i)

To insert one document in a collection, use insert_one() method.
      
      mycol.insert_one({"Name": 'Rio', "Number": 9654892, "Place": 'Sweden', "Postal": 1145})
      for i in mycol.find():
          print(i)

# Reading document in a collection.

find all documents in the collection
      
      for i in mycol.find():
          print(i)
          
find only specific document in a collection
      
      for i in mycol.find({'Name': 'Salena Olmos'}):
          print(i)
          
# Update document in a collection

To update one document in a colletion use update_one() function.
Eg: The document in the collection which contains place Canada needs to be updated with the postal code 8000

      query = {'Place': 'Canada'}
      update = {"$set": {'Postal': 8000}}
      mycol.update_one(query, update)
      for i in mycol.find():
          print(i)
          
To update multiple document in a colletion use update_many() function.
Eg: The documents with the place as "italy" needs to be updated its postal code as 78520

      query= {"Place": "Italy"}
      new_values= {"$set": {'Postal': 78520}}
      mycol.update_many(query, new_values)
      for i in mycol.find():
          print(i) 
          
# 4. Delete document in a collection

To delete one document in a colletion use delete_one() function.
Eg: To delete the document of the person named Bao Ziglar, give the field name (key) and the value. Here 'Name' is the field, 'Bao Ziglar' is the value 

      mycol.delete_one({"Name": "Bao Ziglar"})
      for i in mycol.find():
          print(i)
          
To delete multiple document in a colletion use delete_many() function.
Eg: Delete the documents where the 'Place' as 'Italy'

      mycol.delete_many({"Place": "Italy"})
      for i in mycol.find():
          print(i)
