import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax3d
from math import sqrt
import itertools

def simple_moving_average(data1):  # усреднение значений(простая скользящая средняя)
    lengthList1 = len(data1)
    if lengthList1 > 30:
        for i in range(lengthList1 - 30):  # усреднение значений
            iterator = 0
            for iterator_1 in range(30):
                iterator += 1
                data1[i] = data1[i] + data1[i + iterator]
            data1[i] = data1[i] / 30
        for i in range(30):
            data1.pop()
    return data1

def integration(*axis, N=1):
    for _ in range(N):
        axis = map(lambda x: list(itertools.accumulate(x)), axis)

    return list(axis)


def simple_moving_average_axelerometrs(func_data_x, func_data_y,func_data_z):  # усреднение значений(простая скользящая средняя)
    lengthList = len(func_data_x)
    if lengthList > 45:
        for i in range(lengthList - 45):  # усреднение значений
            iterator = 0
            for iterator_1 in range(45):
                iterator += 1
                func_data_x[i] = func_data_x[i] + func_data_x[i + iterator]
                func_data_y[i] = func_data_y[i] + func_data_y[i + iterator]
                func_data_z[i] = func_data_z[i] + func_data_z[i + iterator]
            func_data_x[i] = func_data_x[i] / 30
            func_data_y[i] = func_data_y[i] / 30
            func_data_z[i] = func_data_z[i] / 30


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


def integration(*axis, N=1):
    for _ in range(N):
        axis = map(lambda x: list(itertools.accumulate(x)), axis)

    return list(axis)


def risovalka_for_3(data1, title1, data2, title2, data3, title3, name, characteristic):
    data1 = simple_moving_average(data1)
    data2 = simple_moving_average(data2)
    data3 = simple_moving_average(data3)
    fig = plt.figure()  # графики
    plt.subplot(311)
    plt.plot(data1)
    plt.title('{}'.format(title1))  # IR
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(312)
    plt.plot(data2)
    plt.title('{}'.format(title2))
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(313)
    plt.plot(data3)
    plt.title('{}'.format(title3))
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.tight_layout()
    plt.savefig("modules/img/{}.png".format(name), fmt='png')


def risovalka_for_2(data1, title1, data2, title2, name, characteristic):
    data1 = simple_moving_average(data1)
    data2 = simple_moving_average(data2)
    fig = plt.figure()  # графики
    plt.subplot(211)
    plt.plot(data1)
    plt.title('{}'.format(title1))  # IR
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.subplot(212)
    plt.plot(data2)
    plt.title('{}'.format(title2))
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('{}'.format(characteristic))
    plt.grid()

    plt.tight_layout()
    plt.savefig("modules/img/{}.png".format(name), fmt='png')

def risovalka_for_axes(gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2):
    simple_moving_average_axelerometrs(gx1, gy1, gz1)
    simple_moving_average_axelerometrs(tx1, ty1, tz1)
    simple_moving_average_axelerometrs(gx2, gy2, gz2)
    simple_moving_average_axelerometrs(tx2, ty2, tz2)

    gx1, gy1, gz1 = integration(gx1, gy1, gz1, N=2)
    gx2, gy2, gz2 = integration(gx2, gy2, gz2, N=2)
    tx1, ty1, tz1 = integration(tx1, ty1, tz1, N=2)
    tx2, ty2, tz2 = integration(tx2, ty2, tz2, N=2)

    length_list = len(gx1)

    print("Длина траектории = ", calculating_the_distance(gx1, gy1, gz1))

    fig = plt.figure()  # график траектории перемещения
    ax = ax3d.Axes3D(fig)
    ax.plot(gx1, gy1, gz1, color='green')
    ax.scatter(gx1[0], gy1[0], gz1[0])
    ax.scatter(gx1[length_list - 1], gy1[length_list - 1], gz1[length_list - 1], color='red')
    plt.savefig("modules/img/trajectory.png", fmt='png')

    fig1 = plt.figure()  # графики изменения проекций ускорения по 3 осям
    plt.subplot(311)
    plt.plot(gx1)
    plt.title('Axelleration(x)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(312)
    plt.plot(gy1)
    plt.title('Axelleration(y)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(313)
    plt.plot(gz1)
    plt.title('Axelleration(z)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(321)
    plt.plot(tx1)
    plt.title('Axelleration(x)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(322)
    plt.plot(ty1)
    plt.title('Axelleration(y)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(323)
    plt.plot(tz1)
    plt.title('Axelleration(z)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.tight_layout()
    plt.savefig("modules/img/XYZprojectionFirstAxel.png", fmt='png')

    fig1 = plt.figure()  # графики изменения проекций ускорения по 3 осям
    plt.subplot(321)
    plt.plot(gx2)
    plt.title('Axelleration(x)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(322)
    plt.plot(gy2)
    plt.title('Axelleration(y)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(323)
    plt.plot(gz2)
    plt.title('Axelleration(z)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(324)
    plt.plot(tx2)
    plt.title('Axelleration(x)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(325)
    plt.plot(ty2)
    plt.title('Axelleration(y)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.subplot(326)
    plt.plot(tz2)
    plt.title('Axelleration(z)')
    plt.xticks(fontsize='10')
    plt.yticks(fontsize='10')
    plt.xlabel('Number of points')
    plt.ylabel('Distance, meters')
    plt.grid()

    plt.tight_layout()
    plt.savefig("modules/img/XYZprojectionSecondAxel.png", fmt='png')

def execute_from_db3(n,m,gprs,aprs,telemetry):
    data1 = []
    data2 = []
    data3 = []
    for i in range(len(gprs)):
        data1.append(gprs[i][n])
    for i in range(len(aprs)):
        data2.append(aprs[i][m])
    for i in range(len(telemetry)):
        data3.append(telemetry[i][n])
    return data1,data2,data3

def execute_from_db2(n,gprs,telemetry):
    data1 = []
    data2 = []
    for i in range(len(gprs)):
        data1.append(gprs[i][n])
    for i in range(len(telemetry)):
        data2.append(telemetry[i][n])
    return data1,data2

def execute_axels(gprs,telemetry):
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
    return  gx1,gy1,gz1,gx2,gy2,gz2,tx1,ty1,tz1,tx2,ty2,tz2

def clear_list3(d1, d2, d3):
    d1.clear()
    d2.clear()
    d3.clear()
def clear_list2(d1, d2):
    d1.clear()
    d2.clear()

def parsing_datas3(n,m, data1, title1, data2, title2, data3, title3, name, characteristic):
    d1,d2,d3 = execute_from_db3(n,m,data1,data2,data3)
    risovalka_for_3(d1, title1, d2, title2, d3, title3, name, characteristic)
    clear_list3(d1, d2, d3)


def parsing_datas2(n, data1, title1, data2, title2, name, characteristic):
    d1, d2 = execute_from_db2(n,data1,data2)
    risovalka_for_2(d1, title1, d2, title2, name, characteristic)
    clear_list2(d1, d2)

def parsing_axels(data1, data2):
    gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2 = execute_axels(data1,data2)
    risovalka_for_axes(gx1, gy1, gz1, gx2, gy2, gz2, tx1, ty1, tz1, tx2, ty2, tz2)

def getData(mysql):

    cur = mysql.connect().cursor()
    cur.execute("select * from gprs WHERE numberOfFlight = 10001")
    gprs = list(cur.fetchall())

    mysql.connect().commit
    cur = mysql.connect().cursor()
    cur.execute("select * from aprs WHERE numberOfFlight = 10001")
    aprs = list(cur.fetchall())
    mysql.connect().commit
    cur = mysql.connect().cursor()
    cur.execute("select * from telemetry WHERE numberOfFlight = 10001")
    telemetry = list(cur.fetchall())
    mysql.connect().commit

    parsing_datas3(6,6, gprs, 'Temperature 1 from gprs', aprs, 'Temperature 1 from aprs', telemetry,
                   'Temperature 1 from telemetry', 'temp1', 'Temperature,°C', )

    parsing_datas3(8,7, gprs, 'Pressure 1 from gprs', aprs, 'Pressure 1 from aprs', telemetry, 'Pressure 1 from telemetry',
                   'pressure1', 'Pressure,P', )

    parsing_datas2(7, gprs, 'Temperature 2 from gprs', telemetry, 'Temperature 2 from telemetry', 'temp2', 'Temperature,°C', )

    parsing_datas2(9,gprs, 'Pressure 2 from gprs', telemetry, 'Pressure 2 from telemetry', 'pressure2', 'Pressure,P')

    parsing_datas2(10,gprs, 'Battery voltage from gprs', telemetry, 'Battery voltage from telemetry', 'bat_volt',
                    'Battery voltage,Volt')

    parsing_datas2(11,gprs, 'Battery temperature from gprs', telemetry, 'Battery temperature from telemetry', 'bat_temp',
                    'Battery temperature,°C')
    parsing_axels(gprs,telemetry)

    parsing_datas2(18,gprs, 'Ultraviolet 1 from gprs', telemetry, 'Ultraviolet 1 from telemetry', 'ultraviolet1', 'Ultraviolet,Lux')

    parsing_datas2(19,gprs, 'Ultraviolet 2 from gprs', telemetry, 'Ultraviolet 2 from telemetry', 'ultraviolet2', 'Ultraviolet,Lux')

    parsing_datas2(20,gprs, 'Infrared 1 from gprs', telemetry, 'Infrared 1 from telemetry', 'infrared1', 'Infrared,Lux')

    parsing_datas2(21,gprs, 'Infrared 2 from gprs', telemetry, 'Infrared 2 from telemetry', 'infrared2', 'Infrared,Lux')

    parsing_datas2(22,gprs, 'Hdop from gprs', telemetry, 'Hdop from telemetry', 'hdop', 'Hdop')

    parsing_datas2(23,gprs, 'Vdop from gprs', telemetry, 'Vdop from telemetry', 'vdop', 'Vdop')

    parsing_datas2(24,gprs, 'SATS from gprs', telemetry, 'SATS from telemetry', 'sats', 'SATS')

    parsing_datas2(25,gprs, 'Radiation from gprs', telemetry, 'Radiation from telemetry', 'radiation', 'Radiation,Microrentgen')

    parsing_datas2(26,gprs, 'Ozone from gprs', telemetry, 'Ozone from telemetry', 'ozone', 'Ozone')

