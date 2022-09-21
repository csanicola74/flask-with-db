#######################
##  Import Packages  ##
#######################
import sqlite3
import pandas as pd

###########################
##  Connect to Database  ##
###########################


def get_db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn


db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

# save the data to a dataframe
df = pd.DataFrame(patientListSql)
df

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob',
              'gender', 'zipcode', 'ethnicity', 'diagnosis']
df
