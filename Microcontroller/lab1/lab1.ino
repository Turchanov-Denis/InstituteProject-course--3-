// Turchanov Denis 3PM ADMO
int State = 0; // текущее состояние кнопки

int lastState = 0; // последнее состояние кнопки

int selector = 0; // переключатель (вкл. или выкл. светодиоды)

void setup()
{
  pinMode(2, INPUT); // получение "данных"
  pinMode(13, OUTPUT); // вывод "данных"
  pinMode(12, OUTPUT); // вывод "данных"
}

void loop()
{
  State = digitalRead(2); // считываем, в каком состоянии сейчас кнопка
  if (State != lastState) { // если отличается от предыдущего состояния то проверяем нажата ли кнопка
    if (State == HIGH) { // если кнопка не нажата
      if (selector == 0) { // меняем на противоположное
        selector = 1;
      } else {
        selector = 0;
      }
    }
    delay(10); // Ждем 10 миллисекунд
  }
  lastState = State; // присваиваем последнему состоянию настоящее состояние кнопки
  if (selector == 1) { // если переключатель включен, то зажигаем диоды
    delay(250); // Ждем 250 миллисекунд
    digitalWrite(13, HIGH); // включаем красный диод
    digitalWrite(12, LOW);  // отключаем синий диод
    delay(250); // Ждем 250 миллисекунд
    digitalWrite(13, LOW); // отключаем красный диод
    digitalWrite(12, HIGH); // включаем синий диод
  } else {
    digitalWrite(13, LOW); // отключаем красный диод
    digitalWrite(12, LOW); // отключаем синий диод
  }
}