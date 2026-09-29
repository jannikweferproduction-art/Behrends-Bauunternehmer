import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://besserbauenbehrends.de',
  trailingSlash: 'always',
  integrations: [sitemap({ filter: (page) => !page.includes('/kontakt/danke/') })],
});
