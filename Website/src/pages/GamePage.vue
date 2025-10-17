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
            Test your knowledge of benthic species and compete on the leaderboard
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
              <q-icon name="timer" size="32px" color="deep-orange" />
              <div class="stat-text">
                <div class="stat-number">30s</div>
                <div class="stat-label">Per Question</div>
              </div>
            </div>
          </div>

          <!-- Settings Card -->
          <div class="settings-card">
            <h3 class="settings-title">Game Settings</h3>
            
            <div class="setting-group">
              <label class="setting-label">Player Name (for leaderboard)</label>
              <q-input
                v-model="playerName"
                outlined
                placeholder="Enter your name"
                maxlength="20"
                class="player-name-input"
              >
                <template v-slot:prepend>
                  <q-icon name="person" />
                </template>
              </q-input>
            </div>

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
                  <span>Common species with 3 choices • 1x multiplier</span>
                </div>
                <div v-else-if="difficulty === 'medium'" class="info-text">
                  <q-icon name="info" size="16px" />
                  <span>Mixed species with 4 choices • 1.5x multiplier</span>
                </div>
                <div v-else class="info-text">
                  <q-icon name="info" size="16px" />
                  <span>Challenging species with 5 choices • 2x multiplier</span>
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
              :disable="!playerName.trim()"
              class="start-btn"
            />
          </div>

          <!-- Leaderboard Preview -->
          <div class="leaderboard-preview">
            <h3 class="leaderboard-title">
              <q-icon name="leaderboard" size="24px" />
              Top Players
            </h3>
            <q-tabs
              v-model="leaderboardTab"
              dense
              class="leaderboard-tabs"
              active-color="primary"
              indicator-color="primary"
            >
              <q-tab name="easy-5" label="Easy • 5Q" />
              <q-tab name="medium-10" label="Medium • 10Q" />
              <q-tab name="hard-15" label="Hard • 15Q" />
            </q-tabs>
            <div class="leaderboard-content">
              <div v-if="loadingLeaderboard" class="loading-state">
                <q-spinner color="primary" size="32px" />
              </div>
              <div v-else-if="topPlayers.length === 0" class="empty-state">
                <q-icon name="emoji_events" size="48px" color="grey-4" />
                <p>No scores yet. Be the first!</p>
              </div>
              <div v-else class="leaderboard-list">
                <div
                  v-for="(player, index) in topPlayers.slice(0, 5)"
                  :key="player.id"
                  class="leaderboard-item"
                >
                  <div class="rank" :class="`rank-${index + 1}`">
                    <q-icon v-if="index === 0" name="workspace_premium" size="24px" color="yellow-5" />
                    <q-icon v-else-if="index === 1" name="military_tech" size="24px" color="grey-2" />
                    <q-icon v-else-if="index === 2" name="military_tech" size="24px" color="orange" />
                    <span v-else>{{ index + 1 }}</span>
                  </div>
                  <div class="player-info">
                    <div class="player-name">{{ player.playerName }}</div>
                    <div class="player-stats">
                      {{ player.accuracy }}% • {{ formatTime(player.totalTime) }}
                    </div>
                  </div>
                  <div class="player-score">{{ player.totalScore }}</div>
                </div>
              </div>
            </div>
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
            <div class="timer-display" :class="{ 'timer-warning': questionTimeLeft <= 10 }">
              <q-icon name="timer" size="20px" />
              <span>{{ questionTimeLeft }}s</span>
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
            <!-- Timer Progress Ring -->
            <div class="timer-ring">
              <q-circular-progress
                :value="(questionTimeLeft / QUESTION_TIME_LIMIT) * 100"
                size="60px"
                :thickness="0.15"
                color="primary"
                track-color="grey-3"
                class="timer-progress"
              >
                <div class="timer-text">{{ questionTimeLeft }}</div>
              </q-circular-progress>
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
                :disable="questionTimeLeft === 0"
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
            <div v-if="lastAnswerCorrect" class="points-earned">
              <q-icon name="add_circle" size="24px" color="green" />
              <span>+{{ lastPointsEarned }} points</span>
              <q-badge v-if="lastTimeBonus > 0" color="orange" class="time-bonus-badge">
                +{{ lastTimeBonus }} speed bonus!
              </q-badge>
            </div>
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

          <h1 class="results-title">Great Job, {{ playerName }}!</h1>
          <p class="results-subtitle">
            Here's how you performed
          </p>

          <!-- Score Display -->
          <div class="score-card">
            <div class="final-score">
              <div class="score-label">Final Score</div>
              <div class="score-value">{{ score }}</div>
              <div class="score-breakdown">
                <div class="breakdown-item">
                  <q-icon name="check_circle" size="16px" color="green" />
                  <span>{{ correctAnswers * 100 }} base points</span>
                </div>
                <div class="breakdown-item">
                  <q-icon name="speed" size="16px" color="orange" />
                  <span>{{ totalSpeedBonus }} speed bonus</span>
                </div>
                <div class="breakdown-item">
                  <q-icon name="local_fire_department" size="16px" color="red" />
                  <span>×{{ difficultyMultiplier }} difficulty multiplier</span>
                </div>
              </div>
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
                <q-icon name="timer" size="32px" color="blue" />
              </div>
              <div class="result-stat-content">
                <div class="result-stat-value">{{ formatTime(totalGameTime) }}</div>
                <div class="result-stat-label">Total Time</div>
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
          </div>

          <!-- Leaderboard Position -->
          <div v-if="leaderboardPosition !== null" class="leaderboard-position-card">
            <q-icon name="leaderboard" size="48px" color="primary" />
            <h3>You ranked #{{ leaderboardPosition }} on the leaderboard!</h3>
            <p>{{ difficulty.toUpperCase() }} • {{ numQuestions }} Questions</p>
          </div>

          <!-- Save to Leaderboard -->
          <div v-if="!scoreSaved" class="save-score-card">
            <q-spinner v-if="savingScore" color="primary" size="32px" />
            <div v-else>
              <q-icon name="cloud_upload" size="48px" color="primary" />
              <p>Saving your score to the leaderboard...</p>
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
              label="View Full Leaderboard"
              icon="leaderboard"
              @click="gameState = 'leaderboard'"
              class="action-btn"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Full Leaderboard Screen -->
    <div v-else-if="gameState === 'leaderboard'" class="leaderboard-screen">
      <div class="container">
        <div class="leaderboard-full">
          <div class="leaderboard-header">
            <h1 class="leaderboard-title-main">
              <q-icon name="emoji_events" size="48px" />
              Leaderboard
            </h1>
            <q-btn
              flat
              round
              icon="close"
              @click="gameState = 'start'"
              class="close-btn"
            />
          </div>

          <q-tabs
            v-model="leaderboardTab"
            dense
            class="leaderboard-tabs-full"
            active-color="primary"
            indicator-color="primary"
            align="center"
          >
            <q-tab name="easy-5" label="Easy • 5Q" />
            <q-tab name="easy-10" label="Easy • 10Q" />
            <q-tab name="easy-15" label="Easy • 15Q" />
            <q-tab name="medium-5" label="Medium • 5Q" />
            <q-tab name="medium-10" label="Medium • 10Q" />
            <q-tab name="medium-15" label="Medium • 15Q" />
            <q-tab name="hard-5" label="Hard • 5Q" />
            <q-tab name="hard-10" label="Hard • 10Q" />
            <q-tab name="hard-15" label="Hard • 15Q" />
          </q-tabs>

          <div class="leaderboard-content-full">
            <div v-if="loadingLeaderboard" class="loading-state">
              <q-spinner color="primary" size="48px" />
              <p>Loading leaderboard...</p>
            </div>
            <div v-else-if="topPlayers.length === 0" class="empty-state">
              <q-icon name="emoji_events" size="64px" color="grey-4" />
              <p>No scores yet for this category. Be the first!</p>
            </div>
            <div v-else class="leaderboard-table">
              <div
                v-for="(player, index) in topPlayers"
                :key="player.id"
                class="leaderboard-row"
                :class="{ 'highlighted': player.playerName === playerName && player.timestamp > Date.now() - 60000 }"
              >
                <div class="rank-cell" :class="`rank-${index + 1}`">
                  <q-icon v-if="index === 0" name="workspace_premium" size="32px" color="amber" />
                  <q-icon v-else-if="index === 1" name="military_tech" size="32px" color="grey-6" />
                  <q-icon v-else-if="index === 2" name="military_tech" size="32px" color="orange" />
                  <span v-else class="rank-number">{{ index + 1 }}</span>
                </div>
                <div class="player-cell">
                  <div class="player-name-full">{{ player.playerName }}</div>
                  <div class="player-date">{{ formatDate(player.timestamp) }}</div>
                </div>
                <div class="stats-cell">
                  <q-chip dense color="green" text-color="white" icon="check_circle">
                    {{ player.accuracy }}%
                  </q-chip>
                  <q-chip dense color="blue" text-color="white" icon="timer">
                    {{ formatTime(player.totalTime) }}
                  </q-chip>
                  <q-chip dense color="orange" text-color="white" icon="local_fire_department">
                    {{ player.bestStreak }} streak
                  </q-chip>
                </div>
                <div class="score-cell">{{ player.totalScore }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { collection, addDoc, query, orderBy, limit, getDocs, where } from 'firebase/firestore'
import { db } from '../../firebase'


// ===== CONSTANTS =====
const QUESTION_TIME_LIMIT = 30 // seconds per question
const SPEED_BONUS_THRESHOLD = 15 // bonus points if answered within this time
const BASE_POINTS = 100


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
const playerName = ref('')
const selectedAnswer = ref('')
const showingFeedback = ref(false)
const lastAnswerCorrect = ref(false)
const lastPointsEarned = ref(0)
const lastTimeBonus = ref(0)


// ===== TIMER STATE =====
const questionTimeLeft = ref(QUESTION_TIME_LIMIT)
const questionStartTime = ref(0)
const totalGameTime = ref(0)
let timerInterval = null


// ===== GAME LOGIC STATE =====
const questions = ref([])
const answers = ref([])
const currentQuestionIndex = ref(0)
const currentStreak = ref(0)
const bestStreak = ref(0)



// ===== LEADERBOARD STATE =====
const leaderboardTab = ref('medium-10')
const topPlayers = ref([])
const loadingLeaderboard = ref(false)
const scoreSaved = ref(false)
const savingScore = ref(false)
const leaderboardPosition = ref(null)


// ===== COMPUTED PROPERTIES =====
const numOptionsForDifficulty = computed(() => {
  if (difficulty.value === 'easy') return 3
  if (difficulty.value === 'medium') return 4
  return 5
})


const difficultyMultiplier = computed(() => {
  if (difficulty.value === 'easy') return 1
  if (difficulty.value === 'medium') return 1.5
  return 2
})


const currentQuestion = computed(() => {
  return questions.value[currentQuestionIndex.value] || null
})


const score = computed(() => {
  return Math.round(answers.value.reduce((total, answer) => {
    return total + (answer.pointsEarned || 0)
  }, 0) * difficultyMultiplier.value)
})


const totalSpeedBonus = computed(() => {
  return answers.value.reduce((total, answer) => {
    return total + (answer.speedBonus || 0)
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
  if (totalSpeedBonus.value >= 200) {
    earned.push({ id: 'speedy', name: 'Speed Demon', icon: 'speed', color: 'red' })
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


function formatTime(seconds) {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins}:${secs.toString().padStart(2, '0')}`
}


function formatDate(timestamp) {
  const date = new Date(timestamp)
  const now = new Date()
  const diffMs = now.getTime() - date.getTime()
  const diffMins = Math.floor(diffMs / 60000)
  
  if (diffMins < 1) return 'Just now'
  if (diffMins < 60) return `${diffMins}m ago`
  if (diffMins < 1440) return `${Math.floor(diffMins / 60)}h ago`
  return date.toLocaleDateString()
}


// ===== TIMER FUNCTIONS =====
function startQuestionTimer() {
  questionTimeLeft.value = QUESTION_TIME_LIMIT
  questionStartTime.value = Date.now()
  
  if (timerInterval) {
    clearInterval(timerInterval)
  }
  
  timerInterval = window.setInterval(() => {
    questionTimeLeft.value--
    
    if (questionTimeLeft.value <= 0) {
      if (timerInterval) {
        clearInterval(timerInterval)
      }
      handleTimeout()
    }
  }, 1000)
}


function stopQuestionTimer() {
  if (timerInterval) {
    clearInterval(timerInterval)
    timerInterval = null
  }
}


function handleTimeout() {
  console.log('Time ran out!')
  handleAnswer('') // Empty answer = timeout
}


// ===== GAME FUNCTIONS =====
function generateGameQuestions(numQuestions, excludedSpecies = [], numOptions = 4) {
  console.log('Generating questions:', { numQuestions, numOptions })
  
  const allQuestions = []
  
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
  
  const selectedQuestions = getRandomElements(allQuestions, numQuestions)
  
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
  if (!playerName.value.trim()) return
  
  console.log('Starting game:', { difficulty: difficulty.value, numQuestions: numQuestions.value, player: playerName.value })
  
  resetGame()
  generateGameQuestions(numQuestions.value, [], numOptionsForDifficulty.value)
  preloadImages(questions.value)
  
  gameState.value = 'playing'
  totalGameTime.value = 0
  startQuestionTimer()
}


function handleAnswer(answer) {
  console.log('Answer submitted:', answer)
  
  stopQuestionTimer()
  
  const timeSpent = QUESTION_TIME_LIMIT - questionTimeLeft.value
  totalGameTime.value += timeSpent
  
  selectedAnswer.value = answer
  const isCorrect = answer === currentQuestion.value.correctAnswer
  lastAnswerCorrect.value = isCorrect
  
  // Calculate points
  let pointsEarned = 0
  let speedBonus = 0
  
  if (isCorrect) {
    pointsEarned = BASE_POINTS
    
    // Speed bonus calculation
    if (questionTimeLeft.value >= SPEED_BONUS_THRESHOLD) {
      speedBonus = Math.round((questionTimeLeft.value / QUESTION_TIME_LIMIT) * 50)
      pointsEarned += speedBonus
    }
  }
  
  lastPointsEarned.value = Math.round(pointsEarned * difficultyMultiplier.value)
  lastTimeBonus.value = speedBonus
  
  // Record answer
  answers.value.push({
    questionId: currentQuestionIndex.value,
    selectedAnswer: answer,
    correctAnswer: currentQuestion.value.correctAnswer,
    isCorrect: isCorrect,
    timeSpent: timeSpent,
    pointsEarned: pointsEarned,
    speedBonus: speedBonus
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
    stopQuestionTimer()
    gameState.value = 'complete'
    saveScoreToLeaderboard()
  } else {
    startQuestionTimer()
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
  lastPointsEarned.value = 0
  lastTimeBonus.value = 0
  totalGameTime.value = 0
  scoreSaved.value = false
  leaderboardPosition.value = null
  stopQuestionTimer()
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


// ===== LEADERBOARD FUNCTIONS =====
async function loadLeaderboard(category) {
  loadingLeaderboard.value = true
  
  try {
    const [diff, numQ] = category.split('-')
    
    const q = query(
      collection(db, 'leaderboard'),
      where('difficulty', '==', diff),
      where('numQuestions', '==', parseInt(numQ)),
      orderBy('totalScore', 'desc'),
      limit(100)
    )
    
    const querySnapshot = await getDocs(q)
    const players = []
    
    querySnapshot.forEach((doc) => {
      players.push({
        id: doc.id,
        ...doc.data()
      })
    })
    
    topPlayers.value = players
    console.log('Loaded leaderboard:', players.length, 'entries')
  } catch (error) {
    console.error('Error loading leaderboard:', error)
  } finally {
    loadingLeaderboard.value = false
  }
}


async function saveScoreToLeaderboard() {
  savingScore.value = true
  
  try {
    const scoreData = {
      playerName: playerName.value.trim(),
      difficulty: difficulty.value,
      numQuestions: numQuestions.value,
      totalScore: score.value,
      accuracy: accuracy.value,
      correctAnswers: correctAnswers.value,
      totalTime: totalGameTime.value,
      bestStreak: bestStreak.value,
      timestamp: Date.now()
    }
    
    await addDoc(collection(db, 'leaderboard'), scoreData)
    
    console.log('Score saved to leaderboard:', scoreData)
    scoreSaved.value = true
    
    // Reload leaderboard to get updated position
    await loadLeaderboard(`${difficulty.value}-${numQuestions.value}`)
    
    // Find player's position
    const position = topPlayers.value.findIndex(p => 
      p.playerName === playerName.value && 
      Math.abs(p.timestamp - scoreData.timestamp) < 5000
    )
    
    if (position !== -1) {
      leaderboardPosition.value = position + 1
    }
  } catch (error) {
    console.error('Error saving score:', error)
  } finally {
    savingScore.value = false
  }
}


// ===== WATCHERS =====
watch(leaderboardTab, (newTab) => {
  loadLeaderboard(newTab)
})


// ===== LIFECYCLE =====
onMounted(() => {
  console.log('Game page mounted')
  console.log('Species data loaded:', speciesData.length, 'species')
  
  // Load default leaderboard
  loadLeaderboard(leaderboardTab.value)
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
  min-height: 100vh;
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
  max-height: 500px;
  object-fit: contain;
  display: block;
  background: #f5f7fa;
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

// TIMER AND LEADERBOARD STYLES
.timer-display {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  padding: 0.5rem 1rem;
  background: white;
  border-radius: 8px;
  border: 2px solid #e0e0e0;
  transition: all 0.3s;
  
  &.timer-warning {
    border-color: #f44336;
    background: #ffebee;
    color: #d32f2f;
    animation: pulse 0.5s ease-in-out infinite alternate;
  }
}

@keyframes pulse {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(1.05);
  }
}

.timer-ring {
  position: absolute;
  bottom: 1.5rem;
  left: 1.5rem;
  background: white;
  border-radius: 50%;
  padding: 0.5rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.timer-text {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1a1a1a;
}

.player-name-input {
  :deep(.q-field__control) {
    height: 56px;
  }
}

.points-earned {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  justify-content: center;
  font-size: 1.25rem;
  font-weight: 700;
  color: #4CAF50;
  margin-top: 1rem;
}

.time-bonus-badge {
  font-size: 0.875rem;
  padding: 0.5rem 1rem;
}

.score-breakdown {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
}

.breakdown-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9375rem;
  color: #666;
}

.leaderboard-preview {
  background: white;
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  margin-top: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.leaderboard-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1.5rem;
}

.leaderboard-tabs {
  margin-bottom: 1.5rem;
}

.leaderboard-content {
  min-height: 200px;
}

.loading-state,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 3rem 1rem;
  color: #999;
}

.leaderboard-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.leaderboard-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-radius: 12px;
  transition: all 0.3s;
  
  &:hover {
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }
}

.rank {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.125rem;
  flex-shrink: 0;
  
  &.rank-1 {
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
  }
  
  &.rank-2 {
    background: linear-gradient(135deg, #C0C0C0 0%, #808080 100%);
  }
  
  &.rank-3 {
    background: linear-gradient(135deg, #CD7F32 0%, #8B4513 100%);
  }
}

.player-info {
  flex: 1;
}

.player-name {
  font-size: 1rem;
  font-weight: 600;
  color: #1a1a1a;
}

.player-stats {
  font-size: 0.875rem;
  color: #666;
  margin-top: 0.25rem;
}

.player-score {
  font-size: 1.25rem;
  font-weight: 700;
  color: #667eea;
}

.leaderboard-position-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  margin-bottom: 2rem;
  
  h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 1rem 0 0.5rem 0;
  }
  
  p {
    opacity: 0.9;
    font-size: 1rem;
    margin: 0;
  }
}

.save-score-card {
  background: #f5f7fa;
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  margin-bottom: 2rem;
  
  p {
    margin-top: 1rem;
    color: #666;
  }
}

// FULL LEADERBOARD SCREEN
.leaderboard-screen {
  min-height: 100vh;
  padding: 2rem 0;
}

.leaderboard-full {
  background: white;
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.leaderboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.leaderboard-title-main {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-size: 2rem;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
}

.close-btn {
  color: #666;
}

.leaderboard-tabs-full {
  margin-bottom: 2rem;
}

.leaderboard-content-full {
  min-height: 400px;
}

.leaderboard-table {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.leaderboard-row {
  display: grid;
  grid-template-columns: 60px 1fr auto 100px;
  gap: 1rem;
  align-items: center;
  padding: 1rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-radius: 12px;
  border: 2px solid transparent;
  transition: all 0.3s;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }
  
  &.highlighted {
    border-color: #667eea;
    background: linear-gradient(135deg, #e8eaf6 0%, #f3e5f5 100%);
  }
  
  @media (max-width: 768px) {
    grid-template-columns: 50px 1fr 80px;
    
    .stats-cell {
      display: none;
    }
  }
}

.rank-cell {
  display: flex;
  align-items: center;
  justify-content: center;
}

.rank-number {
  font-size: 1.25rem;
  font-weight: 700;
  color: #666;
}

.player-cell {
  flex: 1;
}

.player-name-full {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1a1a1a;
}

.player-date {
  font-size: 0.875rem;
  color: #999;
  margin-top: 0.25rem;
}

.stats-cell {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.score-cell {
  font-size: 1.5rem;
  font-weight: 800;
  color: #667eea;
  text-align: right;
}
</style>

