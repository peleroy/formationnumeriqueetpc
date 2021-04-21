#include <rgb_lcd.h>
#include <TSTemperature.h>

rgb_lcd rgbLcd;
double _ABVAR_1_T = 0.0 ;
unsigned long _ABVAR_2_t = 0UL ;

void setup()
{
  rgbLcd.begin(16,2);
  Serial.begin(9600);
  rgbLcd.setRGB(constrain(10,0,255),constrain(10,0,255),constrain(10,0,255));
}

void loop()
{
  _ABVAR_1_T = getTemperature(analogRead(0), 10000.0f, 3975) ;
  _ABVAR_2_t = millis() ;
  Serial.print(_ABVAR_2_t);
  Serial.print("/");
  Serial.print(_ABVAR_1_T);
  Serial.println();
  rgbLcd.setCursor(0, 0);
  rgbLcd.print("T(oC)=" );
  rgbLcd.print(_ABVAR_1_T );
  rgbLcd.print("                ");
  rgbLcd.setCursor(0, 1);
  rgbLcd.print("t(ms)=" );
  rgbLcd.print(_ABVAR_2_t );
  rgbLcd.print("                ");
  delay( 2000 );
}


