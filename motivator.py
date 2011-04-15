#!/usr/bin/env python
"""
motivator.py

A simple motivation webpage
"""
import sys
import sqlite3
import random

from bottle import route, run

@route('/')
def motivator():
	quote, author = retrieve_quote()

	quote = "\""+quote+"\""+"\n"
	author = "~"+author

	return quote, author
	
def retrieve_quote():
	with sqlite3.connect('motivate.db') as con:
		cur = con.cursor()
		sql = """ SELECT quote, author FROM motivate """

		cur.execute(sql)
		result = cur.fetchall()
		
		r = random.randint(0, len(result) - 1)
		quote, author = result[r]

		return quote, author

def main():
	run(reloader=True)	

if __name__ == "__main__":
	status = main()
	sys.exit(status)
