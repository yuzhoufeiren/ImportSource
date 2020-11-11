import pymysql
import gevent
from gevent import monkey


# 将耗时的操作，自动换成gevent模块中的
monkey.patch_all()



def read_insert1(filename):
    """"""
    while True:
        # 1、读取
        print(filename)
        with open(filename, 'r') as f:
            data = f.readlines()

        data1 = data[0]
        print(data1)

        # 2、sql插入

        con = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='slwS123!@#.',
            db='xd_blog',
            charset='utf8'
        )

        cue = con.cursor()

        cue.execute("""update test set content1="%s" where id="11";""" % data1)
        # print(cue.fetchall())
        con.commit()

        # 关闭
        cue.close()
        con.close()


def read_insert2(filename):
    """"""
    while True:
        # 1、读取
        print(filename)
        with open(filename, 'r') as f:
            data = f.readlines()

        # 2、数据处理
        data1 = data[0]
        print(data1)

        # 3、sql插入

        con = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='slwS123!@#.',
            db='xd_blog',
            charset='utf8'
        )

        cue = con.cursor()

        cue.execute("""update test set content2="%s" where id="11";""" % data1)
        con.commit()

        # 关闭链接
        cue.close()
        con.close()


def main():
    """"""
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='slwS123!@#.',
        db='xd_blog',
        charset='utf8'
    )

    cue = con.cursor()
    gevent.joinall([
        gevent.spawn(read_insert1, 'slw1.txt'),
        gevent.spawn(read_insert2, 'slw2.txt'),
    ])


if __name__ == '__main__':

    main()
    # read()
    # 执行read函数

