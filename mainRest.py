from RestClient import *

print('All træpiller')
pellets, resp = GetAll()
print( resp.status_code)
for pellet in pellets:
    print (pellet)


print('Opret TræPille')  
nyPellet = { 'brand': 'PetersPellets', 'price': 5446, 'quality': 3}  
resp = Add(nyPellet)
print( resp.status_code)
print( resp.content)


print('All træpiller')
pellets, resp = GetAll()
print( resp.status_code)
for pellet in pellets:
    print (pellet)
