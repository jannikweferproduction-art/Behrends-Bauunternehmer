<?php
// Verarbeitet das Anfrageformular und leitet per E-Mail an den Betrieb weiter.
// Voraussetzung: Webspace mit PHP und funktionierender mail()-Funktion.

$empfaenger = 'janekbehrends@gmx.de';
$absender   = 'website@besserbauenbehrends.de'; // Adresse der eigenen Domain, damit Mails nicht als Spam gelten

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /kontakt/', true, 303);
    exit;
}

// Spam-Falle: Dieses Feld ist für Menschen unsichtbar.
if (!empty($_POST['webseite'])) {
    header('Location: /kontakt/danke/', true, 303);
    exit;
}

function feld(string $name, int $max = 200): string {
    $wert = trim((string)($_POST[$name] ?? ''));
    $wert = str_replace(["\r", "\0"], '', $wert);
    return mb_substr($wert, 0, $max);
}

$name      = feld('name', 120);
$telefon   = feld('telefon', 60);
$email     = feld('email', 160);
$ort       = feld('ort', 120);
$art       = feld('art', 80);
$zeitraum  = feld('zeitraum', 120);
$nachricht = feld('nachricht', 5000);

$gueltig = $name !== '' && $telefon !== '' && $ort !== '' && $art !== '' && $nachricht !== ''
    && ($email === '' || filter_var($email, FILTER_VALIDATE_EMAIL));

if (!$gueltig) {
    header('Location: /kontakt/?fehler=1#kontakt', true, 303);
    exit;
}

// Zeilenumbrüche in Kopfzeilen verhindern (Header-Injection).
$einzeilig = fn(string $s): string => preg_replace('/[\n\t]+/', ' ', $s);

$betreff = 'Website-Anfrage: ' . $einzeilig($art) . ' in ' . $einzeilig($ort);
$text = "Neue Anfrage über besserbauenbehrends.de\n\n"
      . "Name:      $name\n"
      . "Telefon:   $telefon\n"
      . "E-Mail:    " . ($email ?: '–') . "\n"
      . "Ort:       $ort\n"
      . "Vorhaben:  $art\n"
      . "Zeitraum:  " . ($zeitraum ?: '–') . "\n\n"
      . "Nachricht:\n$nachricht\n";

$kopf = [
    'From: Website Besser bauen Behrends <' . $absender . '>',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
];
if ($email !== '') {
    $kopf[] = 'Reply-To: ' . $einzeilig($email);
}

$ok = mail($empfaenger, '=?UTF-8?B?' . base64_encode($betreff) . '?=', $text, implode("\r\n", $kopf));

header('Location: ' . ($ok ? '/kontakt/danke/' : '/kontakt/?fehler=2#kontakt'), true, 303);
exit;
