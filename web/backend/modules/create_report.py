import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax3d
from math import sqrt
import itertools
from time import strftime,strptime
from threading import Thread
import numpy as np

import os


def integration(*axis, N=1):
    for _ in range(N):
        axis = map(lambda x: list(itertools.accumulate(x)), axis)

    return list(axis)

def integration(*axis, N=1):
    for _ in range(N):
        axis = map(lambda x: list(itertools.accumulate(x)), axis)

    return list(axis)

def calculating_the_distance(func_data_x, func_data_y, func_data_z):  # функция, рассчитывающая длину тракетории
    track = 0.0  # длина траектории перемещения
    length = 0.0  # расстояние между двумя соседними точками

    for i in range(len(func_data_x) - 2):  # вычисление длины траектории перемещения
        vector_x = func_data_x[i + 1] - func_data_x[i]
        vector_y = func_data_y[i + 1] - func_data_y[i]
        vector_z = func_data_z[i + 1] - func_data_z[i]
        length = sqrt(vector_x * vector_x + vector_y * vector_y + vector_z * vector_z)
        track = track + length
    return track

def risovalka_for_3(data1, title1, data2, title2, data3, title3, name, characteristic, gprs_data,aprs_data,telemetry_data,gd,ad,td ):
    fig = plt.figure()  # графики

    gprs = np.arange(0, len(data1))
    aprs = np.arange(0, len(data2))
    telemetry = np.arange(0, len(data3))

    plt.subplot(311)
    plt.plot(gprs, data1)
    plt.title('{}'.format(title1))  # IR
    plt.xticks(gprs, gprs_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(312)
    plt.plot(aprs, data2)
    plt.title('{}'.format(title2))
    plt.xticks(aprs, aprs_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(ad))
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(313)
    plt.plot(telemetry, data3)
    plt.title('{}'.format(title3))
    plt.xticks(telemetry, telemetry_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(td))
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.tight_layout()
    plt.savefig("backend/modules/img/{}.png".format(name), fmt='png')


def risovalka_for_2(data1, title1, data2, title2, name, characteristic, gprs_data,telemetry_data,gd,td ):
    fig = plt.figure()  # графики

    gprs = np.arange(0, len(data1))
    telemetry = np.arange(0, len(data2))

    plt.subplot(211)
    plt.plot(gprs, data1)
    plt.title('{}'.format(title1))  # IR
    plt.xticks(gprs, gprs_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(212)
    plt.plot(telemetry, data2)
    plt.title('{}'.format(title2))
    plt.xticks(telemetry, telemetry_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(td))
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.tight_layout()
    plt.savefig("backend/modules/img/{}.png".format(name), fmt='png')


def risovalka_for_axes(gx1, gy1, gz1, tx1, ty1, tz1, gprs_data,telemetry_data,gd,td ):
    gx1, gy1, gz1 = integration(gx1, gy1, gz1, N=2)
    tx1, ty1, tz1 = integration(tx1, ty1, tz1, N=2)

    length_list = len(gx1)

    fig = plt.figure()  # график траектории перемещения
    ax = ax3d.Axes3D(fig)
    ax.plot(gx1, gy1, gz1, color='green')
    ax.scatter(gx1[0], gy1[0], gz1[0])
    ax.scatter(gx1[length_list - 1], gy1[length_list - 1], gz1[length_list - 1], color='red')
    plt.savefig("backend/modules/img/trajectory.png", fmt='png')

    gprs = np.arange(0, len(gx1))
    telemetry = np.arange(0, len(tx1))

    fig = plt.figure()  # графики изменения проекций ускорения по 3 осям
    plt.subplot(321)
    plt.plot(gprs, gx1)
    plt.title('Акселерометр(x)')
    plt.xticks(gprs, gprs_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('Дистанция, метры')
    plt.grid()

    
    plt.subplot(323)
    plt.plot(gprs, gy1)
    plt.title('Акселерометр(y)')
    plt.xticks(gprs, gprs_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('Дистанция, метры')
    plt.grid()
    


    plt.subplot(325)
    plt.plot(gprs, gz1)
    plt.title('Акселерометр(z)')
    plt.xticks(gprs, gprs_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(322)
    plt.plot(telemetry, tx1)
    plt.title('Акселерометр(x)')
    plt.xticks(telemetry,telemetry_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(324)
    plt.plot(telemetry, ty1)
    plt.title('Акселерометр(y)')
    plt.xticks(telemetry,telemetry_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(326)
    plt.plot(telemetry,tz1)
    plt.title('Акселерометр(z)')
    plt.xticks(telemetry,telemetry_data,fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Время на дату:{}'.format(gd))
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.tight_layout()
    plt.savefig("backend/modules/img/XYZprojectionFirstAxel.png", fmt='png')



def execute_from_db3(n, m, gprs, aprs, telemetry):
    data1 = []
    data2 = []
    data3 = []
    for i in range(len(gprs)):
        data1.append(gprs[i][n])
    for i in range(len(aprs)):
        data2.append(aprs[i][m])
    for i in range(len(telemetry)):
        data3.append(telemetry[i][n])
    return data1, data2, data3


def execute_from_db2(n, gprs, telemetry):
    data1 = []
    data2 = []
    for i in range(len(gprs)):
        data1.append(gprs[i][n])
    for i in range(len(telemetry)):
        data2.append(telemetry[i][n])
    return data1, data2


def execute_axels(gprs, telemetry):
    gx1 = []
    gy1 = []
    gz1 = []
    tx1 = []
    ty1 = []
    tz1 = []

    for i in range(len(gprs)):
        gx1.append(gprs[i][11])
        gy1.append(gprs[i][12])
        gz1.append(gprs[i][13])
    for i in range(len(telemetry)):
        tx1.append(telemetry[i][11])
        ty1.append(telemetry[i][12])
        tz1.append(telemetry[i][13])

    return gx1, gy1, gz1, tx1, ty1, tz1



def parsing_datas3(n, m, data1, title1, data2, title2, data3, title3, name, characteristic, gprs_data,aprs_data,telemetry_data,gd,ad,td ):
    d1, d2, d3 = execute_from_db3(n, m, data1, data2, data3)
    risovalka_for_3(d1, title1, d2, title2, d3, title3, name, characteristic, gprs_data,aprs_data,telemetry_data,gd,ad,td)

def parsing_datas2(n, data1, title1, data2, title2, name, characteristic, gprs_data,telemetry_data,gd,td):
    d1, d2 = execute_from_db2(n, data1, data2)
    risovalka_for_2(d1, title1, d2, title2, name, characteristic, gprs_data,telemetry_data,gd,td)

def parsing_axels(data1, data2, gprs_data,telemetry_data,gd,td ):
    gx1, gy1, gz1, tx1, ty1, tz1 = execute_axels(data1, data2)
    risovalka_for_axes(gx1, gy1, gz1, tx1, ty1, tz1, gprs_data,telemetry_data,gd,td)


def hour_min_sec(tme):
    mas =[]

    for i in range(len(tme)):
        t = strptime(str(tme[i]), '%Y-%m-%d %H:%M:%S')
        mas.append(strftime('%H:%M:%S',t))
    k = len(tme)-1
    t1 = strptime(str(tme[0]), '%Y-%m-%d %H:%M:%S')
    t2 = strptime(str(tme[k]), '%Y-%m-%d %H:%M:%S')

    f =str(strftime('%B',t1))
    l =str(strftime('%B',t2))

    first=strftime('%d',t1)
    last=strftime('%d',t2)

    if f==l:
        if first != last:
            string =str(f) + ' ' + str(first)+ ' — ' + str(last)
        if first == last:
            string =str(f) + ' ' + str(first)
    else:  
        string =str(f) + ' ' + str(first)+ ' — ' +str(l)+ ' ' + str(last)

    return mas,string

def rem(path):
   if os.path.isfile(path):
     os.remove(path)




def getData(mysql):
    l = os.listdir('backend/modules/img/')

    try:
        for i in range(len(l)):
            os.remove('backend/modules/img/{}'.format(l[i]))
    except:
        pass
    cur = mysql.connect().cursor()
    l = cur.execute("select count(*) from gprs where numberOfFlight=10001")
    if l > 40:
        cur.execute(
            "select * from gprs where id % (floor((select count(*) from gprs where numberOfFlight=10001)/4)) = 0")
    else:
        cur.execute("select * from gprs where numberOfFlight=10001")
    gprs = list(cur.fetchall())

    mysql.connect().commit
    cur = mysql.connect().cursor()
    l = cur.execute("select count(*) from aprs where numberOfFlight=10001")
    if l > 40:
        cur.execute(
            "select * from aprs where id % (floor((select count(*) from aprs where numberOfFlight=10001)/4)) = 0")
    else:
        cur.execute("select * from aprs where numberOfFlight=10001")
    aprs = list(cur.fetchall())

    mysql.connect().commit
    cur = mysql.connect().cursor()
    l = cur.execute("select count(*) from telemetry where numberOfFlight=10001")
    if l > 40:
        cur.execute(
            "select * from telemetry where id % (floor((select count(*) from telemetry where numberOfFlight=10001)/4)) = 0")
    else:
        cur.execute("select * from telemetry where numberOfFlight=10001")
    telemetry = list(cur.fetchall())

    mysql.connect().commit

    gprs_data, aprs_data, telemetry_data = execute_from_db3(2, 2, gprs, aprs, telemetry)

    gprs_data,gd = hour_min_sec(gprs_data)
    aprs_data,ad = hour_min_sec(aprs_data)
    telemetry_data,td = hour_min_sec(telemetry_data)

    matplotlib.rcParams['figure.figsize'] = (10, 7)

    parsing_datas3(6, 6, gprs, 'Температура 1 по gprs', aprs, 'Температура 1 по aprs', telemetry,
                   'Температура 1 по telemetry', 'temp1', 'Температура,°C', gprs_data, aprs_data, telemetry_data,gd,ad,td)

    parsing_datas3(8, 7, gprs, 'Давление 1 по gprs', aprs, 'Давление 1 по aprs', telemetry, 'Давление 1 по telemetry',
                   'pressure1', 'Давление,Паскаль', gprs_data, aprs_data, telemetry_data,gd,ad,td)

    parsing_datas2(7, gprs, 'Температура 2 по gprs', telemetry, 'Температура 2 по telemetry', 'temp2', 'Температура,°C',
                   gprs_data, telemetry_data,gd,td)

    parsing_datas2(9, gprs, 'Давление 2 по gprs', telemetry, 'Давление 2 по telemetry', 'pressure2', 'Давление,Паскаль',
                   gprs_data, telemetry_data,gd,td)

    parsing_datas2(10, gprs, 'Напряжение аккумулятора по gprs', telemetry, 'Напряжение аккумулятора по telemetry',
                   'bat_volt',
                   'Напряжение аккумулятора,Вольт', gprs_data, telemetry_data,gd,td)

    parsing_axels(gprs, telemetry, gprs_data, telemetry_data,gd,td)

    parsing_datas2(14, gprs, 'Hdop по gprs', telemetry, 'Hdop по telemetry', 'hdop', 'Hdop', gprs_data, telemetry_data,gd,td)

    parsing_datas2(15, gprs, 'Vdop по gprs', telemetry, 'Vdop по telemetry', 'vdop', 'Vdop', gprs_data, telemetry_data,gd,td)

    parsing_datas2(16, gprs, 'SATS по gprs', telemetry, 'SATS по telemetry', 'sats', 'SATS', gprs_data, telemetry_data,gd,td)



    cur = mysql.connect().cursor()
    cur.execute("select id from gprs where numberOfFlight=10001 ORDER BY id DESC LIMIT 1 ")
    last_id_gprs = list(cur.fetchall())
    last_id_gprs = last_id_gprs[0][0]
    mysql.connect().commit


    cur = mysql.connect().cursor()
    cur.execute("select id from aprs where numberOfFlight=10001 ORDER BY id DESC LIMIT 1 ")
    last_id_aprs = list(cur.fetchall())
    last_id_aprs = last_id_aprs[0][0]

    mysql.connect().commit

    cur = mysql.connect().cursor()
    cur.execute("select id from telemetry where numberOfFlight=10001 ORDER BY id DESC LIMIT 1 ")
    last_id_telemetry = list(cur.fetchall())
    last_id_telemetry = last_id_telemetry[0][0]
    mysql.connect().commit

    try:
        os.remove('backend/modules/report.zip')
    except:
        pass
    return last_id_gprs,last_id_aprs,last_id_telemetry


