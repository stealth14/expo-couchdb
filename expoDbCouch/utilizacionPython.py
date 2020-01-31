import couchdb 

#conexion
conn=couchdb.Server("http://127.0.0.1:5984" )

#instancia de base de datos
db =  couchdb.Database('ronny')


#datos
nombres = ["ronny", "luis", "pedro"]
  
#inserción
for nombre in nombres:

  doc = {"rol": "estudiante","nombre":nombre}
  db.save(doc)
