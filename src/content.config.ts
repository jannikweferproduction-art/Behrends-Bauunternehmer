import { defineCollection } from 'astro:content';
import { glob, file } from 'astro/loaders';
import { z } from 'astro/zod';

// Leistungsseiten: eine Markdown-Datei pro Leistungsbereich.
const leistungen = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/leistungen' }),
  schema: ({ image }) =>
    z.object({
      titel: z.string(),
      kurztitel: z.string(),
      reihenfolge: z.number(),
      seitentitel: z.string(),
      beschreibung: z.string(),
      ueberschrift: z.string(),
      einleitung: z.string(),
      anlaesse: z.array(z.string()),
      leistungen: z.array(z.object({ titel: z.string(), text: z.string() })),
      bild: image(),
      bildAlt: z.string(),
      kontaktTitel: z.string(),
      kontaktText: z.string(),
      whatsappText: z.string(),
    }),
});

// Projekte: Liste in src/content/projekte.yaml.
const projekte = defineCollection({
  loader: file('src/content/projekte.yaml'),
  schema: ({ image }) =>
    z.object({
      titel: z.string(),
      leistung: z.enum(['umbau-sanierung', 'neubau-rohbau', 'aussenanlagen']),
      bild: image(),
      alt: z.string(),
      ort: z.string().optional(),
      jahr: z.number().optional(),
      detail: z.string().optional(),
      format: z.enum(['quer', 'hoch', 'quadrat']).default('quer'),
    }),
});

export const collections = { leistungen, projekte };
