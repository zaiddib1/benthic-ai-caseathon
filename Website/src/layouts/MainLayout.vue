<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="modern-header">
      <q-toolbar class="header-toolbar">
        <q-toolbar-title class="brand-title">
          <div class="brand-wrapper">
            <div class="brand-icon">
              <q-icon name="waves" size="24px" />
            </div>
            <span class="brand-name">DeepFin</span>
          </div>
        </q-toolbar-title>

        <q-tabs v-model="activeTab" class="nav-tabs">
          <q-route-tab name="home" to="/" label="Home" />
          <q-route-tab name="solution" to="/solution" label="Our Solution" />
          <q-route-tab name="game" to="/game" label="Organisms Game" />
          <q-route-tab name="about" to="/about" label="About" />
        </q-tabs>

        <q-btn
          flat
          dense
          round
          icon="science"
          aria-label="Research"
          class="q-ml-sm"
          to="/dataset"
        />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="modern-footer">
      <q-toolbar class="footer-toolbar">
        <q-toolbar-title>
          <div class="footer-content">
            <div class="footer-left">
              <q-icon name="copyright" size="16px" class="q-mr-xs" />
              <span>2025 DeepFin | Marine Biodiversity Conservation</span>
            </div>
            <div class="footer-right">
              <q-icon name="eco" size="18px" class="q-mr-xs" />
              <span>Powered by AI & Marine Science</span>
            </div>
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const activeTab = ref('home');
</script>

<style scoped lang="scss">
// HEADER
.modern-header {
  background: linear-gradient(135deg, #0575E6 0%, #021B79 100%);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.header-toolbar {
  min-height: 70px;
}

.brand-title {
  flex-shrink: 0;
}

.brand-wrapper {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.brand-icon {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 800;
  color: white;
  letter-spacing: -0.01em;
}

.nav-tabs {
  color: rgba(255, 255, 255, 0.9);
  
  :deep(.q-tab) {
    font-weight: 600;
    
    &:hover {
      background: rgba(255, 255, 255, 0.1);
    }
  }
  
  :deep(.q-tab--active) {
    background: rgba(255, 255, 255, 0.15);
  }
  
  :deep(.q-tab__indicator) {
    background: white;
    height: 3px;
    border-radius: 3px 3px 0 0;
  }
}

// FOOTER
.modern-footer {
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  color: rgba(255, 255, 255, 0.9);
}

.footer-toolbar {
  min-height: 60px;
  padding: 0 2rem;
  
  @media (max-width: 768px) {
    padding: 0 1rem;
  }
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  width: 100%;
  font-size: 0.875rem;
  
  @media (max-width: 768px) {
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
  }
}

.footer-left,
.footer-right {
  display: flex;
  align-items: center;
  
  @media (max-width: 768px) {
    justify-content: center;
  }
}

.footer-right {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 0.5rem 1rem;
  border-radius: 50px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}
</style>
