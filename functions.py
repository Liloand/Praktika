import re
import connection_to_db as c

def prompt(msg):
    print(msg)

def getter(msg):
    return input(msg)

def file_into_array(msg_get_file_way='Input path: ', msg_if_file_not_founded='File not founded')-> list:
    try:
        filename = getter(msg_get_file_way)
        with open(filename) as f:
            array_logs = f.readlines()
        return array_logs
    except FileNotFoundError:
        raise Exception(msg_if_file_not_founded)

def seporator(log_line):
    log_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{0,3}\.\d{1,3}) (\S+) (\S+) \[(\d{2}\/\w{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) ([\+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}) (\d+)\s?"?([^"]*)"?\s?"?([^"]*)?"?$'
    
    match = re.match(log_pattern, log_line)
    if match:
        IP_Address = match.group(1)
        Identity = match.group(2)
        Username = match.group(3)
        Date_Log = match.group(4)
        Time_Log = match.group(5)
        Zone = match.group(6)
        Method = match.group(7)
        Requested_Resource = match.group(8)
        HTTP_Version = match.group(9)
        Status_Code = match.group(10)
        Response_Size = match.group(11)
        Referer = match.group(12)
        User_Agent = match.group(13)

        return c.insert_data(IP_Address, Identity, Username, Date_Log, Time_Log, Zone, Method, Requested_Resource, HTTP_Version, Status_Code, Response_Size, Referer, User_Agent)








