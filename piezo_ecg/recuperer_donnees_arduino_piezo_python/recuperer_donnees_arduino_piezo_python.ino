int A = 0 ;
unsigned long t = 0UL ;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  A = analogRead(A0) ;
  t = millis() ;
  Serial.print(A);
  Serial.print(" ");
  Serial.print(t);
  Serial.println();
}
