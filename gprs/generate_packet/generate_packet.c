#include <stdio.h>
#include <stdbool.h>
#include <inttypes.h>
#include <time.h>
#include <stdbool.h>
#pragma pack (push,1)

struct gprs_telem_packet {
    uint8_t start[3]; /* SYT */
    uint32_t time;
    float lat;
    float lon;
    float alt;
    float temp1;
    float temp2;
    float pressure1;
    float pressure2;
    uint8_t bat_crg;
    float bat_volt;
    float bat_temp;
    float vect_axel1x;
    float vect_axel1y;
    float vect_axel1z;
    float vect_axel2x;
    float vect_axel2y;
    float vect_axel2z;
    float ultraviolet1;
    float ultraviolet2;
    float infrared1;
    float infrared2;
    float hdop;
    float vdop;
    uint8_t sats;
    float radiation;
    float dust;
    uint8_t ozone;
    uint32_t status;
    uint8_t stop[3]; /* TYS */
};
#pragma pack (pop)

typedef struct gprs_telem_packet gprs_telem_packet;

gprs_telem_packet gprsTelemetryPacketBuilder() {
    gprs_telem_packet packet;

    packet.start[0] = 0x53;
    packet.start[1] = 0x59;
    packet.start[2] = 0x54;
    packet.lat = 1111.123;
    packet.lon = 130.0;
    packet.alt = 213.9;
    packet.temp1 = 18.123;
    packet.temp2 = 10.123;
    packet.pressure1 = 10.123;
    packet.pressure2 = 0.123;
    packet.bat_crg = 9;
    packet.bat_volt = 11.2;
    packet.bat_temp = 20.5;
    packet.vect_axel1x = 441.0;
    packet.vect_axel1y = -10.0;
    packet.vect_axel1z = 5.0;
    packet.vect_axel2x = 64.0;
    packet.vect_axel2y = 0.0;
    packet.vect_axel2z = 1.0;
    packet.ultraviolet1 = 10.1;
    packet.ultraviolet2 = 332.2;
    packet.infrared1 = 53.0;
    packet.infrared2 = 42.0;
    packet.hdop = 12.3;
    packet.vdop = 12234.3;
    packet.sats = 123;
    packet.radiation = 1.4;
    packet.dust = 154.0;
    packet.ozone = true;
    packet.status = 2;
    packet.stop[0] = 0x54;
    packet.stop[1] = 0x59;
    packet.stop[2] = 0x53;

    return packet;
}

int main()
{
    int start_t,end_t,i=0,l;

    FILE *file;
    file = fopen("../gprs_packet.bin","w");
    uint8_t *p;
    gprs_telem_packet packet;
    packet = gprsTelemetryPacketBuilder();
    p = &packet;
    start_t = clock();
    packet.time = time(NULL);
    printf("sizeof(struct gprs_telem_packet) = %lu\n", sizeof(gprs_telem_packet));
//    for(i=0;i<sizeof(packet);i++) {
//        printf("[%04d] %X\n", i, p[i]);
//    }
    fwrite (&packet, sizeof(char),sizeof(packet), file );
    fclose(file);
    return 0;

}



/*struct tm* aTm = localtime(&t);
end_t = clock();
printf("%f %f\n", start_t,end_t);
end_t = end_t - start_t;
s.year=aTm->tm_year+1900;
s.mon = aTm->tm_mon+1;
s.day = aTm->tm_mday;
s.hour = aTm->tm_hour;
s.min = aTm->tm_min;
s.sec = aTm->tm_sec;
s.ms = end_t;
printf("%i%i%i%i%i%i%i\n",aTm->tm_year+1900, aTm->tm_mon+1, aTm->tm_mday, aTm->tm_hour, aTm->tm_min, aTm->tm_sec,end_t);
printf("%i%i%i%i%i%i%i\n",s.year,s.mon,s.day,s.hour,s.min,s.sec,s.ms);
*/

/*print/x (unsigned char[])packet.lat*/