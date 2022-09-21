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
db
