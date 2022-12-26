#!/usr/bin/python3
"""
A script that takes in an argument and displays all value
in the states table where name matches the argument
Example: ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities JOIN
                   states ON states.id = cities.state_id
                   ORDER BY cities.id""")

    for row in cur.fetchall():
        print(row)
    db.close()
