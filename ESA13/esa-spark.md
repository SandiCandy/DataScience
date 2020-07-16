# Installation
* Betriebssystem OS X
* Paketmanager Homebrew (macht das Leben leichter…)
* Installation über Homebrew (Probleme: Java8 wird benötigt). Nach Installation von Java8 keine weiteren Probleme

# Anwendung
'''spark-submit spark-esa.py

# Anmerkungen Lösung (auch in spark-esa.py enthalten)

- "Einleitungstext" (alles, was vor dem ersten Werk steht) wurde manuell gelöscht
- "Copyrighttexte und Punktion (.,;:()...) in spark-esa.py automatisiert entfernt

## Einschränkungen
* Verkuerzte Worte wie "I'll" = I will, "that`s"="that is" werden als eigenstaendige Woerter gesehen
* Prinzipiell kann man noch Stopwoerter (haeufig auftretente und meist irrelevante Woerter zur Erfassung des Inhalts) herausfiltern - war hier allerdings nicht gefordert
* Weiterhin ist es sinnvoll Anfuehrungszeichen zu filtern also 'Beispiel --> Beispiel), dabei ist zu beachten, dass ' auch im Wort vorkommen kann (I'll)
* Aehnliches gilt fuer - (z.B. Beispiel- --> Beispiel). Aber auch - kann mitten im Wort vorkommen (z.B. wild-fowl)

## Lösung
Lösung siehe Screenshot 'ergebnis.png' *have mit 5873x*
