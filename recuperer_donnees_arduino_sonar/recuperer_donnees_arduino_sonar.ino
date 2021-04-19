#include <Wire.h>
#include <rgb_lcd.h>
#include <Ultrasonic2.h>

rgb_lcd monRgb;
int d = 0 ;
Ultrasonic2 monUltrasonic_pin2(2);

void setup()
{
  monRgb.branch();
  Serial.begin(9600);
  monRgb.retroeclairage(10,10,10);
}

void loop()
{
  d = monUltrasonic_pin2.mesurer(1) ;
  Serial.print(d);
  Serial.println();
  monRgb.placerCurseurEn(0,0);
  monRgb.ecrire("d(cm):" );
  monRgb.ecrire(d );
}
