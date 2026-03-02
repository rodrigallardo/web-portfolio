# SEO TODO List

## Completed ✅
- [x] Phase 1: Meta Tags & Open Graph
- [x] Phase 2: Structured Data (JSON-LD)
- [x] Phase 3: Sitemap & Robots.txt

## Pending Tasks 📋

### Phase 2: Structured Data (JSON-LD) ✅ COMPLETE
- [x] Add Person/Artist schema for about page
  - Include name, nationality, artform, image
  - Link to social media profiles
- [x] Add VisualArtwork schema for artwork detail pages
  - Include name, image, creator, date created, art medium
  - Include width, height, availability, price (if listed)
- [x] Add BreadcrumbList schema for navigation
- [ ] Test with Google Rich Results Test (user action)

**Resources:**
- Schema.org Person: https://schema.org/Person
- Schema.org VisualArtwork: https://schema.org/VisualArtwork
- Google Rich Results Test: https://search.google.com/test/rich-results

### Phase 4: Image Optimization
- [ ] Add lazy loading attribute to all images
- [ ] Consider converting images to WebP format
- [ ] Add responsive images with srcset
- [ ] Verify all images have descriptive alt text

### Phase 5: Testing & Verification
- [ ] Test with Google Lighthouse
  - Target: 90+ SEO score
  - Target: 90+ Performance score
- [ ] Test with Google Rich Results Test
- [ ] Verify meta tags with social media debuggers
  - Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
  - Twitter Card Validator: https://cards-dev.twitter.com/validator
- [ ] Check mobile-friendliness
- [ ] Submit sitemap to Google Search Console

## Additional SEO Improvements (Future)
- [ ] Add default Open Graph image (og-default.jpg)
- [ ] Add blog/news section for content marketing
- [ ] Implement image alt text translations (ES/EN)
- [ ] Add FAQ schema for common questions
- [ ] Consider adding reviews/testimonials schema
- [ ] Optimize page load speed (currently good)

## Notes
- Sitemap automatically generated at: https://rodrigallardo.art/sitemap-index.xml
- robots.txt configured to allow all crawlers
- hreflang tags implemented for ES/EN language alternates
- Canonical URLs configured for all pages
