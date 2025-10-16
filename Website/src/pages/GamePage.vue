<template>
  <q-page class="game-page">
    <!-- Start Screen -->
    <div v-if="gameState === 'start'" class="start-screen">
      <div class="container">
        <div class="start-content">
          <div class="game-badge">
            <q-icon name="casino" size="20px" />
            <span>Interactive Challenge</span>
          </div>          
          <h1 class="game-title">Species Identification Game</h1>
          <p class="game-subtitle">
            Test your knowledge of benthic species and compete with our AI model
          </p>

          <!-- Stats Preview -->
          <div class="preview-stats">
            <div class="preview-stat-item">
              <q-icon name="pets" size="32px" color="primary" />
              <div class="stat-text">
                <div class="stat-number">7</div>
                <div class="stat-label">Species</div>
              </div>
            </div>
            <div class="preview-stat-item">
              <q-icon name="image" size="32px" color="teal" />
              <div class="stat-text">
                <div class="stat-number">35</div>
                <div class="stat-label">Images</div>
              </div>
            </div>
            <div class="preview-stat-item">
              <q-icon name="emoji_events" size="32px" color="amber" />
              <div class="stat-text">
                <div class="stat-number">100</div>
                <div class="stat-label">Points Each</div>
              </div>
            </div>
          </div>

          <!-- Settings Card -->
          <div class="settings-card">
            <h3 class="settings-title">Game Settings</h3>
            
            <div class="setting-group">
              <label class="setting-label">Difficulty Level</label>
              <q-btn-toggle
                v-model="difficulty"
                spread
                unelevated
                toggle-color="primary"
                :options="[
                  { label: 'Easy', value: 'easy', icon: 'sentiment_satisfied' },
                  { label: 'Medium', value: 'medium', icon: 'psychology' },
                  { label: 'Hard', value: 'hard', icon: 'local_fire_department' }
                ]"
                class="difficulty-toggle"
              />
              <div class="difficulty-info">
                <div v-if="difficulty === 'easy'" class="info-text">
                  <q-icon name="info" size="16px" />
                  <span>Common species with 3 choices per question</span>
                </div>
                <div v-else-if="difficulty === 'medium'" class="info-text">
                  <q-icon name="info" size="16px" />
                  <span>Mixed species with 4 choices per question</span>
                </div>
                <div v-else class="info-text">
                  <q-icon name="info" size="16px" />
                  <span>Challenging species with 5 choices per question</span>
                </div>
              </div>
            </div>

            <div class="setting-group">
              <label class="setting-label">Number of Questions</label>
              <q-btn-toggle
                v-model="numQuestions"
                spread
                unelevated
                toggle-color="primary"
                :options="[
                  { label: '5', value: 5 },
                  { label: '10', value: 10 },
                  { label: '15', value: 15 }
                ]"
              />
            </div>

            <q-btn
              unelevated
              color="primary"
              size="lg"
              label="Start Game"
              icon="play_arrow"
              @click="startGame"
              class="start-btn"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Playing Screen -->
    <div v-else-if="gameState === 'playing'" class="playing-screen">
      <div class="container">
        <!-- Progress Header -->
        <div class="progress-header">
          <div class="progress-info">
            <div class="question-counter">
              <q-icon name="help_outline" size="20px" />
              <span>Question {{ currentQuestionIndex + 1 }} / {{ questions.length }}</span>
            </div>
            <div class="score-display">
              <q-icon name="stars" size="20px" />
              <span>Score: {{ score }}</span>
            </div>
          </div>
          <q-linear-progress
            :value="(currentQuestionIndex / questions.length)"
            color="primary"
            size="8px"
            rounded
            class="progress-bar"
          />
        </div>

        <!-- Question Card -->
        <div v-if="currentQuestion && !showingFeedback" class="question-card">
          <div class="image-container">
            <img
              :src="currentQuestion.imageUrl"
              :alt="'Species identification question'"
              class="species-image"
            />
            <div class="image-label">
              <q-icon name="image_search" size="20px" />
              <span>Identify this benthic species</span>
            </div>
          </div>

          <div class="options-container">
            <h3 class="question-text">What species is this?</h3>
            <div class="options-grid" :class="`options-${numOptionsForDifficulty}`">
              <q-btn
                v-for="option in currentQuestion.options"
                :key="option"
                :label="option"
                unelevated
                color="white"
                text-color="primary"
                @click="handleAnswer(option)"
                class="option-btn"
                :class="{ 'option-selected': selectedAnswer === option }"
              >
                <q-icon name="chevron_right" size="18px" class="option-icon" />
              </q-btn>
            </div>
          </div>
        </div>

        <!-- Feedback Card -->
        <div v-else-if="showingFeedback" class="feedback-card" :class="{ 'correct': lastAnswerCorrect, 'incorrect': !lastAnswerCorrect }">
          <div class="feedback-header">
            <div v-if="lastAnswerCorrect" class="feedback-icon correct">
              <q-icon name="check_circle" size="64px" />
            </div>
            <div v-else class="feedback-icon incorrect">
              <q-icon name="cancel" size="64px" />
            </div>
            <h2 class="feedback-title">
              {{ lastAnswerCorrect ? 'Correct!' : 'Incorrect' }}
            </h2>
            <p class="feedback-subtitle" v-if="!lastAnswerCorrect">
              The correct answer was <strong>{{ currentQuestion?.correctAnswer }}</strong>
            </p>
          </div>

          <div class="species-info-card">
            <div class="species-header">
              <div>
                <h3 class="species-name">{{ currentQuestion?.speciesInfo.name }}</h3>
                <p class="species-scientific">{{ currentQuestion?.speciesInfo.scientificName }}</p>
              </div>
              <q-badge
                :color="getConservationColor(currentQuestion?.speciesInfo.conservation)"
                :label="currentQuestion?.speciesInfo.conservation"
                class="conservation-badge"
              />
            </div>

            <div class="species-details">
              <div class="detail-item">
                <q-icon name="lightbulb" size="20px" color="amber" />
                <div class="detail-content">
                  <div class="detail-label">Did you know?</div>
                  <div class="detail-text">{{ currentQuestion?.speciesInfo.facts }}</div>
                </div>
              </div>
              <div class="detail-row">
                <div class="detail-item">
                  <q-icon name="terrain" size="20px" color="blue" />
                  <div class="detail-content">
                    <div class="detail-label">Habitat</div>
                    <div class="detail-text">{{ currentQuestion?.speciesInfo.habitat }}</div>
                  </div>
                </div>
                <div class="detail-item">
                  <q-icon name="waves" size="20px" color="cyan" />
                  <div class="detail-content">
                    <div class="detail-label">Depth Range</div>
                    <div class="detail-text">{{ currentQuestion?.speciesInfo.depthRange }}</div>
                  </div>
                </div>
              </div>
            </div>

            <q-btn
              unelevated
              color="primary"
              label="Next Question"
              icon-right="arrow_forward"
              @click="goToNextQuestion"
              class="next-btn"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Results Screen -->
    <div v-else-if="gameState === 'complete'" class="results-screen">
      <div class="container">
        <div class="results-content">
          <div class="results-badge">
            <q-icon name="emoji_events" size="20px" />
            <span>Game Complete</span>
          </div>

          <h1 class="results-title">Great Job!</h1>
          <p class="results-subtitle">
            Here's how you performed
          </p>

          <!-- Score Display -->
          <div class="score-card">
            <div class="final-score">
              <div class="score-label">Final Score</div>
              <div class="score-value">{{ score }}</div>
              <div class="score-max">out of {{ questions.length * 100 }}</div>
            </div>
            <q-linear-progress
              :value="accuracy / 100"
              color="green"
              size="12px"
              rounded
            />
          </div>

          <!-- Stats Grid -->
          <div class="results-stats">
            <div class="result-stat">
              <div class="result-stat-icon">
                <q-icon name="verified" size="32px" color="green" />
              </div>
              <div class="result-stat-content">
                <div class="result-stat-value">{{ accuracy }}%</div>
                <div class="result-stat-label">Accuracy</div>
              </div>
            </div>
            <div class="result-stat">
              <div class="result-stat-icon">
                <q-icon name="local_fire_department" size="32px" color="orange" />
              </div>
              <div class="result-stat-content">
                <div class="result-stat-value">{{ bestStreak }}</div>
                <div class="result-stat-label">Best Streak</div>
              </div>
            </div>
            <div class="result-stat">
              <div class="result-stat-icon">
                <q-icon name="psychology" size="32px" color="purple" />
              </div>
              <div class="result-stat-content">
                <div class="result-stat-value">{{ correctAnswers }}</div>
                <div class="result-stat-label">Correct</div>
              </div>
            </div>
          </div>

          <!-- Achievements -->
          <div v-if="achievements.length > 0" class="achievements">
            <h3 class="achievements-title">Achievements Unlocked</h3>
            <div class="achievements-grid">
              <div v-for="achievement in achievements" :key="achievement.id" class="achievement-card">
                <q-icon :name="achievement.icon" size="32px" :color="achievement.color" />
                <div class="achievement-name">{{ achievement.name }}</div>
              </div>
            </div>
          </div>

          <!-- Review Mistakes -->
          <div v-if="incorrectAnswers.length > 0" class="mistakes-section">
            <h3 class="mistakes-title">Review Your Mistakes</h3>
            <div class="mistakes-list">
              <div v-for="mistake in incorrectAnswers" :key="mistake.questionId" class="mistake-item">
                <q-icon name="cancel" size="20px" color="red" />
                <div class="mistake-info">
                  <div class="mistake-text">
                    You answered: <strong>{{ mistake.selectedAnswer }}</strong>
                  </div>
                  <div class="mistake-correct">
                    Correct: <strong>{{ mistake.correctAnswer }}</strong>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="results-actions">
            <q-btn
              unelevated
              color="primary"
              size="lg"
              label="Play Again"
              icon="replay"
              @click="playAgain"
              class="action-btn"
            />
            <q-btn
              outline
              color="primary"
              size="lg"
              label="Back to Home"
              icon="home"
              to="/"
              class="action-btn"
            />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// ===== SPECIES DATA =====
const speciesData = [
  {
    name: 'Eel',
    scientificName: 'Anguilla anguilla',
    conservation: 'Vulnerable',
    habitat: 'Rocky crevices and muddy bottoms',
    depthRange: '0-700m',
    facts: 'Eels can travel thousands of miles to spawn in the Sargasso Sea!',
    images: [
      '/species/eel/eel-1.jpg',
      '/species/eel/eel-2.jpg',
      '/species/eel/eel-3.jpg',
      '/species/eel/eel-4.jpg',
      '/species/eel/eel-5.jpg'
    ]
  },
  {
    name: 'Scallop',
    scientificName: 'Pecten maximus',
    conservation: 'Least Concern',
    habitat: 'Sandy and gravelly seabeds',
    depthRange: '0-200m',
    facts: 'Scallops have up to 200 tiny eyes along the edge of their mantle!',
    images: [
      '/species/scallop/scallop-1.jpg',
      '/species/scallop/scallop-2.jpg',
      '/species/scallop/scallop-3.jpg',
      '/species/scallop/scallop-4.jpg',
      '/species/scallop/scallop-5.jpg'
    ]
  },
  {
    name: 'Crab',
    scientificName: 'Cancer pagurus',
    conservation: 'Least Concern',
    habitat: 'Rocky seabeds and kelp forests',
    depthRange: '0-100m',
    facts: 'Crabs walk sideways because their legs bend that way, making it more efficient!',
    images: [
      '/species/crab/crab-1.jpg',
      '/species/crab/crab-2.jpg',
      '/species/crab/crab-3.jpg',
      '/species/crab/crab-4.jpg',
      '/species/crab/crab-5.jpg'
    ]
  },
  {
    name: 'Flatfish',
    scientificName: 'Pleuronectiformes',
    conservation: 'Least Concern',
    habitat: 'Sandy and muddy bottoms',
    depthRange: '0-1000m',
    facts: 'Flatfish are born swimming upright but one eye migrates as they mature!',
    images: [
      '/species/flatfish/flatfish-1.jpg',
      '/species/flatfish/flatfish-2.jpg',
      '/species/flatfish/flatfish-3.jpg',
      '/species/flatfish/flatfish-4.jpg',
      '/species/flatfish/flatfish-5.jpg'
    ]
  },
  {
    name: 'Roundfish',
    scientificName: 'Gadus morhua',
    conservation: 'Vulnerable',
    habitat: 'Open water and near seabed',
    depthRange: '0-600m',
    facts: 'Roundfish like cod can change color to blend in with their surroundings!',
    images: [
      '/species/roundfish/roundfish-1.jpg',
      '/species/roundfish/roundfish-2.jpg',
      '/species/roundfish/roundfish-3.jpg',
      '/species/roundfish/roundfish-4.jpg',
      '/species/roundfish/roundfish-5.jpg'
    ]
  },
  {
    name: 'Skate',
    scientificName: 'Raja clavata',
    conservation: 'Near Threatened',
    habitat: 'Sandy and muddy seabeds',
    depthRange: '20-300m',
    facts: 'Skates lay eggs in protective cases called "mermaid\'s purses"!',
    images: [
      '/species/skate/skate-1.jpg',
      '/species/skate/skate-2.jpg',
      '/species/skate/skate-3.jpg',
      '/species/skate/skate-4.jpg',
      '/species/skate/skate-5.jpg'
    ]
  },
  {
    name: 'Whelk',
    scientificName: 'Buccinum undatum',
    conservation: 'Least Concern',
    habitat: 'Rocky and sandy seabeds',
    depthRange: '0-1200m',
    facts: 'Whelks can drill through the shells of other mollusks to eat them!',
    images: [
      '/species/whelk/whelk-1.jpg',
      '/species/whelk/whelk-2.jpg',
      '/species/whelk/whelk-3.jpg',
      '/species/whelk/whelk-4.jpg',
      '/species/whelk/whelk-5.jpg'
    ]
  }
]

// ===== GAME STATE =====
const gameState = ref('start')
const difficulty = ref('medium')
const numQuestions = ref(10)
const selectedAnswer = ref('')
const showingFeedback = ref(false)
const lastAnswerCorrect = ref(false)

// ===== GAME LOGIC STATE =====
const questions = ref([])
const answers = ref([])
const currentQuestionIndex = ref(0)
const currentStreak = ref(0)
const bestStreak = ref(0)

// ===== COMPUTED PROPERTIES =====
const numOptionsForDifficulty = computed(() => {
  if (difficulty.value === 'easy') return 3
  if (difficulty.value === 'medium') return 4
  return 5
})

const currentQuestion = computed(() => {
  return questions.value[currentQuestionIndex.value] || null
})

const score = computed(() => {
  return answers.value.reduce((total, answer) => {
    return total + (answer.isCorrect ? 100 : 0)
  }, 0)
})

const accuracy = computed(() => {
  if (answers.value.length === 0) return 0
  const correct = answers.value.filter(a => a.isCorrect).length
  return Math.round((correct / answers.value.length) * 100)
})

const correctAnswers = computed(() => {
  return answers.value.filter(a => a.isCorrect).length
})

const incorrectAnswers = computed(() => {
  return answers.value.filter(a => !a.isCorrect)
})

const achievements = computed(() => {
  const earned = []
  
  if (accuracy.value === 100) {
    earned.push({ id: 'perfect', name: 'Perfect Score!', icon: 'workspace_premium', color: 'amber' })
  }
  if (bestStreak.value >= 5) {
    earned.push({ id: 'streak', name: '5 Streak Master', icon: 'local_fire_department', color: 'orange' })
  }
  if (correctAnswers.value >= 10) {
    earned.push({ id: 'expert', name: 'Marine Expert', icon: 'school', color: 'blue' })
  }
  if (accuracy.value >= 80) {
    earned.push({ id: 'accurate', name: 'Sharp Eye', icon: 'visibility', color: 'green' })
  }
  
  return earned
})

// ===== UTILITY FUNCTIONS =====
function shuffleArray(array) {
  const shuffled = [...array]
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
  }
  return shuffled
}

function getRandomElements(array, count) {
  const shuffled = shuffleArray(array)
  return shuffled.slice(0, count)
}

// ===== GAME FUNCTIONS =====
function generateGameQuestions(numQuestions, excludedSpecies = [], numOptions = 4) {
  console.log('Generating questions:', { numQuestions, numOptions })
  
  const allQuestions = []
  
  // Create a pool of all possible questions
  speciesData.forEach(species => {
    if (excludedSpecies.includes(species.name)) return
    
    species.images.forEach(imagePath => {
      allQuestions.push({
        imageUrl: imagePath,
        correctAnswer: species.name,
        speciesInfo: {
          name: species.name,
          scientificName: species.scientificName,
          conservation: species.conservation,
          habitat: species.habitat,
          depthRange: species.depthRange,
          facts: species.facts
        }
      })
    })
  })
  
  // Select random questions
  const selectedQuestions = getRandomElements(allQuestions, numQuestions)
  
  // Add options to each question
  selectedQuestions.forEach(question => {
    const otherSpecies = speciesData
      .filter(s => s.name !== question.correctAnswer)
      .map(s => s.name)
    
    const wrongOptions = getRandomElements(otherSpecies, numOptions - 1)
    const allOptions = shuffleArray([question.correctAnswer, ...wrongOptions])
    
    question.options = allOptions
  })
  
  questions.value = selectedQuestions
  console.log('Generated questions:', questions.value)
}

function preloadImages(questions) {
  questions.forEach(q => {
    const img = new Image()
    img.src = q.imageUrl
  })
}

function startGame() {
  console.log('Starting game:', { difficulty: difficulty.value, numQuestions: numQuestions.value })
  
  resetGame()
  generateGameQuestions(numQuestions.value, [], numOptionsForDifficulty.value)
  preloadImages(questions.value)
  
  gameState.value = 'playing'
}

function handleAnswer(answer) {
  console.log('Answer submitted:', answer)
  
  selectedAnswer.value = answer
  const isCorrect = answer === currentQuestion.value.correctAnswer
  lastAnswerCorrect.value = isCorrect
  
  // Record answer
  answers.value.push({
    questionId: currentQuestionIndex.value,
    selectedAnswer: answer,
    correctAnswer: currentQuestion.value.correctAnswer,
    isCorrect: isCorrect
  })
  
  // Update streak
  if (isCorrect) {
    currentStreak.value++
    if (currentStreak.value > bestStreak.value) {
      bestStreak.value = currentStreak.value
    }
  } else {
    currentStreak.value = 0
  }
  
  showingFeedback.value = true
}

function goToNextQuestion() {
  showingFeedback.value = false
  selectedAnswer.value = ''
  currentQuestionIndex.value++
  
  if (currentQuestionIndex.value >= questions.value.length) {
    gameState.value = 'complete'
  }
}

function resetGame() {
  questions.value = []
  answers.value = []
  currentQuestionIndex.value = 0
  currentStreak.value = 0
  bestStreak.value = 0
  selectedAnswer.value = ''
  showingFeedback.value = false
  lastAnswerCorrect.value = false
}

function playAgain() {
  gameState.value = 'start'
  resetGame()
}

function getConservationColor(status) {
  switch (status) {
    case 'Least Concern': return 'green'
    case 'Near Threatened': return 'orange'
    case 'Vulnerable': return 'deep-orange'
    case 'Endangered': return 'red'
    default: return 'grey'
  }
}

onMounted(() => {
  console.log('Game page mounted')
  console.log('Species data loaded:', speciesData.length, 'species')
})
</script>

<style scoped lang="scss">
// DESIGN SYSTEM
$gradient-ocean: linear-gradient(135deg, #0575E6 0%, #021B79 100%);
$gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
$gradient-success: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
$gradient-error: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);

.game-page {
  min-height: 100vh;
  background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
}

.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  
  @media (max-width: 768px) {
    padding: 1rem;
  }
}

// START SCREEN
.start-screen {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 4rem 0;
}

.start-content {
  text-align: center;
}

.game-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: $gradient-primary;
  color: white;
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.game-title {
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0 1rem 0;
  letter-spacing: -0.02em;
}

.game-subtitle {
  font-size: 1.125rem;
  color: #666;
  margin-bottom: 3rem;
}

.preview-stats {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 3rem;
  flex-wrap: wrap;
}

.preview-stat-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.stat-text {
  text-align: left;
}

.stat-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  color: #666;
  margin-top: 0.25rem;
}

// SETTINGS CARD
.settings-card {
  background: white;
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 0 auto;
  
  @media (max-width: 768px) {
    padding: 1.5rem;
  }
}

.settings-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 2rem 0;
  text-align: center;
}

.setting-group {
  margin-bottom: 2rem;
}

.setting-label {
  display: block;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 1rem;
}

.difficulty-toggle {
  :deep(.q-btn) {
    padding: 0.75rem 1rem;
  }
}

.difficulty-info {
  margin-top: 0.75rem;
}

.info-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #666;
  background: #f5f7fa;
  padding: 0.75rem 1rem;
  border-radius: 10px;
}

.start-btn {
  width: 100%;
  height: 56px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 12px;
  margin-top: 1rem;
  box-shadow: 0 4px 16px rgba(25, 118, 210, 0.3);
  transition: all 0.3s;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(25, 118, 210, 0.4);
  }
}

// PLAYING SCREEN
.playing-screen {
  padding: 2rem 0;
}

.progress-header {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.progress-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.question-counter,
.score-display {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
}

.progress-bar {
  margin-top: 0.5rem;
}

// QUESTION CARD
.question-card {
  background: white;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.image-container {
  position: relative;
}

.species-image {
  width: 100%;
  height: auto;
  max-height: 500px;  // Added max-height for better control
  object-fit: contain;  // Changed from 'cover' to 'contain'
  display: block;
  background: #f5f7fa;  // Added background color for letterboxing
}

.image-label {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 0.75rem 1.25rem;
  border-radius: 50px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #333;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.options-container {
  padding: 2.5rem;
  
  @media (max-width: 768px) {
    padding: 1.5rem;
  }
}

.question-text {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 2rem 0;
  text-align: center;
}

.options-grid {
  display: grid;
  gap: 1rem;
  
  &.options-3 {
    grid-template-columns: 1fr;
  }
  
  &.options-4 {
    grid-template-columns: repeat(2, 1fr);
    
    @media (max-width: 599px) {
      grid-template-columns: 1fr;
    }
  }
  
  &.options-5 {
    grid-template-columns: repeat(2, 1fr);
    
    @media (max-width: 599px) {
      grid-template-columns: 1fr;
    }
  }
}

.option-btn {
  height: 64px;
  font-size: 1.125rem;
  font-weight: 600;
  border-radius: 12px;
  border: 2px solid #e0e0e0;
  text-transform: none;
  position: relative;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &:hover {
    border-color: #667eea;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.2);
  }
  
  .option-icon {
    position: absolute;
    right: 1rem;
    opacity: 0;
    transition: all 0.3s;
  }
  
  &:hover .option-icon {
    opacity: 1;
    transform: translateX(4px);
  }
}

// FEEDBACK CARD
.feedback-card {
  background: white;
  border-radius: 24px;
  padding: 3rem 2.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  
  @media (max-width: 768px) {
    padding: 2rem 1.5rem;
  }
  
  &.correct {
    border-top: 4px solid #4CAF50;
  }
  
  &.incorrect {
    border-top: 4px solid #F44336;
  }
}

.feedback-header {
  text-align: center;
  margin-bottom: 2rem;
}

.feedback-icon {
  margin-bottom: 1rem;
  
  &.correct {
    color: #4CAF50;
  }
  
  &.incorrect {
    color: #F44336;
  }
}

.feedback-title {
  font-size: 2rem;
  font-weight: 800;
  margin: 0 0 0.5rem 0;
}

.feedback-subtitle {
  font-size: 1.125rem;
  color: #666;
}

.species-info-card {
  background: linear-gradient(135deg, #f5f7fa 0%, #e3e7ed 100%);
  border-radius: 16px;
  padding: 2rem;
  
  @media (max-width: 768px) {
    padding: 1.5rem;
  }
}

.species-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  gap: 1rem;
}

.species-name {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 0.25rem 0;
}

.species-scientific {
  font-size: 1rem;
  font-style: italic;
  color: #666;
}

.conservation-badge {
  font-size: 0.875rem;
  padding: 0.5rem 1rem;
  font-weight: 600;
}

.species-details {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.detail-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  
  @media (max-width: 599px) {
    grid-template-columns: 1fr;
  }
}

.detail-item {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}

.detail-content {
  flex: 1;
}

.detail-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #666;
  margin-bottom: 0.25rem;
}

.detail-text {
  font-size: 0.9375rem;
  color: #333;
  line-height: 1.6;
}

.next-btn {
  width: 100%;
  height: 56px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(25, 118, 210, 0.3);
  transition: all 0.3s;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(25, 118, 210, 0.4);
  }
}

// RESULTS SCREEN
.results-screen {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 4rem 0;
}

.results-content {
  text-align: center;
}

.results-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: $gradient-success;
  color: white;
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.results-title {
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0 1rem 0;
}

.results-subtitle {
  font-size: 1.125rem;
  color: #666;
  margin-bottom: 3rem;
}

// SCORE CARD
.score-card {
  background: white;
  border-radius: 24px;
  padding: 3rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  
  @media (max-width: 768px) {
    padding: 2rem;
  }
}

.final-score {
  margin-bottom: 1.5rem;
}

.score-label {
  font-size: 1rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.score-value {
  font-size: 4rem;
  font-weight: 800;
  background: $gradient-primary;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  margin-bottom: 0.5rem;
  
  @media (max-width: 768px) {
    font-size: 3rem;
  }
}

.score-max {
  font-size: 1.125rem;
  color: #666;
}

.results-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 3rem;
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
}

.result-stat {
  background: white;
  border-radius: 16px;
  padding: 2rem 1.5rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.result-stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1;
}

.result-stat-label {
  font-size: 0.9375rem;
  color: #666;
}

// ACHIEVEMENTS
.achievements {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.achievements-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 1.5rem 0;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.achievement-card {
  background: linear-gradient(135deg, #f5f7fa 0%, #e3e7ed 100%);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
}

.achievement-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: #333;
  margin-top: 0.75rem;
}

// MISTAKES
.mistakes-section {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  text-align: left;
}

.mistakes-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 1.5rem 0;
}

.mistakes-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.mistake-item {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: #fff5f5;
  border-radius: 10px;
}

.mistake-info {
  flex: 1;
}

.mistake-text {
  font-size: 0.9375rem;
  color: #333;
  margin-bottom: 0.25rem;
}

.mistake-correct {
  font-size: 0.875rem;
  color: #4CAF50;
}

// ACTIONS
.results-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.action-btn {
  min-width: 200px;
  height: 56px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 12px;
  
  &:first-child {
    box-shadow: 0 4px 16px rgba(25, 118, 210, 0.3);
    
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(25, 118, 210, 0.4);
    }
  }
}
</style>
