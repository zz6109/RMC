import serial
import pymysql
import time

def sql_input():
    sp = serial.Serial( port='/dev/ttyUSB0', baudrate=9600, timeout=1) 
    conn = pymysql.connect(host='10.10.13.177', user='jaehwan', password='1234', db='dht11', charset='utf8')

    curs = conn.cursor() 

    humi = 0
    temp = 0

    while True:
        if sp.readable():
            rcv = sp.readline()

            if (rcv.decode()[0:4]=="humi"):
                humi = int(rcv.decode()[4:6])
                print(humi)
            if (rcv.decode()[0:4]=="temp"):
                temp = int(rcv.decode()[4:6])
                print(temp)
        
            sql = "insert into dht11.location1(Temperature, Humidity) values(%s, %s)"
            curs.execute(sql, (temp, humi))
            conn.commit()

        