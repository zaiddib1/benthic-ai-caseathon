<template>
    <q-page class="ocean-page">
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-overlay">
          <div class="container">
            <div class="text-center q-pa-xl">
              <h1 class="hero-title text-white q-mb-md">
                Exploring the Ocean Floor with AI
              </h1>
              <p class="hero-subtitle text-white q-mb-xl">
                Advanced computer vision for benthic species identification and marine biodiversity monitoring
              </p>
              <div class="q-gutter-md row justify-center">
                <q-btn
                  unelevated
                  size="lg"
                  color="light-blue-7"
                  label="Try Our AI Model"
                  icon="smart_toy"
                  to="/solution"
                  class="cta-button"
                />
                <q-btn
                  outline
                  size="lg"
                  color="white"
                  label="Play Species Game"
                  icon="casino"
                  to="/game"
                  class="cta-button"
                />
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Features Section -->
      <section class="features-section q-py-xl">
        <div class="container">
          <h2 class="section-title text-center q-mb-xl">
            Advancing Marine Research
          </h2>
          <div class="row q-col-gutter-lg">
            <div class="col-12 col-md-4">
              <q-card class="feature-card" flat bordered>
                <q-card-section class="text-center">
                  <q-icon name="image_search" size="64px" color="primary" class="q-mb-md" />
                  <h3 class="text-h6 q-mb-sm">Image Classification</h3>
                  <p class="text-body2 text-grey-7">
                    State-of-the-art deep learning models trained on thousands of underwater images to accurately identify benthic species
                  </p>
                </q-card-section>
              </q-card>
            </div>
  
            <div class="col-12 col-md-4">
              <q-card class="feature-card" flat bordered>
                <q-card-section class="text-center">
                  <q-icon name="radar" size="64px" color="teal" class="q-mb-md" />
                  <h3 class="text-h6 q-mb-sm">Object Detection</h3>
                  <p class="text-body2 text-grey-7">
                    Real-time detection and localization of multiple species in complex underwater environments
                  </p>
                </q-card-section>
              </q-card>
            </div>
  
            <div class="col-12 col-md-4">
              <q-card class="feature-card" flat bordered>
                <q-card-section class="text-center">
                  <q-icon name="insights" size="64px" color="deep-orange" class="q-mb-md" />
                  <h3 class="text-h6 q-mb-sm">Ecosystem Monitoring</h3>
                  <p class="text-body2 text-grey-7">
                    Track biodiversity patterns and support conservation efforts with automated species distribution analysis
                  </p>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Interactive Game Preview -->
      <section class="game-preview-section q-py-xl">
        <div class="container">
          <div class="row items-center q-col-gutter-xl">
            <div class="col-12 col-md-6">
              <h2 class="section-title q-mb-md">
                Test Your Marine Knowledge
              </h2>
              <p class="text-body1 text-grey-8 q-mb-lg">
                Challenge yourself to identify benthic species from real underwater imagery. Compete with our AI model and learn about fascinating seafloor creatures while contributing to marine science education.
              </p>
              <q-list bordered class="rounded-borders q-mb-lg">
                <q-item>
                  <q-item-section avatar>
                    <q-icon color="green" name="check_circle" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Multiple difficulty levels</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item>
                  <q-item-section avatar>
                    <q-icon color="green" name="check_circle" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Real underwater imagery</q-item-label>
                  </q-item-section>
                </q-item>
                <q-item>
                  <q-item-section avatar>
                    <q-icon color="green" name="check_circle" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Educational species facts</q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
              <q-btn
                unelevated
                color="primary"
                size="lg"
                label="Start Playing"
                icon-right="play_arrow"
                to="/game"
              />
            </div>
            <div class="col-12 col-md-6">
              <q-card class="game-preview-card">
                <q-img
                  src="/game-preview.jpg"
                  ratio="16/9"
                  class="rounded-borders"
                >
                  <div class="absolute-bottom text-subtitle1 text-center">
                    Can you identify this species?
                  </div>
                </q-img>
              </q-card>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Stats Section -->
      <section class="stats-section q-py-xl">
        <div class="container">
          <div class="row q-col-gutter-lg text-center">
            <div class="col-12 col-md-3">
              <div class="stat-item">
                <div class="stat-number text-h3 text-weight-bold text-primary">
                  50+
                </div>
                <div class="stat-label text-body1 text-grey-7">
                  Species Identified
                </div>
              </div>
            </div>
            <div class="col-12 col-md-3">
              <div class="stat-item">
                <div class="stat-number text-h3 text-weight-bold text-teal">
                  95%
                </div>
                <div class="stat-label text-body1 text-grey-7">
                  Model Accuracy
                </div>
              </div>
            </div>
            <div class="col-12 col-md-3">
              <div class="stat-item">
                <div class="stat-number text-h3 text-weight-bold text-deep-orange">
                  10K+
                </div>
                <div class="stat-label text-body1 text-grey-7">
                  Training Images
                </div>
              </div>
            </div>
            <div class="col-12 col-md-3">
              <div class="stat-item">
                <div class="stat-number text-h3 text-weight-bold text-blue">
                  24/7
                </div>
                <div class="stat-label text-body1 text-grey-7">
                  Real-time Detection
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="cta-section q-py-xl">
        <div class="container text-center">
          <h2 class="text-h4 text-white q-mb-md">
            Ready to Explore Marine Biodiversity?
          </h2>
          <p class="text-body1 text-white q-mb-lg">
            Discover how our AI solution can revolutionize underwater species monitoring
          </p>
          <q-btn
            unelevated
            size="lg"
            color="white"
            text-color="primary"
            label="View Our Solution"
            icon-right="arrow_forward"
            to="/solution"
          />
        </div>
      </section>
    </q-page>
  </template>
  
  <script setup lang="ts">
  // Component logic can be added here as needed
  </script>
  
  <style scoped lang="scss">
  .ocean-page {
    background: #f5f9fa;
  }
  
  .hero-section {
    position: relative;
    min-height: 600px;
    background: linear-gradient(180deg, rgba(0, 105, 148, 0.9) 0%, rgba(10, 77, 104, 0.95) 100%),
                url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23ffffff" fill-opacity="0.1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,144C960,149,1056,139,1152,128C1248,117,1344,107,1392,101.3L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
  }
  
  .hero-overlay {
    width: 100%;
  }
  
  .hero-title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 700;
    line-height: 1.2;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }
  
  .hero-subtitle {
    font-size: clamp(1rem, 2.5vw, 1.5rem);
    max-width: 800px;
    margin: 0 auto;
    opacity: 0.95;
  }
  
  .cta-button {
    min-width: 180px;
    transition: transform 0.2s;
  
    &:hover {
      transform: translateY(-2px);
    }
  }
  
  .features-section {
    background: white;
  }
  
  .section-title {
    font-size: 2rem;
    font-weight: 600;
    color: #0a4d68;
  }
  
  .feature-card {
    height: 100%;
    transition: transform 0.3s, box-shadow 0.3s;
  
    &:hover {
      transform: translateY(-8px);
      box-shadow: 0 8px 24px rgba(0, 105, 148, 0.15);
    }
  }
  
  .game-preview-section {
    background: linear-gradient(135deg, #e8f4f8 0%, #d4e7ed 100%);
  }
  
  .game-preview-card {
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  
    &:hover {
      box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15);
    }
  }
  
  .stats-section {
    background: white;
  }
  
  .stat-item {
    padding: 1.5rem;
  }
  
  .stat-number {
    margin-bottom: 0.5rem;
  }
  
  .cta-section {
    background: linear-gradient(135deg, #006994 0%, #0a4d68 100%);
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }
  
  @media (max-width: 768px) {
    .hero-section {
      min-height: 500px;
    }
  }
  </style>
  