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
               if len(row) == 4:
                _, pcode, locality, state = row
                # inset data
                self.insert_data(pcode, locality, state)

            #Commit
            self.syncDB()

    def entropyCalc(self):
        """Analyse the postcode data to determine the entropy of the fourth column
        Takes no parameters and returns a single floating point number that is the
        total entropy of the fourth column.
        """
        # Query to count occurrences of each digit in the fourth position
        query = """
        SELECT SUBSTRING(postcode, 4, 1) AS digit, COUNT(*) AS count
        FROM pcode
        GROUP BY digit;
        """
        self.cursor.execute(query)
        counts = self.cursor.fetchall()

        # Calculate total number of postcodes
        total = sum(count for _, count in counts)

        # Calculate frequencies and entropy
        entropy = 0
        for digit, count in counts:
            probability = count / total
            entropy -= probability * math.log2(probability)

        return entropy
