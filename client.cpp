#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>

// WLAN-Konfiguration
const char* ssid = "xxxx";
const char* password = "xxxxx";
const char* ip =  "http://x.x.x.x:5000"

// GPIO-Konfiguration
const int GPIO_PIN = 4;

// Initialisierung
int ID = 0;
int pin = 0;
int old_pin = pin;

// WiFi-Client erstellen
WiFiClient client;

void setup() {
  // Serielle Schnittstelle initialisieren
  Serial.begin(115200);

  // Verbindung zum WLAN herstellen
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Verbindung zum WLAN wird hergestellt...");
  }
  Serial.println("Verbunden mit WLAN: " + String(ssid));

  // GPIO-Pin konfigurieren
  pinMode(GPIO_PIN, INPUT);
  int pin = digitalRead(GPIO_PIN);
  int old_pin = pin;
}

void loop() {
  // Aktuellen Pinwert lesen
  int pin = digitalRead(GPIO_PIN);
  Serial.println(pin);
  // Wenn sich der Pinwert geändert hat
  if (pin != old_pin) {
    // Daten als JSON kodieren
    String data = "{\"pin\": " + String(pin) + ", \"id\": " + String(ID) + "}";

    // HTTP-POST-Anfrage senden
    HTTPClient http;
    http.begin(client, ip);
    http.addHeader("Content-Type", "application/json");
    int httpResponseCode = http.POST(data);
    String response = http.getString();
    http.end();

    // Antwort ausgeben
    Serial.println("HTTP-Code: " + String(httpResponseCode));
    Serial.println("Antwort: " + response);
  }

  // Aktuellen Pinwert speichern
  old_pin = pin;

  // Kurze Pause, um CPU-Last zu reduzieren
  delay(100);
}