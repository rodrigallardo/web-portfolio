# Artist Portfolio Website

A bilingual (Spanish/English) static portfolio website built with Astro, TypeScript, and Tailwind CSS. Features a classic gallery aesthetic for showcasing original artworks and prints.

## 🌐 Live Site

**Production:** https://rodrigallardo.github.io/web-portfolio

## ✨ Features

- **Bilingual Support:** Spanish (default) and English with easy language switching
- **Two Galleries:** Separate sections for Originals and Prints
- **Dynamic Detail Pages:** Each artwork has its own detail page with enlarged image
- **Classic Gallery Design:** Clean, minimal aesthetic with neutral colors
- **Responsive:** Mobile-first design that works on all devices
- **Static Site:** No CMS needed - content managed via JSON files
- **Auto-Deploy:** Push to main branch automatically deploys to GitHub Pages

## 🚀 Quick Start

### Prerequisites
- Node.js 20+ installed
- npm or pnpm

### Local Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# View at http://localhost:4321/web-portfolio
```

### Build for Production

```bash
# Create production build
npm run build

# Preview production build locally
npm run preview
```

## 📁 Project Structure

```
web-portfolio/
├── src/
│   ├── components/
│   │   └── Navigation.astro      # Navigation bar with language switcher
│   ├── content/
│   │   ├── config.ts              # Content collections schema
│   │   ├── originals/             # Original artworks (JSON files)
│   │   └── prints/                # Prints (JSON files)
│   ├── i18n/
│   │   ├── en.json                # English translations
│   │   ├── es.json                # Spanish translations
│   │   └── index.ts               # i18n utilities
│   ├── layouts/
│   │   └── Layout.astro           # Main page layout
│   ├── pages/
│   │   ├── index.astro            # Originals gallery (Spanish)
│   │   ├── prints.astro           # Prints gallery (Spanish)
│   │   ├── about.astro            # About page (Spanish)
│   │   ├── originals/[id].astro   # Artwork detail page
│   │   ├── prints/[id].astro      # Print detail page
│   │   └── en/                    # English language pages
│   └── styles/
│       └── global.css             # Tailwind imports
├── public/
│   └── images/                    # Artwork images (optimized)
├── .github/
│   └── workflows/
│       └── deploy.yml             # CI/CD workflow
└── astro.config.mjs               # Astro configuration
```

## 🎨 Managing Content

### Adding a New Artwork

1. **Add the image** to `public/images/`:
   ```bash
   # Place optimized image in public/images/
   public/images/my-painting.jpg
   ```

2. **Create a JSON file** in `src/content/originals/` or `src/content/prints/`:
   ```json
   {
     "title": "My Painting Title",
     "description": "Description of the artwork...",
     "price": "$500",
     "year": 2024,
     "dimensions": "24 x 36 inches",
     "medium": "Oil on canvas",
     "image": "/images/my-painting.jpg",
     "available": true
   }
   ```

3. **Name the file** (filename becomes the URL):
   - File: `my-painting.json`
   - URL: `/web-portfolio/originals/my-painting`

4. **Commit and push** to deploy:
   ```bash
   git add .
   git commit -m "Add new painting"
   git push origin main
   ```

### Editing Existing Artwork

Simply edit the JSON file in `src/content/originals/` or `src/content/prints/`, then commit and push.

### Deleting Artwork

1. Delete the JSON file from `src/content/originals/` or `src/content/prints/`
2. Optionally delete the image from `public/images/`
3. Commit and push changes

## 🚢 Deployment

### Automatic Deployment (Recommended)

The site automatically deploys to GitHub Pages when you push to the `main` branch.

**Setup (One-time):**
1. Go to your GitHub repository Settings
2. Navigate to Pages → Source
3. Select "GitHub Actions" as the source

**To Deploy:**
```bash
git push origin main
```

The GitHub Actions workflow will automatically:
1. Build the Astro site
2. Deploy to GitHub Pages
3. Site will be live at `https://rodrigallardo.github.io/web-portfolio`

### Manual Deployment

```bash
# Build the site
npm run build

# The dist/ folder contains the static site
# Upload contents to any static hosting service
```

## 🌍 Languages

The site supports Spanish (default) and English:

- **Spanish (default):** `/web-portfolio/`
- **English:** `/web-portfolio/en/`

### Adding Translations

Edit the translation files:
- `src/i18n/es.json` - Spanish translations
- `src/i18n/en.json` - English translations

## 🎨 Customization

### Colors

Edit Tailwind classes in component files or add custom colors to `tailwind.config.mjs`.

### Fonts

Current fonts (via Google Fonts):
- **Headings:** Playfair Display (serif)
- **Body:** Inter (sans-serif)

Change in `src/layouts/Layout.astro`.

### About Page Content

Edit:
- `src/pages/about.astro` (Spanish)
- `src/pages/en/about.astro` (English)

## 📋 Commands Reference

| Command | Action |
|---------|--------|
| `npm install` | Install dependencies |
| `npm run dev` | Start dev server at `localhost:4321` |
| `npm run build` | Build production site to `./dist/` |
| `npm run preview` | Preview production build locally |
| `npm run astro check` | Type-check the project |

## 🛠 Tech Stack

- **Framework:** [Astro](https://astro.build) v5.17
- **Language:** TypeScript (strict mode)
- **Styling:** [Tailwind CSS](https://tailwindcss.com) v4
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions

## 📝 Future Features

- WhatsApp contact button with painting-specific templates
- Image optimization script for managing high-res originals
- Google Analytics integration

## 📄 License

All artwork and content © Artist Name. All rights reserved.
