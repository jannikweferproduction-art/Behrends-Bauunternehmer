# Phase 5 – Freigabe

Besser bauen Behrends · Stand: 29.09.2026

## 1. Unternehmen
Janek Behrends, gelernter Maurer, Einzelunternehmen „Besser bauen Behrends – Bauunternehmen“, An den Eichen 19, 26409 Wittmund. Gegründet 11/2023. Leistungen: Umbau & Sanierung (Schwerpunkt), Neubau & Rohbau, Außenanlagen & Entwässerung. Einzugsgebiet Landkreis Wittmund + Nachbarkreise (ca. 40 km). Zielgruppen: private Hausbesitzer und Bauherren, Architekten. Ziele: Kunden gewinnen, Vertrauen aufbauen, später Mitarbeiter gewinnen.

## 2. Seitenstruktur
Start · Umbau & Sanierung · Neubau & Rohbau · Außenanlagen · Projekte · Über uns · Kontakt · Impressum · Datenschutz → Details: `phase-2-strategie.md`

## 3. Inhalte und Texte
Positionierung, Versprechen, Hero A, Leistungstexte, Ablauf, Kontaktbereich, SEO → `phase-2-strategie.md`

## 4./5. Design
Drei Richtungen → `phase-3-designrichtungen.md`, Entwürfe → `entwuerfe/`
**Gewählt: Richtung 1 – Verband**, ergänzt um „Pos.“-Beschriftungen aus Richtung 2 für Handwerksdetails.

## 6. Bilder
→ `phase-4-bilder.md`

## 7. Technischer Umsetzungsvorschlag

| Thema | Entscheidung | Begründung |
|---|---|---|
| Grundlage | **Astro** (statische Website) | Sehr schnell, kein Server-Code, keine Plugin-Updates, sicher |
| Inhalte | Markdown-Dateien für Seiten/Leistungen, eine Projektliste | Pflege ohne HTML-Kenntnisse |
| Gestaltung | Eigenes CSS mit Design-Tokens | Kein Framework-Ballast, volle Kontrolle über das Verbandsraster |
| Schriften | Archivo + Source Sans 3, lokal eingebunden | Keine Verbindung zu Google (DSGVO) |
| Bilder | Automatische Optimierung (AVIF/WebP, mehrere Größen) | Schnelle Ladezeit auch mobil |
| Animation | Nur CSS + wenige Zeilen JavaScript (Rollschicht-Aufbau, dezentes Einblenden), abschaltbar über „reduzierte Bewegung“ | Keine zusätzliche Bibliothek nötig |
| Skills | `modern-web-design` für Designsystem, Barrierefreiheit, Responsive. **Nicht eingesetzt:** `motion-framer` und `animated-component-libraries` (setzen React voraus, hier nicht nötig), `gsap-scrollTrigger` (keine Scroll-Erzählung, die das rechtfertigt) | Keine unnötigen Abhängigkeiten |
| Kontaktformular | Kleines PHP-Skript beim Hoster (falls Webspace mit PHP) – sonst EU-Formulardienst | Daten bleiben in Deutschland/EU |
| WhatsApp | Link `wa.me` mit vorausgefülltem Text, kein eingebettetes Widget | Keine Datenübertragung beim Seitenaufruf |
| Karte | Statische Kartenskizze statt Google Maps | Kein Cookie-Banner nötig |
| Cookie-Banner | **Entfällt**, da keine Tracking- und keine Fremddienste | Besseres Nutzererlebnis |
| SEO | Seitentitel/Beschreibungen, `schema.org`-Firmendaten, Sitemap, saubere URLs | Lokale Auffindbarkeit |
| Barrierefreiheit | Ziel WCAG 2.2 AA: Kontraste, Tastaturbedienung, Fokus sichtbar, Überschriftenhierarchie, Alternativtexte | Pflicht und Qualitätsmerkmal |
| Rechtstexte | Impressum nach DDG (ohne veralteten OS-Plattform-Hinweis), Datenschutzerklärung passend zur schlanken Technik | Rechtssicherheit – finale Prüfung durch den Inhaber |
| Hosting | Offen – abhängig davon, wo die Domain liegt | Build läuft auf jedem Webspace |

## Offene Punkte (blockieren die Umsetzung nicht)
Alle **[bestätigen]**-Stellen gehen bis zur Rückmeldung von Janek Behrends **nicht** online: Sie werden entweder vorsichtig formuliert oder weggelassen. Nach seiner Rückmeldung werden sie ergänzt.
