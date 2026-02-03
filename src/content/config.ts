import { defineCollection, z } from 'astro:content';

const artworkSchema = z.object({
  title: z.string(),
  description: z.string(),
  price: z.string(),
  year: z.number(),
  dimensions: z.string(),
  medium: z.string(),
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
