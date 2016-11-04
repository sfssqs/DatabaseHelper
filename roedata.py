# coding=utf-8
import dbhelper

'''
    ROE and Revenue data operator
    Table Name : roe_revenue
'''

global DB_FILE_PATH
DB_FILE_PATH = 'roe_revenue.db'
global TABLE_NAME
TABLE_NAME = 'roe_revenue'
global SHOW_SQL
SHOW_SQL = True
global LOG
LOG = 'roedata:'


def create_table():
    print(LOG + 'Create database table...')
    create_table_sql = '''CREATE TABLE 'roe_revenue' (
                          `id`              int(11)         NOT NULL,
                          `code`            varchar(6)      NOT NULL,
                          `name`            varchar(24)     NOT NULL,
                          `roe`             REAL(32)        DEFAULT NULL,
                          'roe_sort'        int(16)         DEFAULT NULL,
                          `revenue`         REAL(32)        DEFAULT NULL,
                          `revenue_sort`    int(16)         DEFAULT NULL,
                           PRIMARY          KEY             (`id`)
                        )'''
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.create_table(conn, create_table_sql)


def save_data():
    print(LOG + 'Save data...')
    save_sql = '''INSERT INTO 'roe_revenue' values (?, ?, ?, ?, ?, ?, ?)'''
    data = [(000001, '000001', u'汤臣倍健', -190.08, 0, 263.03, 0),
            (000002, '000001', u'中国石油', 17.00, 0, 1.03, 0),
            (600001, '600001', u'中国石化', 25.42, 0, -100.11, 0),
            (600002, '600002', u'建设银行', 1.06, 0, 32.2, 0)]
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.save(conn, save_sql, data)


def main():
    create_table()
    save_data()


if __name__ == '__main__':
    main()
