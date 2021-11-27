#include <MCUFRIEND_kbv.h>
#include <SPI.h>

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

#define pinBtnEsq 11
#define pinBtnDir 10

int idCounter = 1;

extern int pkmLen;
extern uint8_t pokemon_logo[];
extern uint8_t pokeball[];
extern uint8_t* pkmBmpArr[10];
extern uint8_t* pkmNameArr[10];
extern uint8_t* pkmTypeArr[10];

void setup() {
  pinMode(pinBtnEsq, INPUT);
  pinMode(pinBtnDir, INPUT);
  
  uint16_t ID = tft.readID();
  tft.begin(ID);
  tft.setRotation(1);
  
  drawPkm(idCounter, pkmNameArr[idCounter], pkmTypeArr[idCounter]);
}

void loop() {
  if (digitalRead(pinBtnEsq)){
    if (idCounter == 1) idCounter = pkmLen - 1;
    else idCounter--;
    drawPkm(idCounter, pkmNameArr[idCounter], pkmTypeArr[idCounter]);
  }
  else if (digitalRead(pinBtnDir)){
    if (idCounter == pkmLen - 1) idCounter = 1;
    else idCounter++;
    drawPkm(idCounter, pkmNameArr[idCounter], pkmTypeArr[idCounter]);
  }
}

void refreshScreen(){
  tft.fillScreen(BLACK);
  tft.setCursor(10, 100);
  tft.drawRect(8, 36, 96, 96, WHITE);
  tft.drawRect(112, 112, 200, 18, WHITE);
  tft.fillRect(112, 112, 200, 18, WHITE);
  tft.drawRect(112, 151, 200, 18, WHITE);
  tft.fillRect(112, 151, 200, 18, WHITE);
  tft.drawRect(112, 190, 200, 18, WHITE);
  tft.fillRect(112, 190, 200, 18, WHITE);
  drawBitmap(120, 10, pokemon_logo, 180, 101, WHITE);
  drawBitmap(18, 150, pokeball, 75, 75, WHITE);
}

void drawPkm(int id, char* nome, char* type) {
  refreshScreen();

  // SPRITE
  drawBitmap(8, 36, pkmBmpArr[id], 96, 96, WHITE);
  
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
  tft.print(type);
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
