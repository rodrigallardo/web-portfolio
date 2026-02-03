# Findings

## Research & Discoveries

### Current Repository State
- Clean repository with only initial commit
- No existing code or dependencies
- On branch: `feature/initial-setup`
- Main branch exists for future PRs

### Tech Stack Recommendation

After analyzing the requirements, here's the recommended stack:

**Framework: Astro**
- Purpose-built for static content-heavy sites
- Excellent performance (ships zero JS by default)
- Simple to learn, great documentation
- Built-in image optimization
- Perfect for GitHub Pages deployment
- Strong TypeScript support

**Styling: Tailwind CSS**
- Utility-first CSS framework
- Easy to use without deep CSS knowledge
- Highly popular and well-documented
- Responsive design made simple
- Customizable design system

**Language: TypeScript**
- Type safety helps catch errors early
- Better IDE support and autocomplete
- Industry standard for modern web development

**Content Management**
- JSON files for painting data (easy to edit)
- Organized folder structure for images
- Astro Content Collections for type-safe content

**Why this stack?**
- Astro is the most popular framework for static sites in 2024-2025
- Very beginner-friendly with minimal JavaScript knowledge needed
- Tailwind makes styling straightforward
- GitHub Pages deployment is well-documented
- Large community and ecosystem

## Codebase Structure

Proposed directory structure:
```
web-portfolio/
├── src/
│   ├── components/      # Reusable UI components
│   ├── layouts/         # Page layouts
│   ├── pages/          # Routes (index.astro, paintings/[id].astro)
│   └── content/        # Painting data (JSON/collections)
├── public/
│   └── images/         # Optimized painting images
├── scripts/            # Image optimization script (future)
├── .github/
│   └── workflows/      # GitHub Actions for CI/CD
├── astro.config.mjs    # Astro configuration
├── tailwind.config.mjs # Tailwind configuration
└── package.json        # Dependencies
```

## Dependencies & Integrations

**Core Dependencies:**
- `astro` - Static site framework
- `tailwindcss` - Styling
- `@astrojs/tailwind` - Astro + Tailwind integration

**Future Integrations:**
- Google Analytics (via Astro integration or script)
- WhatsApp contact button
- Image optimization tooling (Sharp, ImageMagick)

**Internationalization (i18n):**
- Simple JSON-based approach for translations
- URL structure: `/` (Spanish default), `/en/` (English)
- Language switcher component in navigation
- Separate content files per language or language field in content

## Constraints & Limitations

**Requirements:**
- Must be static (no server-side rendering at runtime)
- Must work with GitHub Pages
- Content must be easily editable without a CMS
- No transaction functionality needed

**Technical Constraints:**
- GitHub Pages only serves static files
- Need CI/CD to rebuild on content changes
- Images must be optimized before deployment
- High-res originals must stay private
- Must support Spanish (default) and English
- Two separate catalogs: Originals and Prints

**Design Requirements:**
- Classic gallery aesthetic
- Display: title, price (USD), description, year, dimensions, medium
- Navigation: Originals, Prints, About pages
- Language switcher (ES/EN)

## References

- [Astro Documentation](https://docs.astro.build)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [GitHub Pages with Astro](https://docs.astro.build/en/guides/deploy/github/)
- [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/)
