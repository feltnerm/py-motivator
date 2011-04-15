#!/usr/bin/env python
"""
Create the motivator database
"""
import sqlite3

with sqlite3.connect('motivate.db') as con:
	sql = """ DROP TABLE motivate"""

	con.execute(sql)
	
	sql = """CREATE TABLE motivate (id INTEGER PRIMARY KEY, 
								    quote char(422) NOT NULL, 
								    author char(100))"""

	print 'Creating table: motivate'								
	con.execute(sql)
	print 'Created.'

	with open('initial-quotes','r') as file:
		for line in file:

			l = line.split("\",")
			
			quote, author = l[0],l[1]
			quote = quote.lstrip("\"")
			author = author.lstrip(" ")
			quote = quote.rstrip()
			author = author.rstrip()

			print 'Inserting values.'
			print "Quote: ["+quote+"]"
			print "Author: ["+author+"]"

			sql = """ INSERT INTO motivate (quote, author) VALUES
					  (%r, %r)""" % (quote, author)
			
			con.execute(sql)
			print 'Inserted.'
	con.commit()

	curs = con.cursor()

	curs.execute("SELECT * FROM motivate")

	print 'RESULTS'
	for id, quote, author in curs.fetchall():
		print """"%s" ~%s""" % (quote, author)
