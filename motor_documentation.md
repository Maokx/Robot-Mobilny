# Moduł motor - dokumentacja

Numer pinu | Opis
-----------|-----
12 | Prędkość lewej strony
13 | Prędkość prawej strony
19 | 1 z 2 pinów kierunku lewej strony
16 | 2 z 2 pinów kierunku lewej strony
26 | 1 z 2 pinów kierunku prawej strony
20 | 2 z 2 pinów kierunku prawej strony

## Funkcje:
- init() - Funkcja ustawia odpowiednie piny jako wyjścia. Uruchamia instacnje PWM dla pinów prędkości. Konfiguruje prędkość początkową na 0. Funkcja jest konieczna do poprawnego uruchomienia modułu. 

- direction(lewa_kierunek, prawa_kierunek) - Ustawienie kierunku ruchu dla lewej pary napędowej oraz prawej pary. Parametry mogą przyjmować wartości 1 (do przodu), 0 (do tyłu)

- drive(predkosc, kierunek) - Jazda robota po lini prostej do przodu lub do tyłu. Parametr predkosc może przyjmować wartości z zakresu 0-100 (0 robot zatrzymany, 100 maksymalna prędkość). Parametr kierunek moze przyjmowac wartosci 1 lub 0, gdzie 1 oznacza jazdę do przodu, 0 jazdę do tyłu.

