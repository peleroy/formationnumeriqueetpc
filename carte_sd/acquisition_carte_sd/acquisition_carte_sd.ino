#include <SD.h>
#include <SDPlus.h>
#include <codeCache.h>
#include <Duinoedu_MathPlus.h>

SDPlus maSD;
boolean __ardublockDigitalRead(int pinNumber)
{
  pinMode(pinNumber, INPUT);
  return digitalRead(pinNumber);
}


unsigned long tmp = 0UL ;
int _ABVAR_2_a;
void clignotement();
int _ABVAR_3_a;

void setup()
{
  pinMode( 2 , INPUT);
  maSD.brancher(4);
  pinMode( 3 , OUTPUT);
}

void loop()
{
  if (__ardublockDigitalRead(2))
  {
    maSD.brancher(4);
    maSD.definirFichierCourant("file.txt");	
    clignotement(2);
    maSD.ecrire("t(ms) T(oC)");
    maSD.nouvelleLigne(1);
    tmp = millis() ;
    for (_ABVAR_2_a=1; _ABVAR_2_a<= ( 5 ); ++_ABVAR_2_a )
    {
      maSD.ecrire(String(( millis() - tmp )) );
      maSD.espace(1);
      maSD.tabulation(0);
      maSD.ecrire(convertirEnDegres(analogRead(A0)));
      maSD.nouvelleLigne(1);	
      delay( 1000 );
    }
    clignotement(5);
  }
}

void clignotement(int nb)
{
  for (_ABVAR_3_a=1; _ABVAR_3_a<= ( nb ); ++_ABVAR_3_a )
  {
    digitalWrite(3 , HIGH);
    delay( 100 );
    digitalWrite(3 , LOW);
    delay( 100 );
  }
}
