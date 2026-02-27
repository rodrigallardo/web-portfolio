# Task Plan: SEO Improvements

## Goal
Improve SEO for rodrigallardo.art to increase discoverability in search engines and social media sharing.

## Current Phase
Complete - Phases 1 & 3 ✅

## Phases

### Phase 1: Meta Tags & Open Graph
- [x] Add meta descriptions to all pages
- [x] Add Open Graph tags (og:title, og:description, og:image, og:url)
- [x] Add Twitter Card tags
- [x] Add canonical URLs
- [x] Add hreflang tags for bilingual support
- [x] Update Layout.astro to accept SEO props
- [x] Create SEO.astro component
- **Status:** complete ✅

### Phase 2: Structured Data (JSON-LD)
- [ ] Add Person/Artist schema for about page
- [ ] Add VisualArtwork schema for artwork detail pages
- [ ] Add BreadcrumbList schema for navigation
- [ ] Test with Google Rich Results Test
- **Status:** pending

### Phase 3: Sitemap & Robots.txt
- [x] Install @astrojs/sitemap integration
- [x] Configure sitemap in astro.config.mjs
- [x] Generate XML sitemap (16 pages)
- [x] Create robots.txt file
- [ ] Submit sitemap to Google Search Console (user action required)
- **Status:** complete ✅

### Phase 4: Image Optimization
- [ ] Add lazy loading to images
- [ ] Verify all images have descriptive alt text
- [ ] Consider WebP format for better compression
- **Status:** pending

### Phase 5: Testing & Verification
- [ ] Test with Google Lighthouse
- [ ] Test with Google Rich Results Test
- [ ] Verify meta tags with social media debuggers
- [ ] Check mobile-friendliness
- **Status:** pending

## SEO Priorities

| Priority | Item | Impact | Effort |
|----------|------|--------|--------|
| HIGH | Meta descriptions | High | Low |
| HIGH | Open Graph tags | High | Low |
| HIGH | Sitemap | High | Low |
| MEDIUM | Structured data | Medium | Medium |
| MEDIUM | Canonical URLs | Medium | Low |
| LOW | Image lazy loading | Low | Low |

## Key Questions
1. What should be the main description for the site? (for homepage meta description)
2. Do you have a representative image for social sharing? (og:image)
3. Should we prioritize Google, Instagram, or other platforms?

## Files to Modify
1. src/layouts/Layout.astro - Add SEO component
2. src/components/SEO.astro - New component for meta tags
3. src/components/StructuredData.astro - New component for JSON-LD
4. public/robots.txt - New file
5. astro.config.mjs - Enable sitemap integration
6. All page files - Add SEO props

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Start with meta tags | Quick wins, high impact |
| Use Astro SEO integration | Native support, less custom code |
| Structured data for artworks | Rich results in Google |

## Notes
- Custom domain already configured (https://rodrigallardo.art)
- HTTPS already enabled (good for SEO)
- Bilingual site (ES/EN) - need hreflang tags
- Google Analytics already tracking
