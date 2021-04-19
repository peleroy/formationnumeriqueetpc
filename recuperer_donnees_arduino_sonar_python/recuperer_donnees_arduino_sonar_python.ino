#include <Wire.h>
#include <rgb_lcd.h>
#include <Ultrasonic2.h>

rgb_lcd monRgb;
int d = 0 ;
Ultrasonic2 monUltrasonic_pin2(2);
unsigned long t = 0UL ;

void setup()
{
  monRgb.branch();
  Serial.begin(9600);
  monRgb.retroeclairage(10,10,10);
}

void loop()
{
  d = monUltrasonic_pin2.mesurer(1) ;
  t = millis() ;
  Serial.print(d);
  Serial.print(" ");
  Serial.print(t);
  Serial.println();
  monRgb.placerCurseurEn(0,0);
  monRgb.ecrire("d(cm):" );
  monRgb.ecrire(d );
  monRgb.placerCurseurEn(1,0);
  monRgb.ecrire("t(ms):" );
  monRgb.ecrire(String(t)  );
}
