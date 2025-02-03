// Turchanov Denis 3PM ADMO
#include <DHT.h> // библиотека для датчика DHT
#include <LiquidCrystal_I2C.h> // библиотека для дисплея с подключением I2C
#include <RTClib.h> // библиотека для работы с DS1307
#include "Adafruit_BMP085.h" // библиотека для работы с BMP085
#include <Wire.h> // библиотека для работы с I2C

DHT dht(2, DHT22); // сообщаем на каком порту датчик
LiquidCrystal_I2C LCD(0x27, 16, 2); // присваиваем имя LCD для дисплея
RTC_DS1307 rtc; // обозначаем датчик DS1307
Adafruit_BMP085 bmp; // обозначаем дачтки BMP085
float humidity, temperature; // значения влажности и температуры
int hour, minute, second, pressure; // значения часа, минуты, секунды и давления
void setup() {
  dht.begin(); // запускаем датчик DHT
  rtc.begin(); // запускаем датчик DS1307
  bmp.begin(); // запускаем датчик BMP085
  LCD.init();  // инициализация дисплея
  LCD.backlight();  // включение подсветки дисплея
}

void loop() {
  humidity  =  dht.readHumidity(); // считываем влажность
  temperature = dht.readTemperature(); // считываем температуру
  pressure = bmp.readPressure(); // считываем давление (т.к. BMP180 здесь нет, то ищем давление данным способом)
  DateTime now = rtc.now(); // считываем время
  hour = now.hour(); // час
  minute = now.minute(); // минута
  second = now.second(); // секунда
  LCD.setCursor(0, 0); // ставим курсор в первую ячейку первой строки
  LCD.print(hour); // выводим час
  LCD.print(":"); // разделитель времени
  LCD.print(minute); // выводим минуты
  LCD.print(":");  // разделитель времени
  LCD.print(second); // выводим секунды
  LCD.print(" ");  // разделитель времени
  LCD.print(temperature); // выводим температуру
  LCD.print("C"); // выводим единицу измерения температуры
  LCD.setCursor(0, 1); // ставим курсор в первую ячейку второй строки
  LCD.print(pressure); // выводим давление
  LCD.print("PA "); // выводим единицу измерения давления
  LCD.print(humidity); // выводим влажность
  LCD.print("%");
  delay(1000); // ждем 1000 миллисекунд
}