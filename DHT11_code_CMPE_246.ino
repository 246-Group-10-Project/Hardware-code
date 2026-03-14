//Import DHT library 
#include <DHT.h>
#include <Arduino.h>

//DHT setup
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin(11); 
}

void loop(){
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)){
    Serial.println("Sensor read failed");
    delay(2000);
    return;
  }

  Serial.print("The temperature is:");
  Serial.print(t);
  Serial.print("C");

  Serial.print(" The Humidity is: ");
  Serial.print(h);
  Serial.println("%");

  delay(2000);
}