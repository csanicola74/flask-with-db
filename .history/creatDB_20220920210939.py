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

# Creating table
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL
            gender CHAR(25) NOT NULL,
            zipcode CHAR(25) NOT NULL,
            phonenum CHAR(25) NOT NULL,
            diagnosis CHAR(25) NOT NULL,
        ); """

db.execute(table)
connect.commit()

# insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('12345', 'John', 'Smith', '01/01/2000')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('23456', 'Jane', 'Doe', '02/02/2001')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('34567', 'Mary', 'Smith', '03/03/2002')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('45678', 'Bob', 'Smith', '04/04/2003')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('56789', 'Jane', 'Doe', '05/05/2004')")
