
## Name
Erste ETL-Pipeline mit Finanzdaten

## Beschreibung
Einarbeitung in praktische Anwendung von ETL-Prozessen.\
Scraping mittels request und API.\
Transformation (Bereinigung) mittels Pandas.\
Querying der Daten mittels SQL.\
Visualisierung mittels Matplotlib (oder Seaborn).\
Machine-Learning Algorithmen für Zeitreihen-Analyse

## Zukünftige Roadmap
TO-DO / Weitere Add-Ons: \
Scheduling und mehrere Quellen extrahieren, integrieren (Duplikaterkennung, Schema Matching)\
Verwendung anderer Technologien: NoSQL oder Cloud anstatt SQL verwenden, Apache Spark für Batch Processing, NiFi und Airflow \
Interaktive Dashboards / Integration in Power BI

## Inspiration und Hilfestellungen
Vorlesung "Data Engineering", gelesen von Prof. Dr. Fabian Panse, Universität Augsburg \
"Fundamentals of Data Engineering"
"Data Engineering with Python"
"Principles of Data Integration"

## Projektstatus
Beginn: 30.08.2024 \
Basic Framework hergestellt: Zieht Zeitreihendaten mittels API und lädt Daten in MySQL DBS \
Alle Symbole auf einmal gescraped, neue Spalte "rate_of_change"; \
Integration und Scheduling abgeschlossen (Stand 14.09.24)\ 
Als nächstes Visualisierung und EDA + PDA mit Machine-Learning\
Voraussichtlich abgeschlossen: 30.09.2024 \
Wöchentliche Updates folgen

### Features der DB-Connection
- Create Table if not exists
- Insert einen Stock
    - Update Data wenn der Timestamp schon existiert
    - Komplett Inserten, wenn es das noch nicht gibt.
- Stock Info holen
