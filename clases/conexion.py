# import pymongo
# import json

# cliente=pymongo.MongoClient("mongodb://localhost:27017/")
# print(cliente.list_database_names())
# db=cliente["Talento_humano"]
# jose=db["persona"]
# martha=db["hojav"]

# with open ("C:/Users/linit/OneDrive/Escritorio/proyectoIpsKLYV/clases/hv.json") as k:
#     gatito=json.load(k)
# martha.insert_many(gatito)
# for i in martha.find():
#     print("------",i)

# with open("C:/Users/linit/OneDrive/Escritorio/proyectoIpsKLYV/clases/personas.json") as f:
#     data = json.load(f)

# jose.insert_many(data)
# for doc in jose.find():
#     print("-------",doc)