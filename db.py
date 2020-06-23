from mysql.connector import connection 
  
  
dict = { 
  'user': 'root', 
  'host': 'ubuntu18', 
  'database': 'cse'
} 
  
# Connecting to the server 
conn = connection.MySQLConnection(**dict) 
  
print(conn) 
  
# Disconnecting from the server 
conn.close() 
