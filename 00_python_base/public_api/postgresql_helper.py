import psycopg2


class PgHelper:
    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.port = kwargs['port']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.dbname = kwargs['dbname']
        self.charset = "utf8"
        try:
            self.conn = psycopg2.connect(host=self.url, user=self.username, passwd=self.password, port=self.port,
                                         charset=self.charset, db=self.dbname)
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception:
            print('connection err')


    def col_query(self, sql):
        """
        打印表的列名
        :return list
        """
        self.cur.execute(sql)
        return self.cur.fetchall()


    def commit(self):
        self.conn.commit()


    def close(self):
        self.cur.close()
        self.conn.close()
