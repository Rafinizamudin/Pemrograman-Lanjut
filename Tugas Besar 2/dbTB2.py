import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'Rynac-425',
    'db': 'perpustakaan',
}

# Create a connection to the database``
conn = MySQLdb.connect(**db_config)