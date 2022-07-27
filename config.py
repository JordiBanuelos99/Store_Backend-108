import pymongo
import certifi

con_str = "mongodb+srv://JordiBanuelos99:Redfox3015@cluster0.eyqpn.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Organic_Store")