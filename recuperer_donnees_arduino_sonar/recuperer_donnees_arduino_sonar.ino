#include <rgb_lcd.h>
#include <Ultrasonic.h>

rgb_lcd rgbLcd;
int _ABVAR_1_d = 0 ;
Ultrasonic us_pin2(2);

void setup()
{
  rgbLcd.begin(16,2);
  Serial.begin(9600);
  rgbLcd.setRGB(constrain(10,0,255),constrain(10,0,255),constrain(10,0,255));
}

void loop()
{
  _ABVAR_1_d = us_pin2.MeasureInCentimeters() ;
  Serial.print(_ABVAR_1_d);
  Serial.println();
  rgbLcd.setCursor(0, 0);
  rgbLcd.print("d(cm)=" );
  rgbLcd.print(_ABVAR_1_d );
  rgbLcd.print("                ");
}


