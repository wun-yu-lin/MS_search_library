import mysql.connector
import sys
sys.path.insert(1, './')
import config
import errorhandling.errorhandling as errorhandling


db_fig ={
    'host':config.MYSQL_HOST,
    'user':config.MYSQL_USER,
    'password':config.MYSQL_PASSWORD,
    'database':config.MYSQL_DATABASE,
    "pool_name":"mysql_pool_v2",
    "pool_size":config.MYSQL_POOL_SIZE
}


query_config = {
    "group_concat_max_len":config.GROUP_CONCAT_MAX_LEN
}

def filter_query_string(query_string_arr)->bool:
    sql_filter_arr = config.SQL_FILTER_STRING

    for item in query_string_arr:
        for spec in sql_filter_arr: 
            if item == None: continue
            if item.upper().find(spec.upper())!=-1:
                return False 
    return True

    

##mysql connection pool
try:
    mysql_connection_pool = mysql.connector.pooling.MySQLConnectionPool(**db_fig)
    print("create mysql connection success!")

except Exception as err:
    print(err)
    print("create mysql connection error!")
    

def get_mysql_connection_from_pool(mysql_connection_pool):
    mysql_connection = mysql_connection_pool.get_connection()
    print("get mysql connection success!")
    return mysql_connection

def insert_ms_data_into_database(mz, rt):

    mysql_connection = get_mysql_connection_from_pool(mysql_connection_pool)
    cursor = mysql_connection.cursor(dictionary=True)


    
    mysql_str = "insert into ms_data (mz, rt) values (%s, %s)"

    try:
        cursor.execute(mysql_str, (mz, rt,))
        mysql_connection.commit()
        print("insert ms_data success")
    except Exception as err:
        print(err)
        results= errorhandling.handle_error({"code": 400, "message": "MySQL Server error"}), 400
    finally:
        if mysql_connection.in_transaction:
            mysql_connection.rollback()
        cursor.close()
        mysql_connection.close()

    return True

def insert_ms_data_into_ms_data_index(mz, rt):

    mysql_connection = get_mysql_connection_from_pool(mysql_connection_pool)
    cursor = mysql_connection.cursor(dictionary=True)


    
    mysql_str = "insert into ms_data_index (mz, rt) values (%s, %s)"

    try:
        
        cursor.execute(mysql_str, (mz, rt,))
        mysql_connection.commit()
        print("insert ms_data success")
    except Exception as err:
        print(err)
        results= errorhandling.handle_error({"code": 400, "message": "MySQL Server error"}), 400
    finally:
        if mysql_connection.in_transaction:
            mysql_connection.rollback()
        cursor.close()
        mysql_connection.close()

    return True
def insert_ms_data_into_ms_data_unique_index(mz, rt):

    mysql_connection = get_mysql_connection_from_pool(mysql_connection_pool)
    cursor = mysql_connection.cursor(dictionary=True)


    
    mysql_str = "insert into ms_data_unique_index (mz, rt) values (%s, %s)"

    try:
        
        cursor.execute(mysql_str, (mz, rt,))
        mysql_connection.commit()
        print("insert ms_data success")
    except Exception as err:
        print(err)
        results= errorhandling.handle_error({"code": 400, "message": "MySQL Server error"}), 400
    finally:
        if mysql_connection.in_transaction:
            mysql_connection.rollback()
        cursor.close()
        mysql_connection.close()

    return True


# import numpy as np
# arr = np.random.randint(0, 5000, size=2000000)

for item in range(0,2000000):
    insert_ms_data_into_database(mz=float(item), rt=float(item))
    insert_ms_data_into_ms_data_index(mz=float(item), rt=float(item))
    insert_ms_data_into_ms_data_unique_index(mz=float(item), rt=float(item))