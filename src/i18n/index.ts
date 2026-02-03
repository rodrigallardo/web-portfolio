import es from './es.json';
import en from './en.json';

export const languages = {
  es: 'Español',
  en: 'English',
};

export const defaultLang = 'es';

export const ui = {
  es,
  en,
} as const;

export function getLangFromUrl(url: URL) {
  // Account for base path /web-portfolio
  const pathname = url.pathname;

  // Check if path contains /en/ or starts with /web-portfolio/en
  if (pathname.includes('/en/') || pathname.includes('/en')) {
    return 'en' as keyof typeof ui;
  }

  return defaultLang;
}

export function useTranslations(lang: keyof typeof ui) {
  return function t(key: string) {
    const keys = key.split('.');
    let value: any = ui[lang];
    for (const k of keys) {
      value = value[k];
    }
    return value || key;
  };
}
