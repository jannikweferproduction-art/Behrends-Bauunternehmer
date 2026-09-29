// Zentrale Firmendaten – hier ändern, dann gelten sie auf der ganzen Website.
export const betrieb = {
  name: 'Besser bauen Behrends',
  zusatz: 'Bauunternehmen',
  inhaber: 'Janek Behrends',
  beruf: 'Maurer',
  gruendung: 'November 2023',
  strasse: 'An den Eichen 19',
  plz: '26409',
  ort: 'Wittmund',
  telefonAnzeige: '0172 4300736',
  telefonLink: 'tel:+491724300736',
  whatsappNummer: '491724300736',
  email: 'janekbehrends@gmx.de',
  einzugsgebiet: [
    'Wittmund',
    'Carolinensiel',
    'Esens',
    'Friedeburg',
    'Jever',
    'Schortens',
    'Wilhelmshaven',
    'Aurich',
    'Wiesmoor',
  ],
  umkreisKm: 40,
};

export const whatsappLink = (text = 'Hallo Herr Behrends, ich habe eine Anfrage zu folgendem Vorhaben: ') =>
  `https://wa.me/${betrieb.whatsappNummer}?text=${encodeURIComponent(text)}`;

export const navigation = [
  { href: '/umbau-sanierung/', label: 'Umbau & Sanierung', gruppe: 'leistungen' },
  { href: '/neubau-rohbau/', label: 'Neubau & Rohbau', gruppe: 'leistungen' },
  { href: '/aussenanlagen/', label: 'Außenanlagen', gruppe: 'leistungen' },
  { href: '/projekte/', label: 'Projekte' },
  { href: '/ueber-uns/', label: 'Über uns' },
  { href: '/kontakt/', label: 'Kontakt' },
];
