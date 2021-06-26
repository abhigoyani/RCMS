from connection import cur,conn

def insert_new_temp(host,usr1,usr2,usr3):

    sql = "insert into temp_user(user1_id,user2_id,user3_id,host) values ('{user1}','{user2}','{user3}','{host}');".format(user1=usr1,user2=usr2,user3=usr3,host=host)
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        print('1')
        return False
    