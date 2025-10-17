/* eslint-disable */
<template>
  <q-page class="ocean-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-background">
        <div class="hero-pattern"></div>
        <div class="hero-gradient"></div>
      </div>
      <div class="hero-content">
        <div class="container">
          <div class="hero-inner">
            <div class="hero-badge">
              <q-icon name="waves" size="18px" />
              <span>AI-Powered Marine Research</span>
            </div>
            <h1 class="hero-title">
              Exploring the Ocean Floor<br/>with Artificial Intelligence
            </h1>
            <p class="hero-subtitle">
              Advanced computer vision for benthic organisms identification and marine biodiversity monitoring
            </p>
            
            <!-- Stats Pills -->
            <div class="hero-stats">
              <div class="stat-pill">
                <q-icon name="precision_manufacturing" size="20px" />
                <span>94% Accuracy</span>
              </div>
              <div class="stat-pill">
                <q-icon name="image" size="20px" />
                <span>10K+ Images</span>
              </div>
              <div class="stat-pill">
                <q-icon name="pets" size="20px" />
                <span>7 Organisms</span>
              </div>
            </div>

            <div class="hero-actions">
              <q-btn
                unelevated
                size="lg"
                color="white"
                text-color="primary"
                label="Try Our AI Model"
                icon="smart_toy"
                to="/solution"
                class="hero-btn primary-btn"
              />
              <q-btn
                outline
                size="lg"
                color="white"
                label="Play Organisms Game"
                icon="casino"
                to="/game"
                class="hero-btn secondary-btn"
              />
            </div>
          </div>
        </div>
      </div>
      
      <!-- Animated waves -->
      <div class="waves-container">
        <svg class="waves" xmlns="http://www.w3.org/2000/svg" viewBox="0 24 150 28" preserveAspectRatio="none">
          <defs>
            <path id="wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
          </defs>
          <g class="wave-parallax">
            <use href="#wave" x="48" y="0" fill="rgba(255,255,255,0.7)" />
            <use href="#wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
            <use href="#wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
            <use href="#wave" x="48" y="7" fill="#fff" />
          </g>
        </svg>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
      <div class="container">
        <div class="section-header">
          <div class="section-badge">
            <q-icon name="auto_awesome" size="16px" />
            <span>Capabilities</span>
          </div>
          <h2 class="section-title">
            Advancing Marine Research
          </h2>
          <p class="section-subtitle">
            Cutting-edge AI technology for comprehensive underwater ecosystem analysis
          </p>
        </div>

        <div class="features-grid">
          <div class="feature-card-wrapper">
            <div class="feature-card">
              <div class="feature-icon-wrapper">
                <div class="feature-icon-bg gradient-blue"></div>
                <q-icon name="image_search" size="48px" color="primary" class="feature-icon" />
              </div>
              <h3 class="feature-title">Image Classification</h3>
              <p class="feature-description">
                State-of-the-art deep learning models trained on thousands of underwater images to accurately identify benthic organisms
              </p>
              <div class="feature-metrics">
                <div class="metric-item">
                  <q-icon name="speed" size="18px" color="primary" />
                  <span>Real-time Processing</span>
                </div>
                <div class="metric-item">
                  <q-icon name="verified" size="18px" color="green" />
                  <span>High Accuracy</span>
                </div>
              </div>
            </div>
          </div>

          <div class="feature-card-wrapper">
            <div class="feature-card featured">
              <div class="featured-badge">
                <q-icon name="star" size="14px" />
                <span>Most Popular</span>
              </div>
              <div class="feature-icon-wrapper">
                <div class="feature-icon-bg gradient-teal"></div>
                <q-icon name="radar" size="48px" color="teal" class="feature-icon" />
              </div>
              <h3 class="feature-title">Object Detection</h3>
              <p class="feature-description">
                Real-time detection and localization of multiple organisms in complex underwater environments
              </p>
              <div class="feature-metrics">
                <div class="metric-item">
                  <q-icon name="layers" size="18px" color="teal" />
                  <span>Multi-object Support</span>
                </div>
                <div class="metric-item">
                  <q-icon name="map" size="18px" color="green" />
                  <span>Spatial Mapping</span>
                </div>
              </div>
            </div>
          </div>

          <div class="feature-card-wrapper">
            <div class="feature-card">
              <div class="feature-icon-wrapper">
                <div class="feature-icon-bg gradient-orange"></div>
                <q-icon name="insights" size="48px" color="deep-orange" class="feature-icon" />
              </div>
              <h3 class="feature-title">Ecosystem Monitoring</h3>
              <p class="feature-description">
                Track biodiversity patterns and support conservation efforts with automated organism distribution analysis
              </p>
              <div class="feature-metrics">
                <div class="metric-item">
                  <q-icon name="trending_up" size="18px" color="deep-orange" />
                  <span>Trend Analysis</span>
                </div>
                <div class="metric-item">
                  <q-icon name="eco" size="18px" color="green" />
                  <span>Conservation</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Interactive Game Preview -->
    <section class="game-section">
      <div class="container">
        <div class="game-content">
          <div class="game-info">
            <div class="section-badge">
              <q-icon name="casino" size="16px" />
              <span>Interactive Learning</span>
            </div>
            <h2 class="section-title">
              Test Your Marine Knowledge
            </h2>
            <p class="game-description">
              Challenge yourself to identify benthic organisms from real underwater imagery. Compete with our AI model and learn about fascinating seafloor creatures while contributing to marine science education.
            </p>

            <div class="game-features">
              <div class="game-feature-item">
                <div class="feature-check">
                  <q-icon name="check" size="20px" color="white" />
                </div>
                <div class="feature-text">
                  <div class="feature-text-title">Multiple Difficulty Levels</div>
                  <div class="feature-text-desc">From beginner to expert challenges</div>
                </div>
              </div>
              <div class="game-feature-item">
                <div class="feature-check">
                  <q-icon name="check" size="20px" color="white" />
                </div>
                <div class="feature-text">
                  <div class="feature-text-title">Real Underwater Imagery</div>
                  <div class="feature-text-desc">Authentic photos from marine research</div>
                </div>
              </div>
              <div class="game-feature-item">
                <div class="feature-check">
                  <q-icon name="check" size="20px" color="white" />
                </div>
                <div class="feature-text">
                  <div class="feature-text-title">Educational Organism Facts</div>
                  <div class="feature-text-desc">Learn about marine biodiversity</div>
                </div>
              </div>
            </div>

            <q-btn
              unelevated
              size="lg"
              color="primary"
              label="Start Playing Now"
              icon-right="play_arrow"
              to="/game"
              class="game-cta-btn"
            />
          </div>

          <div class="game-preview">
            <div class="preview-card">
              <div class="preview-window">
                <q-img
                  src="/game-preview.jpg"
                  ratio="16/9"
                  class="preview-image"
                >
                  <div class="preview-overlay">
                    <div class="preview-question">
                      <q-icon name="help_outline" size="32px" />
                      <span>Can you identify this organisms?</span>
                    </div>
                  </div>
                </q-img>
              </div>
              <div class="preview-stats">
                <div class="preview-stat">
                  <q-icon name="emoji_events" size="24px" color="amber" />
                  <div>
                    <div class="preview-stat-value">
                      <template v-if="loadingStats">
                        <q-spinner size="20px" color="amber" />
                      </template>
                      <template v-else>
                        {{ totalPlayers.toLocaleString() }}
                      </template>
                    </div>
                    <div class="preview-stat-label">Players</div>
                  </div>
                </div>
                <div class="preview-stat">
                  <q-icon name="psychology" size="24px" color="purple" />
                  <div>
                    <div class="preview-stat-value">
                      <template v-if="loadingStats">
                        <q-spinner size="20px" color="purple" />
                      </template>
                      <template v-else>
                        {{ averageScore }}%
                      </template>
                    </div>
                    <div class="preview-stat-label">Avg Score</div>
                  </div>
                </div>
                <div class="preview-stat">
                  <q-icon name="school" size="24px" color="green" />
                  <div>
                    <div class="preview-stat-value">7</div>
                    <div class="preview-stat-label">Organisms</div>
                  </div>
                </div>              
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
      <div class="container">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon-wrapper gradient-blue">
              <q-icon name="pets" size="40px" color="white" />
            </div>
            <div class="stat-content">
              <div class="stat-number">7</div>
              <div class="stat-label">Organisms Identified</div>
              <div class="stat-sublabel">Across multiple ecosystems</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon-wrapper gradient-teal">
              <q-icon name="verified" size="40px" color="white" />
            </div>
            <div class="stat-content">
              <div class="stat-number">94%</div>
              <div class="stat-label">Model Accuracy</div>
              <div class="stat-sublabel">On validation dataset</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon-wrapper gradient-orange">
              <q-icon name="photo_library" size="40px" color="white" />
            </div>
            <div class="stat-content">
              <div class="stat-number">10K+</div>
              <div class="stat-label">Training Images</div>
              <div class="stat-sublabel">High-quality annotations</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon-wrapper gradient-purple">
              <q-icon name="speed" size="40px" color="white" />
            </div>
            <div class="stat-content">
              <div class="stat-number">24/7</div>
              <div class="stat-label">Real-time Detection</div>
              <div class="stat-sublabel">Always available</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="cta-background"></div>
      <div class="container">
        <div class="cta-content">
          <div class="cta-icon-wrapper">
            <q-icon name="explore" size="64px" color="white" />
          </div>
          <h2 class="cta-title">
            Ready to Explore Marine Biodiversity?
          </h2>
          <p class="cta-description">
            Discover how our AI solution can revolutionize underwater organisms monitoring and contribute to marine conservation efforts
          </p>
          <div class="cta-buttons">
            <q-btn
              unelevated
              size="lg"
              color="white"
              text-color="primary"
              label="View Our Solution"
              icon-right="arrow_forward"
              to="/solution"
              class="cta-btn-primary"
            />
            <q-btn
              outline
              size="lg"
              color="white"
              label="Learn More"
              icon="info"
              class="cta-btn-secondary"
              to="/about"
            />
          </div>
        </div>
      </div>
    </section>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { collection, getDocs, query } from 'firebase/firestore'
import { db } from '../../firebase' // Adjust path to your Firebase config

// Stats from Firebase
const totalPlayers = ref(0)
const averageScore = ref(0)
const loadingStats = ref(true)

// Load stats from Firebase
async function loadGameStats() {
  loadingStats.value = true
  
  try {
    const q = query(collection(db, 'leaderboard'))
    const querySnapshot = await getDocs(q)
    
    // Count unique players
    const uniquePlayers = new Set<string>()
    let totalScore = 0
    let scoreCount = 0
    
    querySnapshot.forEach((doc) => {
      const data = doc.data()
      
      // Track unique player names
      if (data.playerName) {
        uniquePlayers.add(data.playerName)
      }
      
      // Calculate average accuracy across all games
      if (data.accuracy !== undefined) {
        totalScore += data.accuracy
        scoreCount++
      }
    })
    
    totalPlayers.value = uniquePlayers.size
    averageScore.value = scoreCount > 0 ? Math.round(totalScore / scoreCount) : 0
    
    console.log('Game stats loaded:', {
      totalPlayers: totalPlayers.value,
      averageScore: averageScore.value,
      totalGames: querySnapshot.size
    })
  } catch (error) {
    console.error('Error loading game stats:', error)
    // Fallback to default values
    totalPlayers.value = 0
    averageScore.value = 0
  } finally {
    loadingStats.value = false
  }
}

onMounted(() => {
  loadGameStats()
})
</script>


<style scoped lang="scss">
// DESIGN SYSTEM
$primary: #1976D2;
$teal: #00897B;
$orange: #FF6F00;
$purple: #7B1FA2;

$gradient-blue: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
$gradient-teal: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
$gradient-orange: linear-gradient(135deg, #f12711 0%, #f5af19 100%);
$gradient-purple: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
$gradient-ocean: linear-gradient(135deg, #0575E6 0%, #021B79 100%);

.ocean-page {
  background: #f8f9fa;
  overflow-x: hidden;
}

// HERO SECTION
.hero-section {
  position: relative;
  min-height: 700px;
  display: flex;
  align-items: center;
  overflow: hidden;
  
  @media (max-width: 768px) {
    min-height: 600px;
  }
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.hero-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/></pattern></defs><rect width="60" height="60" fill="url(%23grid)" /></svg>');
  opacity: 0.4;
}

.hero-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #0575E6 0%, #021B79 100%);
}

.hero-content {
  position: relative;
  z-index: 1;
  width: 100%;
  padding: 4rem 0;
}

.hero-inner {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: 0.625rem 1.5rem;
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 600;
  color: white;
  margin-bottom: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: fadeInDown 0.8s ease-out;
}

.hero-title {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 800;
  color: white;
  line-height: 1.15;
  margin: 0 0 1.5rem 0;
  letter-spacing: -0.02em;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.hero-subtitle {
  font-size: clamp(1.125rem, 2.5vw, 1.375rem);
  color: rgba(255, 255, 255, 0.95);
  max-width: 700px;
  margin: 0 auto 2.5rem;
  line-height: 1.6;
  font-weight: 400;
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
  animation: fadeInUp 0.8s ease-out 0.6s both;
}

.stat-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  padding: 0.625rem 1.25rem;
  border-radius: 50px;
  color: white;
  font-size: 0.9375rem;
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s;
  
  &:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-2px);
  }
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  animation: fadeInUp 0.8s ease-out 0.8s both;
}

.hero-btn {
  min-width: 200px;
  height: 56px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: none;
  letter-spacing: 0.02em;
  border-radius: 12px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &.primary-btn {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    
    &:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
    }
  }
  
  &.secondary-btn {
    border-width: 2px;
    
    &:hover {
      background: rgba(255, 255, 255, 0.1);
      transform: translateY(-3px);
    }
  }
}

// WAVES
.waves-container {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100px;
  overflow: hidden;
  z-index: 1;
}

.waves {
  position: relative;
  width: 100%;
  height: 100%;
  margin-bottom: -7px;
}

.wave-parallax use {
  animation: wave-move 25s cubic-bezier(.55,.5,.45,.5) infinite;
  
  &:nth-child(1) {
    animation-delay: -2s;
    animation-duration: 7s;
  }
  &:nth-child(2) {
    animation-delay: -3s;
    animation-duration: 10s;
  }
  &:nth-child(3) {
    animation-delay: -4s;
    animation-duration: 13s;
  }
  &:nth-child(4) {
    animation-delay: -5s;
    animation-duration: 20s;
  }
}

@keyframes wave-move {
  0% {
    transform: translate3d(-90px,0,0);
  }
  100% { 
    transform: translate3d(85px,0,0);
  }
}

// FEATURES SECTION
.features-section {
  padding: 6rem 0;
  background: white;
  position: relative;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.section-title {
  font-size: clamp(2rem, 4vw, 2.75rem);
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 1rem 0;
  letter-spacing: -0.02em;
}

.section-subtitle {
  font-size: 1.125rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
}

.feature-card-wrapper {
  position: relative;
}

.feature-card {
  background: white;
  border-radius: 24px;
  padding: 2.5rem 2rem;
  height: 100%;
  border: 1px solid #e0e0e0;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, transparent, #667eea, transparent);
    opacity: 0;
    transition: opacity 0.4s;
  }
  
  &:hover {
    transform: translateY(-12px);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
    border-color: transparent;
    
    &::before {
      opacity: 1;
    }
  }
  
  &.featured {
    border-color: #667eea;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.15);
    
    &::before {
      opacity: 1;
    }
  }
}

.featured-badge {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.375rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.375rem 0.875rem;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 600;
}

.feature-icon-wrapper {
  position: relative;
  width: 80px;
  height: 80px;
  margin-bottom: 1.5rem;
}

.feature-icon-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 20px;
  opacity: 0.1;
  transition: all 0.4s;
  
  .feature-card:hover & {
    opacity: 0.15;
    transform: scale(1.1) rotate(5deg);
  }
}

.feature-icon {
  position: relative;
  z-index: 1;
  margin-top: 16px;
  margin-left: 16px;
}

.feature-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 1rem 0;
}

.feature-description {
  font-size: 1rem;
  color: #666;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.feature-metrics {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.metric-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.9375rem;
  color: #555;
  font-weight: 500;
}

// GAME SECTION
.game-section {
  padding: 6rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #e3e7ed 100%);
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="rgba(0,0,0,0.03)"/></pattern></defs><rect width="100" height="100" fill="url(%23dots)" /></svg>');
    opacity: 0.6;
  }
}

.game-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  position: relative;
  z-index: 1;
  
  @media (max-width: 968px) {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}

.game-info {
  .section-title {
    text-align: left;
    margin-bottom: 1.5rem;
  }
}

.game-description {
  font-size: 1.125rem;
  color: #555;
  line-height: 1.8;
  margin-bottom: 2.5rem;
}

.game-features {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.game-feature-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.feature-check {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(17, 153, 142, 0.3);
}

.feature-text-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.25rem;
}

.feature-text-desc {
  font-size: 0.9375rem;
  color: #666;
}

.game-cta-btn {
  height: 56px;
  min-width: 220px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: none;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(25, 118, 210, 0.3);
  transition: all 0.3s;
  
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(25, 118, 210, 0.4);
  }
}

.game-preview {
  position: relative;
}

.preview-card {
  background: white;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
  transition: all 0.4s;
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.2);
  }
}

.preview-window {
  position: relative;
  overflow: hidden;
}

.preview-image {
  border-radius: 24px 24px 0 0;
}

.preview-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
  padding: 2rem;
}

.preview-question {
  display: flex;
  align-items: center;
  gap: 1rem;
  color: white;
  font-size: 1.125rem;
  font-weight: 600;
}

.preview-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  padding: 1.5rem;
}

.preview-stat {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.preview-stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1;
}

.preview-stat-label {
  font-size: 0.8125rem;
  color: #666;
  margin-top: 0.25rem;
}

// STATS SECTION
.stats-section {
  padding: 6rem 0;
  background: white;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.stat-card {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-radius: 20px;
  padding: 2rem;
  border: 1px solid #e0e0e0;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
    border-color: transparent;
  }
}

.stat-icon-wrapper {
  width: 72px;
  height: 72px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  
  &.gradient-blue {
    background: $gradient-blue;
  }
  &.gradient-teal {
    background: $gradient-teal;
  }
  &.gradient-orange {
    background: $gradient-orange;
  }
  &.gradient-purple {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
  line-height: 1;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 1.125rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 0.25rem;
}

.stat-sublabel {
  font-size: 0.875rem;
  color: #666;
}

// CTA SECTION
.cta-section {
  padding: 6rem 0;
  position: relative;
  overflow: hidden;
}

.cta-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid-cta" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/></pattern></defs><rect width="100" height="100" fill="url(%23grid-cta)" /></svg>');
    opacity: 0.5;
  }
}

.cta-content {
  position: relative;
  z-index: 1;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.cta-icon-wrapper {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 2rem;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.cta-title {
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 800;
  color: white;
  margin: 0 0 1.5rem 0;
  letter-spacing: -0.02em;
}

.cta-description {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 2.5rem;
  line-height: 1.7;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.cta-btn-primary,
.cta-btn-secondary {
  height: 56px;
  min-width: 200px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: none;
  border-radius: 12px;
  transition: all 0.3s;
}

.cta-btn-primary {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
  }
}

.cta-btn-secondary {
  border-width: 2px;
  
  &:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-3px);
  }
}

// CONTAINER
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  
  @media (max-width: 768px) {
    padding: 0 1.5rem;
  }
}

// ANIMATIONS
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
