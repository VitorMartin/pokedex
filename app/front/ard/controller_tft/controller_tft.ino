/*
 * drawRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) 
 * fillRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color) 
*/

#include <MCUFRIEND_kbv.h>
#include <SPI.h>
#include <SD.h>
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

extern uint8_t* pkmBmpAllArray[9];
extern uint8_t pokemon_logo[];
extern uint8_t pokeball[];
//const unsigned char sprite[] PROGMEM;


int ApertureDiameter = 12;
int delayMS = 400;

int x_size = 320;
int y_size = 240;

int x_centre = x_size/2;
int y_centre = y_size/2;

int NA_radius = 50;

unsigned short *line = 0;

int16_t x_rect1 = 8;
int16_t y_rect1 = 36;
int16_t h_rect1 = 96;
int16_t w_rect1 = 96;
int16_t color_rect1 = WHITE;

int16_t x_rect2 = 112;
int16_t y_rect2 = 72+40;
int16_t h_rect2 = 18;
int16_t w_rect2 = 200;
int16_t color_rect2 = WHITE;

int16_t x_rect3 = 112;
int16_t y_rect3 = 111+40;
int16_t h_rect3 = 18;
int16_t w_rect3 = 200;
int16_t color_rect3 = WHITE;

int16_t x_rect4 = 112;
int16_t y_rect4 = 150+40;
int16_t h_rect4 = 18;
int16_t w_rect4 = 200;
int16_t color_rect4 = WHITE;


int16_t x_logo = 120;
int16_t y_logo = 10;
int16_t h_logo = 50;
int16_t w_logo = 180;
int16_t color_logo = WHITE;

void setup() {
  Serial.begin(9600);
  uint16_t ID = tft.readID(); // Lê o ID do display e armazena na variável
  Serial.print ("Identificador do driver: ");
  Serial.println(ID,HEX);
  tft.begin(ID); // Pega o ID que foi salvo e deixa o LCD pronto para começar
  tft.setRotation(1);

  refreshScreen();
  delay(1000);
}

void loop() {
  char pk1[] = "1;Bulbasaur;Grass, Poison";
  char pk2[] = "4;Charmander;Fire";
  char pk3[] = "7;Squirtle;Water";
  drawPkm(pk1);
  delay(1000);
  drawPkm(pk2);
  delay(1000);
  drawPkm(pk3);
  delay(1000);
  
  /*
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.println(data); //1;Bulbasaur;Poison, grass
    drawPkm(data)
  }
  */
}

void refreshScreen(){
  tft.fillScreen(BLACK);
  tft.setCursor(10, 100);
  tft.drawRect(x_rect1, y_rect1, w_rect1, h_rect1, color_rect1);
  tft.drawRect(x_rect2, y_rect2, w_rect2, h_rect2, color_rect2);
  tft.fillRect(x_rect2, y_rect2, w_rect2, h_rect2, color_rect2);
  tft.drawRect(x_rect3, y_rect3, w_rect3, h_rect3, color_rect3);
  tft.fillRect(x_rect3, y_rect3, w_rect3, h_rect3, color_rect3);
  tft.drawRect(x_rect4, y_rect4, w_rect4, h_rect4, color_rect4);
  tft.fillRect(x_rect4, y_rect4, w_rect4, h_rect4, color_rect4);
  drawBitmap(x_logo, y_logo, pokemon_logo, 180, 101, WHITE);
  drawBitmap(18, 150, pokeball, 75, 75, WHITE);
}

void drawPkm(char msg[]) {
  char* id = strtok(msg, ";");
  char* nome = strtok(NULL, ";");
  char* tipos = strtok(NULL, ";");

  refreshScreen();
  // SPRITE
  switch (*id){
    case '1':
      extern uint8_t pkmBmp1[];
      drawBitmap(8, 36, pkmBmp1, 96, 96, WHITE);
      break;
    case '2':
      extern uint8_t pkmBmp2[];
      drawBitmap(8, 36, pkmBmp2, 96, 96, WHITE);
      break;
    case '3':
      extern uint8_t pkmBmp3[];
      drawBitmap(8, 36, pkmBmp3, 96, 96, WHITE);
      break;
    case '4':
      extern uint8_t pkmBmp4[];
      drawBitmap(8, 36, pkmBmp4, 96, 96, WHITE);
      break;
    case '5':
      extern uint8_t pkmBmp5[];
      drawBitmap(8, 36, pkmBmp5, 96, 96, WHITE);
      break;
    case '6':
      extern uint8_t pkmBmp6[];
      drawBitmap(8, 36, pkmBmp6, 96, 96, WHITE);
      break;
    case '7':
      extern uint8_t pkmBmp7[];
      drawBitmap(8, 36, pkmBmp7, 96, 96, WHITE);
      break;
    case '8':
      extern uint8_t pkmBmp8[];
      drawBitmap(8, 36, pkmBmp8, 96, 96, WHITE);
      break;
    case '9':
      extern uint8_t pkmBmp9[];
      drawBitmap(8, 36, pkmBmp9, 96, 96, WHITE);
      break;
    default:
      break;
  }
  // ID
  tft.setCursor(190, 114);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print(id);

  // NOME
  tft.setCursor(120, 153);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print(nome);

  // TIPO
  tft.setCursor(120,192);
  tft.setTextColor(BLACK);
  tft.setTextSize(2);
  tft.print(tipos);
}

void drawBitmap(int16_t x, int16_t y, uint8_t *bitmap, int16_t w, int16_t h, uint16_t color) {
  int16_t i, j, byteWidth = (w + 7) / 8;
  uint8_t byte;

  for(j=0; j<h; j++) {
    for(i=0; i<w; i++) {
      if(i & 7) byte <<= 1;
      else      byte   = pgm_read_byte(bitmap + j * byteWidth + i / 8);
      if(byte & 0x80) tft.drawPixel(x+i, y+j, color);
    }
  }
}
