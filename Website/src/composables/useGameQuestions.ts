// src/composables/useGameQuestions.ts

import { ref, computed } from 'vue'
import { speciesData, type SpeciesInfo } from '../data/gameImages'

export interface GameQuestion {
  id: number
  imageUrl: string
  correctAnswer: string
  options: string[]
  speciesInfo: SpeciesInfo
}

export interface GameAnswer {
  questionId: number
  selectedAnswer: string
  correctAnswer: string
  isCorrect: boolean
  timeSpent: number
}

export function useGameQuestions() {
  const questions = ref<GameQuestion[]>([])
  const answers = ref<GameAnswer[]>([])
  const currentQuestionIndex = ref(0)
  const questionStartTime = ref(0)

  const currentQuestion = computed(() => {
    return questions.value[currentQuestionIndex.value] || null
  })

  const isGameComplete = computed(() => {
    return currentQuestionIndex.value >= questions.value.length
  })

  const score = computed(() => {
    return answers.value.filter(a => a.isCorrect).length * 100
  })

  const accuracy = computed(() => {
    if (answers.value.length === 0) return 0
    return Math.round((answers.value.filter(a => a.isCorrect).length / answers.value.length) * 100)
  })

  const streak = computed(() => {
    let currentStreak = 0
    let maxStreak = 0
    
    for (const answer of answers.value) {
      if (answer.isCorrect) {
        currentStreak++
        maxStreak = Math.max(maxStreak, currentStreak)
      } else {
        currentStreak = 0
      }
    }
    
    return maxStreak
  })

  function generateGameQuestions(
    numQuestions: number,
    difficulty?: 'easy' | 'medium' | 'hard',
    numOptions: number = 4
  ): void {
    const availableSpecies = difficulty
      ? speciesData.filter(s => s.difficulty === difficulty)
      : speciesData

    const generatedQuestions: GameQuestion[] = []

    for (let i = 0; i < numQuestions; i++) {
      // Pick random species
      const correctSpecies = availableSpecies[
        Math.floor(Math.random() * availableSpecies.length)
      ]

      // Pick random image from that species
      const imageUrl = correctSpecies.images[
        Math.floor(Math.random() * correctSpecies.images.length)
      ]

      // Get wrong options (excluding correct answer)
      const wrongSpecies = availableSpecies
        .filter(s => s.id !== correctSpecies.id)

      // Randomly select wrong options
      const wrongOptions = wrongSpecies
        .sort(() => Math.random() - 0.5)
        .slice(0, numOptions - 1)
        .map(s => s.name)

      // Combine and shuffle all options
      const options = [correctSpecies.name, ...wrongOptions]
        .sort(() => Math.random() - 0.5)

      generatedQuestions.push({
        id: i + 1,
        imageUrl,
        correctAnswer: correctSpecies.name,
        options,
        speciesInfo: correctSpecies
      })
    }

    questions.value = generatedQuestions
    currentQuestionIndex.value = 0
    answers.value = []
    questionStartTime.value = Date.now()
  }

  function submitAnswer(selectedAnswer: string): boolean {
    if (!currentQuestion.value) return false

    const timeSpent = Math.round((Date.now() - questionStartTime.value) / 1000)
    const isCorrect = selectedAnswer === currentQuestion.value.correctAnswer

    answers.value.push({
      questionId: currentQuestion.value.id,
      selectedAnswer,
      correctAnswer: currentQuestion.value.correctAnswer,
      isCorrect,
      timeSpent
    })

    return isCorrect
  }

  function nextQuestion(): void {
    currentQuestionIndex.value++
    questionStartTime.value = Date.now()
  }

  function resetGame(): void {
    questions.value = []
    answers.value = []
    currentQuestionIndex.value = 0
    questionStartTime.value = 0
  }

  function preloadImages(questions: GameQuestion[]): void {
    questions.forEach(q => {
      const img = new Image()
      img.src = q.imageUrl
      img.onerror = () => {
        console.error('Failed to preload image:', q.imageUrl)
      }
      img.onload = () => {
        console.log('Successfully preloaded image:', q.imageUrl)
      }
    })
  }

  return {
    questions,
    answers,
    currentQuestion,
    currentQuestionIndex,
    isGameComplete,
    score,
    accuracy,
    streak,
    generateGameQuestions,
    submitAnswer,
    nextQuestion,
    resetGame,
    preloadImages
  }
}