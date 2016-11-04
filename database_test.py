# coding=utf-8
import dbhelper

DB_FILE_PATH = ''
TABLE_NAME = ''
SHOW_SQL = True


def create_table():
    print('TEST: Create database table...')
    create_table_sql = '''CREATE TABLE `student` (
                          `id` int(11) NOT NULL,
                          `name` varchar(20) NOT NULL,
                          `gender` varchar(4) DEFAULT NULL,
                          `age` int(11) DEFAULT NULL,
                          `address` varchar(200) DEFAULT NULL,
                          `phone` varchar(20) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                        )'''
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.create_table(conn, create_table_sql)


def drop_table():
    print('TEST: Delete database table...')
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.drop_table(conn, TABLE_NAME)


def save_data():
    print('TEST: Save data...')
    save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
    data = [(1, 'Hongten', u'男', 20, u'广东省广州市', '13423****62'),
            (2, 'Tom', u'男', 22, u'美国旧金山', '15423****63'),
            (3, 'Jake', u'女', 18, u'广东省广州市', '18823****87'),
            (4, 'Cate', u'女', 21, u'广东省广州市', '14323****32')]
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.save(conn, save_sql, data)


def fetchall():
    print('TEST: Query all data...')

    fetchall_sql = '''SELECT * FROM student'''
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.fetchall(conn, fetchall_sql)


def fetchone():
    print('TEST: Query single data...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = 1
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.fetchone(conn, fetchone_sql, data)


def update_data():
    print('TEST: Update data...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.update(conn, update_sql, data)


def delete_data():
    print('TEST: Delete data...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = dbhelper.get_conn(DB_FILE_PATH)
    dbhelper.delete(conn, delete_sql, data)


def init():
    global DB_FILE_PATH
    DB_FILE_PATH = 'hongten.db'
    global TABLE_NAME
    TABLE_NAME = 'student'
    global SHOW_SQL
    SHOW_SQL = True

    print('show_sql : {}'.format(SHOW_SQL))

    drop_table()
    create_table()
    save_data()


def main():
    init()
    fetchall()
    print('#' * 50)

    fetchone()
    print('#' * 50)

    update_data()
    fetchall()

    print('#' * 50)
    # delete_data()
    fetchall()


if __name__ == '__main__':
    main()
