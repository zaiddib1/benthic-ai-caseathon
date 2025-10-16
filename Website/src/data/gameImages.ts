// src/data/gameImages.ts

export interface SpeciesInfo {
  id: string
  name: string
  scientificName: string
  images: string[]
  facts: string
  habitat: string
  depthRange: string
  conservation: string
  difficulty: 'easy' | 'medium' | 'hard'
}

// Helper to generate image paths from public folder
const generateImages = (species: string) => {
  return Array.from({ length: 5 }, (_, i) => `/species/${species}/${species}-${i + 1}.jpg`)
}

export const speciesData: SpeciesInfo[] = [
  {
    id: 'eel',
    name: 'Eel',
    scientificName: 'Anguilliformes',
    images: generateImages('eel'),
    facts: 'Eels can swim backwards and have been known to travel over land in wet conditions to reach new water sources.',
    habitat: 'Rocky crevices and coral reefs',
    depthRange: '0-100 meters',
    conservation: 'Least Concern',
    difficulty: 'medium'
  },
  {
    id: 'scallop',
    name: 'Scallop',
    scientificName: 'Pectinidae',
    images: generateImages('scallop'),
    facts: 'Scallops have up to 200 tiny eyes along the edge of their shell and can swim by rapidly clapping their shells together.',
    habitat: 'Sandy and muddy seafloors',
    depthRange: '0-200 meters',
    conservation: 'Least Concern',
    difficulty: 'easy'
  },
  {
    id: 'crab',
    name: 'Crab',
    scientificName: 'Brachyura',
    images: generateImages('crab'),
    facts: 'Crabs can walk in all directions but mostly move sideways due to the articulation of their legs.',
    habitat: 'Rocky shores and seafloor',
    depthRange: '0-500 meters',
    conservation: 'Least Concern',
    difficulty: 'easy'
  },
  {
    id: 'flatfish',
    name: 'Flatfish',
    scientificName: 'Pleuronectiformes',
    images: generateImages('flatfish'),
    facts: 'Flatfish are born swimming upright, but as they mature, one eye migrates to join the other on one side of their body.',
    habitat: 'Sandy and muddy bottoms',
    depthRange: '0-1000 meters',
    conservation: 'Least Concern',
    difficulty: 'hard'
  },
  {
    id: 'roundfish',
    name: 'Roundfish',
    scientificName: 'Gadiformes',
    images: generateImages('roundfish'),
    facts: 'Roundfish like cod can produce millions of eggs in a single spawning season to ensure species survival.',
    habitat: 'Open water and near seafloor',
    depthRange: '50-800 meters',
    conservation: 'Vulnerable',
    difficulty: 'medium'
  },
  {
    id: 'skate',
    name: 'Skate',
    scientificName: 'Rajidae',
    images: generateImages('skate'),
    facts: 'Skates lay egg cases known as "mermaid\'s purses" that often wash up on beaches after the young hatch.',
    habitat: 'Sandy and muddy bottoms',
    depthRange: '20-3000 meters',
    conservation: 'Near Threatened',
    difficulty: 'hard'
  },
  {
    id: 'whelk',
    name: 'Whelk',
    scientificName: 'Buccinidae',
    images: generateImages('whelk'),
    facts: 'Whelks are carnivorous sea snails that use their radula to drill holes in other shellfish shells to eat the soft tissue inside.',
    habitat: 'Rocky and sandy seafloors',
    depthRange: '0-1200 meters',
    conservation: 'Least Concern',
    difficulty: 'medium'
  }
]

// Helper functions
export const getSpeciesById = (id: string): SpeciesInfo | undefined => {
  return speciesData.find(s => s.id === id)
}

export const getSpeciesByName = (name: string): SpeciesInfo | undefined => {
  return speciesData.find(s => s.name === name)
}

export const getAllSpeciesNames = (): string[] => {
  return speciesData.map(s => s.name)
}

export const getSpeciesByDifficulty = (difficulty: 'easy' | 'medium' | 'hard'): SpeciesInfo[] => {
  return speciesData.filter(s => s.difficulty === difficulty)
}