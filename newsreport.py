#!/usr/bin/python

"""
This program queries a sql database and prints or saves the results.

The program is part of the Udacity Full Stack Web developer program and the
goal of the program is to query an existing database and use the results to
make a report of the data.
"""

import psycopg2
import datetime

DBNAME = "news"
print_bool = True


def query_news(sql_query):
    """execute sql query given as argument and returns the result."""
    c.execute(sql_query)
    return c.fetchall()


def write_output(context, content):
    """print query output from format_output() if print_bool = True."""
    f.write(str(context) + "\n")
    for item in content:
        f.write(str(item))
    f.write("\n")


def format_output(context, content):
    """
    format query output.

    takes as an argument the question a query is meant to answer and uses
    the number of the question to decide how the output should be formatted
    when it is printed in the terminal or saved to a file.
    """
    print_list = []
    print(context)
    formatting_key = context[1:2]
    for item in content:
        if (formatting_key == '1') or (formatting_key == '2'):
            unit, name, answer = " views", str(item[0]), str(item[1])
        if (formatting_key == '3'):
            unit, name, answer = " % errors", str(item[1]), str(item[0])[:4]
        output = (name + " - " + answer + unit)
        print(output)
        if print_bool:
            print_list.append(output + "\n")
    print("")
    if print_bool:
        write_output(context, print_list)


def popular_articles():
    """
    return answer to question 1.

    "What are the 3 most popular articles of all time?"
    """
    context = "(1) The 3 Most Popular Articles are:"
    popular_articles = query_news("""SELECT articles.title,
        COUNT(articles.title) AS t FROM articles
        JOIN log ON log.path = CONCAT('/article/', articles.slug)
        GROUP BY articles.title ORDER BY t
        DESC
        LIMIT 3""")
    format_output(context, popular_articles)


def popular_authors():
    """
    return answer to question 2.

    "Who are the most popular article authors of all time?"
    """
    context = "(2) The Most Popular Authors are:"
    popular_authors = query_news("""
        SELECT authors.name, sum(ac.t) AS av
        FROM (SELECT articles.author, COUNT(articles.title) AS t
            FROM articles JOIN log ON log.path = concat('/article/',
                articles.slug)
            GROUP BY articles.title, articles.id
            ORDER BY t DESC)
        AS ac JOIN authors ON ac.author = authors.id
        GROUP BY authors.name
        ORDER BY av DESC""")
    format_output(context, popular_authors)


def error_ratio():
    """
    return answer to question 3.

    "On which days did more than 1% of requests lead to errors?"
    """
    context = "(3) Dates where > 1% of requests resulting in errors include:"
    high_error_days = query_news("""
    SELECT ratio, date FROM
        (SELECT (((qtable.errors::NUMERIC/
            (qtable.errors::NUMERIC + qtable.successes::NUMERIC))
            *100)::NUMERIC) AS ratio, qtable.date
        FROM
            (SELECT f.n AS errors, s.n AS successes,
            f.d as date FROM
                (SELECT count(status) AS n, time::date AS d
                FROM log WHERE status LIKE '%404%'
                GROUP BY d, status
                ORDER BY d) AS f
            JOIN
                (SELECT count(status) AS n, time::date AS d
                FROM log WHERE status LIKE '%200%'
                GROUP BY d, status
                ORDER BY d) AS s
            ON f.d = s.d) AS qtable)
    AS subq WHERE ratio > 1""")
    format_output(context, high_error_days)


if __name__ == '__main__':
    """Run program."""
    # connects to database and creates cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # sets up file writing, if print_bool = True
    if print_bool:
        dt = datetime.datetime.now()
        filename = "news_report_" + str(dt)[-24:-16] + "_" + str(dt)[-15:-7]
        f = open(filename, 'w')
    # runs report
    popular_articles()  # prints 3 most popular articles
    popular_authors()  # prints authors in order of popularity
    error_ratio()  # prints dates of days with > 1% error rates for requests
    # ends file writing and prints location of file, if print_bool = True
    if print_bool:
        print("A new file, '" + filename + "' has been created in the current"
              + " directory containing the output of this program.")
        f.close()
    c.close()  # close database connection
