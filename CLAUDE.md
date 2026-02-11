# CLAUDE.md - AI Assistant Development Guide

This file provides context and guidelines for AI assistants (like Claude) working on this repository.

## Repository Purpose

**web-portfolio** is a static artist portfolio website built to showcase original artworks and prints. The site is:
- Bilingual (Spanish default, English)
- Statically generated for optimal performance
- Automatically deployed to GitHub Pages
- Designed with a classic gallery aesthetic
- Easy to manage without CMS (content via JSON files)

**Live Site:** https://rodrigallardo.github.io/web-portfolio
**Repository:** https://github.com/rodrigallardo/web-portfolio

## Project Status

**Current State:** ✅ Production-ready with all core features deployed
**Phase:** 6 of 6 completed (Core platform + WhatsApp + Google Analytics)

### Completed Features ✅
- Two artwork galleries (Originals and Prints)
- Dynamic detail pages for each artwork
- Bilingual support (ES/EN) with language switcher
- About page
- WhatsApp contact integration (floating + inline buttons)
- **Google Analytics 4 integration:**
  - Track artwork page views
  - Track WhatsApp button clicks (floating + inline)
  - Track language switches (ES ↔ EN)
  - Track gallery navigation
  - Geographic tracking (automatic)
  - Configured via GitHub secrets
- CI/CD with automatic GitHub Pages deployment
- Classic gallery design (neutral colors, clean typography)
- Responsive mobile-first design

### Known Issues ⚠️
- Test WhatsApp phone number (1234567890) needs replacement
- Sample artwork with placeholder SVG images
- Placeholder About page content

### Future Work 🔜
- Phase 5: Image optimization workflow
- SEO enhancements (sitemap, structured data)
- Custom domain configuration

## Project Structure

```
web-portfolio/
├── .github/workflows/
│   └── deploy.yml              # GitHub Actions CI/CD workflow
│
├── public/
│   ├── images/                 # Artwork images (web-optimized)
│   ├── favicon.ico
│   └── favicon.svg
│
├── src/
│   ├── components/
│   │   ├── Navigation.astro    # Nav bar + language switcher
│   │   ├── WhatsAppButton.astro # Floating contact button
│   │   └── Analytics.astro     # Google Analytics 4 tracking
│   │
│   ├── content/
│   │   ├── config.ts           # Content Collections schema
│   │   ├── originals/          # Original artwork JSON files
│   │   └── prints/             # Print artwork JSON files
│   │
│   ├── i18n/
│   │   ├── es.json             # Spanish translations
│   │   ├── en.json             # English translations
│   │   └── index.ts            # Translation utilities
│   │
│   ├── layouts/
│   │   └── Layout.astro        # Main layout wrapper
│   │
│   ├── pages/
│   │   ├── index.astro         # Originals gallery (Spanish)
│   │   ├── prints.astro        # Prints gallery (Spanish)
│   │   ├── about.astro         # About page (Spanish)
│   │   ├── originals/[id].astro # Artwork detail (Spanish)
│   │   ├── prints/[id].astro    # Print detail (Spanish)
│   │   └── en/                 # Full English mirror of all pages
│   │
│   └── styles/
│       └── global.css          # Tailwind CSS imports
│
├── .env.example                # GA4 configuration template
├── astro.config.mjs            # Astro configuration
├── package.json                # Dependencies
├── tsconfig.json               # TypeScript configuration
├── README.md                   # User documentation
├── CLAUDE.md                   # This file (AI assistant guide)
├── task_plan.md                # Planning, TODOs, priorities
├── findings.md                 # Technical documentation
└── progress.md                 # Session logs
```

**Note:** `.env` file exists locally for development but is gitignored (not in repository)

## Tech Stack

### Core Technologies
- **Framework:** Astro v5.17.1 (static site generator)
- **Language:** TypeScript (strict mode)
- **Styling:** Tailwind CSS v4.1.18 (via Vite plugin)
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions

### Key Dependencies
```json
{
  "@tailwindcss/vite": "^4.1.18",
  "astro": "^5.17.1",
  "tailwindcss": "^4.1.18"
}
```

### Development Environment
- Node.js: v20+ (currently v25.5.0)
- npm: v11+ (currently v11.8.0)
- Git: Latest version
- GitHub CLI: For deployment monitoring

### Why This Stack?
- **Astro:** Purpose-built for content sites, ships minimal JS, excellent performance
- **TypeScript:** Type safety prevents bugs, better IDE support
- **Tailwind:** Utility-first CSS, easy to use without deep CSS knowledge
- **GitHub Pages:** Free, reliable, integrates with repository
- **Content Collections:** Type-safe artwork data with schema validation

## Content Schema

Artworks are stored as JSON files in `src/content/originals/` or `src/content/prints/`:

```typescript
{
  titleEs: string;           // Artwork title (Spanish)
  titleEn: string;           // Artwork title (English)
  descriptionEs?: string;    // Detailed description (Spanish, optional)
  descriptionEn?: string;    // Detailed description (English, optional)
  price?: string;            // Display price (e.g., "$100", optional)
  year: number;              // Year created
  dimensionsCm: string;      // Size in cm (e.g., "80 x 60")
  image: string;             // Path to image (e.g., "/web-portfolio/images/artwork.jpg")
  available: boolean;        // Availability status
}
```

**Key Points:**
- Bilingual titles (titleEs/titleEn) are required
- Descriptions are optional (some artworks may not have descriptions)
- Price is optional (shows "Ask for Price" button if missing)
- Dimensions use centimeters (automatically converted to inches for English pages)
- Image paths must include the base URL prefix: `/web-portfolio/images/`

## Configuration

### Astro Config (astro.config.mjs)
```javascript
{
  site: 'https://rodrigallardo.github.io',
  base: '/web-portfolio',
  vite: {
    plugins: [tailwindcss()]
  }
}
```

**Important:**
- `site`: Full URL for canonical URLs and sitemap
- `base`: Repository name for GitHub Pages routing
- All internal links must include `/web-portfolio` prefix

### Bilingual URL Structure
- Spanish (default): `/`, `/prints`, `/about`, `/originals/[id]`
- English: `/en/`, `/en/prints`, `/en/about`, `/en/originals/[id]`

### GitHub Secrets Configuration

**Google Analytics 4 Measurement ID:**
The GA4 Measurement ID is stored as a GitHub repository secret:

**Location:** Repository Settings → Secrets and variables → Actions → `github-pages` environment
**Secret Name:** `GA_MEASUREMENT_ID`
**Secret Value:** `G-VGTBVLLR7E` (current production value)

**How It Works:**
1. GitHub Actions workflow references the `github-pages` environment in the build job
2. During build, the secret is passed as environment variable: `PUBLIC_GA_MEASUREMENT_ID`
3. Astro reads it via `import.meta.env.PUBLIC_GA_MEASUREMENT_ID`
4. Analytics.astro component uses it to initialize GA4 tracking

**Local Development:**
- Create `.env` file in project root (gitignored)
- Add: `PUBLIC_GA_MEASUREMENT_ID=G-VGTBVLLR7E`
- Restart dev server to enable analytics locally

**Why Secrets:**
- Keeps configuration out of codebase
- Can be updated without code changes
- Follows security best practices
- Automatically injected during CI/CD

**Note:** GA4 Measurement IDs are public by design (visible in client-side code), but using secrets is best practice for configuration management.

## Development Workflow Requirements

### 1. Feature Branch Workflow

**ALWAYS use feature branches for new work:**

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Examples:
git checkout -b feature/add-google-analytics
git checkout -b feature/update-about-page
git checkout -b fix/whatsapp-phone-number
```

**Branch naming convention:**
- Features: `feature/description`
- Fixes: `fix/description`
- Documentation: `docs/description`
- Use kebab-case (lowercase with hyphens)

### 2. Conventional Commits

**ALWAYS use conventional commits format:**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Code style (formatting, missing semicolons, etc.)
- `refactor:` - Code change that neither fixes a bug nor adds a feature
- `perf:` - Performance improvement
- `test:` - Adding tests
- `chore:` - Maintenance tasks

**Examples:**
```bash
git commit -m "feat: add Google Analytics integration"

git commit -m "fix: correct WhatsApp phone number in all pages"

git commit -m "docs: update README with custom domain setup"

git commit -m "feat(i18n): add Portuguese language support"
```

**For multi-line commits:**
```bash
git commit -m "feat: add image optimization workflow

- Create Sharp-based image processing script
- Add npm script for batch optimization
- Update README with usage instructions
- Add .gitignore entry for high-res originals

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

### 3. Merge to Main

**After feature is complete:**

```bash
# Ensure you're on your feature branch
git checkout feature/your-feature-name

# Commit all changes
git add .
git commit -m "feat: complete description of feature"

# Switch to main and merge
git checkout main
git merge feature/your-feature-name

# Push to trigger deployment
git push origin main
```

**Deployment happens automatically:**
- GitHub Actions builds the site
- Deploys to GitHub Pages
- Live in ~2 minutes

### 4. Monitor Builds with GitHub CLI

**ALWAYS check deployment status after pushing to main:**

```bash
# View recent workflow runs
gh run list

# Watch the latest run
gh run watch

# View specific run details
gh run view <run-id>

# View workflow logs if build fails
gh run view <run-id> --log
```

**Check build status:**
```bash
# List all runs for deploy workflow
gh run list --workflow=deploy.yml

# View latest deploy run
gh run view --workflow=deploy.yml
```

**If build fails:**
1. Check logs: `gh run view <run-id> --log`
2. Identify error in logs
3. Fix error locally
4. Test locally: `npm run build`
5. Commit fix and push
6. Monitor new build

**Common build errors:**
- TypeScript type errors (check with `npm run astro check`)
- Missing images referenced in JSON
- Invalid JSON syntax
- Broken imports

### 5. Local Development

**Before pushing changes:**

```bash
# Install dependencies
npm install

# Run dev server
npm run dev
# Visit http://localhost:4321/web-portfolio

# Type-check
npm run astro check

# Build locally to catch errors
npm run build

# Preview production build
npm run preview
```

**Testing checklist:**
- [ ] Dev server runs without errors
- [ ] All pages load correctly
- [ ] TypeScript check passes
- [ ] Build completes successfully
- [ ] Preview works as expected
- [ ] Changes look good on mobile and desktop

## Important Files to Know

### Configuration Files
- `astro.config.mjs` - Astro settings, GitHub Pages config
- `tsconfig.json` - TypeScript configuration
- `package.json` - Dependencies and scripts
- `.github/workflows/deploy.yml` - CI/CD pipeline

### Content Files
- `src/content/originals/*.json` - Original artwork data
- `src/content/prints/*.json` - Print artwork data
- `src/content/config.ts` - Content schema validation
- `public/images/` - Artwork images

### UI Components
- `src/layouts/Layout.astro` - Main layout wrapper
- `src/components/Navigation.astro` - Nav bar + language switcher
- `src/components/WhatsAppButton.astro` - Contact button
- `src/components/Analytics.astro` - Google Analytics 4 tracking

### i18n Files
- `src/i18n/es.json` - Spanish translations
- `src/i18n/en.json` - English translations
- `src/i18n/index.ts` - Translation utilities

### Documentation Files
- `README.md` - User-facing documentation (includes GA4 setup guide)
- `findings.md` - Technical documentation
- `CLAUDE.md` - This file (AI assistant guide)

**Note:** Planning files (task_plan.md, progress.md) are regenerated as needed for active work sessions

### Environment & Configuration Files
- `.env.example` - Template for local GA4 configuration
- `.env` - Local environment variables (gitignored, not in repo)
- `.github/workflows/deploy.yml` - CI/CD pipeline (includes secret injection)

## Common Tasks

### Adding New Artwork

1. Add optimized image to `public/images/`:
   ```bash
   cp /path/to/artwork.jpg public/images/
   ```

2. Create JSON file in appropriate collection:
   ```bash
   # For original
   nano src/content/originals/artwork-name.json

   # For print
   nano src/content/prints/print-name.json
   ```

3. Use the schema structure shown above

4. Commit and push:
   ```bash
   git checkout -b feature/add-new-artwork
   git add .
   git commit -m "feat: add new artwork [Title]"
   git checkout main
   git merge feature/add-new-artwork
   git push origin main
   ```

### Updating WhatsApp Phone Number

**Critical:** Phone number appears in 5 files (see Known Issues above)

```bash
git checkout -b fix/update-whatsapp-number

# Edit these files:
# - src/components/WhatsAppButton.astro (line 12)
# - src/pages/originals/[id].astro (line 20)
# - src/pages/prints/[id].astro (line 20)
# - src/pages/en/originals/[id].astro (line 19)
# - src/pages/en/prints/[id].astro (line 19)

# Replace: const phoneNumber = '1234567890';
# With: const phoneNumber = '5491234567890'; // Example

git add .
git commit -m "fix: update WhatsApp phone number to production number"
git checkout main
git merge fix/update-whatsapp-number
git push origin main
```

### Adding Translations

1. Update translation files:
   ```bash
   nano src/i18n/es.json
   nano src/i18n/en.json
   ```

2. Add new keys to both files

3. Use in components:
   ```astro
   ---
   import { useTranslations, getLangFromUrl } from '../i18n';
   const lang = getLangFromUrl(Astro.url);
   const t = useTranslations(lang);
   ---

   <p>{t('your.new.key')}</p>
   ```

### Updating About Page

```bash
git checkout -b feature/update-about-page

# Edit content:
nano src/pages/about.astro          # Spanish
nano src/pages/en/about.astro       # English

git add .
git commit -m "docs: update About page with artist bio"
git checkout main
git merge feature/update-about-page
git push origin main
```

### Current Gallery Design

**Scrollable Gallery Layout (Production):**

The gallery uses a vertical scrollable layout optimized for showcasing individual artworks.

**Features:**
- Full-screen scrollable sections (one painting per viewport)
- Responsive sizing: 50vh (mobile), 60vh (desktop)
- Minimal spacing between artworks (space-y-0)
- Centered display with hover effects
- Title, price, and availability shown below each image
- Responsive typography (text-xl mobile, text-3xl desktop)

**Design Philosophy:**
- Let artwork breathe without distractions
- Focus viewer attention on one piece at a time
- Easy scrolling through the collection
- Mobile-optimized for smaller screens

## Troubleshooting

### Build Fails

1. **Check logs:**
   ```bash
   gh run view --log
   ```

2. **Common issues:**
   - TypeScript errors: Run `npm run astro check` locally
   - Missing images: Check all image paths in JSON files
   - Invalid JSON: Validate with `npm run build`
   - Import errors: Check all import paths

3. **Fix and retry:**
   ```bash
   # Fix the issue
   npm run build  # Test locally
   git add .
   git commit -m "fix: resolve build error"
   git push origin main
   ```

### Images Not Loading

- Verify path includes `/web-portfolio/images/`
- Check file exists in `public/images/`
- Ensure correct filename in JSON

### Styles Broken

- Check Tailwind class names (v4 syntax)
- Verify `global.css` is imported in Layout
- Clear browser cache

### Deployment Not Triggering

- Ensure GitHub Pages is set to "GitHub Actions" source
- Check workflow permissions in repository settings
- Verify push was to `main` branch

## Best Practices

### Code Style
- Use TypeScript strict mode (already configured)
- Follow existing code patterns
- Keep components small and focused
- Use Tailwind utility classes (avoid custom CSS)
- Add comments for complex logic

### Content Management
- Keep JSON files clean and consistent
- Validate schema before committing
- Use descriptive artwork IDs (filename becomes URL)
- Optimize images before adding (<500KB recommended)
- Use kebab-case for filenames

### Git Practices
- Always work in feature branches
- Write clear, conventional commit messages
- Commit logical units of work
- Don't commit node_modules, dist, .astro
- Keep commits focused (one feature per branch)

### Testing
- Always test locally before pushing
- Check both Spanish and English versions
- Test on mobile and desktop layouts
- Verify WhatsApp buttons work
- Check responsive design

### Documentation
- Update README.md for user-facing changes
- Update task_plan.md for TODOs
- Update findings.md for technical changes
- Keep CLAUDE.md current

## GitHub CLI Commands Reference

```bash
# Authentication
gh auth login

# Repository
gh repo view
gh repo view --web

# Workflows
gh workflow list
gh workflow view deploy.yml
gh workflow run deploy.yml

# Runs
gh run list
gh run list --workflow=deploy.yml
gh run view
gh run view <run-id>
gh run view <run-id> --log
gh run watch

# Issues & PRs (if needed in future)
gh issue list
gh pr create
gh pr view

# Deployments
gh api repos/rodrigallardo/web-portfolio/deployments
```

## Quick Reference: URLs

- **Live Site:** https://rodrigallardo.github.io/web-portfolio
- **Repository:** https://github.com/rodrigallardo/web-portfolio
- **Actions:** https://github.com/rodrigallardo/web-portfolio/actions
- **Settings:** https://github.com/rodrigallardo/web-portfolio/settings

## Quick Reference: Commands

```bash
# Start new feature
git checkout -b feature/my-feature

# Development
npm install
npm run dev

# Testing
npm run astro check
npm run build
npm run preview

# Deploy
git checkout main
git merge feature/my-feature
git push origin main

# Monitor
gh run watch
```

## Project Philosophy

- **Simplicity:** Keep it simple, don't over-engineer
- **Performance:** Static site, minimal JS, fast loading
- **Maintainability:** Clear code, good documentation
- **Accessibility:** Semantic HTML, keyboard navigation
- **Design:** Classic gallery aesthetic, artwork is the hero
- **Content-first:** Easy to manage content without technical knowledge

## Notes for AI Assistants

- `findings.md` contains complete technical documentation
- Planning files (task_plan.md, progress.md) are created as needed for active sessions
- Follow the feature branch workflow strictly
- Use conventional commits for all changes
- Test locally before pushing to main
- Monitor deployments with GitHub CLI
- Update documentation when making changes
- Respect the bilingual structure (ES default, EN mirror)
- WhatsApp phone number is test value (1234567890) - needs replacement
- **Current Gallery Design:**
  - Scrollable full-screen layout (one painting per viewport)
  - Responsive sizing: 50vh (mobile) to 60vh (desktop)
  - Typography: Cormorant Garamond serif font throughout
  - Minimal spacing between artworks
- **Google Analytics:**
  - GA4 Measurement ID stored in GitHub secret (github-pages environment)
  - Never hardcode the Measurement ID in source code
  - Use environment variables for configuration
  - Analytics verified working in production
- **Content Schema:**
  - Use titleEs/titleEn for bilingual titles
  - Descriptions and price are optional
  - Dimensions in centimeters (dimensionsCm)
  - Image paths must include /web-portfolio/images/ prefix

## Getting Help

- **User Documentation:** README.md
- **Technical Docs:** findings.md
- **Planning & TODOs:** task_plan.md
- **Session History:** progress.md
- **Astro Docs:** https://docs.astro.build
- **Tailwind Docs:** https://tailwindcss.com/docs
- **GitHub CLI:** https://cli.github.com/manual/

---

**Last Updated:** 2026-02-10
**Project Version:** v1.2.0 (Gallery redesign + typography improvements)
**Next Phase:** Image Optimization (optional enhancement)

## Change Log

### 2026-02-10 - Session 10
**Gallery Redesign & Typography Improvements:**
- Added 3 new artworks: Valizas Reflejo, Edward Hopper Study, Terrazas Palermo
- Redesigned gallery from card grid to scrollable full-screen layout
- Implemented responsive artwork sizing (50vh mobile, 60vh desktop)
- Standardized typography to Cormorant Garamond serif font
- Improved navbar responsiveness for smaller devices
- Enhanced mobile layout with reduced spacing and appropriate text sizing
- Fixed gallery card titles to use correct bilingual properties (titleEs/titleEn)
- Commits:
  - feat: add responsive orientation-aware layout for artwork detail pages
  - refactor: move description under title without caption
  - feat: move price to metadata section with smaller button
  - fix: restore artwork titles in gallery cards
  - feat: add responsive layout improvements for mobile displays
  - refactor: reduce spacing between artworks on larger devices
  - feat: standardize typography with Cormorant Garamond serif font
  - fix: improve navbar layout for smaller devices

### 2026-02-03 - Session 9
- Explored alternative scrollable gallery layout
- Implemented vertical scroll with full aspect ratio images and card containers
- User preferred original grid layout
- Saved experimental design in feature/scrollable-gallery-layout branch
- Updated planning files and documentation
