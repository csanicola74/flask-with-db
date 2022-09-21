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


#############################
##  Creating the Database  ##
#############################

# Creating table,
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit()
