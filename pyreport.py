#!/usr/bin/env python3

import psycopg2

print('''

  ____        ____                       _             ____   ____
 |  _ \ _   _|  _ \ ___ _ __   ___  _ __| |_          |  _ \ / ___|
 | |_) | | | | |_) / _ \ '_ \ / _ \| '__| __|  _____  | |_) | |  _
 |  __/| |_| |  _ <  __/ |_) | (_) | |  | |_  |_____| |  __/| |_| |
 |_|    \__, |_| \_\___| .__/ \___/|_|   \__|         |_|    \____|
        |___/          |_|

''')


def top_articles():

    conn = psycopg2.connect(database="news")
    pop_articles = conn.cursor()
    pop_articles.execute('''select title, count(path) from articles join log on
                        articles.slug = substring(log.path from 10) where
                        status = '200 OK' group by title order
                        by count desc limit 3;''')
    pop_list = pop_articles.fetchall()
    print('\n')
    print('[+] Most Popular Articles')
    print('\n')
    for row in pop_list:
        print(row[0] + ': ' + str(row[1]) + ' views')
    print('\n')
    print('*' * 40)
    conn.close()


def top_authors():

    conn = psycopg2.connect(database="news")
    pop_authors = conn.cursor()
    pop_authors.execute('''select name, views from authors, author_views where
                        authors.id=author_views.author order by views desc;''')
    pop_auth_list = pop_authors.fetchall()
    print('\n')
    print('[+] Most Popular Authors')
    print('\n')
    for row in pop_auth_list:
        print(row[0] + ': ' + str(row[1]) + ' views')
    print('\n')
    print('*' * 40)
    conn.close()


def errors():

    conn = psycopg2.connect(database="news")
    errors = conn.cursor()
    errors.execute('''select time, round(avg(val)::numeric,2) from calc
                   where val > 1 group by time;''')
    errors_list = errors.fetchall()
    print('\n')
    print('[+] Days With > 1% Error Rate')
    print('\n')
    for row in errors_list:
        print(str(row[0]) + ' : ' + str(row[1]) + ' percent errors')
    print('\n')
    print('*' * 40)
    conn.close()


def main():

    print('Please Select Option: ')
    print('1: Run Top Articles Report')
    print('2: Run Top Authors Report')
    print('3: Run Errors Greater That 1% Per Day Report')
    print('4: Run All Reports')
    option = input('> ')

    if option == '1':
        print('\n')
        print('[+] Running Top Articles Report')
        print('\n')
        top_articles()
        print('\n')
        print('[+] Reports Complete')
        print('\n')

    if option == '2':
        print('\n')
        print('[+] Running Top Authors Report')
        print('\n')
        top_authors()
        print('\n')
        print('[+] Reports Complete')
        print('\n')

    if option == '3':
        print('\n')
        print('[+] Running Error Report')
        print('\n')
        errors()
        print('\n')
        print('[+] Reports Complete')
        print('\n')

    if option == '4':
        print('\n')
        print('[+] Running All Reports')
        print('\n')
        top_articles()
        top_authors()
        errors()
        print('\n')
        print('[+] Reports Complete')
        print('\n')

if __name__ == __name__:
    main()
