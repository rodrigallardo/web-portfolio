# Artist Portfolio Website

A bilingual (Spanish/English) static portfolio website built with Astro, TypeScript, and Tailwind CSS. Features a classic gallery aesthetic for showcasing original artworks and prints.

## 🌐 Live Site

**Production:** https://rodrigallardo.github.io/web-portfolio

## ✨ Features

- **Bilingual Support:** Spanish (default) and English with easy language switching
- **Two Galleries:** Separate sections for Originals and Prints
- **Dynamic Detail Pages:** Each artwork has its own detail page with enlarged image
- **WhatsApp Integration:** Floating contact button + inline "Ask about this painting" buttons
- **Google Analytics 4:** Track artwork views, WhatsApp clicks, language switches, and navigation
- **Minimal Gallery Design:** Ultra-minimal navigation, no footer, subtle interactions - inspired by professional oil painter portfolios
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

## 📊 Analytics Setup (Optional)

Google Analytics 4 is pre-configured but disabled by default. To enable tracking:

### Step 1: Create GA4 Account

1. Go to https://analytics.google.com
2. Sign in with your Google account
3. Click "Admin" (gear icon in bottom left)
4. Under "Property" column, click "Create Property"
5. Enter property name (e.g., "Artist Portfolio")
6. Set timezone and currency
7. Click "Next" → "Create"

### Step 2: Create Data Stream

1. Under "Data Streams", click "Add stream" → "Web"
2. Enter URL: `https://rodrigallardo.github.io/web-portfolio`
3. Enter stream name: "GitHub Pages"
4. Click "Create stream"
5. **Copy the Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 3: Configure GitHub Secret (Production)

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `GA_MEASUREMENT_ID`
5. Value: `G-XXXXXXXXXX` (your Measurement ID)
6. Click **Add secret**

### Step 4: Configure Local Development (Optional)

1. Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Measurement ID:
   ```env
   PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
   ```

3. Restart the dev server:
   ```bash
   npm run dev
   ```

**Note:** The `.env` file is gitignored and only used for local testing.

### Step 5: Deploy

The GitHub secret is automatically used during deployment:
```bash
git push origin main
```

The GitHub Actions workflow will build with your GA_MEASUREMENT_ID secret.

### What Gets Tracked

- **Artwork Views:** Which paintings get the most views
- **WhatsApp Clicks:** Both floating and inline button engagement
- **Language Switches:** User language preferences (ES ↔ EN)
- **Gallery Navigation:** Movement between Originals, Prints, About
- **Geographic Data:** Automatic country/city tracking (built into GA4)

### Viewing Analytics

1. Go to https://analytics.google.com
2. Select your property
3. View real-time data or historical reports

**Note:** GA4 is completely optional. If you don't set it up, the site works perfectly without analytics.

## 📝 Future Features

- Image optimization script for managing high-res originals
- SEO enhancements (sitemap, structured data)
- Custom domain configuration

## 📄 License

All artwork and content © Artist Name. All rights reserved.
