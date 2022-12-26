import sqlite3

def update_thoughts(k_name):
    conn = sqlite3.connect("Databases/number.db")
    cur = conn.cursor()

    sql = f'''
    UPDATE Numbers
    SET thoughts=thoughts+1 
    '''

    cur.execute(sql)

    sql_get = f'''
    select thoughts from Numbers
    '''
    cur.execute(sql_get)
    res = cur.fetchone()

    if k_name == "kimberly":
        sql2 = f'''
            UPDATE Numbers
            SET kim_thought_last=1;
        '''
    else:
        sql2 = f'''
            UPDATE Numbers
            SET kim_thought_last=0;
        '''
    
    #green = 1, blue = 0

    cur.execute(sql2)

    conn.commit()
    cur.close
    conn.close()

    return res

# get the last_thought_kim column
def get_last_thought():
    conn = sqlite3.connect("Databases/number.db")
    cur = conn.cursor()

    sql = ''' 
    SELECT * from Numbers;
    '''

    cur.execute(sql)
    res = cur.fetchone()

    cur.close
    conn.close()

    return res