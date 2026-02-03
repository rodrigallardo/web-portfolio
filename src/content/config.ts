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
});

const originals = defineCollection({
  type: 'data',
  schema: artworkSchema,
});

const prints = defineCollection({
  type: 'data',
  schema: artworkSchema,
});

export const collections = {
  originals,
  prints,
};
