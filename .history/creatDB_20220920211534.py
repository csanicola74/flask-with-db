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
            ethnicity CHAR(25) NOT NULL,
            diagnosis CHAR(25) NOT NULL,
        ); """

db.execute(table)
connect.commit()

# insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, zipcode, ethnicity, diagnosis) values('12345', 'John', 'Smith', '01/01/2000', 'Male', '11774', 'White', 'Flu')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, zipcode, ethnicity, diagnosis) values('23456', 'Jane', 'Doe', '02/02/2001', 'Female', '11483', 'Spanish', 'Injury')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, zipcode, ethnicity, diagnosis) values('34567', 'Mary', 'Smith', '03/03/2002', 'Female', '11678', 'Spanish', 'Covid')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, zipcode, ethnicity, diagnosis) values('45678', 'Bob', 'Smith', '04/04/2003', 'Male', '11833', 'White', 'Covid')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, zipcode, ethnicity, diagnosis) values('56789', 'Jane', 'Doe', '05/05/2004', 'Female', '11900', 'Black', 'Flu')")
