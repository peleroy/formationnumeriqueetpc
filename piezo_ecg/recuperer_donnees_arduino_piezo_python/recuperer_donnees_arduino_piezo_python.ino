int _ABVAR_1_A = 0 ;
unsigned long _ABVAR_2_t = 0UL ;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  _ABVAR_1_A = analogRead(0) ;
  _ABVAR_2_t = millis() ;
  Serial.print(_ABVAR_1_A);
  Serial.print("/");
  Serial.print(_ABVAR_2_t);
  Serial.println();
}


