import { defineCollection, z } from 'astro:content';

const artworkSchema = z.object({
  titleEs: z.string(),
  titleEn: z.string(),
  descriptionEs: z.string(),
  descriptionEn: z.string(),
  price: z.string().optional(),
  year: z.number(),
  dimensionsCm: z.string(), // Format: "60 x 80" (width x height in cm)
  image: z.string(),
  available: z.boolean().default(true),
  order: z.number().optional(), // Display order (lower numbers first)
  orientation: z.enum(['landscape', 'portrait']), // Artwork orientation for layout
});

// Schema for individual print sizes
const printSizeSchema = z.object({
  name: z.string(),                      // Display name: "A3", "A2", etc.
  dimensionsCm: z.string(),              // Format: "29.7 x 42" (width x height in cm)
  price: z.string(),                     // Display price: "$1000 UYU", etc.
  available: z.boolean().default(true),  // Per-size availability
});

// Print schema with optional sizes array for multi-size support
const printSchema = z.object({
  titleEs: z.string(),
  titleEn: z.string(),
  descriptionEs: z.string(),
  descriptionEn: z.string(),
  price: z.string().optional(),          // Legacy field (used if no sizes array)
  year: z.number(),
  dimensionsCm: z.string().optional(),   // Legacy field (used if no sizes array)
  image: z.string(),
  available: z.boolean().default(true),
  order: z.number().optional(),
  orientation: z.enum(['landscape', 'portrait']), // Artwork orientation for layout
  sizes: z.array(printSizeSchema).optional(), // Multi-size support
});

const studySchema = z.object({
  titleEs: z.string(),
  titleEn: z.string(),
  descriptionEs: z.string(),
  descriptionEn: z.string(),
  studyType: z.enum(['copy', 'original']), // 'copy' = not for sale, 'original' = can be for sale
  originalArtist: z.string().optional(), // For copies: "Edward Hopper", "Vincent van Gogh", etc.
  price: z.string().optional(),
  year: z.number(),
  dimensionsCm: z.string(), // Format: "60 x 80" (width x height in cm)
  image: z.string(),
  available: z.boolean().default(true),
  order: z.number().optional(), // Display order (lower numbers first)
  orientation: z.enum(['landscape', 'portrait']), // Artwork orientation for layout
});

const originals = defineCollection({
  type: 'data',
  schema: artworkSchema,
});

const prints = defineCollection({
  type: 'data',
  schema: printSchema,
});

const studies = defineCollection({
  type: 'data',
  schema: studySchema,
});

export const collections = {
  originals,
  prints,
  studies,
};
