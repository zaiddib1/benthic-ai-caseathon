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
                <q-icon name="info" size="18px" />
                <span>About DeepFin</span>
              </div>
              <h1 class="hero-title">
                Marine Organisms Identification<br/>Made Simple
              </h1>
              <p class="hero-subtitle">
                Our AI-powered platform for the William & Mary AI Club Case-a-thon 2025
              </p>
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
  
      <!-- What is DeepFin Section -->
      <section class="content-section">
        <div class="container">
          <div class="content-card">
            <div class="section-header">
              <q-icon name="waves" size="48px" color="primary" />
              <h2>What is DeepFin?</h2>
            </div>
            <div class="content-body">
              <p>
                DeepFin is an artificial intelligence platform designed to identify and classify benthic marine organisms 
                from underwater images. Benthic organisms live on or near the ocean floor and play crucial roles in marine 
                ecosystems. Our platform uses advanced computer vision to help researchers, conservationists, and marine 
                biologists quickly analyze underwater imagery.
              </p>
              <p>
                The platform offers two main features: <strong>Image Classification</strong> for identifying the primary 
                organisms in a photo, and <strong>Object Detection</strong> for locating multiple organisms within complex 
                underwater scenes. Currently, we can identify seven key benthic organisms: Eel, Scallop, Crab, Flatfish, 
                Roundfish, Skate, and Whelk.
              </p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- How It Works Section -->
      <section class="content-section alt-bg">
        <div class="container">
          <div class="content-card">
            <div class="section-header">
              <q-icon name="psychology" size="48px" color="teal" />
              <h2>How the Models Work</h2>
            </div>
            <div class="content-body">
              <div class="model-explanation">
                <div class="model-item">
                  <div class="model-number">1</div>
                  <div class="model-content">
                    <h3>Image Classification Model</h3>
                    <p>
                      Uses a convolutional neural network trained on thousands of labeled underwater images. When you 
                      upload a photo, the model analyzes visual patterns and returns the most likely organisms with 
                      confidence scores for all seven categories.
                    </p>
                  </div>
                </div>
  
                <div class="model-item">
                  <div class="model-number">2</div>
                  <div class="model-content">
                    <h3>Object Detection Model</h3>
                    <p>
                      Built on YOLO11 (You Only Look Once), this model can detect and localize multiple organisms in a 
                      single image. It draws bounding boxes around each detected organism and provides organisms labels 
                      with confidence scores. The model processes images in real-time, making it practical for analyzing 
                      large datasets.
                    </p>
                  </div>
                </div>
  
                <div class="model-item">
                  <div class="model-number">3</div>
                  <div class="model-content">
                    <h3>Training & Deployment</h3>
                    <p>
                      Both models were trained using PyTorch (CNN) and Ultralytics (YOLO) frameworks on a dataset of over 10,000 
                      annotated underwater images. The models are hosted on Hugging Face, using Torch Lightning APIs,
                      while the web frontend is built with Vue.js and Quasar, deployed on Cloudflare.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Case-a-thon Section -->
      <section class="content-section">
        <div class="container">
          <div class="content-card">
            <div class="section-header">
              <q-icon name="emoji_events" size="48px" color="deep-orange" />
              <h2>W&M AI Case-a-thon 2025</h2>
            </div>
            <div class="content-body">
              <p>
                This project was created as our submission to the William & Mary AI Club Case-a-thon, held on 
                October 18, 2025, at the Integrated Science Center. The Case-a-thon is a unique hybrid competition 
                that combines the technical challenges of a hackathon with strategic case analysis.
              </p>
              <p>
                Unlike traditional hackathons, participants are encouraged to use existing AI tools and frameworks 
                ethically to solve real-world problems. Teams must present not just a working application, but also 
                their design philosophy, technical reasoning, and the broader implications of their solution.
              </p>
              <p>
                We chose to focus on the marine sciences prompt as we believed there is a critical need for automated tools 
                in marine biology research. Our solution helps streamline the time-consuming process of analyzing underwater 
                imagery, allowing researchers to focus more on conservation and ecosystem management. DeepFin demonstrates 
                how AI can be practically applied to solve real environmental challenges.
              </p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Team Section -->
      <section class="team-section">
        <div class="container">
          <div class="section-header-center">
            <div class="section-badge">
              <q-icon name="group" size="16px" />
              <span>Our Team</span>
            </div>
            <h2 class="section-title">Meet the Team</h2>
            <p class="section-subtitle">The people behind DeepFin</p>
          </div>
  
          <div class="team-grid">
            <!-- Add your team members here -->
            <div class="team-card">
              <div class="team-avatar">
                <q-avatar size="120px" class="team-avatar">
                    <img src="/src/assets/daniel-shi.jpeg" alt="Daniel Shi" />
                  </q-avatar>                                
                </div>
              <h3 class="team-name">Daniel Shi</h3>
              <p class="team-role">Data Science + CAMS</p>
              <p class="team-bio">Lead development of classification model, and fine-tuned object detection model.</p>
            </div>
  
            <div class="team-card">
                <q-avatar size="120px" class="team-avatar">
                    <img src="/src/assets/zaid-dib.jpeg" alt="Zaid Dib" />
                  </q-avatar> 
              <h3 class="team-name">Zaid Dib</h3>
              <p class="team-role">Computer Science + CAMS</p>
              <p class="team-bio">Designed and implemented frontend, and connected website to the models on hugging face.</p>
            </div>
  
            <div class="team-card">
                <q-avatar size="120px" class="team-avatar">
                    <img src="/src/assets/mikey-martinez.jpeg" alt="Michael Martinez" />
                  </q-avatar> 
              <h3 class="team-name">Michael Martinez</h3>
              <p class="team-role">Data Science + Applied Math</p>
              <p class="team-bio">Lead development of object detection model.</p>
            </div>

          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="cta-section">
        <div class="cta-background"></div>
        <div class="container">
          <div class="cta-content">
            <h2 class="cta-title">Try DeepFin Today</h2>
            <p class="cta-description">
              Experience our AI models firsthand or test your knowledge with our organisms identification game
            </p>
            <div class="cta-buttons">
              <q-btn
                unelevated
                size="lg"
                color="white"
                text-color="primary"
                label="Use AI Model"
                icon-right="smart_toy"
                to="/solution"
                class="cta-btn-primary"
              />
              <q-btn
                outline
                size="lg"
                color="white"
                label="Play Game"
                icon="casino"
                to="/game"
                class="cta-btn-secondary"
              />
            </div>
          </div>
        </div>
      </section>
    </q-page>
  </template>
  
  <script setup lang="ts">
  // Simple about page - no complex logic needed
  </script>
  
  <style scoped lang="scss">
  $primary: #1976D2;
  $gradient-blue: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  
  .ocean-page {
    background: #f8f9fa;
    overflow-x: hidden;
  }
  
  // HERO SECTION (matching HomePage)
  .hero-section {
    position: relative;
    min-height: 500px;
    display: flex;
    align-items: center;
    overflow: hidden;
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
    max-width: 800px;
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
  }
  
  .hero-title {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 800;
    color: white;
    line-height: 1.2;
    margin: 0 0 1.5rem 0;
    letter-spacing: -0.02em;
    text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
    color: rgba(255, 255, 255, 0.95);
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
  }
  
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
  
  // CONTENT SECTIONS
  .content-section {
    padding: 5rem 0;
    
    &.alt-bg {
      background: linear-gradient(135deg, #f5f7fa 0%, #e3e7ed 100%);
    }
  }
  
  .content-card {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    border-radius: 24px;
    padding: 3rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    
    @media (max-width: 768px) {
      padding: 2rem;
    }
  }
  
  .section-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 2px solid #f0f0f0;
    
    h2 {
      font-size: 2rem;
      font-weight: 700;
      color: #1a1a1a;
      margin: 0;
    }
    
    @media (max-width: 768px) {
      flex-direction: column;
      text-align: center;
    }
  }
  
  .content-body {
    p {
      font-size: 1.125rem;
      color: #555;
      line-height: 1.8;
      margin-bottom: 1.5rem;
      
      &:last-child {
        margin-bottom: 0;
      }
    }
  }
  
  // MODEL EXPLANATION
  .model-explanation {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-top: 2rem;
  }
  
  .model-item {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    
    @media (max-width: 768px) {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
  }
  
  .model-number {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: $gradient-blue;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.75rem;
    font-weight: 800;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
  }
  
  .model-content {
    flex: 1;
    
    h3 {
      font-size: 1.375rem;
      font-weight: 700;
      color: #1a1a1a;
      margin: 0 0 0.75rem 0;
    }
    
    p {
      font-size: 1rem;
      color: #666;
      line-height: 1.7;
      margin: 0;
    }
  }
  
  // TEAM SECTION
  .team-section {
    padding: 6rem 0;
    background: white;
  }
  
  .section-header-center {
    text-align: center;
    margin-bottom: 4rem;
  }
  
  .section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: $gradient-blue;
    color: white;
    padding: 0.5rem 1.25rem;
    border-radius: 50px;
    font-size: 0.875rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
  }
  
  .section-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #1a1a1a;
    margin: 0 0 1rem 0;
  }
  
  .section-subtitle {
    font-size: 1.125rem;
    color: #666;
  }
  
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1000px;
    margin: 0 auto;
  }
  
  .team-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    border: 1px solid #e0e0e0;
    transition: all 0.3s;
    
    &:hover {
      transform: translateY(-8px);
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
      border-color: transparent;
    }
  }
  
  .team-avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: $gradient-blue;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
    margin-top: 20px;
  }
  
  .team-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: #1a1a1a;
    margin: 0 0 0.5rem 0;
  }
  
  .team-role {
    font-size: 0.9375rem;
    color: #667eea;
    font-weight: 600;
    margin: 0 0 1rem 0;
  }
  
  .team-bio {
    font-size: 0.9375rem;
    color: #666;
    line-height: 1.6;
    margin: 0;
  }
  
  // CTA SECTION
  .cta-section {
    padding: 5rem 0;
    position: relative;
    overflow: hidden;
  }
  
  .cta-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: $gradient-blue;
  }
  
  .cta-content {
    position: relative;
    z-index: 1;
    text-align: center;
    max-width: 700px;
    margin: 0 auto;
  }
  
  .cta-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: white;
    margin: 0 0 1rem 0;
  }
  
  .cta-description {
    font-size: 1.25rem;
    color: rgba(255, 255, 255, 0.95);
    margin-bottom: 2.5rem;
    line-height: 1.6;
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
    min-width: 180px;
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
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    
    @media (max-width: 768px) {
      padding: 0 1.5rem;
    }
  }
  </style>
  