#include <Wire.h>
#include <rgb_lcd.h>
#include <Duinoedu_MathPlus.h>

rgb_lcd monRgb;
double T = 0.0 ;
unsigned long t = 0UL ;

void setup()
{
  monRgb.branch();
  Serial.begin(9600);
  monRgb.retroeclairage(10,10,10);
}

void loop()
{
  T = convertirEnDegres(analogRead(A0)) ;
  t = millis() ;
  Serial.print(t);
  Serial.print(" ");
  Serial.print(T,1);
  Serial.println();
  monRgb.placerCurseurEn(0,0);
  monRgb.ecrire("T(oC):" );
  monRgb.ecrire(String(T,1)  );
  monRgb.placerCurseurEn(1,0);
  monRgb.ecrire("t(ms):" );
  monRgb.ecrire(String(t)  );
  delay( 2000 );
}
