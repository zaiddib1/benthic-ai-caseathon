<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="modern-header">
      <q-toolbar class="header-toolbar">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
          class="q-mr-sm"
        />

        <q-toolbar-title class="brand-title">
          <div class="brand-wrapper">
            <div class="brand-icon">
              <q-icon name="waves" size="24px" />
            </div>
            <span class="brand-name">BenthicAI</span>
          </div>
        </q-toolbar-title>

        <q-tabs v-model="activeTab" class="gt-sm nav-tabs">
          <q-route-tab name="home" to="/" label="Home" />
          <q-route-tab name="solution" to="/solution" label="Our Solution" />
          <q-route-tab name="game" to="/game" label="Species Game" />
          <q-route-tab name="about" to="/about" label="About" />
        </q-tabs>

        <q-btn
          flat
          dense
          round
          icon="science"
          aria-label="Research"
          class="q-ml-sm"
        />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="modern-drawer"
    >
      <q-list>
        <q-item-label header class="drawer-header">
          Navigation
        </q-item-label>

        <q-item clickable v-ripple to="/" exact class="drawer-item">
          <q-item-section avatar>
            <q-icon name="home" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Home</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to="/solution" class="drawer-item">
          <q-item-section avatar>
            <q-icon name="psychology" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Our Solution</q-item-label>
            <q-item-label caption>AI Computer Vision</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to="/game" class="drawer-item">
          <q-item-section avatar>
            <q-icon name="casino" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Species Game</q-item-label>
            <q-item-label caption>Test Your Knowledge</q-item-label>
          </q-item-section>
        </q-item>

        <q-separator class="q-my-md" />

        <q-item-label header class="drawer-header">
          Resources
        </q-item-label>

        <q-item clickable v-ripple to="/about" class="drawer-item">
          <q-item-section avatar>
            <q-icon name="info" />
          </q-item-section>
          <q-item-section>
            <q-item-label>About</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to="/data" class="drawer-item">
          <q-item-section avatar>
            <q-icon name="dataset" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Dataset Info</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="modern-footer">
      <q-toolbar class="footer-toolbar">
        <q-toolbar-title>
          <div class="footer-content">
            <div class="footer-left">
              <q-icon name="copyright" size="16px" class="q-mr-xs" />
              <span>2025 BenthicAI | Marine Biodiversity Conservation</span>
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

const leftDrawerOpen = ref(false);
const activeTab = ref('home');

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
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

// DRAWER
.modern-drawer {
  background: linear-gradient(180deg, #f5f7fa 0%, #ffffff 100%);
}

.drawer-header {
  font-weight: 700;
  color: #667eea;
  padding: 1rem 1rem 0.5rem;
}

.drawer-item {
  border-radius: 10px;
  margin: 0.25rem 0.5rem;
  transition: all 0.3s;
  
  &:hover {
    background: rgba(102, 126, 234, 0.1);
  }
  
  &.q-router-link--active {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
    color: #667eea;
    
    :deep(.q-item__label) {
      font-weight: 700;
    }
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
