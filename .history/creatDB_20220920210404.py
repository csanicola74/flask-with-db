#######################
##  Import Packages  ##
#######################
import sqlite3


##############################
##  Connecting to Database  ##
##############################

# Connecting to sqlite
# connection object
connect = sqlite3.connect('./patients.db')

# storing the database into a variable to make it accessible for manipulations later
db = connect.cursor()
connect.commit()  # anything we do we need to commit to the connection
