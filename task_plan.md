# Task Plan: WhatsApp Phone Number Integration

## Goal
Centralize WhatsApp phone number configuration and update to real Uruguay phone number (+598 098182712).

## Current Phase
Complete ✅

## Phases

### Phase 1: Configuration Centralization
- [x] Create centralized config file (src/config.ts)
- [x] Add WHATSAPP_PHONE_NUMBER constant
- [x] Add site metadata constants
- [x] Document configuration structure
- **Status:** complete

### Phase 2: Component Updates
- [x] Update WhatsAppButton component to use config
- [x] Update Spanish originals detail page
- [x] Update Spanish prints detail page
- [x] Update English originals detail page
- [x] Update English prints detail page
- [x] Remove all hardcoded phone numbers
- **Status:** complete

### Phase 3: Testing & Deployment
- [x] Test build locally
- [x] Verify WhatsApp links in built HTML
- [x] Commit changes to feature branch
- [x] Merge to main
- [x] Push and deploy
- [x] Monitor deployment (29s total)
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Centralize in config.ts | Single source of truth, easy updates |
| Format: no spaces/dashes | WhatsApp URL format requirement |
| Include country code | International format (598 for Uruguay) |
| Keep SITE_NAME and SITE_URL | Future scalability |

## Key Questions
1. Where to centralize? → src/config.ts (follows Astro conventions)
2. What format? → Country code + number, no symbols (598098182712)
3. Update all files? → Yes, remove all hardcoded instances
4. Export as constant? → Yes, for TypeScript type safety

## Files Modified
1. src/config.ts (created) - Centralized configuration
2. src/components/WhatsAppButton.astro - Floating button
3. src/pages/originals/[id].astro - Spanish originals detail
4. src/pages/prints/[id].astro - Spanish prints detail
5. src/pages/en/originals/[id].astro - English originals detail
6. src/pages/en/prints/[id].astro - English prints detail

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| None | - | Smooth implementation |

## Notes
- Phone number format: 598098182712 (Uruguay +598 098182712)
- Old test number (1234567890) removed from all 5 files
- WhatsApp URL format: https://wa.me/{number}?text={message}
- Config file allows easy future updates
- Build tested successfully
- All WhatsApp buttons now functional with real number

## Result
✅ **Success!** WhatsApp integration now uses Uruguay phone number, centralized in config file.
