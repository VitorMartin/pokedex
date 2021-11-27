/*
 * drawRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) 
 * fillRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) 
*/

#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;
#define BLACK 0x0000
#define NAVY 0x000F
#define DARKGREEN 0x03E0
#define DARKCYAN 0x03EF
#define MAROON 0x7800
#define PURPLE 0x780F
#define OLIVE 0x7BE0
#define LIGHTGREY 0xC618
#define DARKGREY 0x7BEF
#define BLUE 0x001F
#define GREEN 0x07E0
#define CYAN 0x07FF
#define RED 0xF800
#define MAGENTA 0xF81F
#define YELLOW 0xFFE0
#define WHITE 0xFFFF
#define YELLOW 0xFD20
#define GREENYELLOW 0xAFE5
#define PINK 0xF81F


int ApertureDiameter = 12;
int delayMS = 400;

int x_size = 320;
int y_size = 240;

int x_centre = x_size/2;
int y_centre = y_size/2;

int NA_radius = 50;

unsigned short *line = 0;

int16_t x_rect1 = 36;
int16_t y_rect1 = 36;
int16_t h_rect1 = 96;
int16_t w_rect1 = 96;
int16_t color_rect1 = WHITE;




void setup() {
  Serial.begin(9600);
  uint16_t ID = tft.readID(); // Lê o ID do display e armazena na variável
  Serial.print ("Identificador do driver: ");
  Serial.println(ID,HEX);
  tft.begin(ID); // Pega o ID que foi salvo e deixa o LCD pronto para começar
  tft.setRotation(1);
  tft.fillScreen(YELLOW);
  tft.setCursor(10, 100);
  tft.drawRect(x_rect1, y_rect1, w_rect1, h_rect1, color_rect1);
  tft.fillRect(x_rect1, y_rect1, w_rect1, h_rect1, color_rect1);
  tft.setTextColor(PINK);
  tft.setTextSize(3);
  tft.print("Meu driver: ");
  tft.setCursor(220,100);
  tft.print(String(ID,HEX));
  
}

void loop() {

}
