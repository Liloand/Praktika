import connection_to_db as c
import functions as f

hostname = f.getter('Input hostname: ')
username = f.getter('Input user name: ')
user_password = f.getter('Input your password: ')

connection = c.create_connection_with_server(hostname, username, user_password)
connection = c.create_connection_with_bd(hostname, username, user_password)

try:
    c.execute_sql(c.create_table_log(), connection)
except:
    pass


array_logs = f.file_into_array()

for log in array_logs:
    c.execute_sql(f.seporator(log), connection)
                       
