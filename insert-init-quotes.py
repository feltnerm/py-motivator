#!/usr/bin/env python
"""
Insert some initial quotes into the db
"""
import sys
import sqlite3

i = raw_input("Continue with adding initial quotes: (Y/n)?")

if i != 'y':
	sys.exit(1)

else:
	with sqlite3.connect('motivate.db') as con:
		with open('initial-quotes','r') as file:
			for line in file:
				quote, author = line.split("\",")

				quote = quote.lstrip("\"")
				author = author.lstrip(" ")
				author = author.rstrip("\n")
				
				print 'Inserting values...'
				print "Quote: ["+quote+"]"
				print "Author: ["+author+"]"
				
				sql = "INSERT INTO motivate (quote, author) VALUES (%r,%r)" % (quote, author)
				print "Running \n" + "%s" % sql

				con.execute(sql)
				print "Success!"

