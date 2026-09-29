# Besser bauen Behrends – Website

Website für das Bauunternehmen von Janek Behrends, Wittmund.
Gebaut mit [Astro](https://astro.build) als statische Website: kein WordPress, keine Datenbank, keine Cookies.

## Befehle

| Befehl | Wirkung |
|---|---|
| `npm install` | Abhängigkeiten installieren (einmalig) |
| `npm run dev` | Vorschau unter http://localhost:4321, aktualisiert sich beim Speichern |
| `npm run build` | Fertige Website in den Ordner `dist/` bauen |
| `npm run preview` | Den gebauten Stand aus `dist/` ansehen |

**Veröffentlichen:** `npm run build` ausführen und den **Inhalt** von `dist/` per FTP/SFTP in das Hauptverzeichnis des Webspace laden (inklusive der versteckten `.htaccess`-Dateien).

## Inhalte pflegen

| Was | Wo |
|---|---|
| Telefon, E-Mail, Adresse, Einzugsgebiet | `src/data/betrieb.ts` |
| Texte der drei Leistungsseiten | `src/content/leistungen/*.md` |
| Projekte (Galerie) | `src/content/projekte.yaml` |
| Fotos | `src/assets/fotos/` |
| Startseite, Über uns, Kontakt | `src/pages/*.astro` |
| Impressum, Datenschutz | `src/pages/impressum.astro`, `src/pages/datenschutz.astro` |
| Farben, Schriften, Abstände | `src/styles/global.css` (oben unter `:root`) |

### Neues Projekt hinzufügen

1. Foto (JPG, Querformat, mindestens 1600 px breit) nach `src/assets/fotos/` kopieren, z. B. `pflaster-02-einfahrt.jpg`.
2. In `src/content/projekte.yaml` einen Eintrag ergänzen:

   ```yaml
   - id: einfahrt-jever
     titel: Einfahrt mit Betonsteinpflaster
     leistung: aussenanlagen        # umbau-sanierung | neubau-rohbau | aussenanlagen
     bild: ../assets/fotos/pflaster-02-einfahrt.jpg
     alt: Frisch gepflasterte Einfahrt vor einem Klinkerhaus
     detail: Unterbau neu, Rinne zur Entwässerung
     ort: Jever                     # optional
     jahr: 2026                     # optional
     format: quer                   # quer | hoch | quadrat
   ```

3. `npm run build` – Bilder werden automatisch verkleinert und in moderne Formate (AVIF/WebP) umgewandelt.

Die ersten zwei Projekte einer Leistung erscheinen automatisch auch auf der jeweiligen Leistungsseite, die ersten vier Projekte (außer dem Hero-Foto) auf der Startseite.

## Kontaktformular

`public/kontakt.php` verschickt Anfragen per E-Mail an die Adresse in der Datei. Voraussetzung: Webspace mit PHP und funktionierender `mail()`-Funktion (bei den üblichen deutschen Hostern Standard). Die Absenderadresse `website@besserbauenbehrends.de` sollte beim Hoster existieren oder erlaubt sein, sonst landen Mails im Spam.

Ohne PHP-Webspace (z. B. Netlify) muss das Formular auf einen Formulardienst umgestellt werden (`action` in `src/components/KontaktAbschnitt.astro`).

## Projektunterlagen

Strategie, Designrichtungen, Bilderliste und Entwürfe liegen in `docs/`, Originalmaterial in `material/`.
