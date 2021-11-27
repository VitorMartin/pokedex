/*********************************************/
// This procedure reads a bitmap and draws it to the screen
// its sped up by reading many pixels worth of data at a time
// instead of just one pixel at a time. increading the buffer takes
// more RAM but makes the drawing a little faster. 20 pixels' worth
// is probably a good place


#define BUFFPIXEL 20

void bmpdraw(File f, int x, int y) 
{
  bmpFile.seek(bmpImageoffset);

  uint32_t time = millis();
  uint16_t p;
  uint8_t g, b;
  int i, j;

  uint8_t sdbuffer[3 * BUFFPIXEL];  // 3 * pixels to buffer
  uint8_t buffidx = 3*BUFFPIXEL;


  for (i=0; i< bmpHeight; i++) 
  {

    for (j=bmpWidth; j>0; j--) 
    {
      // read more pixels
      if (buffidx >= 3*BUFFPIXEL) 
      {
        bmpFile.read(sdbuffer, 3*BUFFPIXEL);
        buffidx = 0;
      }

      // convert pixel from 888 to 565
      b = sdbuffer[buffidx++];     // blue
      g = sdbuffer[buffidx++];     // green
      p = sdbuffer[buffidx++];     // red

      p >>= 3;
      p <<= 6;

      g >>= 2;
      p |= g;
      p <<= 5;

      b >>= 3;
      p |= b;

      // write out the 16 bits of color
      Tft.setPixel(j,i,p);
    }
  }
  Serial.print(millis() - time, DEC);
  Serial.println(" ms");
}
