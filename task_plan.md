# Task Plan

## Overview

Build a static artist portfolio website showcasing paintings with detail pages. The site will be hosted on GitHub Pages with CI/CD for automatic deployments. Focus on simplicity, aesthetics, and ease of content management.

**Core Features (Phase 1-3):**
- Two catalog pages: Originals and Prints
- Individual artwork detail pages (price, description, year, dimensions, medium, enlarged image)
- About page
- Bilingual support (Spanish default, English)
- Language switcher
- Classic gallery aesthetic
- Static site generation
- GitHub Pages hosting
- CI/CD pipeline

**Future Features (Phase 4+):**
- WhatsApp contact button with painting-specific templates
- Image optimization script for protecting high-res originals
- Google Analytics integration

## Phases

### Phase 1: Project Setup & Configuration
- [x] Initialize planning files
- [ ] Initialize Astro project with TypeScript
- [ ] Configure Tailwind CSS
- [ ] Set up project structure (folders, configs)
- [ ] Configure for GitHub Pages deployment
- [ ] Create .gitignore for proper file exclusion
- [ ] Initial commit of base setup

### Phase 2: CI/CD Pipeline
- [ ] Create GitHub Actions workflow
- [ ] Configure workflow to build on push to main
- [ ] Configure workflow to deploy to GitHub Pages
- [ ] Test deployment pipeline
- [ ] Document deployment process

### Phase 3: Core UI & Content Structure
- [ ] Design and implement main layout with navigation
- [ ] Implement i18n system (Spanish/English)
- [ ] Create language switcher component
- [ ] Create Originals gallery page
- [ ] Create Prints gallery page
- [ ] Create About page
- [ ] Create artwork detail page with dynamic routing
- [ ] Set up content structure (JSON schema for artworks)
- [ ] Add sample artworks for testing (originals and prints)
- [ ] Implement responsive design
- [ ] Apply classic gallery aesthetic styling

### Phase 4: WhatsApp Integration (Future)
- [ ] Create floating contact button component
- [ ] Implement WhatsApp deep linking
- [ ] Add painting-specific message templates
- [ ] Test on mobile and desktop

### Phase 5: Image Optimization (Future)
- [ ] Create image processing script
- [ ] Implement resolution downscaling
- [ ] Set up separate folder for high-res originals (gitignored)
- [ ] Document image management workflow

### Phase 6: Analytics Integration (Future)
- [ ] Add Google Analytics
- [ ] Configure tracking for painting page views
- [ ] Set up geographic tracking
- [ ] Test analytics collection

## Decisions

**Tech Stack:** Astro + TypeScript + Tailwind CSS
- Rationale: Best balance of ease-of-use, performance, and static site capabilities
- Astro is purpose-built for content sites and has excellent GitHub Pages support

**Content Format:** JSON files
- Rationale: Easy to edit, structured, type-safe with TypeScript
- Can be validated and version-controlled

**Hosting:** GitHub Pages
- Rationale: Free, reliable, integrates with repository
- Custom domain support available

**CI/CD:** GitHub Actions
- Rationale: Native integration, free for public repos, well-documented

## Open Questions

- [x] Design aesthetic: Classic gallery style
- [x] Artwork information: title, price (USD), description, year, dimensions, medium
- [x] Languages: Spanish (default) + English
- [x] Separate catalogs: Originals and Prints
- [x] Additional pages: About page
- [x] Navigation structure: Originals IS the homepage (land directly on gallery)
- [x] Design: Classic gallery aesthetic - neutral colors, clean typography, grid layout, ample whitespace
- [ ] Do you have sample paintings/images to use during development?

## Notes

- Starting with core functionality (2 catalogs + detail pages + about + i18n + deployment)
- Additional features will be added incrementally after core is stable
- User is not strong in frontend, so prioritizing simplicity and good documentation
- Planning files should be excluded from final site but kept in repo for reference
- Prints catalog will showcase available prints of original paintings
- Classic gallery aesthetic: clean, neutral, focused on the artwork
