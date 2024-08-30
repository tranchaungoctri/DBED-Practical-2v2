import mysql.connector
import math

# DBED Assignment 2
# Student ID: a1904209
# Name: Chau Ngoc Tri Tran

class DBEDAssign2():
    def __init__(self,name):
        self.name=name

    def disp(self):
        print(self.name)

    def setUp(self):
        """Set up the DB connection to the 'postal' database"""
        self.connection = mysql.connector.connect(database='postal')
        self.cursor = self.connection.cursor(buffered=True)

    def syncDB(self):
        """We need to commit after insertion to ensure that the changes stick.
        syncDB is a wrapper to the connection commit that takes no parameters and
        returns no result."""
        self.connection.commit()

    def tearDown(self):
        """tearDown destroys the cursor and the connection to clean up."""
        self.cursor.close()
        self.connection.close()

    def show_all(self):
        """Select all rows in the database's pcode table and return it as a list to the user"""
        query ="SELECT * from pcode;"
        self.cursor.execute(query,)
        return self.cursor.fetchall()

    def select_by_pcode(self,pcode):
        """Perform a SELECT * query using the pcode parameter for postcode. Returns the query
        result as a list object."""
        query = "SELECT * FROM pcode WHERE postcode = %s;"
        self.cursor.execute(query, (pcode,))
        return self.cursor.fetchall()

    def insert_data(self,pcode,locality,state):
        """Insert data into the database"""
        query = "INSERT INTO pcode (postcode, locality, state) VALUES (%s, %s, %s);"
        self.cursor.execute(query, (pcode, locality, state))
        self.syncDB()

    def readData(self,fname):
        """Read in the data from the CSV datafile called fname and put it into the database
        Takes a single string parameter and does not return any values.
        IMPORTANT: you must call syncDB before exiting or your changes won't stick!"""
        with open('./'+fname,"r") as csv:
            # Skip the header
            csv.readline()

            # Your code here to insert the data
            for row in csv:
                pcode = row[0]
                locality = row[1]
                state = row[2]

                self.insert_data(pcode, locality, state)

            #Commit
            self.syncDB()

    def entropyCalc(self):
        """Analyse the postcode data to determine the entropy of the fourth column
        Takes no parameters and returns a single floating point number that is the
        total entropy of the fourth column.
        """
        counts = {}

        self.cursor.execute("SELECT SUBSTRING(postcode, 4, 1) FROM pcode")
        results = self.cursor.fetchall()

        for row in results:
            digit = row[0]
            if digit.isdigit():
                counts[digit] += 1

        total = sum(counts.values())
        entropy = 0.0
        for count in counts.values():
            if count > 0:
                probability = count / total
                entropy -= probability * math.log2(probability)

        return entropy
