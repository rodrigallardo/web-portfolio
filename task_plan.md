# Task Plan

## Overview

Build a static artist portfolio website showcasing paintings with detail pages. The site will be hosted on GitHub Pages with CI/CD for automatic deployments. Focus on simplicity, aesthetics, and ease of content management.

**Status:** Core functionality complete and deployed ✅
**Live Site:** https://rodrigallardo.github.io/web-portfolio

## Completed Features

### ✅ Core Platform (Phases 1-6)
- **Two Galleries:** Originals and Prints catalogs with grid layouts
- **Detail Pages:** Individual artwork pages with enlarged images, pricing, and metadata
- **Bilingual:** Spanish (default) and English with language switcher
- **About Page:** Artist bio and contact information
- **Classic Gallery Design:** Neutral colors, serif headings, minimal UI
- **Responsive:** Mobile-first design
- **WhatsApp Integration:**
  - Floating contact button on all pages
  - Inline "Ask about this painting" button on detail pages
  - Painting-specific message templates
- **Google Analytics 4:**
  - Track artwork page views
  - Track WhatsApp button clicks (floating + inline)
  - Track language switches
  - Track gallery navigation
  - Geographic tracking (automatic)
  - Environment-based configuration
- **CI/CD:** Automatic deployment to GitHub Pages on push to main
- **Documentation:** Comprehensive README with content management guide and GA4 setup instructions

## Implementation Phases

### Phase 1: Project Setup & Configuration ✅
- [x] Initialize planning files (task_plan.md, findings.md, progress.md)
- [x] Install Node.js and npm
- [x] Initialize Astro project with TypeScript (strict mode)
- [x] Configure Tailwind CSS v4
- [x] Set up project structure (src/content, src/i18n, public/images)
- [x] Configure for GitHub Pages deployment (base: /web-portfolio)
- [x] Create .gitignore
- [x] Initial commit to feature/initial-setup branch

### Phase 2: CI/CD Pipeline ✅
- [x] Create GitHub Actions workflow (.github/workflows/deploy.yml)
- [x] Configure workflow to build on push to main
- [x] Configure workflow to deploy to GitHub Pages
- [x] Update README with deployment documentation
- [x] Merge to main and push to GitHub
- [x] Test deployment pipeline

### Phase 3: Core UI & Content Structure ✅
- [x] Create Navigation component with language switcher
- [x] Update main Layout with Google Fonts (Playfair Display + Inter)
- [x] Implement i18n system (es.json, en.json, i18n utilities)
- [x] Create Originals gallery page (index.astro)
- [x] Create Prints gallery page (prints.astro)
- [x] Create About page (about.astro)
- [x] Create dynamic artwork detail pages ([id].astro)
- [x] Set up Astro Content Collections with schema validation
- [x] Add sample artworks (3 originals, 2 prints with placeholder images)
- [x] Implement responsive grid layout
- [x] Apply classic gallery aesthetic styling
- [x] Create full English routes (/en/*)

### Phase 4: WhatsApp Integration ✅
- [x] Create WhatsAppButton component (floating green button)
- [x] Implement WhatsApp deep linking
- [x] Add bilingual message templates (general + artwork-specific)
- [x] Integrate floating button into Layout
- [x] Add inline "Ask about this painting" button to all detail pages
- [x] Style buttons to match gallery aesthetic
- [x] Deploy to production

### Phase 5: Image Optimization 🔜
- [ ] Create image processing script (resize, optimize)
- [ ] Implement resolution downscaling workflow
- [ ] Set up high-res-originals/ folder (gitignored)
- [ ] Add script to package.json
- [ ] Document image management workflow in README

### Phase 6: Google Analytics Integration ✅ COMPLETE
- [x] Set up Google Analytics 4 account
- [x] Add GA4 tracking script to Layout
- [x] Configure custom events for:
  - Artwork page views
  - WhatsApp button clicks
  - Language switches
  - Gallery navigation
- [x] Set up geographic tracking (automatic via GA4)
- [x] Test analytics collection
- [x] Document in README

## Critical TODOs

### 🔴 High Priority - Production Setup
- [ ] **Configure GitHub Pages:**
  - Go to Repository Settings → Pages
  - Set Source to "GitHub Actions"
  - Verify deployment works

- [ ] **Update WhatsApp Phone Number:**
  - Replace test number (1234567890) in 5 files:
    - `src/components/WhatsAppButton.astro` (line 12)
    - `src/pages/originals/[id].astro` (line 20)
    - `src/pages/prints/[id].astro` (line 20)
    - `src/pages/en/originals/[id].astro` (line 19)
    - `src/pages/en/prints/[id].astro` (line 19)
  - Use international format: e.g., '5491234567890' (no + or spaces)
  - Commit and push to deploy

- [ ] **Update About Page Content:**
  - Edit `src/pages/about.astro` (Spanish)
  - Edit `src/pages/en/about.astro` (English)
  - Add real artist bio, statement, contact info
  - Replace placeholder text

- [ ] **Add Real Artwork Content:**
  - Replace sample artworks in `src/content/originals/`
  - Replace sample artworks in `src/content/prints/`
  - Add optimized images to `public/images/`
  - Follow schema: title, description, price, year, dimensions, medium, image, available

### 🟡 Medium Priority - Configuration
- [ ] **Set Up Custom Domain:**
  - Purchase domain (if not already done)
  - Add CNAME file to public/ folder
  - Configure DNS settings
  - Update astro.config.mjs with new domain
  - Update README with new URL

- [ ] **Update Site Metadata:**
  - Change site title from "Artist Portfolio" to artist name
  - Add meta descriptions for SEO
  - Add Open Graph tags for social sharing
  - Add artist name to footer copyright

- [ ] **Git Configuration:**
  - Set up git user name and email:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

### 🟢 Low Priority - Enhancements
- [ ] **Test Mobile Experience:**
  - Test on iOS Safari
  - Test on Android Chrome
  - Verify WhatsApp buttons work on mobile
  - Check responsive design

- [ ] **Add More Artwork:**
  - Continue adding originals as they're completed
  - Add prints as they become available
  - Keep JSON files organized

- [ ] **Content Enhancements:**
  - Add artist photo to About page
  - Add exhibition history
  - Add awards/recognition
  - Add press mentions

- [ ] **SEO Optimization:**
  - Add sitemap.xml
  - Add robots.txt
  - Optimize image alt text
  - Add structured data (JSON-LD)

- [ ] **Performance:**
  - Optimize image loading (lazy loading)
  - Add image preloading for above-fold content
  - Minimize CSS/JS if needed

## Experimental Features

### 🧪 Scrollable Gallery Layout (feature/scrollable-gallery-layout)
**Status:** Implemented but not merged - saved in feature branch for potential future use

**Design:**
- Vertical scrollable layout instead of grid
- Paintings displayed in full aspect ratio (not cropped)
- Card-style containers with rounded corners and shadows
- Scroll snap for smooth one-painting-at-a-time navigation
- Side-by-side layout: image on left, details on right
- Scrollbar positioned at right edge of screen

**Decision:** User preferred original grid layout. Experimental design saved for potential future exploration.

**To test this design:**
```bash
git checkout feature/scrollable-gallery-layout
npm run dev
```

## Future Feature Ideas

### Potential Enhancements
- [ ] **Gallery Layout Exploration:**
  - Explore alternative layouts (masonry, carousel, etc.)
  - Consider hybrid approaches
  - User testing for preferred experience

- [ ] **Newsletter Signup:**
  - Add email collection for new artwork notifications
  - Integrate with Mailchimp or similar

- [ ] **Social Media Links:**
  - Add Instagram, Facebook links to footer
  - Add social sharing buttons

- [ ] **Search & Filter:**
  - Add search by title
  - Filter by year, medium, availability
  - Sort by price, date

- [ ] **Virtual Exhibition:**
  - Create "Current Exhibition" section
  - Highlight featured artworks

- [ ] **Artist Statement:**
  - Dedicated page for detailed artist statement
  - Link from About page

- [ ] **Press Kit:**
  - Downloadable press kit PDF
  - High-res artist photos
  - Bio in multiple formats

## Technical Decisions

**Tech Stack:** Astro v5.17 + TypeScript + Tailwind CSS v4
- **Why Astro:** Purpose-built for content sites, excellent performance, simple to use
- **Why TypeScript:** Type safety, better IDE support, catches errors early
- **Why Tailwind:** Utility-first, easy to customize, no CSS expertise needed

**Content Format:** JSON files in Astro Content Collections
- **Why JSON:** Easy to edit, structured, version-controlled
- **Why Content Collections:** Type-safe, validated, excellent DX

**Hosting:** GitHub Pages
- **Why:** Free, reliable, automatic deployment, custom domain support

**CI/CD:** GitHub Actions
- **Why:** Native integration, free for public repos, simple configuration

**Fonts:** Google Fonts
- **Headings:** Playfair Display (classic serif)
- **Body:** Inter (modern sans-serif)

**Design Philosophy:**
- Classic gallery aesthetic
- Neutral color palette (grays, whites, blacks)
- Ample whitespace
- Minimal UI elements
- Focus on the artwork

## Project Structure

```
web-portfolio/
├── .github/workflows/
│   └── deploy.yml                 # GitHub Actions CI/CD
├── public/
│   └── images/                    # Artwork images (optimized, web-ready)
├── src/
│   ├── components/
│   │   ├── Navigation.astro       # Nav bar with language switcher
│   │   └── WhatsAppButton.astro   # Floating WhatsApp contact button
│   ├── content/
│   │   ├── config.ts              # Content schema validation
│   │   ├── originals/             # Original artwork JSON files
│   │   └── prints/                # Print JSON files
│   ├── i18n/
│   │   ├── es.json                # Spanish translations
│   │   ├── en.json                # English translations
│   │   └── index.ts               # i18n utilities
│   ├── layouts/
│   │   └── Layout.astro           # Main page layout
│   ├── pages/
│   │   ├── index.astro            # Originals gallery (ES)
│   │   ├── prints.astro           # Prints gallery (ES)
│   │   ├── about.astro            # About page (ES)
│   │   ├── originals/[id].astro   # Artwork detail (ES)
│   │   ├── prints/[id].astro      # Print detail (ES)
│   │   └── en/                    # English versions
│   └── styles/
│       └── global.css             # Tailwind imports
├── astro.config.mjs               # Astro config (GitHub Pages setup)
├── package.json                   # Dependencies
├── README.md                      # Documentation
└── [planning files]               # task_plan.md, findings.md, progress.md
```

## Key Files to Edit

**For content updates:**
- `src/content/originals/*.json` - Add/edit original artworks
- `src/content/prints/*.json` - Add/edit prints
- `src/pages/about.astro` - Update artist bio (Spanish)
- `src/pages/en/about.astro` - Update artist bio (English)
- `public/images/` - Add artwork images

**For configuration:**
- `src/components/WhatsAppButton.astro` - Update phone number
- `src/pages/*/[id].astro` - Update phone number (4 files)
- `astro.config.mjs` - Update domain/base URL
- `src/layouts/Layout.astro` - Update site title, meta tags

## Notes

- All core functionality is complete and deployed
- Test phone number (1234567890) is currently in use - must be replaced
- Sample artworks with placeholder images - replace with real content
- GitHub Pages needs to be configured (one-time setup)
- Custom domain support is ready but needs DNS configuration
- Image optimization workflow is planned but not yet implemented
- Google Analytics integration is planned but not yet implemented
- Planning files are tracked in git for reference but not deployed to site
