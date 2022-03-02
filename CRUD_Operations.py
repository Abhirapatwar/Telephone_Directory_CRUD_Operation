import pymongo
connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
# x=client.list_database_names()
# print(x)

####################################### Creating a database

teledir_db=client['Telephone_Directory']
teledir_db['data_collection']
document=[{
	"name": "Anuj",
	"phone_number": "1000000001",
	"place": "yavatmal"
}, {
	"name": "Amol",
	"phone_number": "2000000002",
	"place": "nashik"
}, {
	"name": "Arjun",
	"phone_number": "3000000003",
	"place": "nagpur"
}, {
	"name": "Dev",
	"phone_number": "4000000004",
	"place": "Aurangabad"
}, {
	"name": "kartik",
	"phone_number": "5000000005",
	"place": "yavatmal"
}]
teledir_db.data_collection.insert_many(document)
x=client.list_database_names()
# print(x)
# ['Telephone_Directory', 'admin', 'config', 'local', 'student_database']

####################################### listing available collections

print(teledir_db.list_collection_names())
# ['data_collection']

####################################### Updating a data

data_to_update=teledir_db.data_collection.find_one({"phone_number":"1000000001"})
update_to={'$set':{"phone_number":"1100000011"}}
teledir_db.data_collection.update_one(data_to_update,update_to)

####################################### Retrieving a data

updated_data=teledir_db.data_collection.find_one({"phone_number":"1100000011"})
# print(updated_data)
# {'_id': ObjectId('621ec803d19eb1dcce2dddd3'), 'name': 'Anuj', 'phone_number': '1100000011', 'place': 'yavatmal'}

####################################### Deleting a data

query={'name': 'Amol'}
teledir_db.data_collection.delete_one(query)
# print(list(teledir_db.data_collection.find({})))
# [{'_id': ObjectId('621ec803d19eb1dcce2dddd3'), 'name': 'Anuj', 'phone_number': '1100000011', 'place': 'yavatmal'},
#  {'_id': ObjectId('621ec803d19eb1dcce2dddd5'), 'name': 'Arjun', 'phone_number': '3000000003', 'place': 'nagpur'},
#  {'_id': ObjectId('621ec803d19eb1dcce2dddd6'), 'name': 'Dev', 'phone_number': '4000000004', 'place': 'Aurangabad'},
#  {'_id': ObjectId('621ec803d19eb1dcce2dddd7'), 'name': 'kartik', 'phone_number': '5000000005', 'place': 'yavatmal'}]
