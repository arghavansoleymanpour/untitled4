def initialize():
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         db="foofle")