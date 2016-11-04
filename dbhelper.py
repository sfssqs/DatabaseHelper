# coding=utf-8

import sqlite3
import os

SHOW_SQL = True


def get_conn(path):
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('Hardware:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('Memory:[:memory:]')
        return sqlite3.connect(':memory:')


def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


def create_table(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('execute sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('Create database table success!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def drop_table(conn, table):
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('execute sql:[{}]'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('Delete database [{}] success!'.format(table))
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def close_all(conn, cu):
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()


def save(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('Execute sql:[{}],Parameter:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def fetchall(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('Execute sql:[{}]'.format(sql))
        cu.execute(sql)
        r = cu.fetchall()
        if len(r) > 0:
            for e in range(len(r)):
                print(r[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def fetchone(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            # Do this instead
            d = (data,)
            cu = get_cursor(conn)
            if SHOW_SQL:
                print('Execute sql:[{}],Parameter:[{}]'.format(sql, data))
            cu.execute(sql, d)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] equal None!'.format(data))
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def update(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('Execute sql:[{}],Parameter:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def delete(conn, sql, data):
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('Execute sql:[{}],Parameter:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
