<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="header-gradient">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
          class="q-mr-sm"
        />

        <q-toolbar-title class="text-weight-bold">
          <div class="flex items-center">
            <q-icon name="waves" size="sm" class="q-mr-sm" />
            BenthicAI
          </div>
        </q-toolbar-title>

        <q-tabs v-model="activeTab" class="gt-sm">
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
      class="drawer-ocean"
    >
      <q-list>
        <q-item-label header class="text-weight-bold">
          Navigation
        </q-item-label>

        <q-item clickable v-ripple to="/" exact>
          <q-item-section avatar>
            <q-icon name="home" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Home</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to="/solution">
          <q-item-section avatar>
            <q-icon name="psychology" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Our Solution</q-item-label>
            <q-item-label caption>AI Computer Vision</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to="/game">
          <q-item-section avatar>
            <q-icon name="casino" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Species Game</q-item-label>
            <q-item-label caption>Test Your Knowledge</q-item-label>
          </q-item-section>
        </q-item>

        <q-separator class="q-my-md" />

        <q-item-label header class="text-weight-bold">
          Resources
        </q-item-label>

        <q-item clickable v-ripple to="/about">
          <q-item-section avatar>
            <q-icon name="info" />
          </q-item-section>
          <q-item-section>
            <q-item-label>About</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple to="/data">
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

    <q-footer elevated class="footer-ocean">
      <q-toolbar>
        <q-toolbar-title class="text-caption">
          <div class="row items-center justify-between">
            <div>
              © 2025 BenthicAI | Marine Biodiversity Conservation
            </div>
            <div class="q-gutter-sm">
              <q-icon name="eco" size="xs" />
              <span class="text-caption">Powered by AI & Marine Science</span>
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
.header-gradient {
  background: linear-gradient(135deg, #006994 0%, #0a4d68 50%, #1a3a52 100%);
}

.drawer-ocean {
  background: linear-gradient(180deg, #e8f4f8 0%, #d4e7ed 100%);
}

.footer-ocean {
  background: linear-gradient(90deg, #0a3d62 0%, #0c2f48 100%);
}

.q-toolbar {
  min-height: 64px;
}
</style>
