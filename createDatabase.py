'''

	GUTSHackathon 2014
	-- Tom Wallis for team HereForBeer

	Converts from .csv to SQLite. Note that we moved from SQLite to MySQL, so this is largely useless now. 

	Code shamelessly stolen in almost its entirety from http://stackoverflow.com/questions/5942402/python-csv-to-sqlite


'''

# Imports etc
import sqlite3, csv

# Some useful variables to keep track of what we're doing:
sqlitePath = './terrorData.db' # Change this if not running this script from the sqlite database file. 
terrorDataPath = './test.csv'#'./globalterrorismdb_0814dist_dev.csv' # Change this if not running this script from the same folder as the csv.
databaseVariableString = "test1 VARCHAR(50), test2 INTEGER" # GET THE REAL ONE FROM GUSTAVO!





# ----------------------------------
# Functions and main code. 


# Divides data into 10,000 rows each. 
# Notes: This is a generator!
def chunks(data, rows=10000):

    for i in xrange(0, len(data), rows):
        yield data[i:i+rows] 

# Main loop. 
# Notes: For importability, we include everything in this `if`. Means we can hack things up elsewhere if we need to using `chunks()`.
if __name__ == "__main__":

	# Set up the database initially.
	conn = sqlite3.connect(sqlitePath)
	conn.text_factory = str
	cur = conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS terrorData (' + databaseVariableString + ')')

	csvData = csv.reader(open(terrorDataPath, "rb")) 

	divData = chunks(csvData) # divide into 10000 rows each

	# Take each chunk and throw it into the database. 
	for chunk in divData:
		cur.execute('BEGIN TRANSACTION')

		for textTest, intTest in chunk:
			cur.execute('INSERT OR IGNORE INTO mytable (test1, test2) VALUES (?,?)', (textTest, intTest))

		cur.execute('COMMIT')

	print "DONE....."

