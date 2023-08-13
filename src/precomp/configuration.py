"""Configuration file for the application"""

hostname = 'localhost'
database = 'db-name'
username = 'postgres'
pwd = 'password'
port_id = 5000


#! databasetype://username:password@hostname:port/database
dbLink = 'postgresql://'+username+':'+pwd+'@'+hostname+':'+str(port_id)+'/'+database
