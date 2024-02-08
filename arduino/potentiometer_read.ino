void setup()
{
    Serial.begin(9600);
}
void loop()
{
    // Read data from potentiometer
    int potentiometer_value = analogRead(A0);
    // Get current time
    unsigned long time = millis();
    // Send data through the serial port
    Serial.print(time);
    Serial.print(",");
    Serial.println(potentiometer_value);
    // Wait one second to read potentiometer value again
    delay(1000);
}