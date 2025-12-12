# WET - Projekt

Dieses Repository enthält zwei Ordner:

## 1. Django Tutorial
Dieser Ordner enthält das **obligatorische Django-Tutorial**, um zu zeigen, dass das offizielle Django-Tutorial vollständig bearbeitet wurde.

## 2. Portfolio
Dieser Ordner enthält das **Hauptprojekt (Portfolio-Webseite)**.  
Das Projekt wurde nach der gleichen Django-Struktur wie im Tutorial umgesetzt und folgt den üblichen Django-Konventionen (Models, Views, Templates, Static Files, Tests).

Die Webseite wurde **nicht deployed** und ist für die lokale Ausführung vorgesehen.

---

## Lokale Ausführung

Zuerst in den Portfolio-Ordner wechseln:

```bash
cd Portfolio
```

Danach den Django-Entwicklungsserver starten:

```bash
python manage.py runserver
```

Die Webseite ist anschließend im Browser unter http://127.0.0.1:8000/ erreichbar.


## Portfolio – Ordnerstruktur

Die Ordnerstruktur des Portfolio-Projekts folgt der üblichen Django-Projektstruktur:

```
.
├── main/ # Haupt-Django-App
│ ├── migrations/ # Datenbank-Migrationen
│ ├── static/
│ │ └── main/ # Statische Dateien der App
│ │ ├── style.css # Zentrales Stylesheet
│ │ ├── me.webp # Profilbild
│ │ └── cv.pdf # Lebenslauf als PDF
│ ├── templates/
│ │ └── main/ # HTML-Templates der App
│ │ ├── base.html # Basis-Template
│ │ ├── home.html # Startseite
│ │ └── cv.html # CV-Seite
│ ├── admin.py # Admin-Konfiguration
│ ├── apps.py # App-Konfiguration
│ ├── models.py # Datenbank-Modelle (Projects, Skills)
│ ├── tests.py # Automatisierte Tests
│ └── views.py # Views (Home, CV, Suche)
│
├── portfolio/ # Projekt-Konfiguration
│ ├── settings.py # Zentrale Django-Settings
│ ├── urls.py # URL-Routing
│ ├── asgi.py # ASGI-Konfiguration
│ └── wsgi.py # WSGI-Konfiguration
│
├── db.sqlite3 # SQLite-Datenbank
└── manage.py # Django-Management-Skript
```



### Kurzbeschreibung
- Die App **`main`** enthält die gesamte Logik, Templates, statischen Dateien und Tests des Portfolios.
- Der Ordner **`portfolio`** enthält die globale Projektkonfiguration.
- Die Datenbank wird lokal über **SQLite** verwaltet.



## Einsatz von KI im Projekt

Der Code wurde grösstenteils selbst geschrieben. Einige wenige Korrekturen von ChatGPT wurden übernommen, jedoch nur, nachdem sie vollständig verstanden wurden.

KI wurde hauptsächlich als Lernhilfe eingesetzt, insbesondere um zu verstehen, warum bestimmter Code nicht funktionierte oder weshalb Fehlermeldungen auftraten. Sie diente dabei als Unterstützung beim Nachvollziehen von Konzepten und bei der Fehlersuche, jedoch nicht als Ersatz für eigenes Denken oder eigenständiges Programmieren.


### Stärken der KI

Die KI kennt sich gut mit allgemeinen Regeln in Django, HTML und CSS aus. Während ich HTML mithilfe von Übungen auf w3schools.com lernte, konnte sie mir erklären, warum meine Antworten falsch waren oder warum bestimmte Lösungen dennoch Sinn ergaben.
Auch in Bezug auf meine Erfahrungen mit Django konnte die KI meist fehlerfrei einschätzen, welche Funktionen oder Namensgebungen zu einer Idee passen oder welche vermutlich gemeint waren.


### Schwächen der KI

Je umfangreicher ein Projekt wird, desto schwieriger ist es für ChatGPT, den Überblick darüber zu behalten, was bereits implementiert ist. Außerdem musste mir die Seite selbst auch visuell gefallen. Viele Vorschläge der KI ignorierten meine bisherige Seite, deren Stil oder meine eigenen Ideen.

Aus diesem Grund nutzte ich die KI meist so, dass ich zuerst selbst versuchte, ein Problem zu lösen. Wenn ich dabei nicht erfolgreich war, fragte ich die KI, indem ich meinen Code, das Ergebnis und mein Ziel schilderte. Auch hierbei musste jedoch mehrfach klargestellt werden, dass ich nicht möchte, dass ChatGPT die Aufgabe vollständig selbst programmiert. Stattdessen sollte sie mir Dinge erklären. Dennoch gab sie häufig sehr lange Code-Blöcke als Lösungen für vergleichsweise einfache Fragen aus, obwohl ich zuvor explizit darum gebeten hatte, nur Erklärungen zu liefern und keinen fertigen Code.