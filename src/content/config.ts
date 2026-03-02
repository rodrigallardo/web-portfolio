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
});

const originals = defineCollection({
  type: 'data',
  schema: artworkSchema,
});

const prints = defineCollection({
  type: 'data',
  schema: artworkSchema,
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
