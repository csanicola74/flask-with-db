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
