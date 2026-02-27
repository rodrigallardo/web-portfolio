# Task Plan: Custom Domain Setup - rodrigallardo.art

## Goal
Configure custom domain `rodrigallardo.art` for the portfolio website, replacing the GitHub Pages default URL.

## Current Phase
Complete ✅

## Phases

### Phase 1: Code Configuration
- [x] Update Astro config (site URL and base path)
- [x] Create CNAME file in public directory
- [x] Update all baseUrl variables across pages
- [x] Update favicon paths
- [x] Update image paths in JSON content files
- [x] Update Navigation component
- [x] Update LanguageDetector redirects
- [x] Update Analytics tracking
- [x] Update i18n utility
- **Status:** complete

### Phase 2: Testing & Documentation
- [x] Test build locally
- [x] Verify CNAME file in dist
- [x] Create comprehensive setup guide (CUSTOM_DOMAIN_SETUP.md)
- [x] Document GitHub configuration steps
- [x] Document Squarespace DNS configuration
- [x] Document troubleshooting procedures
- **Status:** complete

### Phase 3: Deployment
- [x] Create feature branch (feature/custom-domain-setup)
- [x] Commit all changes
- [x] Merge to main
- [x] Push to GitHub
- [x] Monitor deployment (28s total)
- **Status:** complete

### Phase 4: DNS & GitHub Configuration
- [x] User configured GitHub Pages custom domain
- [x] User configured Squarespace DNS (A records + CNAME)
- [x] DNS propagated successfully
- [x] HTTPS enabled automatically
- [x] Site live at https://rodrigallardo.art
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use apex domain (not www) | Cleaner, more professional |
| Remove /web-portfolio base path | Custom domain uses root path |
| Keep both URLs working | GitHub Pages URL still accessible for compatibility |
| Use A records + CNAME | Standard GitHub Pages DNS setup |
| Enable HTTPS | Security and SEO best practice |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| None | - | Smooth deployment |

## Key Questions
1. Which domain to use? → rodrigallardo.art (purchased from Squarespace)
2. Remove GitHub Pages URL? → No, keep both working
3. www subdomain? → Yes, redirect to apex domain
4. HTTPS? → Yes, enabled automatically

## Notes
- All 20 files updated (pages, components, content)
- CNAME file automatically deployed to GitHub Pages
- DNS propagated faster than expected
- HTTPS provisioned automatically by GitHub
- Old URL (rodrigallardo.github.io/web-portfolio) still works
- New URL (rodrigallardo.art) is primary

## Files Modified
1. astro.config.mjs - Site URL and base path
2. public/CNAME - Custom domain declaration
3. src/components/Navigation.astro - baseUrl updates
4. src/components/LanguageDetector.astro - Redirect paths
5. src/components/Analytics.astro - Tracking paths
6. src/layouts/Layout.astro - Favicon paths
7. src/i18n/index.ts - Comments update
8. src/pages/*.astro (8 files) - baseUrl variables
9. src/content/**/*.json (5 files) - Image paths

## Result
✅ **Success!** Site now live at https://rodrigallardo.art with HTTPS enabled.
