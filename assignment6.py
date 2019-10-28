#(91, 'Robert', 'Lewis', '1994-07-17', 'Wilsonborough', 'MT', '53741')
#(92, 'Kelly', 'Weber', '1999-08-01', 'Connieview', 'OK', '09271')
#(93, 'Timothy', 'Zhang', '2000-08-27', 'Porterport', 'IA', '97619')

import sqlalchemy as db
import json
# change the following line to import your Customer class
from tland65_cust_class import Customer


def main():
	# connect and read from customer.sqlite
    engine = db.create_engine('sqlite:///customer.sqlite')
    connection = engine.connect()
    results = connection.execute("select * from customer")

    # put the customers into a list
    customers = []
    for row in results:
        c = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        customers.append(c.to_json())

    # output to a json file
    with open('assignment6.json', 'w') as output:
        json.dump(customers, output)

#main function call
main()
