import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax3d
from math import sqrt
import itertools
from time import strftime,strptime
from threading import Thread


def integration(*axis, N=1):
    for _ in range(N):
        axis = map(lambda x: list(itertools.accumulate(x)), axis)

    return list(axis)

def integration(*axis, N=1):
    for _ in range(N):
        axis = map(lambda x: list(itertools.accumulate(x)), axis)

    return list(axis)


def risovalka_for_3(data1, title1, data2, title2, data3, title3, name, characteristic, gprs_data,aprs_data,telemetry_data ):
    fig = plt.figure()  # графики
    plt.subplot(311)
    plt.plot( data1)
    plt.title('{}'.format(title1))  # IR
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(312)
    plt.plot( data2)
    plt.title('{}'.format(title2))
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(313)
    plt.plot( data3)
    plt.title('{}'.format(title3))
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.tight_layout()
    #plt.savefig("backend/modules/img/{}.png".format(name), fmt='png')


def risovalka_for_2(data1, title1, data2, title2, name, characteristic, gprs_data,telemetry_data ):
    fig = plt.figure()  # графики
    plt.subplot(211)
    plt.plot( data1)
    plt.title('{}'.format(title1))  # IR
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(212)
    plt.plot( data2)
    plt.title('{}'.format(title2))
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.tight_layout()
    #plt.savefig("backend/modules/img/{}.png".format(name), fmt='png')


def risovalka_for_axes(gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2, gprs_data,telemetry_data ):
    gx1, gy1, gz1 = integration(gx1, gy1, gz1, N=2)
    gx2, gy2, gz2 = integration(gx2, gy2, gz2, N=2)
    tx1, ty1, tz1 = integration(tx1, ty1, tz1, N=2)
    tx2, ty2, tz2 = integration(tx2, ty2, tz2, N=2)
    length_list = len(gx1)


    fig = plt.figure()  # графики изменения проекций ускорения по 3 осям
    plt.subplot(321)
    plt.plot(gprs_data, gx1)
    plt.title('Акселерометр(x)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(323)
    plt.plot(gprs_data, gy1)
    plt.title('Акселерометр(y)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(325)
    plt.plot(gprs_data, gz1)
    plt.title('Акселерометр(z)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(322)
    plt.plot(telemetry_data, tx1)
    plt.title('Акселерометр(x)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(324)
    plt.plot(telemetry_data, ty1)
    plt.title('Акселерометр(y)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(326)
    plt.plot(telemetry_data,tz1)
    plt.title('Акселерометр(z)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.tight_layout()
    #plt.savefig("backend/modules/img/XYZprojectionFirstAxel.png", fmt='png')

    fig = plt.figure()  # графики изменения проекций ускорения по 3 осям
    plt.subplot(321)
    plt.plot(str(gprs_data), gx2)
    plt.title('Акселерометр(x)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(323)
    plt.plot(str(gprs_data), gy2)
    plt.title('Акселерометр(y)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(325)
    plt.plot(str(gprs_data), gz2)
    plt.title('Акселерометр(z)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(322)
    plt.plot(str(telemetry_data), tx2)
    plt.title('Акселерометр(x)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(324)
    plt.plot(str(telemetry_data), ty2)
    plt.title('Акселерометр(y)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.subplot(326)
    plt.plot(str(telemetry_data),tz2)
    plt.title('Акселерометр(z)')
    plt.xticks(fontsize='6',rotation= 60)
    plt.yticks(fontsize='10')
    plt.xlabel('Дата и время')
    plt.ylabel('Дистанция, метры')
    plt.grid()

    plt.tight_layout()
    #plt.savefig("backend/modules/img/XYZprojectionSecondAxel.png", fmt='png')


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
    gx2 = []
    gy1 = []
    gy2 = []
    gz1 = []
    gz2 = []
    tx1 = []
    tx2 = []
    ty1 = []
    ty2 = []
    tz1 = []
    tz2 = []
    for i in range(len(gprs)):
        gx1.append(gprs[i][12])
        gy1.append(gprs[i][13])
        gz1.append(gprs[i][14])
        gx2.append(gprs[i][15])
        gy2.append(gprs[i][16])
        gz2.append(gprs[i][17])
    for i in range(len(telemetry)):
        tx1.append(telemetry[i][12])
        ty1.append(telemetry[i][13])
        tz1.append(telemetry[i][14])
        tx2.append(telemetry[i][15])
        ty2.append(telemetry[i][16])
        tz2.append(telemetry[i][17])
    return gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2



def parsing_datas3(n, m, data1, title1, data2, title2, data3, title3, name, characteristic, gprs_data,aprs_data,telemetry_data ):
    d1, d2, d3 = execute_from_db3(n, m, data1, data2, data3)
    risovalka_for_3(d1, title1, d2, title2, d3, title3, name, characteristic, gprs_data,aprs_data,telemetry_data)

def parsing_datas2(n, data1, title1, data2, title2, name, characteristic, gprs_data,telemetry_data):
    d1, d2 = execute_from_db2(n, data1, data2)
    risovalka_for_2(d1, title1, d2, title2, name, characteristic, gprs_data,telemetry_data)

def parsing_axels(data1, data2, gprs_data,telemetry_data ):
    gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2 = execute_axels(data1, data2)
    risovalka_for_axes(gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2, gprs_data,telemetry_data)


def hour_min_sec(tme):
    mas =[]
    print(type(tme))
    for i in range(len(tme)):
        t = strptime(str(tme[i]), '%Y-%m-%d %H:%M:%S')
        mas.append(strftime('%b %H:%M:%S',t))
    print(mas)
    return mas


def getData(mysql):
    cur = mysql.connect().cursor()
    l = cur.execute("select count(*) from gprs where numberOfFlight=10001")
    if l > 40:
        cur.execute("select * from gprs where id % (floor((select count(*) from gprs where numberOfFlight=10001)/4)) = 0")
    else: cur.execute("select * from gprs where numberOfFlight=10001")
    gprs = list(cur.fetchall())
    mysql.connect().commit
    cur = mysql.connect().cursor()
    l = cur.execute("select count(*) from aprs where numberOfFlight=10001")
    if l > 40:
        cur.execute("select * from aprs where id % (floor((select count(*) from aprs where numberOfFlight=10001)/4)) = 0")
    else: cur.execute("select * from aprs where numberOfFlight=10001")
    aprs = list(cur.fetchall())
    mysql.connect().commit
    cur = mysql.connect().cursor()
    l = cur.execute("select count(*) from telemetry where numberOfFlight=10001")
    if l > 40:
        cur.execute("select * from telemetry where id % (floor((select count(*) from telemetry where numberOfFlight=10001)/4)) = 0")
    else: cur.execute("select * from telemetry where numberOfFlight=10001")
    telemetry = list(cur.fetchall())
    mysql.connect().commit

    gprs_data,aprs_data,telemetry_data  = execute_from_db3(2, 2, gprs, aprs, telemetry)

    hour_min_sec(gprs_data)


    parsing_datas3(6,6, gprs, 'Температура 1 по gprs', aprs, 'Температура 1 по aprs', telemetry,
                   'Температура 1 по telemetry', 'temp1', 'Температура,°C',gprs_data,aprs_data,telemetry_data)

    parsing_datas3(8,7, gprs, 'Давление 1 по gprs', aprs, 'Давление 1 по aprs', telemetry, 'Давление 1 по telemetry',
                   'pressure1', 'Давление,Паскаль',gprs_data,aprs_data,telemetry_data )

    parsing_datas2(7, gprs, 'Температура 2 по gprs', telemetry, 'Температура 2 по telemetry', 'temp2', 'Температура,°C',gprs_data,telemetry_data )

    parsing_datas2(9,gprs, 'Давление 2 по gprs', telemetry, 'Давление 2 по telemetry', 'pressure2', 'Давление,Паскаль',gprs_data,telemetry_data)

    parsing_datas2(10,gprs, 'Напряжение аккумулятора по gprs', telemetry, 'Напряжение аккумулятора по telemetry', 'bat_volt',
                    'Напряжение аккумулятора,Вольт',gprs_data,telemetry_data)

    parsing_datas2(11,gprs, 'Температура аккумулятора по gprs', telemetry, 'Температура аккумулятора по telemetry', 'bat_temp',
                    'Температура аккумулятора,°C',gprs_data,telemetry_data)
    parsing_axels(gprs,telemetry,gprs_data,telemetry_data)

    parsing_datas2(18,gprs, 'Ультрафиолет 1 по gprs', telemetry, 'Ультрафиолет 1 по telemetry', 'ultraviolet1', 'Ультрафиолет,Люкс',gprs_data,telemetry_data)

    parsing_datas2(19,gprs, 'Ультрафиолет 2 по gprs', telemetry, 'Ультрафиолет 2 по telemetry', 'ultraviolet2', 'Ультрафиолет,Люкс',gprs_data,telemetry_data)

    parsing_datas2(20,gprs, 'Инфракрасное излучение 1 по gprs', telemetry, 'Инфракрасное излучение 1 по telemetry', 'infrared1', 'Инфракрасное излучение,Люкс',gprs_data,telemetry_data)

    parsing_datas2(21,gprs, 'Инфракрасное излучение 2 по gprs', telemetry, 'Инфракрасное излучение 2 по telemetry', 'infrared2', 'Инфракрасное излучение,Люкс',gprs_data,telemetry_data)

    parsing_datas2(22,gprs, 'Hdop по gprs', telemetry, 'Hdop по telemetry', 'hdop', 'Hdop',gprs_data,telemetry_data)

    parsing_datas2(23,gprs, 'Vdop по gprs', telemetry, 'Vdop по telemetry', 'vdop', 'Vdop',gprs_data,telemetry_data)

    parsing_datas2(24,gprs, 'SATS по gprs', telemetry, 'SATS по telemetry', 'sats', 'SATS',gprs_data,telemetry_data)

    parsing_datas2(25,gprs, 'Радиация по gprs', telemetry, 'Радиация по telemetry', 'radiation', 'Радиация, Рикрорентген',gprs_data,telemetry_data)

    parsing_datas2(26,gprs, 'Озон по gprs', telemetry, 'Озон по telemetry', 'ozone', 'Озон',gprs_data,telemetry_data)