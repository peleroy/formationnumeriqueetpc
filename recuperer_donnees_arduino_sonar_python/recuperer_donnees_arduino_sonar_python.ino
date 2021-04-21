#include <rgb_lcd.h>
#include <Ultrasonic.h>

rgb_lcd rgbLcd;
int _ABVAR_1_d = 0 ;
Ultrasonic us_pin2(2);
unsigned long _ABVAR_2_t = 0UL ;

void setup()
{
  rgbLcd.begin(16,2);
  Serial.begin(9600);
  rgbLcd.setRGB(constrain(10,0,255),constrain(10,0,255),constrain(10,0,255));
}

void loop()
{
  _ABVAR_1_d = us_pin2.MeasureInCentimeters() ;
  _ABVAR_2_t = millis() ;
  Serial.print(_ABVAR_1_d);
  Serial.print("/");
  Serial.print(_ABVAR_2_t);
  Serial.println();
  rgbLcd.setCursor(0, 0);
  rgbLcd.print("d(cm)=" );
  rgbLcd.print(_ABVAR_1_d );
  rgbLcd.print("                ");
  rgbLcd.setCursor(0, 1);
  rgbLcd.print("t(ms)=" );
  rgbLcd.print(_ABVAR_2_t );
  rgbLcd.print("                ");
}


