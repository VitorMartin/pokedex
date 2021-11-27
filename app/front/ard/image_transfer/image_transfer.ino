/*  Demo of draw circle's APP
    drawCircle(int poX, int poY, int r,INT16U color);
    fillCircle(int poX, int poY, int r,INT16U color);
*/

#include <stdint.h>
#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;
#include <SPI.h>

#define WHITE 0xFFFF
#define BLACK 0x0000


int ApertureDiameter = 12;
int delayMS = 400;

int x_size = 320;
int y_size = 240;

int x_centre = x_size/2;
int y_centre = y_size/2;

int NA_radius = 50;

unsigned short *line = 0;


void setup()
{  
  Serial.begin(9600);
  uint16_t ID = tft.readID();
  tft.begin(ID); // Pega o ID que foi salvo e deixa o LCD pronto para começar
  tft.setRotation(1);
  delay(1000);
  
  tft.fillCircle(x_centre, y_centre, ApertureDiameter/2, WHITE);
  delay(1000);
  tft.fillCircle(x_centre, y_centre, ApertureDiameter/2, BLACK);
  
  line = new unsigned short[x_size];


  Serial.println(-1.0);
}

void loop()
{

  int bytes;
    if (Serial.available() > 0) {
        //char cmd = Serial.read();
        //switch (cmd) {
        //case 'I': // image
            Serial.println("Iniciando...");
            byte receive = Serial.read();
            Serial.println("Imagem: \n");
            Serial.println(receive);
            for (int row = 0; row < x_size; row++) {
                Serial.println("Começando loop");
                bytes = x_size * 2; // one line has 240 pixel @ 2 byte per pixel (color)
                char* p = (char*)line;
                while (bytes > 0) { // serial port has a buffer of only 64 bytes, iterate until the entire line has been read
                    int n = Serial.readBytes(p, bytes);
                    if (n == 0) {
                        // timeout
                        Serial.println("Nao tem nada nessa porra");
                        return;
                    }
                    p += n;
                    bytes -= n;
                }
                for (int col = 0; col < y_size; col++)
                     tft.drawPixel(col,row,line[col]);
                     Serial.flush(); 
            }
            Serial.println("Deveria ter printado");
        //}
    }

    Serial.println("Fora dos for");
}
