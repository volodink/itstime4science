#include <stdio.h>
#include <string.h>
#include <stddef.h>
#include <stdbool.h>
#include <inttypes.h>
#include <time.h>
#include <malloc.h>

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
    float vect_axel1;
    float vect_axel2;
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
    packet.lat = 10.123;
    packet.lon = 110.0;
    packet.alt = 20.9;
    packet.temp1 = 10.123;
    packet.temp2 = 10.123;
    packet.pressure1 = 10.123;
    packet.pressure2 = 10.123;
    packet.bat_crg = 99;
    packet.bat_volt = 11.2;
    packet.bat_temp = 20.5;
    packet.vect_axel1 = 4.0;
    packet.vect_axel2 = 5.0;
    packet.ultraviolet1 = 10.1;
    packet.ultraviolet2 = 32.2;
    packet.infrared1 = 53.0;
    packet.infrared2 = 42.0;
    packet.hdop = 12.3;
    packet.vdop = 12.3;
    packet.sats = 14;
    packet.radiation = 14.4;
    packet.dust = 15.0;
    packet.ozone = true;
    packet.status = "11101111111111111111111";
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
    printf("sizeof status = %lu\n", sizeof(packet.status));
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