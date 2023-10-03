import json


#
# Client side - laver en json string
#

#directory
dict = {
  "Name": "Peter",
  "Address": "Roskilde",
  "Zip": 4000
}

print(dict)
print(dict["Name"])

dictjason = json.dumps(dict)
print(dictjason)




#
# Server side modtager json
#

recvDict = json.loads(dictjason)
print(recvDict)
print(recvDict["Name"])
print(recvDict["Address"])
print(recvDict["Zip"])
