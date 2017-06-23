# !/usr/bin/env python2
#
# new_queries.py -- answers a number of questions about traffic on a
# news website

import psycopg2


def connect(database_name="news"):

    """Create database connection and cursor object, throws exception
    if error occurs."""

    try:
        db_connect = psycopg2.connect("dbname={}".format(database_name))
        cursor = db_connect.cursor()
        return db_connect, cursor
    except psycopg2.Error:
        print "Cannot connect to database"


def most_pop_art():

    '''prints out the names and times viewed
    for the three most popular articles

    first connects to the database, creates a cursor and runs the
    query stored in query via the excute command

    this is followed by collecting the retrieved information as a tuple.
    The database is then changed and the conncetion closed by .close()

    finally, the tuple of results is iterated over to print out the results
    in an easy to read manner
    '''

    db_connect, cursor = connect()
    query = ("SELECT articles.title, pathnum.num FROM articles, pathnum "
             "WHERE pathnum.path like '%' || articles.slug "
             "GROUP BY articles.title, pathnum.num ORDER BY num desc;")
    cursor.execute(query)
    three_most_pop = cursor.fetchall()
    db_connect.commit()
    db_connect.close()

    for art in three_most_pop:
        print str(art[0]) + " - " + str(art[1]) + " views"


def author_pop():

    '''prints out the names of all the authors who submitted articles
        along with the number of views their articles have,
        most popular first'''

    db_connect, cursor = connect()
    query = ("SELECT authors.name, authnum.num FROM authors, authnum "
             "WHERE authors.id=authnum.author ORDER BY num desc;")
    cursor.execute(query)
    author_ranks = cursor.fetchall()
    db_connect.commit()
    db_connect.close()

    for author in author_ranks:
        print str(author[0]) + " - " + str(author[1]) + " views"


def error_days():

    '''prints out the days when the more than 1% of requests resulted
        in an error'''

    db_connect, cursor = connect()
    query = ("SELECT day, cast(errors as float) / cast(total_req as float)*100"
             "as percent from req_and_errs "
             "WHERE cast(errors as float)/cast(total_req as float) > 0.01;")
    cursor.execute(query)
    bad_days = cursor.fetchall()
    db_connect.commit()
    db_connect.close()

    for day in bad_days:
        print str(day[0]) + " - " + str(round(day[1], 2)) + "% errors"

most_pop_art()
author_pop()
error_days()
