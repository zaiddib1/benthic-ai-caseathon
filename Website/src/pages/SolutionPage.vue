<template>
    <q-page class="ai-demo-page">
      <div class="container q-pa-lg">
        <!-- Header Section -->
        <div class="text-center q-mb-xl">
          <h1 class="page-title text-h3 text-weight-bold q-mb-md">
            AI Species Identification
          </h1>
          <p class="text-body1 text-grey-7">
            Upload underwater imagery or select from our samples to see our computer vision model in action
          </p>
        </div>
  
        <div class="row q-col-gutter-lg">
          <!-- Left Panel - Upload & Controls -->
          <div class="col-12 col-md-5">
            <q-card flat bordered class="upload-card">
              <q-card-section>
                <div class="text-h6 q-mb-md">
                  <q-icon name="cloud_upload" class="q-mr-sm" />
                  Upload Image
                </div>
  
                <!-- File Upload -->
                <q-file
                  v-model="uploadedFile"
                  filled
                  accept="image/*"
                  label="Choose underwater image"
                  @update:model-value="handleFileUpload"
                  class="q-mb-md"
                >
                  <template v-slot:prepend>
                    <q-icon name="image" />
                  </template>
                  <template v-slot:append>
                    <q-icon
                      v-if="uploadedFile"
                      name="close"
                      @click.stop.prevent="clearUpload"
                      class="cursor-pointer"
                    />
                  </template>
                </q-file>
  
                <!-- Sample Images -->
                <div class="text-subtitle2 q-mb-sm">Or try our sample images:</div>
                <div class="row q-col-gutter-sm q-mb-lg">
                  <div
                    v-for="(sample, index) in sampleImages"
                    :key="index"
                    class="col-6"
                  >
                    <q-img
                      :src="sample.thumbnail"
                      ratio="1"
                      class="sample-thumbnail cursor-pointer rounded-borders"
                      :class="{ 'sample-selected': selectedSample === index }"
                      @click="selectSample(index)"
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
                  label="Analyze Image"
                  icon="psychology"
                  :loading="isAnalyzing"
                  :disable="!currentImage"
                  @click="analyzeImage"
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
                      <q-item-label caption>Overall Accuracy</q-item-label>
                      <q-linear-progress
                        size="20px"
                        :value="0.95"
                        color="green"
                        class="q-mt-sm"
                      >
                        <div class="absolute-full flex flex-center">
                          <q-badge color="white" text-color="green" label="95.2%" />
                        </div>
                      </q-linear-progress>
                    </q-item-section>
                  </q-item>
                  <q-item>
                    <q-item-section>
                      <q-item-label caption>Species Database</q-item-label>
                      <q-item-label class="text-h6 text-primary">52 Species</q-item-label>
                    </q-item-section>
                  </q-item>
                  <q-item>
                    <q-item-section>
                      <q-item-label caption>Training Dataset</q-item-label>
                      <q-item-label class="text-h6 text-teal">12,847 Images</q-item-label>
                    </q-item-section>
                  </q-item>
                  <q-item>
                    <q-item-section>
                      <q-item-label caption>Avg Processing Time</q-item-label>
                      <q-item-label class="text-h6 text-deep-orange">1.2s</q-item-label>
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
                    v-if="hasResults"
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
                <div v-if="currentImage" class="image-container">
                  <div class="image-wrapper">
                    <img
                      :src="currentImageUrl"
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
                  <div class="q-mt-md text-center">
                    <q-btn-toggle
                      v-model="viewMode"
                      toggle-color="primary"
                      :options="[
                        { label: 'Annotated', value: 'annotated' },
                        { label: 'Original', value: 'original' },
                        { label: 'Side-by-Side', value: 'side-by-side' }
                      ]"
                    />
                  </div>
                </div>
  
                <!-- Placeholder when no image -->
                <div v-else class="placeholder-container">
                  <q-icon name="image_search" size="120px" color="grey-5" />
                  <p class="text-h6 text-grey-6 q-mt-md">
                    Upload or select an image to begin analysis
                  </p>
                </div>
              </q-card-section>
            </q-card>
  
            <!-- Detection Details -->
            <q-card v-if="hasResults" flat bordered class="q-mt-md">
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
                      <q-avatar rounded size="60px">
                        <img :src="detection.thumbnail" />
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
            <q-card v-if="hasResults" flat bordered class="q-mt-md">
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
                      <div class="text-caption text-grey-7">Species Found</div>
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
            <q-img
              :src="selectedSpecies?.thumbnail"
              ratio="16/9"
              class="rounded-borders q-mb-md"
            />
            
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
  
  // State
  const uploadedFile = ref(null)
  const currentImage = ref(null)
  const currentImageUrl = ref('')
  const selectedSample = ref(null)
  const isAnalyzing = ref(false)
  const detections = ref([])
  const viewMode = ref('annotated')
  const processingTime = ref(0)
  const showSpeciesDialog = ref(false)
  const selectedSpecies = ref(null)
  
  // Sample Images Data
  const sampleImages = ref([
    {
      name: 'Coral Reef',
      thumbnail: '/samples/coral-thumb.jpg',
      url: '/samples/coral-full.jpg'
    },
    {
      name: 'Deep Sea',
      thumbnail: '/samples/deepsea-thumb.jpg',
      url: '/samples/deepsea-full.jpg'
    },
    {
      name: 'Rocky Bottom',
      thumbnail: '/samples/rocky-thumb.jpg',
      url: '/samples/rocky-full.jpg'
    },
    {
      name: 'Sandy Floor',
      thumbnail: '/samples/sandy-thumb.jpg',
      url: '/samples/sandy-full.jpg'
    }
  ])
  
  // Mock detection results for demonstration
  const mockDetections = [
    {
      species: 'Common Sea Star',
      scientificName: 'Asterias rubens',
      confidence: 0.947,
      bbox: { x: 15, y: 20, width: 25, height: 30 },
      thumbnail: '/species/seastar.jpg',
      habitat: 'Rocky substrates, shallow waters',
      depthRange: '0-200 meters',
      conservation: 'Least Concern'
    },
    {
      species: 'Sea Urchin',
      scientificName: 'Strongylocentrotus droebachiensis',
      confidence: 0.892,
      bbox: { x: 60, y: 45, width: 18, height: 22 },
      thumbnail: '/species/urchin.jpg',
      habitat: 'Kelp forests, rocky reefs',
      depthRange: '0-1200 meters',
      conservation: 'Least Concern'
    },
    {
      species: 'Anemone',
      scientificName: 'Urticina felina',
      confidence: 0.876,
      bbox: { x: 35, y: 60, width: 20, height: 25 },
      thumbnail: '/species/anemone.jpg',
      habitat: 'Attached to rocks and shells',
      depthRange: '0-100 meters',
      conservation: 'Least Concern'
    }
  ]
  
  // Computed
  const hasResults = computed(() => detections.value.length > 0)
  
  const sortedDetections = computed(() => {
    return [...detections.value].sort((a, b) => b.confidence - a.confidence)
  })
  
  const avgConfidence = computed(() => {
    if (detections.value.length === 0) return 0
    const sum = detections.value.reduce((acc, d) => acc + d.confidence, 0)
    return ((sum / detections.value.length) * 100).toFixed(1)
  })
  
  // Methods
  function handleFileUpload(file) {
    if (file) {
      selectedSample.value = null
      currentImage.value = 'uploaded'
      currentImageUrl.value = URL.createObjectURL(file)
      detections.value = []
    }
  }
  
  function clearUpload() {
    uploadedFile.value = null
    currentImage.value = null
    currentImageUrl.value = ''
    detections.value = []
  }
  
  function selectSample(index) {
    selectedSample.value = index
    uploadedFile.value = null
    currentImage.value = sampleImages.value[index].name
    currentImageUrl.value = sampleImages.value[index].url
    detections.value = []
  }
  
  async function analyzeImage() {
    isAnalyzing.value = true
    detections.value = []
    
    // Simulate API call to ML model
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Set mock results
    detections.value = mockDetections
    processingTime.value = 1.2
    
    isAnalyzing.value = false
    
    $q.notify({
      type: 'positive',
      message: `Analysis complete! Found ${detections.value.length} species.`,
      position: 'top',
      timeout: 2000
    })
  }
  
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
      image: currentImage.value,
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
    link.download = `benthic-analysis-${Date.now()}.json`
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
  