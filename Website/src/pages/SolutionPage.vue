<template>
    <q-page class="ai-demo-page">
      <div class="container q-pa-lg">
        <!-- Header Section -->
        <div class="text-center q-mb-xl">
          <h1 class="page-title text-h3 text-weight-bold q-mb-md">
            AI Species Identification
          </h1>
          <p class="text-body1 text-grey-7">
            Upload underwater imagery to test our computer vision models
          </p>
        </div>
  
        <!-- Task Tabs -->
        <q-tabs
          v-model="activeTask"
          class="text-primary q-mb-lg"
          active-color="primary"
          indicator-color="primary"
          align="center"
        >
          <q-tab name="classification" label="Task 1: Image Classification" />
          <q-tab name="detection" label="Task 2: Object Detection" />
        </q-tabs>
  
        <q-tab-panels v-model="activeTask" animated>
          <!-- TASK 1: IMAGE CLASSIFICATION -->
          <q-tab-panel name="classification">
            <div class="row q-col-gutter-lg">
              <!-- Left Panel - Upload & Controls -->
              <div class="col-12 col-md-5">
                <q-card flat bordered class="upload-card">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="category" class="q-mr-sm" />
                      Upload Image for Classification
                    </div>
                    <div class="text-caption text-grey-7 q-mb-md">
                      Classify a single benthic organism into one of 7 species categories
                    </div>
  
                    <!-- File Upload -->
                    <q-file
                      v-model="classificationFile"
                      filled
                      accept="image/*"
                      label="Choose underwater image"
                      @update:model-value="handleClassificationUpload"
                      class="q-mb-md"
                    >
                      <template v-slot:prepend>
                        <q-icon name="image" />
                      </template>
                      <template v-slot:append>
                        <q-icon
                          v-if="classificationFile"
                          name="close"
                          @click.stop.prevent="clearClassification"
                          class="cursor-pointer"
                        />
                      </template>
                    </q-file>
  
                    <!-- Sample Images -->
                    <div class="text-subtitle2 q-mb-sm">Or try our samples:</div>
                    <div class="row q-col-gutter-sm q-mb-lg">
                      <div
                        v-for="(sample, index) in classificationSamples"
                        :key="index"
                        class="col-4"
                      >
                        <q-img
                          :src="sample.thumbnail"
                          ratio="1"
                          class="sample-thumbnail cursor-pointer rounded-borders"
                          :class="{ 'sample-selected': selectedClassificationSample === index }"
                          @click="selectClassificationSample(index)"
                        >
                          <div class="absolute-bottom text-caption text-center">
                            Sample {{ index + 1 }}
                          </div>
                        </q-img>
                      </div>
                    </div>
  
                    <!-- Analyze Button -->
                    <q-btn
                      unelevated
                      color="primary"
                      size="lg"
                      class="full-width"
                      label="Classify Image"
                      icon="psychology"
                      :loading="isClassifying"
                      :disable="!classificationImage"
                      @click="classifyImage"
                    />
                  </q-card-section>
                </q-card>
  
                <!-- Species Categories -->
                <q-card flat bordered class="q-mt-md">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="list_alt" class="q-mr-sm" />
                      Species Categories
                    </div>
                    <q-list dense>
                      <q-item v-for="(species, index) in speciesCategories" :key="index">
                        <q-item-section avatar>
                          <q-avatar color="primary" text-color="white" size="sm">
                            {{ index + 1 }}
                          </q-avatar>
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>{{ species }}</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-card-section>
                </q-card>
              </div>
  
              <!-- Right Panel - Results -->
              <div class="col-12 col-md-7">
                <q-card flat bordered class="results-card">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="analytics" class="q-mr-sm" />
                      Classification Results
                    </div>
  
                    <!-- Image Display -->
                    <div v-if="classificationImage" class="image-container q-mb-lg">
                      <q-img
                        :src="classificationImageUrl"
                        class="rounded-borders"
                        style="max-height: 400px"
                      />
                    </div>
  
                    <!-- Placeholder -->
                    <div v-else class="placeholder-container">
                      <q-icon name="image_search" size="120px" color="grey-5" />
                      <p class="text-h6 text-grey-6 q-mt-md">
                        Upload an image to begin classification
                      </p>
                    </div>
  
                    <!-- Classification Results -->
                    <div v-if="classificationResults.length > 0">
                      <q-separator class="q-my-md" />
                      <div class="text-subtitle1 text-weight-bold q-mb-md">
                        Prediction Confidence
                      </div>
                      <q-list bordered separator>
                        <q-item v-for="(result, index) in classificationResults" :key="index">
                          <q-item-section>
                            <q-item-label class="text-weight-bold">
                              {{ result.species }}
                            </q-item-label>
                            <q-linear-progress
                              :value="result.confidence"
                              :color="getConfidenceColor(result.confidence)"
                              class="q-mt-sm"
                              size="12px"
                            >
                              <div class="absolute-full flex flex-center">
                                <q-badge
                                  color="white"
                                  :text-color="getConfidenceColor(result.confidence)"
                                  :label="`${(result.confidence * 100).toFixed(1)}%`"
                                />
                              </div>
                            </q-linear-progress>
                          </q-item-section>
                          <q-item-section side v-if="index === 0">
                            <q-badge color="green" label="Top Prediction" />
                          </q-item-section>
                        </q-item>
                      </q-list>
                    </div>
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </q-tab-panel>
  
          <!-- TASK 2: OBJECT DETECTION -->
          <q-tab-panel name="detection">
            <div class="row q-col-gutter-lg">
              <!-- Left Panel - Upload & Controls -->
              <div class="col-12 col-md-5">
                <q-card flat bordered class="upload-card">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="radar" class="q-mr-sm" />
                      Upload Image for Detection
                    </div>
                    <div class="text-caption text-grey-7 q-mb-md">
                      Detect and localize multiple benthic organisms with bounding boxes
                    </div>
  
                    <!-- File Upload -->
                    <q-file
                      v-model="detectionFile"
                      filled
                      accept="image/*"
                      label="Choose underwater image"
                      @update:model-value="handleDetectionUpload"
                      class="q-mb-md"
                    >
                      <template v-slot:prepend>
                        <q-icon name="image" />
                      </template>
                      <template v-slot:append>
                        <q-icon
                          v-if="detectionFile"
                          name="close"
                          @click.stop.prevent="clearDetection"
                          class="cursor-pointer"
                        />
                      </template>
                    </q-file>
  
                    <!-- Sample Images -->
                    <div class="text-subtitle2 q-mb-sm">Or try our samples:</div>
                    <div class="row q-col-gutter-sm q-mb-lg">
                      <div
                        v-for="(sample, index) in detectionSamples"
                        :key="index"
                        class="col-6"
                      >
                        <q-img
                          :src="sample.thumbnail"
                          ratio="1"
                          class="sample-thumbnail cursor-pointer rounded-borders"
                          :class="{ 'sample-selected': selectedDetectionSample === index }"
                          @click="selectDetectionSample(index)"
                        >
                          <div class="absolute-bottom text-caption text-center">
                            {{ sample.name }}
                          </div>
                        </q-img>
                      </div>
                    </div>
  
                    <!-- Analyze Button -->
                    <q-btn
                      unelevated
                      color="primary"
                      size="lg"
                      class="full-width"
                      label="Detect Objects"
                      icon="radar"
                      :loading="isDetecting"
                      :disable="!detectionImage"
                      @click="detectObjects"
                    />
                  </q-card-section>
                </q-card>
  
                <!-- Model Performance Card -->
                <q-card flat bordered class="q-mt-md">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="insights" class="q-mr-sm" />
                      Model Performance
                    </div>
                    <q-list dense>
                      <q-item>
                        <q-item-section>
                          <q-item-label caption>Detection Accuracy</q-item-label>
                          <q-linear-progress
                            size="20px"
                            :value="0.92"
                            color="green"
                            class="q-mt-sm"
                          >
                            <div class="absolute-full flex flex-center">
                              <q-badge color="white" text-color="green" label="92.4%" />
                            </div>
                          </q-linear-progress>
                        </q-item-section>
                      </q-item>
                      <q-item>
                        <q-item-section>
                          <q-item-label caption>Training Images</q-item-label>
                          <q-item-label class="text-h6 text-primary">15,200+</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item>
                        <q-item-section>
                          <q-item-label caption>Avg Processing Time</q-item-label>
                          <q-item-label class="text-h6 text-teal">1.5s</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-card-section>
                </q-card>
              </div>
  
              <!-- Right Panel - Results -->
              <div class="col-12 col-md-7">
                <!-- Image Display with Bounding Boxes -->
                <q-card flat bordered class="results-card">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="visibility" class="q-mr-sm" />
                      Detection Results
                      <q-btn
                        v-if="hasDetections"
                        flat
                        dense
                        round
                        icon="download"
                        color="primary"
                        class="float-right"
                        @click="downloadResults"
                      >
                        <q-tooltip>Download Results</q-tooltip>
                      </q-btn>
                    </div>
  
                    <!-- Image Container -->
                    <div v-if="detectionImage" class="image-container">
                      <div class="image-wrapper">
                        <img
                          :src="detectionImageUrl"
                          alt="Analyzed underwater image"
                          class="analyzed-image"
                        />
                        <!-- Bounding Boxes Overlay -->
                        <div
                          v-for="(detection, index) in detections"
                          :key="index"
                          class="bounding-box"
                          :style="getBoundingBoxStyle(detection)"
                        >
                          <div class="box-label">
                            {{ detection.species }}
                            <span class="confidence">{{ (detection.confidence * 100).toFixed(1) }}%</span>
                          </div>
                        </div>
                      </div>
  
                      <!-- Toggle View Button -->
                      <div class="q-mt-md text-center" v-if="hasDetections">
                        <q-btn-toggle
                          v-model="viewMode"
                          toggle-color="primary"
                          :options="[
                            { label: 'With Boxes', value: 'annotated' },
                            { label: 'Original', value: 'original' }
                          ]"
                        />
                      </div>
                    </div>
  
                    <!-- Placeholder when no image -->
                    <div v-else class="placeholder-container">
                      <q-icon name="image_search" size="120px" color="grey-5" />
                      <p class="text-h6 text-grey-6 q-mt-md">
                        Upload an image to begin detection
                      </p>
                    </div>
                  </q-card-section>
                </q-card>
  
                <!-- Detection Details -->
                <q-card v-if="hasDetections" flat bordered class="q-mt-md">
                  <q-card-section>
                    <div class="text-h6 q-mb-md">
                      <q-icon name="list" class="q-mr-sm" />
                      Detected Species ({{ detections.length }})
                    </div>
  
                    <q-list bordered separator>
                      <q-item
                        v-for="(detection, index) in sortedDetections"
                        :key="index"
                        clickable
                        v-ripple
                        @click="showSpeciesInfo(detection)"
                      >
                        <q-item-section avatar>
                          <q-avatar color="primary" text-color="white">
                            {{ index + 1 }}
                          </q-avatar>
                        </q-item-section>
  
                        <q-item-section>
                          <q-item-label class="text-weight-bold">
                            {{ detection.species }}
                          </q-item-label>
                          <q-item-label caption>
                            {{ detection.scientificName }}
                          </q-item-label>
                          <q-linear-progress
                            :value="detection.confidence"
                            :color="getConfidenceColor(detection.confidence)"
                            class="q-mt-sm"
                            size="8px"
                          />
                        </q-item-section>
  
                        <q-item-section side>
                          <q-badge
                            :color="getConfidenceColor(detection.confidence)"
                            :label="`${(detection.confidence * 100).toFixed(1)}%`"
                          />
                        </q-item-section>
  
                        <q-item-section side>
                          <q-icon name="info" color="grey-6" />
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-card-section>
                </q-card>
  
                <!-- Processing Stats -->
                <q-card v-if="hasDetections" flat bordered class="q-mt-md">
                  <q-card-section>
                    <div class="row q-col-gutter-md text-center">
                      <div class="col-4">
                        <div class="stat-box">
                          <q-icon name="timer" size="sm" color="primary" />
                          <div class="text-h6 q-mt-sm">{{ processingTime }}s</div>
                          <div class="text-caption text-grey-7">Processing Time</div>
                        </div>
                      </div>
                      <div class="col-4">
                        <div class="stat-box">
                          <q-icon name="pets" size="sm" color="teal" />
                          <div class="text-h6 q-mt-sm">{{ detections.length }}</div>
                          <div class="text-caption text-grey-7">Objects Found</div>
                        </div>
                      </div>
                      <div class="col-4">
                        <div class="stat-box">
                          <q-icon name="high_quality" size="sm" color="green" />
                          <div class="text-h6 q-mt-sm">{{ avgConfidence }}%</div>
                          <div class="text-caption text-grey-7">Avg Confidence</div>
                        </div>
                      </div>
                    </div>
                  </q-card-section>
                </q-card>
              </div>
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </div>
  
      <!-- Species Info Dialog -->
      <q-dialog v-model="showSpeciesDialog">
        <q-card style="min-width: 400px">
          <q-card-section class="row items-center q-pb-none">
            <div class="text-h6">{{ selectedSpecies?.species }}</div>
            <q-space />
            <q-btn icon="close" flat round dense v-close-popup />
          </q-card-section>
  
          <q-card-section>
            <div class="text-subtitle2 text-grey-8 q-mb-xs">
              Scientific Name
            </div>
            <div class="text-body1 q-mb-md text-italic">
              {{ selectedSpecies?.scientificName }}
            </div>
  
            <div class="text-subtitle2 text-grey-8 q-mb-xs">
              Habitat
            </div>
            <div class="text-body2 q-mb-md">
              {{ selectedSpecies?.habitat }}
            </div>
  
            <div class="text-subtitle2 text-grey-8 q-mb-xs">
              Depth Range
            </div>
            <div class="text-body2 q-mb-md">
              {{ selectedSpecies?.depthRange }}
            </div>
  
            <div class="text-subtitle2 text-grey-8 q-mb-xs">
              Conservation Status
            </div>
            <q-badge
              :color="getConservationColor(selectedSpecies?.conservation)"
              :label="selectedSpecies?.conservation"
            />
          </q-card-section>
  
          <q-card-actions align="right">
            <q-btn flat label="Close" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-page>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { useQuasar } from 'quasar'
  
  const $q = useQuasar()
  
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
  
  // Sample Images for Classification
  const classificationSamples = ref([
    {
      thumbnail: '/samples/class-1.jpg',
      url: '/samples/class-1-full.jpg'
    },
    {
      thumbnail: '/samples/class-2.jpg',
      url: '/samples/class-2-full.jpg'
    },
    {
      thumbnail: '/samples/class-3.jpg',
      url: '/samples/class-3-full.jpg'
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
  
  // Mock classification results
  const mockClassificationResults = [
    { species: 'Sea Star', confidence: 0.947 },
    { species: 'Sea Urchin', confidence: 0.032 },
    { species: 'Sea Anemone', confidence: 0.012 },
    { species: 'Crab', confidence: 0.005 },
    { species: 'Coral', confidence: 0.002 },
    { species: 'Sea Cucumber', confidence: 0.001 },
    { species: 'Sponge', confidence: 0.001 }
  ]
  
  // Mock detection results
  const mockDetections = [
    {
      species: 'Sea Star',
      scientificName: 'Asterias rubens',
      confidence: 0.947,
      bbox: { x: 15, y: 20, width: 25, height: 30 },
      habitat: 'Rocky substrates, shallow waters',
      depthRange: '0-200 meters',
      conservation: 'Least Concern'
    },
    {
      species: 'Sea Urchin',
      scientificName: 'Strongylocentrotus droebachiensis',
      confidence: 0.892,
      bbox: { x: 60, y: 45, width: 18, height: 22 },
      habitat: 'Kelp forests, rocky reefs',
      depthRange: '0-1200 meters',
      conservation: 'Least Concern'
    },
    {
      species: 'Sea Anemone',
      scientificName: 'Urticina felina',
      confidence: 0.876,
      bbox: { x: 35, y: 60, width: 20, height: 25 },
      habitat: 'Attached to rocks and shells',
      depthRange: '0-100 meters',
      conservation: 'Least Concern'
    }
  ]
  
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
    isClassifying.value = true
    classificationResults.value = []
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    // Set results
    classificationResults.value = mockClassificationResults
    
    isClassifying.value = false
    
    $q.notify({
      type: 'positive',
      message: 'Classification complete!',
      position: 'top',
      timeout: 2000
    })
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
    isDetecting.value = true
    detections.value = []
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Set results
    detections.value = mockDetections
    processingTime.value = 1.5
    
    isDetecting.value = false
    
    $q.notify({
      type: 'positive',
      message: `Detection complete! Found ${detections.value.length} objects.`,
      position: 'top',
      timeout: 2000
    })
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
  .ai-demo-page {
    background: linear-gradient(180deg, #f5f9fa 0%, #e8f4f8 100%);
    min-height: 100vh;
  }
  
  .page-title {
    color: #0a4d68;
  }
  
  .container {
    max-width: 1400px;
    margin: 0 auto;
  }
  
  .upload-card,
  .results-card {
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  }
  
  .sample-thumbnail {
    border: 3px solid transparent;
    transition: all 0.3s;
  
    &:hover {
      border-color: #006994;
      transform: scale(1.05);
    }
  
    &.sample-selected {
      border-color: #006994;
      box-shadow: 0 4px 12px rgba(0, 105, 148, 0.3);
    }
  }
  
  .image-container {
    width: 100%;
  }
  
  .image-wrapper {
    position: relative;
    width: 100%;
    background: #000;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .analyzed-image {
    width: 100%;
    height: auto;
    display: block;
  }
  
  .bounding-box {
    position: absolute;
    border: 3px solid #00ff00;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
    pointer-events: none;
    transition: all 0.3s;
  }
  
  .box-label {
    position: absolute;
    top: -28px;
    left: 0;
    background: rgba(0, 255, 0, 0.9);
    color: #000;
    padding: 4px 8px;
    font-size: 12px;
    font-weight: bold;
    border-radius: 4px;
    white-space: nowrap;
  }
  
  .confidence {
    margin-left: 8px;
    opacity: 0.9;
  }
  
  .placeholder-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 400px;
    background: #f5f5f5;
    border-radius: 8px;
    border: 2px dashed #ccc;
  }
  
  .stat-box {
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
  }
  
  @media (max-width: 768px) {
    .bounding-box {
      border-width: 2px;
    }
  
    .box-label {
      font-size: 10px;
      padding: 2px 6px;
    }
  }
  </style>
  