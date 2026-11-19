# Nukis Wortwelt (Wort-Spielplatz) – Regeln für Claude

Spielerische Lern-App für Kinder mit Sprachstörungen (Logopädie), Hauptfigur Nuki das Eichhörnchen.
Besitzer: Hamdi. **Immer auf Deutsch antworten**, einfache Sprache, Schritt für Schritt. Hamdi programmiert
nicht selbst – mach die Arbeit, prüfe sie, und sag ihm dann kurz, was er sieht und wo.

Live: https://canzo-kinder.github.io/wort-spielplatz/ (GitHub Pages, Repo `Canzo-Kinder/wort-spielplatz`, Branch `main`).

## Wichtig: Es arbeiten oft ZWEI Claude-Sitzungen gleichzeitig an diesem Repo

- **Vor jeder Änderung:** `git fetch && git pull --rebase`. Vor dem Commit nochmal.
- Kleine, fokussierte Commits. Nichts umbauen oder „aufräumen“, worum nicht gebeten wurde –
  die andere Sitzung baut vielleicht gerade daran.
- Bei Konflikten: die Änderungen der anderen Seite **behalten** und die eigenen darauf setzen,
  nie mit `--force` pushen.
- Konflikt in `sw.js`: einfach die Version von `main` nehmen und danach `python3 werkzeug/sw-erneuern.py` ausführen.
- Testbilder, Mitschnitte usw. NIE ins Repo legen (Scratchpad benutzen). Vor dem Commit `git status` ansehen.

## Aufbau

- `index.html` – die ganze App in EINER Datei (HTML/CSS/JS, ca. 700 KB). Keine Build-Schritte, kein Framework.
- `sw.js` – Offline-Speicher (Service Worker). `CORE` = Dateien fürs Offline-Paket, `CLIPS` = alle Sprachaufnahmen.
- `n/*.mp3` – Nukis Sprachaufnahmen (ElevenLabs-Stimme). Zuordnung Text → Datei steht als `CLIPS={…}` in `index.html`;
  Schlüssel = `ckey(text)` (klein geschrieben, ohne Satzzeichen). Fehlt ein Clip, spricht die Geräte-Stimme – das klingt
  falsch, also jeden neuen Satz, den Nuki sagt, als Clip aufnehmen.
- `sfx/*.mp3` – eigene, synthetisch erzeugte Soundeffekte der Spielplatz-Spiele (über `sfx(name)`; Rückfall auf `tone()`).
- `f/` Schriften (Baloo 2, Nunito), `lib/` three.js & jsPDF, `tex/` Texturen, `m/` 3D-Tiere, `v/` Videos und gemalte Hintergründe.
- `werkzeug/sw-erneuern.py` – erneuert Version und Clip-Liste des Offline-Speichers.

## Nach JEDER Änderung an index.html, Clips oder Dateien in CORE

1. Neue Dateien, die offline gebraucht werden, in `CORE` in `sw.js` eintragen (Videos `.mp4` werden absichtlich
   nicht gespeichert, nur ihr Standbild).
2. `python3 werkzeug/sw-erneuern.py` ausführen. Die Version muss die Form `ws-<hex>` behalten
   (sonst findet das Skript sie nicht mehr). Ohne neue Version bekommen Handys die Änderung nicht.
3. Testen (siehe unten), dann committen und pushen.
4. Warten, bis GitHub Pages fertig ist:
   `until gh run list -L1 --json status -q '.[0].status' | grep -q completed; do sleep 5; done`
5. Live prüfen (neue Version und Dateien unter der Live-Adresse abrufbar) – erst dann Hamdi „fertig“ sagen.

## Testen

- Mit Playwright (vorinstalliert): mindestens Handy hoch (390×844), Handy quer (844×390), Tablet (1024×768), Computer.
- Auf JS-Fehler, abgeschnittene Knöpfe, waagrechtes Überlaufen, fehlende Clips und hängende Spiele achten.
- Mikrofon-Spiele mit Fake-Audio testen (`--use-file-for-fake-audio-capture`); am Mac ist das Mikrofon deutlich
  leiser als am iPhone (deshalb gibt es `DESK` mit eigener Schwelle).
- iPhone/iPad sind die wichtigsten Geräte. Android und Mac müssen auch funktionieren.

## Inhalt und Kinderschutz

- Zielgruppe: kleine Kinder (Altersstufen klein/mittel/groß), oft mit Sprachstörung. Kurze Sätze, freundlich, nie
  beschämend („Ups! Nochmal versuchen?“ statt „Falsch“).
- Das Mikrofon hört nur während des Spiels zu; nichts wird aufgenommen oder verschickt. Keine Tracking- oder
  Analyse-Dienste einbauen, keine Daten der Kinder an fremde Server.
- Fortschritt bleibt nur im Gerät (`localStorage`); der Bericht für die Logopädie wird lokal als PDF erzeugt.
- Spielplatz-Spiele kosten Sterne und haben ein Tageslimit, das Eltern einstellen (Eltern-Bereich).

## Werkzeuge außerhalb des Repos

- Neue Nuki-Clips: werden auf Hamdis Server mit ElevenLabs erzeugt (über den Auftrags-Mechanismus am Mac, siehe
  CLAUDE.md in `~/canzo-live` auf Hamdis Mac). API-Schlüssel nie anzeigen oder in Dateien schreiben.
- Higgsfield (Bilder/Videos von Nuki) ist als Verbindung vorhanden; Credits kosten Geld – vorher sagen, wie viele.
