<template>
  <q-page class="ai-demo-page">
    <!-- Hero Section -->
    <div class="hero-section">
      <div class="hero-content">
        <div class="hero-badge">
          <q-icon name="auto_awesome" size="16px" />
          <span>AI-Powered Computer Vision</span>
        </div>
        <h1 class="hero-title">
          Benthic Species Identification
        </h1>
        <p class="hero-subtitle">
          Advanced deep learning models for underwater biodiversity analysis
        </p>
        
        <!-- Stats Bar -->
        <div class="stats-bar">
          <div class="stat-item">
            <div class="stat-value">7</div>
            <div class="stat-label">Species Classes</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <div class="stat-value">94.2%</div>
            <div class="stat-label">Accuracy</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <div class="stat-value">&lt;2s</div>
            <div class="stat-label">Processing</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <div class="stat-value">15K+</div>
            <div class="stat-label">Training Images</div>
          </div>
        </div>
      </div>
    </div>

    <div class="content-container">
      <!-- Task Selector -->
      <div class="task-selector-wrapper">
        <q-tabs
          v-model="activeTask"
          class="custom-tabs"
          active-color="primary"
          indicator-color="primary"
          inline-label
          dense
        >
          <q-tab name="classification" class="custom-tab">
            <q-icon name="category" size="20px" class="q-mr-sm" />
            <div class="tab-content">
              <div class="tab-title">Classification</div>
              <div class="tab-subtitle">Single species identification</div>
            </div>
          </q-tab>
          <q-tab name="detection" class="custom-tab">
            <q-icon name="radar" size="20px" class="q-mr-sm" />
            <div class="tab-content">
              <div class="tab-title">Detection</div>
              <div class="tab-subtitle">Multi-object localization</div>
            </div>
          </q-tab>
        </q-tabs>
      </div>

      <q-tab-panels v-model="activeTask" animated transition-prev="slide-down" transition-next="slide-up" class="custom-panels">
        <!-- TASK 1: IMAGE CLASSIFICATION -->
        <q-tab-panel name="classification" class="custom-panel">
          <div class="task-grid">
            <!-- Left Column -->
            <div class="left-column">
              <!-- Upload Section -->
              <div class="glass-card upload-section">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="cloud_upload" color="primary" size="24px" />
                    <span>Upload Image</span>
                  </div>
                  <q-badge color="primary" outline label="JPG, PNG" />
                </div>

                <q-file
                  v-model="classificationFile"
                  filled
                  accept="image/*"
                  label="Choose or drag image here"
                  @update:model-value="handleClassificationUpload"
                  class="modern-file-input"
                  bg-color="grey-1"
                  borderless
                >
                  <template v-slot:prepend>
                    <q-icon name="image" color="primary" />
                  </template>
                  <template v-slot:append>
                    <q-icon
                      v-if="classificationFile"
                      name="close"
                      @click.stop.prevent="clearClassification"
                      class="cursor-pointer"
                      color="grey-6"
                    />
                  </template>
                </q-file>

                <!-- Sample Images -->
                <div class="samples-section">
                  <div class="section-label">
                    <span>Sample Images</span>
                    <q-icon name="info" size="16px" color="grey-6">
                      <q-tooltip>Click to use pre-loaded samples</q-tooltip>
                    </q-icon>
                  </div>
                  <div class="samples-grid">
                    <div
                      v-for="(sample, index) in classificationSamples"
                      :key="index"
                      class="sample-card"
                      :class="{ 'sample-active': selectedClassificationSample === index }"
                      @click="selectClassificationSample(index)"
                    >
                      <q-img
                        :src="sample.thumbnail"
                        ratio="1"
                        class="sample-image"
                      >
                        <div class="sample-overlay">
                          <q-icon name="check_circle" size="24px" color="white" />
                        </div>
                      </q-img>
                      <div class="sample-label">Sample {{ index + 1 }}</div>
                    </div>
                  </div>
                </div>

                <!-- Action Button -->
                <q-btn
                  unelevated
                  color="primary"
                  size="lg"
                  class="action-btn"
                  :loading="isClassifying"
                  :disable="!classificationImage"
                  @click="classifyImage"
                >
                  <q-icon name="psychology" size="20px" class="q-mr-sm" />
                  <span>Analyze Image</span>
                  <template v-slot:loading>
                    <q-spinner-dots size="20px" />
                    <span class="q-ml-sm">Processing...</span>
                  </template>
                </q-btn>
              </div>

              <!-- Species Reference -->
              <div class="glass-card species-reference">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="pets" color="primary" size="24px" />
                    <span>Target Species</span>
                  </div>
                </div>
                <div class="species-grid">
                  <div v-for="(species, index) in speciesCategories" :key="index" class="species-chip">
                    <div class="species-number">{{ index + 1 }}</div>
                    <div class="species-name">{{ species }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right Column -->
            <div class="right-column">
              <div class="glass-card results-section">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="analytics" color="primary" size="24px" />
                    <span>Results</span>
                  </div>
                  <q-badge v-if="classificationResults.length > 0" color="green" :label="`Confidence: ${(classificationResults[0]?.confidence * 100).toFixed(1)}%`" />
                </div>

                <!-- Image Preview -->
                <div v-if="classificationImage" class="image-preview">
                  <q-img
                    :src="classificationImageUrl"
                    class="preview-image"
                    fit="contain"
                  >
                    <template v-slot:loading>
                      <div class="loading-placeholder">
                        <q-spinner-gears size="50px" color="primary" />
                      </div>
                    </template>
                  </q-img>
                </div>

                <div v-else class="empty-state">
                  <div class="empty-icon-wrapper">
                    <q-icon name="image_search" size="80px" color="grey-4" />
                  </div>
                  <div class="empty-title">No Image Selected</div>
                  <div class="empty-subtitle">Upload an image or select a sample to begin</div>
                </div>

                <!-- Results -->
                <div v-if="classificationResults.length > 0" class="results-content">
                  <div class="results-header">
                    <span class="results-title">Predictions</span>
                    <q-btn flat dense round size="sm" icon="refresh" color="grey-7">
                      <q-tooltip>Reanalyze</q-tooltip>
                    </q-btn>
                  </div>

                  <div class="predictions-list">
                    <div
                      v-for="(result, index) in classificationResults"
                      :key="index"
                      class="prediction-item"
                      :class="{ 'top-prediction': index === 0 }"
                    >
                      <div class="prediction-header">
                        <div class="prediction-info">
                          <q-avatar v-if="index === 0" size="24px" color="green" text-color="white" icon="star" />
                          <span class="prediction-name">{{ result.species }}</span>
                        </div>
                        <span class="prediction-percentage">{{ (result.confidence * 100).toFixed(1) }}%</span>
                      </div>
                      <q-linear-progress
                        :value="result.confidence"
                        :color="getConfidenceColor(result.confidence)"
                        size="8px"
                        rounded
                        class="prediction-bar"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </q-tab-panel>

        <!-- TASK 2: OBJECT DETECTION -->
        <q-tab-panel name="detection" class="custom-panel">
          <div class="task-grid">
            <!-- Left Column -->
            <div class="left-column">
              <!-- Upload Section -->
              <div class="glass-card upload-section">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="cloud_upload" color="primary" size="24px" />
                    <span>Upload Image</span>
                  </div>
                  <q-badge color="primary" outline label="JPG, PNG" />
                </div>

                <q-file
                  v-model="detectionFile"
                  filled
                  accept="image/*"
                  label="Choose or drag image here"
                  @update:model-value="handleDetectionUpload"
                  class="modern-file-input"
                  bg-color="grey-1"
                  borderless
                >
                  <template v-slot:prepend>
                    <q-icon name="image" color="primary" />
                  </template>
                  <template v-slot:append>
                    <q-icon
                      v-if="detectionFile"
                      name="close"
                      @click.stop.prevent="clearDetection"
                      class="cursor-pointer"
                      color="grey-6"
                    />
                  </template>
                </q-file>

                <!-- Sample Images -->
                <div class="samples-section">
                  <div class="section-label">
                    <span>Sample Images</span>
                    <q-icon name="info" size="16px" color="grey-6">
                      <q-tooltip>Click to use pre-loaded samples</q-tooltip>
                    </q-icon>
                  </div>
                  <div class="samples-grid detection-samples">
                    <div
                      v-for="(sample, index) in detectionSamples"
                      :key="index"
                      class="sample-card"
                      :class="{ 'sample-active': selectedDetectionSample === index }"
                      @click="selectDetectionSample(index)"
                    >
                      <q-img
                        :src="sample.thumbnail"
                        ratio="1"
                        class="sample-image"
                      >
                        <div class="sample-overlay">
                          <q-icon name="check_circle" size="24px" color="white" />
                        </div>
                      </q-img>
                      <div class="sample-label">{{ sample.name }}</div>
                    </div>
                  </div>
                </div>

                <!-- Action Button -->
                <q-btn
                  unelevated
                  color="primary"
                  size="lg"
                  class="action-btn"
                  :loading="isDetecting"
                  :disable="!detectionImage"
                  @click="detectObjects"
                >
                  <q-icon name="radar" size="20px" class="q-mr-sm" />
                  <span>Detect Objects</span>
                  <template v-slot:loading>
                    <q-spinner-dots size="20px" />
                    <span class="q-ml-sm">Processing...</span>
                  </template>
                </q-btn>
              </div>

              <!-- Model Info -->
              <div class="glass-card model-info">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="model_training" color="primary" size="24px" />
                    <span>Model Performance</span>
                  </div>
                </div>
                <div class="metrics-grid">
                  <div class="metric-card">
                    <div class="metric-icon">
                      <q-icon name="verified" size="28px" color="green" />
                    </div>
                    <div class="metric-content">
                      <div class="metric-value">92.4%</div>
                      <div class="metric-label">mAP Score</div>
                    </div>
                  </div>
                  <div class="metric-card">
                    <div class="metric-icon">
                      <q-icon name="photo_library" size="28px" color="blue" />
                    </div>
                    <div class="metric-content">
                      <div class="metric-value">15.2K</div>
                      <div class="metric-label">Training Set</div>
                    </div>
                  </div>
                  <div class="metric-card">
                    <div class="metric-icon">
                      <q-icon name="speed" size="28px" color="orange" />
                    </div>
                    <div class="metric-content">
                      <div class="metric-value">1.5s</div>
                      <div class="metric-label">Avg Speed</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right Column -->
            <div class="right-column">
              <!-- Detection Results -->
              <div class="glass-card results-section">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="visibility" color="primary" size="24px" />
                    <span>Detection Results</span>
                  </div>
                  <div v-if="hasDetections" class="header-actions">
                    <q-btn-toggle
                      v-model="viewMode"
                      toggle-color="primary"
                      size="sm"
                      unelevated
                      :options="[
                        { label: 'Annotated', value: 'annotated', icon: 'layers' },
                        { label: 'Original', value: 'original', icon: 'image' }
                      ]"
                    />
                    <q-btn flat dense round size="sm" icon="download" color="primary" @click="downloadResults">
                      <q-tooltip>Download Results</q-tooltip>
                    </q-btn>
                  </div>
                </div>

                <!-- Image with Detections -->
                <div v-if="detectionImage" class="detection-preview">
                  <div class="image-wrapper">
                    <img
                      :src="detectionImageUrl"
                      alt="Detection result"
                      class="detection-image"
                    />
                    <div
                      v-for="(detection, index) in detections"
                      :key="index"
                      v-show="viewMode === 'annotated'"
                      class="bounding-box"
                      :style="getBoundingBoxStyle(detection)"
                    >
                      <div class="box-label">
                        <span class="box-species">{{ detection.species }}</span>
                        <span class="box-confidence">{{ (detection.confidence * 100).toFixed(0) }}%</span>
                      </div>
                    </div>
                  </div>
                </div>

                <div v-else class="empty-state">
                  <div class="empty-icon-wrapper">
                    <q-icon name="image_search" size="80px" color="grey-4" />
                  </div>
                  <div class="empty-title">No Image Selected</div>
                  <div class="empty-subtitle">Upload an image or select a sample to begin</div>
                </div>
              </div>

              <!-- Detection List -->
              <div v-if="hasDetections" class="glass-card detections-list">
                <div class="card-header">
                  <div class="card-title">
                    <q-icon name="list" color="primary" size="24px" />
                    <span>Detected Objects</span>
                  </div>
                  <q-badge color="primary" :label="`${detections.length} found`" />
                </div>

                <div class="detections-content">
                  <div
                    v-for="(detection, index) in sortedDetections"
                    :key="index"
                    class="detection-item"
                    @click="showSpeciesInfo(detection)"
                  >
                    <div class="detection-number">{{ index + 1 }}</div>
                    <div class="detection-info">
                      <div class="detection-name">{{ detection.species }}</div>
                      <div class="detection-scientific">{{ detection.scientificName }}</div>
                      <q-linear-progress
                        :value="detection.confidence"
                        :color="getConfidenceColor(detection.confidence)"
                        size="4px"
                        rounded
                        class="q-mt-xs"
                      />
                    </div>
                    <div class="detection-confidence">
                      <q-badge :color="getConfidenceColor(detection.confidence)" :label="`${(detection.confidence * 100).toFixed(1)}%`" />
                      <q-icon name="chevron_right" size="20px" color="grey-5" class="q-ml-xs" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Statistics -->
              <div v-if="hasDetections" class="glass-card stats-card">
                <div class="stats-grid-compact">
                  <div class="stat-compact">
                    <q-icon name="timer" size="24px" color="primary" />
                    <div>
                      <div class="stat-compact-value">{{ processingTime }}s</div>
                      <div class="stat-compact-label">Processing Time</div>
                    </div>
                  </div>
                  <div class="stat-compact">
                    <q-icon name="pets" size="24px" color="teal" />
                    <div>
                      <div class="stat-compact-value">{{ detections.length }}</div>
                      <div class="stat-compact-label">Objects Found</div>
                    </div>
                  </div>
                  <div class="stat-compact">
                    <q-icon name="high_quality" size="24px" color="green" />
                    <div>
                      <div class="stat-compact-value">{{ avgConfidence }}%</div>
                      <div class="stat-compact-label">Avg Confidence</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </q-tab-panel>
      </q-tab-panels>
    </div>

    <!-- Species Info Dialog -->
    <q-dialog v-model="showSpeciesDialog">
      <q-card class="species-dialog">
        <q-card-section class="dialog-header">
          <div class="dialog-title">
            <q-icon name="pets" size="28px" color="primary" class="q-mr-sm" />
            <span>{{ selectedSpecies?.species }}</span>
          </div>
          <q-btn icon="close" flat round dense v-close-popup color="grey-7" />
        </q-card-section>

        <q-separator />

        <q-card-section class="dialog-content">
          <div class="info-row">
            <div class="info-label">
              <q-icon name="science" size="20px" />
              <span>Scientific Name</span>
            </div>
            <div class="info-value italic">{{ selectedSpecies?.scientificName }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">
              <q-icon name="terrain" size="20px" />
              <span>Habitat</span>
            </div>
            <div class="info-value">{{ selectedSpecies?.habitat }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">
              <q-icon name="waves" size="20px" />
              <span>Depth Range</span>
            </div>
            <div class="info-value">{{ selectedSpecies?.depthRange }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">
              <q-icon name="eco" size="20px" />
              <span>Conservation</span>
            </div>
            <q-badge
              :color="getConservationColor(selectedSpecies?.conservation)"
              :label="selectedSpecies?.conservation"
              class="conservation-badge"
            />
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useQuasar, Notify } from 'quasar'
import { Client, handle_file } from '@gradio/client'
import { Buffer } from 'buffer'

// Initialize Quasar Notify
Notify.setDefaults({
  position: 'top',
  timeout: 2500,
  textColor: 'white'
})

// Import sample images from assets
import eelImage from '../assets/eel.jpg'
import roundfishImage from '../assets/roundfish.jpg'
import skateImage from '../assets/skate.jpg'

window.Buffer = Buffer

const $q = useQuasar()

// Gradio Client
let gradioClient = null

// Active Task
const activeTask = ref('classification')

// TASK 1: CLASSIFICATION STATE
const classificationFile = ref(null)
const classificationImage = ref(null)
const classificationImageUrl = ref('')
const selectedClassificationSample = ref(null)
const isClassifying = ref(false)
const classificationResults = ref([])

// TASK 2: DETECTION STATE
const detectionFile = ref(null)
const detectionImage = ref(null)
const detectionImageUrl = ref('')
const selectedDetectionSample = ref(null)
const isDetecting = ref(false)
const detections = ref([])
const viewMode = ref('annotated')
const processingTime = ref(0)

// Shared state
const showSpeciesDialog = ref(false)
const selectedSpecies = ref(null)

// Species Categories for Classification (7 categories)
const speciesCategories = [
  'Eel',
  'Scallop',
  'Crab',
  'Flatfish',
  'Roundfish',
  'Skate',
  'Whelk'
]

// Sample Images for Classification - Use imported images
const classificationSamples = ref([
  {
    thumbnail: eelImage,
    url: eelImage
  },
  {
    thumbnail: roundfishImage,
    url: roundfishImage
  },
  {
    thumbnail: skateImage,
    url: skateImage
  }
])

// Sample Images for Detection
const detectionSamples = ref([
  {
    name: 'Coral Reef',
    thumbnail: '/samples/detect-coral.jpg',
    url: '/samples/detect-coral-full.jpg'
  },
  {
    name: 'Rocky Bottom',
    thumbnail: '/samples/detect-rocky.jpg',
    url: '/samples/detect-rocky-full.jpg'
  },
  {
    name: 'Deep Sea',
    thumbnail: '/samples/detect-deep.jpg',
    url: '/samples/detect-deep-full.jpg'
  },
  {
    name: 'Sandy Floor',
    thumbnail: '/samples/detect-sandy.jpg',
    url: '/samples/detect-sandy-full.jpg'
  }
])

// COMPUTED
const hasDetections = computed(() => detections.value.length > 0)

const sortedDetections = computed(() => {
  return [...detections.value].sort((a, b) => b.confidence - a.confidence)
})

const avgConfidence = computed(() => {
  if (detections.value.length === 0) return 0
  const sum = detections.value.reduce((acc, d) => acc + d.confidence, 0)
  return ((sum / detections.value.length) * 100).toFixed(1)
})

// GRADIO CLIENT INITIALIZATION
async function initGradioClient() {
  try {
    gradioClient = await Client.connect('dshi01/benthic_classification')
    console.log('Successfully connected to Gradio Space')
  } catch (error) {
    console.error('Failed to connect to Gradio Space:', error)
    $q.notify({
      type: 'negative',
      message: 'Failed to connect to ML model. Please try again later.',
      position: 'top',
      timeout: 3000
    })
  }
}

// Initialize on component mount
onMounted(() => {
  initGradioClient()
})

// CLASSIFICATION METHODS
function handleClassificationUpload(file) {
  if (file) {
    selectedClassificationSample.value = null
    classificationImage.value = 'uploaded'
    classificationImageUrl.value = URL.createObjectURL(file)
    classificationResults.value = []
  }
}

function clearClassification() {
  classificationFile.value = null
  classificationImage.value = null
  classificationImageUrl.value = ''
  classificationResults.value = []
}

function selectClassificationSample(index) {
  selectedClassificationSample.value = index
  classificationFile.value = null
  classificationImage.value = classificationSamples.value[index].url
  classificationImageUrl.value = classificationSamples.value[index].url
  classificationResults.value = []
}

async function classifyImage() {
  // Ensure client is connected
  if (!gradioClient) {
    await initGradioClient()
    if (!gradioClient) {
      $q.notify({
        type: 'negative',
        message: 'Unable to connect to classification model',
        position: 'top'
      })
      return
    }
  }

  isClassifying.value = true
  classificationResults.value = []

  try {
    // Prepare the image
    let imageBlob
    if (classificationFile.value) {
      imageBlob = classificationFile.value
    } else if (classificationImage.value) {
      // Fetch sample image
      const response = await fetch(classificationImageUrl.value)
      imageBlob = await response.blob()
    } else {
      throw new Error('No image selected')
    }

    // Call the Gradio API
    const result = await gradioClient.predict('/predict', {
      image: handle_file(imageBlob)
    })

    console.log('Full API Result:', result.data)

    // Parse the specific format: [{ label: 'Species', confidences: [...] }]
    const predictions = result.data

    if (Array.isArray(predictions) && predictions.length > 0) {
      const prediction = predictions[0]
      
      console.log('Prediction object:', prediction)
      console.log('Confidences array:', prediction.confidences)
      
      if (prediction.confidences && Array.isArray(prediction.confidences)) {
        // Check if confidences contains objects or numbers
        const firstConfidence = prediction.confidences[0]
        
        if (typeof firstConfidence === 'object' && firstConfidence !== null) {
          // Confidences is an array of objects like [{label: 'Eel', confidence: 0.02}, ...]
          classificationResults.value = prediction.confidences
            .map(item => ({
              species: item.label || item.class || 'Unknown',
              confidence: Number(item.confidence || item.score || 0)
            }))
            .sort((a, b) => b.confidence - a.confidence)
        } else {
          // Confidences is an array of numbers [0.95, 0.02, ...]
          classificationResults.value = speciesCategories.map((species, index) => ({
            species: species,
            confidence: Number(prediction.confidences[index]) || 0
          })).sort((a, b) => b.confidence - a.confidence)
        }
      }
    }

    console.log('Parsed Classification Results:', classificationResults.value)

    if (classificationResults.value.length === 0) {
      throw new Error('Unable to parse classification results')
    }

    $q.notify({
      type: 'positive',
      message: 'Classification complete!',
      position: 'top',
      timeout: 2000
    })
  } catch (error) {
    console.error('Classification error:', error)
    $q.notify({
      type: 'negative',
      message: `Classification failed: ${error.message}`,
      position: 'top',
      timeout: 3000
    })
  } finally {
    isClassifying.value = false
  }
}

// DETECTION METHODS
function handleDetectionUpload(file) {
  if (file) {
    selectedDetectionSample.value = null
    detectionImage.value = 'uploaded'
    detectionImageUrl.value = URL.createObjectURL(file)
    detections.value = []
  }
}

function clearDetection() {
  detectionFile.value = null
  detectionImage.value = null
  detectionImageUrl.value = ''
  detections.value = []
}

function selectDetectionSample(index) {
  selectedDetectionSample.value = index
  detectionFile.value = null
  detectionImage.value = detectionSamples.value[index].name
  detectionImageUrl.value = detectionSamples.value[index].url
  detections.value = []
}

async function detectObjects() {
  // Ensure client is connected
  if (!gradioClient) {
    await initGradioClient()
    if (!gradioClient) {
      $q.notify({
        type: 'negative',
        message: 'Unable to connect to detection model',
        position: 'top'
      })
      return
    }
  }

  isDetecting.value = true
  detections.value = []

  try {
    // Prepare the image
    let imageBlob
    if (detectionFile.value) {
      imageBlob = detectionFile.value
    } else if (detectionImage.value) {
      const response = await fetch(detectionImageUrl.value)
      imageBlob = await response.blob()
    } else {
      throw new Error('No image selected')
    }

    const startTime = Date.now()

    // Call the Gradio API
    // Note: Update endpoint name if your Space uses a different one for detection
    const result = await gradioClient.predict('/detect', {
      image: handle_file(imageBlob)
    })

    processingTime.value = ((Date.now() - startTime) / 1000).toFixed(1)

    // Process detection results
    // Adjust based on your actual model output format
    const detectionData = result.data

    if (Array.isArray(detectionData)) {
      detections.value = detectionData.map(det => ({
        species: det.species || det.label || det.class,
        scientificName: det.scientificName || 'Unknown',
        confidence: det.confidence || det.score || 0,
        bbox: det.bbox || det.box || { x: 0, y: 0, width: 0, height: 0 },
        habitat: det.habitat || 'Unknown',
        depthRange: det.depthRange || 'Unknown',
        conservation: det.conservation || 'Unknown'
      }))
    }

    $q.notify({
      type: 'positive',
      message: `Detection complete! Found ${detections.value.length} objects.`,
      position: 'top',
      timeout: 2000
    })
  } catch (error) {
    console.error('Detection error:', error)
    $q.notify({
      type: 'negative',
      message: `Detection failed: ${error.message}`,
      position: 'top',
      timeout: 3000
    })
  } finally {
    isDetecting.value = false
  }
}

// SHARED METHODS
function getBoundingBoxStyle(detection) {
  if (viewMode.value === 'original') return { display: 'none' }

  return {
    left: `${detection.bbox.x}%`,
    top: `${detection.bbox.y}%`,
    width: `${detection.bbox.width}%`,
    height: `${detection.bbox.height}%`
  }
}

function getConfidenceColor(confidence) {
  if (confidence >= 0.9) return 'green'
  if (confidence >= 0.75) return 'light-green'
  if (confidence >= 0.6) return 'orange'
  return 'deep-orange'
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

function showSpeciesInfo(detection) {
  selectedSpecies.value = detection
  showSpeciesDialog.value = true
}

function downloadResults() {
  const results = {
    task: 'Object Detection',
    image: detectionImage.value,
    processingTime: processingTime.value,
    detections: detections.value.map(d => ({
      species: d.species,
      scientificName: d.scientificName,
      confidence: d.confidence,
      boundingBox: d.bbox
    }))
  }

  const blob = new Blob([JSON.stringify(results, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `detection-results-${Date.now()}.json`
  link.click()
  URL.revokeObjectURL(url)

  $q.notify({
    type: 'positive',
    message: 'Results downloaded successfully!',
    position: 'top'
  })
}
</script>

<style scoped lang="scss">
// DESIGN SYSTEM
$primary: #1976D2;
$secondary: #0D47A1;
$accent: #00BCD4;
$success: #4CAF50;
$warning: #FF9800;
$error: #F44336;

$gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
$gradient-ocean: linear-gradient(135deg, #0575E6 0%, #021B79 100%);
$gradient-success: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);

// HERO SECTION
.ai-demo-page {
  min-height: 100vh;
  background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
}

.hero-section {
  background: $gradient-ocean;
  padding: 4rem 2rem 3rem;
  color: white;
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)" /></svg>');
    opacity: 0.3;
  }
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  text-align: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin: 0 0 1rem 0;
  line-height: 1.2;
  letter-spacing: -0.02em;
  
  @media (max-width: 768px) {
    font-size: 2.25rem;
  }
}

.hero-subtitle {
  font-size: 1.25rem;
  opacity: 0.95;
  margin: 0 0 2.5rem 0;
  font-weight: 300;
}

// STATS BAR
.stats-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
  padding: 1.5rem 2rem;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  
  @media (max-width: 768px) {
    flex-wrap: wrap;
    gap: 1rem;
  }
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.875rem;
  opacity: 0.9;
  font-weight: 400;
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: rgba(255, 255, 255, 0.3);
  
  @media (max-width: 768px) {
    display: none;
  }
}

// CONTENT CONTAINER
.content-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

// TASK SELECTOR
.task-selector-wrapper {
  margin-bottom: 2rem;
  display: flex;
  justify-content: center;
}

.custom-tabs {
  background: white;
  border-radius: 16px;
  padding: 0.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  display: inline-flex;
}

.custom-tab {
  border-radius: 12px;
  padding: 1rem 2rem;
  min-height: auto;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &.q-tab--active {
    background: $gradient-primary;
    color: white !important;
  }
}

.tab-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.25rem;
}

.tab-title {
  font-size: 1rem;
  font-weight: 600;
}

.tab-subtitle {
  font-size: 0.75rem;
  opacity: 0.8;
}

// PANELS
.custom-panels {
  background: transparent;
}

.custom-panel {
  padding: 0;
}

// TASK GRID
.task-grid {
  display: grid;
  grid-template-columns: 400px 1fr;
  gap: 2rem;
  
  @media (max-width: 1200px) {
    grid-template-columns: 1fr;
  }
}

.left-column,
.right-column {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

// GLASS CARD
.glass-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 1.75rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.8);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &:hover {
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
    transform: translateY(-2px);
  }
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.card-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.125rem;
  font-weight: 600;
  color: #1a1a1a;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

// FILE INPUT
.modern-file-input {
  margin-bottom: 1.5rem;
  border-radius: 12px;
  overflow: hidden;
  
  :deep(.q-field__control) {
    border-radius: 12px;
    padding: 1rem;
    min-height: 56px;
  }
}

// SAMPLES SECTION
.samples-section {
  margin-bottom: 1.5rem;
}

.section-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.875rem;
  font-weight: 600;
  color: #666;
  margin-bottom: 0.75rem;
}

.samples-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
  
  &.detection-samples {
    grid-template-columns: repeat(2, 1fr);
  }
}

.sample-card {
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  border: 3px solid transparent;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  
  &:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  }
  
  &.sample-active {
    border-color: $primary;
    box-shadow: 0 0 0 4px rgba(25, 118, 210, 0.15);
  }
}

.sample-image {
  border-radius: 8px;
}

.sample-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(25, 118, 210, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
  
  .sample-active & {
    opacity: 1;
  }
}

.sample-label {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 0.5rem;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  font-size: 0.75rem;
  font-weight: 500;
  text-align: center;
}

// ACTION BUTTON
.action-btn {
  width: 100%;
  height: 56px;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: none;
  letter-spacing: 0.02em;
  box-shadow: 0 4px 16px rgba(25, 118, 210, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &:hover:not(:disabled) {
    box-shadow: 0 6px 24px rgba(25, 118, 210, 0.4);
    transform: translateY(-2px);
  }
}

// SPECIES REFERENCE
.species-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.species-chip {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: #f5f5f5;
  border-radius: 10px;
  transition: all 0.2s;
  
  &:hover {
    background: #e3f2fd;
    transform: translateX(4px);
  }
}

.species-number {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: $primary;
  color: white;
  border-radius: 50%;
  font-size: 0.75rem;
  font-weight: 700;
  flex-shrink: 0;
}

.species-name {
  font-size: 0.875rem;
  font-weight: 500;
  color: #333;
}

// MODEL INFO
.metrics-grid {
  display: grid;
  gap: 1rem;
}

.metric-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  transition: all 0.3s;
  
  &:hover {
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }
}

.metric-icon {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 12px;
}

.metric-content {
  flex: 1;
}

.metric-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.metric-label {
  font-size: 0.875rem;
  color: #666;
  font-weight: 500;
}

// IMAGE PREVIEW
.image-preview {
  margin-bottom: 1.5rem;
  border-radius: 16px;
  overflow: hidden;
  background: #000;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.preview-image {
  max-height: 500px;
  border-radius: 16px;
}

.loading-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

// EMPTY STATE
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  background: linear-gradient(135deg, #f5f7fa 0%, #e3e7ed 100%);
  border-radius: 16px;
  border: 2px dashed #cbd5e0;
  padding: 3rem;
}

.empty-icon-wrapper {
  width: 120px;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 50%;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.empty-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 0.5rem;
}

.empty-subtitle {
  font-size: 0.9375rem;
  color: #718096;
  text-align: center;
}

// RESULTS CONTENT
.results-content {
  margin-top: 1.5rem;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.results-title {
  font-size: 1rem;
  font-weight: 600;
  color: #333;
}

// PREDICTIONS LIST
.predictions-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.prediction-item {
  padding: 1.25rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-radius: 14px;
  border: 1px solid #e0e0e0;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &.top-prediction {
    background: linear-gradient(135deg, #e8f5e9 0%, #ffffff 100%);
    border-color: $success;
    box-shadow: 0 4px 16px rgba(76, 175, 80, 0.15);
  }
  
  &:hover {
    transform: translateX(4px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  }
}

.prediction-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.prediction-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.prediction-name {
  font-size: 1rem;
  font-weight: 600;
  color: #1a1a1a;
}

.prediction-percentage {
  font-size: 1.125rem;
  font-weight: 700;
  color: $primary;
}

.prediction-bar {
  margin-top: 0.5rem;
}

// DETECTION PREVIEW
.detection-preview {
  margin-bottom: 1.5rem;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.image-wrapper {
  position: relative;
  background: #000;
}

.detection-image {
  width: 100%;
  height: auto;
  display: block;
}

.bounding-box {
  position: absolute;
  border: 3px solid #00ff00;
  box-shadow: 
    0 0 0 2px rgba(0, 0, 0, 0.3),
    0 0 20px rgba(0, 255, 0, 0.6),
    inset 0 0 20px rgba(0, 255, 0, 0.1);
  backdrop-filter: blur(1px);
  transition: all 0.3s;
  
  &:hover {
    border-color: #ffff00;
    box-shadow: 
      0 0 0 2px rgba(0, 0, 0, 0.4),
      0 0 30px rgba(255, 255, 0, 0.8),
      inset 0 0 30px rgba(255, 255, 0, 0.2);
  }
}

.box-label {
  position: absolute;
  top: -32px;
  left: -3px;
  background: linear-gradient(135deg, #00ff00 0%, #00cc00 100%);
  color: #000;
  padding: 0.375rem 0.75rem;
  font-size: 0.8125rem;
  font-weight: 700;
  border-radius: 6px;
  white-space: nowrap;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.box-species {
  font-size: 0.875rem;
}

.box-confidence {
  opacity: 0.85;
  font-size: 0.75rem;
}

// DETECTIONS LIST
.detections-content {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-height: 400px;
  overflow-y: auto;
  padding-right: 0.5rem;
  
  &::-webkit-scrollbar {
    width: 6px;
  }
  
  &::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
  }
  
  &::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 10px;
    
    &:hover {
      background: #555;
    }
  }
}

.detection-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid transparent;
  
  &:hover {
    background: white;
    border-color: $primary;
    transform: translateX(4px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  }
}

.detection-number {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: $gradient-primary;
  color: white;
  border-radius: 50%;
  font-size: 0.875rem;
  font-weight: 700;
  flex-shrink: 0;
}

.detection-info {
  flex: 1;
  min-width: 0;
}

.detection-name {
  font-size: 0.9375rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.25rem;
}

.detection-scientific {
  font-size: 0.8125rem;
  color: #666;
  font-style: italic;
  margin-bottom: 0.5rem;
}

.detection-confidence {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  flex-shrink: 0;
}

// STATS CARD
.stats-grid-compact {
  display: grid;
  gap: 1rem;
}

.stat-compact {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
  border-radius: 12px;
  border: 1px solid #e0e0e0;
}

.stat-compact-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  line-height: 1;
}

.stat-compact-label {
  font-size: 0.8125rem;
  color: #666;
  margin-top: 0.25rem;
}

// SPECIES DIALOG
.species-dialog {
  min-width: 500px;
  border-radius: 20px;
  
  @media (max-width: 600px) {
    min-width: auto;
    width: 90vw;
  }
}

.dialog-header {
  padding: 1.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dialog-title {
  display: flex;
  align-items: center;
  font-size: 1.375rem;
  font-weight: 700;
  color: #1a1a1a;
}

.dialog-content {
  padding: 1.5rem 2rem 2rem;
}

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid #f0f0f0;
  
  &:last-child {
    border-bottom: none;
  }
}

.info-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9375rem;
  font-weight: 600;
  color: #666;
}

.info-value {
  font-size: 1rem;
  color: #1a1a1a;
  text-align: right;
  
  &.italic {
    font-style: italic;
  }
}

.conservation-badge {
  font-size: 0.875rem;
  padding: 0.375rem 0.75rem;
  font-weight: 600;
}

// RESPONSIVE
@media (max-width: 768px) {
  .hero-section {
    padding: 3rem 1.5rem 2rem;
  }
  
  .task-grid {
    gap: 1.5rem;
  }
  
  .glass-card {
    padding: 1.25rem;
  }
  
  .samples-grid {
    grid-template-columns: repeat(2, 1fr);
    
    &.detection-samples {
      grid-template-columns: 1fr;
    }
  }
  
  .species-grid {
    grid-template-columns: 1fr;
  }
}

// ANIMATIONS
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.glass-card {
  animation: fadeIn 0.5s ease-out;
}

// SMOOTH TRANSITIONS
* {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
