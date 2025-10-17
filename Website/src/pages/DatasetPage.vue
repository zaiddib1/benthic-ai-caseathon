<template>
  <q-page class="dataset-page q-pb-xl">
    <!-- HERO -->
    <section class="hero">
      <div class="hero-bg">
        <div class="hero-grad"></div>
        <div class="hero-pattern"></div>
      </div>
      <div class="container hero-inner">
        <div class="badge">
          <q-icon name="inventory_2" size="18px" />
          <span>Dataset & Reproducibility</span>
        </div>
        <h1 class="title">BenthicAI Datasets</h1>
        <p class="subtitle">
          Everything you need to train, evaluate, and reproduce results for
          <strong>Image Classification</strong> and <strong>Object Detection</strong> on underwater benthic species.
        </p>

        <div class="stats">
          <div class="stat">
            <div class="stat-value">10,500</div>
            <div class="stat-label">Classification Images</div>
          </div>
          <div class="divider"></div>
          <div class="stat">
            <div class="stat-value">2,759</div>
            <div class="stat-label">Detection Images</div>
          </div>
          <div class="divider"></div>
          <div class="stat">
            <div class="stat-value">7</div>
            <div class="stat-label">Species</div>
          </div>
        </div>
      </div>
      <div class="waves"></div>
    </section>

    <div class="container q-mt-xl">

      <!-- OVERVIEW -->
      <q-card flat bordered class="glass q-pa-lg q-mb-xl">
        <div class="section-header">
          <q-icon name="science" size="36px" color="primary" />
          <div>
            <h2 class="h2 q-mb-none">Overview</h2>
            
          </div>
        </div>

        <div class="q-gutter-y-md">
          <p>
            The primary task is <strong>Image Classification</strong>: develop robust models using a
            comprehensive dataset of <strong>10,500</strong> images to identify 7 benthic species
            (Scallop, Roundfish, Crab, Whelk, Skate, Flatfish, Eel) from single-organism underwater images.
          </p>
          <p>
            As an advanced extension, we chose to tackle <strong>Object Detection</strong>: building systems
            to locate and identify multiple organisms within complex seafloor scenes using a smaller
            supplementary dataset.
          </p>
          <p class="muted">
            These AI models can accelerate benthic biodiversity assessments, support marine ecosystem monitoring,
            enable efficient analysis of large-scale underwater surveys, and provide insights into species
            distribution patterns, population dynamics, and habitat characteristics across temporal and spatial scales.
          </p>

          
        </div>
      </q-card>

      <!-- TABS FOR DATASETS -->
      <q-tabs
        v-model="tab"
        inline-label
        class="tabs glass q-mb-lg"
        active-color="primary"
        indicator-color="primary"
      >
        <q-tab name="cls" icon="category" label="Dataset 1 — Classification" />
        <q-tab name="det" icon="radar" label="Dataset 2 — Detection (YOLO)" />
        <q-tab name="repro" icon="published_with_changes" label="Reproducibility" />
      </q-tabs>

      <q-tab-panels v-model="tab" animated class="panels">

        <!-- CLASSIFICATION -->
        <q-tab-panel name="cls" class="q-pa-none">
          <q-card flat bordered class="glass q-pa-lg">

            <div class="section-header">
              <q-icon name="image" size="32px" color="primary" />
              <div>
                <h3 class="h3 q-mb-none">Dataset 1: Classification</h3>
                <div class="muted">Single-organism images with 7 class/order labels</div>
              </div>
            </div>

            <div class="q-gutter-y-lg">
              <div>
                <div class="subheader">Structure</div>
                <q-markup-table dense flat bordered class="code-wrap">
                  <tbody>
                    <tr>
                      <td class="bg-grey-2 text-weight-medium text-dark" style="width: 140px;">Folder</td>
                      <td class="text-light"><code>data/classification_dataset/</code></td>
                    </tr>
                    <tr>
                      <td class="bg-grey-2 text-weight-medium text-dark">Contents</td>
                      <td>
<pre><code>classification_dataset/
├── images/
│   ├── 2015_image001.jpg
│   ├── 2022_image002.jpg
│   └── ...
└── labels.txt</code></pre>
                      </td>
                    </tr>
                    <tr>
                      <td class="bg-grey-2 text-weight-medium text-dark">Label file</td>
                      <td>
<pre><code># labels.txt
2015_image001.jpg Scallop
2022_image002.jpg Eel
.
.
.</code></pre>
                      </td>
                    </tr>
                  </tbody>
                </q-markup-table>
              </div>

              <div>
                <div class="subheader q-mb-sm">Statistics</div>
                <q-markup-table flat bordered square>
                  <thead>
                    <tr>
                      <th>Species</th><th class="text-right">Images</th><th>Source Years</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="row in clsTable" :key="row.species">
                      <td>{{ row.species }}</td>
                      <td class="text-right">{{ row.images.toLocaleString() }}</td>
                      <td>{{ row.years }}</td>
                    </tr>
                    <tr class="text-weight-bold">
                      <td>Total</td>
                      <td class="text-right">{{ 10500..toLocaleString() }}</td>
                      <td></td>
                    </tr>
                  </tbody>
                </q-markup-table>
              </div>

              <div>
                <div class="subheader q-mb-sm">Recommended Preprocessing</div>
                <q-list bordered separator class="glass-lite">
                  <q-item v-for="(it, i) in clsPreproc" :key="i">
                    <q-item-section avatar><q-icon :name="it.icon" color="primary" /></q-item-section>
                    <q-item-section>
                      <q-item-label class="text-weight-medium">{{ it.title }}</q-item-label>
                      <q-item-label caption>{{ it.desc }}</q-item-label>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>

              <div>
  <div class="subheader q-mb-sm">Example Photos</div>
  <div class="grid">
    <q-img
      v-for="(p, i) in placeholderImgs"
      :key="i"
      :ratio="4/3"
      :src="p"
      class="grid-img cursor-pointer"
      @click="openViewer(i)"
    >
      <div class="absolute-bottom text-caption bg-black bg-opacity-50 q-pa-xs">
        Example {{ i + 1 }}: {{ classes[i] }}
      </div>
    </q-img>
  </div>
</div>

<!-- Lightbox dialog -->
<q-dialog v-model="viewerOpen" persistent maximized transition-show="slide-up" transition-hide="slide-down">
  <q-card class="bg-black">
    <div class="row items-center justify-between q-pa-sm">
      <div class="text-white text-subtitle1">{{ classes[selectedIndex] || 'Preview' }}</div>
      <q-btn flat round dense icon="close" color="white" v-close-popup />
    </div>

    <q-separator dark />

    <q-carousel
      v-model="selectedIndex"
      :arrows="true"
      :navigation="true"
      infinite
      swipeable
      animated
      class="bg-black"
      height="calc(100vh - 120px)"
    >
      <q-carousel-slide
        v-for="(p, i) in placeholderImgs"
        :key="i"
        :name="i"
        class="flex flex-center"
      >
        <q-img
          :src="p"
          fit="contain"
          style="max-height: 100%; max-width: 100%;"
          img-class="q-ma-md"
        >
          <div class="absolute-bottom text-caption bg-black bg-opacity-50 q-pa-sm">
            Example {{ i + 1 }} — {{ classes[i] || 'Sample' }}
          </div>
        </q-img>
      </q-carousel-slide>
    </q-carousel>
  </q-card>
</q-dialog>


              <div>
                <div class="subheader q-mb-sm">Baselines</div>
                <q-markup-table flat bordered square>
                  <thead>
                    <tr>
                      <th>Model</th><th>Input</th><th>Augmentations</th><th>Optimizer</th><th>Epochs</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>ConvNeXt-Tiny</td>
                      <td>224×224</td>
                      <td>RandAugment, ColorJitter, RandomResizedCrop</td>
                      <td>AdamW (lr=5e-4, wd=0.05)</td>
                      <td>50</td>
                    </tr>
                  </tbody>
                </q-markup-table>
              </div>

            </div>
          </q-card>
        </q-tab-panel>

        <!-- DETECTION -->
        <q-tab-panel name="det" class="q-pa-none">
          <q-card flat bordered class="glass q-pa-lg">

            <div class="section-header">
              <q-icon name="sensors" size="32px" color="teal" />
              <div>
                <h3 class="h3 q-mb-none">Dataset 2: Detection (YOLO format)</h3>
                <div class="muted">Multi-object scenes with bounding boxes</div>
              </div>
            </div>

            <div class="q-gutter-y-lg">
              <div>
                <div class="subheader">Structure</div>
                <q-markup-table dense flat bordered class="code-wrap">
                  <tbody>
                    <tr>
                      <td class="bg-grey-2 text-weight-medium text-dark" style="width: 140px;">Folders</td>
                      <td>
<pre><code>detection_dataset/
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/</code></pre>
                      </td>
                    </tr>
                   <tr>
  <td class="bg-grey-2 text-weight-medium text-dark">Label Format (YOLO)</td>
  <td>
    <q-markup-table flat bordered dense class="yolo-table">
      <thead>
        <tr>
          <th>class_id</th>
          <th>x_center</th>
          <th>y_center</th>
          <th>width</th>
          <th>height</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>0</code></td>
          <td><code>0.512</code></td>
          <td><code>0.458</code></td>
          <td><code>0.234</code></td>
          <td><code>0.156</code></td>
        </tr>
      </tbody>
    </q-markup-table>
    <div class="text-caption text-grey q-mt-xs">
      All values are normalized between <code>0</code> and <code>1</code>.
    </div>
  </td>
</tr>

                    <tr>
                      <td class="bg-grey-2 text-weight-medium text-dark">data.yaml</td>
                      <td>
<pre><code>names: [Crab, Eel, Flatfish, Roundfish, Scallop, Skate, Whelk]
nc: 7
train: train/images
val: val/images
test: test/images</code></pre>
                      </td>
                    </tr>
                  </tbody>
                </q-markup-table>
              </div>

              <div class="row q-col-gutter-md">
                <div class="col-12 col-md-6">
                  <div class="subheader q-mb-sm">Dataset Splits</div>
                  <q-markup-table flat bordered square>
                    <thead>
                      <tr>
                        <th>Split</th><th class="text-right">Images</th><th class="text-right">Objects</th><th class="text-right">Avg Obj/Image</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="row in detSplits" :key="row.split">
                        <td>{{ row.split }}</td>
                        <td class="text-right">{{ row.images.toLocaleString() }}</td>
                        <td class="text-right">{{ row.objects.toLocaleString() }}</td>
                        <td class="text-right">{{ row.avg.toFixed(2) }}</td>
                      </tr>
                      <tr class="text-weight-bold">
                        <td>Total</td>
                        <td class="text-right">2,759</td>
                        <td class="text-right">2,932</td>
                        <td class="text-right">1.06</td>
                      </tr>
                    </tbody>
                  </q-markup-table>
                </div>

                <div class="col-12 col-md-6">
                  <div class="subheader q-mb-sm">Class Distribution</div>
                  <q-markup-table flat bordered square>
                    <thead>
                      <tr>
                        <th>Class ID</th><th>Species</th>
                        <th class="text-right">Train</th><th class="text-right">Val</th><th class="text-right">Test</th>
                        <th class="text-right">Total</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="row in detClassDist" :key="row.id">
                        <td>{{ row.id }}</td>
                        <td>{{ row.species }}</td>
                        <td class="text-right">{{ row.train }}</td>
                        <td class="text-right">{{ row.val }}</td>
                        <td class="text-right">{{ row.test }}</td>
                        <td class="text-right">{{ row.total }}</td>
                      </tr>
                    </tbody>
                  </q-markup-table>
                </div>
              </div>

              <div>
                <div class="subheader q-mb-sm">Recommended Training (Ultralytics YOLO)</div>
<pre class="code"><code># Train
yolo task=detect mode=train model=yolo11n.pt data=detection_dataset/data.yaml \
  imgsz=640 epochs=100 batch=16 amp=True

# Validate
yolo task=detect mode=val data=detection_dataset/data.yaml model=runs/detect/train/weights/best.pt

# Predict
yolo task=detect mode=predict model=best.pt source=path/to/images/ conf=0.25 iou=0.45</code></pre>
              </div>

              <div>
                <div class="subheader q-mb-sm">Example Scenes (Placeholders)</div>
                <div class="grid">
                  <q-img v-for="(p, i) in placeholderScenes" :key="i" :ratio="16/9" :src="p" class="grid-img">
                    <div class="absolute-bottom text-caption bg-black bg-opacity-50 q-pa-xs">
                      Scene {{ i + 1 }}
                    </div>
                  </q-img>
                </div>
              </div>

            </div>
          </q-card>
        </q-tab-panel>

        <!-- REPRODUCIBILITY -->
        <q-tab-panel name="repro" class="q-pa-none">
          <q-card flat bordered class="glass q-pa-lg">

            <div class="section-header">
              <q-icon name="manage_history" size="32px" color="deep-orange" />
              <div>
                <h3 class="h3 q-mb-none">Reproducibility & Best Practices</h3>
                <div class="muted">Make your experiments exact and comparable</div>
              </div>
            </div>

            <div class="q-gutter-y-lg">
              <div>
                <div class="subheader q-mb-sm">1) Environment</div>
<pre class="code"><code># Conda (CPU)
conda create -n benthicai python=3.10 -y
conda activate benthicai
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics transformers timm pillow scikit-learn numpy pandas pyyaml

# (Optional) GPU builds of PyTorch/Ultralytics as appropriate to your CUDA</code></pre>
              </div>

              <div>
                <div class="subheader q-mb-sm">2) Determinism</div>
<pre class="code"><code>import os, random, numpy as np, torch
seed = 42
random.seed(seed); np.random.seed(seed)
torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
os.environ["PYTHONHASHSEED"] = str(seed)</code></pre>
              </div>

              <div>
                <div class="subheader q-mb-sm">3) Train/Val/Test Splits</div>
                <q-list bordered separator class="glass-lite">
                  <q-item>
                    <q-item-section avatar><q-icon name="table_chart" color="primary" /></q-item-section>
                    <q-item-section>
                      <q-item-label class="text-weight-medium">Classification</q-item-label>
                      <q-item-label caption>Use stratified splits by species (e.g., 70/15/15). Maintain year balance if temporal leakage is a concern (2015 vs 2022).</q-item-label>
                    </q-item-section>
                  </q-item>
                  <q-item>
                    <q-item-section avatar><q-icon name="table_chart" color="teal" /></q-item-section>
                    <q-item-section>
                      <q-item-label class="text-weight-medium">Detection</q-item-label>
                      <q-item-label caption>Use the provided splits (Train/Val/Test). Keep YOLO label/image pairing intact.</q-item-label>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>

              <div>
                <div class="subheader q-mb-sm">4) Evaluation</div>
                <q-markup-table flat bordered square>
                  <thead>
                    <tr><th>Task</th><th>Metrics</th><th>Notes</th></tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Classification</td>
                      <td>Top-1 Acc, Macro F1, Confusion Matrix</td>
                      <td>Report per-class precision/recall; inspect confusions between Flatfish/Roundfish.</td>
                    </tr>
                    <tr>
                      <td>Detection</td>
                      <td>mAP@0.5, mAP@0.5:0.95</td>
                      <td>Include per-class AP, PR curves; track FN on small/occluded organisms.</td>
                    </tr>
                  </tbody>
                </q-markup-table>
              </div>

              <div>
                <div class="subheader q-mb-sm">5) Saving & Sharing Results</div>
                <q-list bordered separator class="glass-lite">
                  <q-item v-for="(tip, i) in shareTips" :key="i">
                    <q-item-section avatar><q-icon :name="tip.icon" color="primary" /></q-item-section>
                    <q-item-section>
                      <q-item-label class="text-weight-medium">{{ tip.title }}</q-item-label>
                      <q-item-label caption>{{ tip.desc }}</q-item-label>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>

              <div>
                <div class="subheader q-mb-sm">6) Class Mapping (id ↔ label)</div>
                <q-markup-table flat bordered square>
                  <thead><tr><th>ID</th><th>Label</th></tr></thead>
                  <tbody>
                    <tr v-for="(lbl, id) in id2label" :key="id">
                      <td>{{ id }}</td>
                      <td>{{ lbl }}</td>
                    </tr>
                  </tbody>
                </q-markup-table>
              </div>

              <div>
                <div class="subheader q-mb-sm">7) Checksums (placeholders)</div>
                <q-markup-table flat bordered square dense>
                  <thead><tr><th>Artifact</th><th>MD5/SHA256</th></tr></thead>
                  <tbody>
                    <tr><td>classification_dataset.zip</td><td><em>to-fill</em></td></tr>
                    <tr><td>detection_dataset.zip</td><td><em>to-fill</em></td></tr>
                    <tr><td>labels.txt</td><td><em>to-fill</em></td></tr>
                    <tr><td>data.yaml</td><td><em>to-fill</em></td></tr>
                  </tbody>
                </q-markup-table>
              </div>

              <q-banner class="bg-blue-1 text-blue-10">
                Tip: Keep a <code>RUN.md</code> per experiment with the exact
                command, seed, env, git commit, and dataset hashes.
              </q-banner>
            </div>
          </q-card>
        </q-tab-panel>
      </q-tab-panels>

      <!-- DOWNLOAD / LINKS (placeholders) -->
      <q-card flat bordered class="glass q-pa-lg q-mt-xl">
        <div class="section-header">
          <q-icon name="download" size="32px" color="primary" />
          <div>
            <h3 class="h3 q-mb-none">Downloads & Links</h3>
            <div class="muted">Replace placeholders with your URLs</div>
          </div>
        </div>
        <div class="row q-col-gutter-md">
          <div class="col-12 col-md-4">
            <q-btn outline color="primary" icon="folder_zip" label="Classification Dataset (ZIP)" class="full-width" />
          </div>
          <div class="col-12 col-md-4">
            <q-btn outline color="teal" icon="folder_zip" label="Detection Dataset (ZIP)" class="full-width" />
          </div>
          <div class="col-12 col-md-4">
            <q-btn outline color="deep-orange" icon="description" label="Data Card / README" class="full-width" />
          </div>
        </div>
      </q-card>

    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const tab = ref<'cls' | 'det' | 'repro'>('cls')

const viewerOpen = ref(false)
const selectedIndex = ref(0)

function openViewer(i) {
  selectedIndex.value = i
  viewerOpen.value = true
}


const classes = [
  'Scallop', 'Roundfish', 'Crab', 'Whelk', 'Skate', 'Flatfish', 'Eel'
]

const clsTable = [
  { species: 'Scallop', images: 1500, years: '2015, 2022' },
  { species: 'Roundfish', images: 1500, years: '2015, 2022' },
  { species: 'Crab', images: 1500, years: '2015, 2022' },
  { species: 'Whelk', images: 1500, years: '2015, 2022' },
  { species: 'Skate', images: 1500, years: '2015, 2022' },
  { species: 'Flatfish', images: 1500, years: '2015, 2022' },
  { species: 'Eel', images: 1500, years: '2015, 2022' }
]

const clsPreproc = [
  { icon: 'crop', title: 'Resize & CenterCrop', desc: 'Resize to 256 on shorter side, center crop to 224×224 (or use RandomResizedCrop during train).' },
  { icon: 'contrast', title: 'Color & Illumination', desc: 'Apply ColorJitter / Histogram Equalization to handle underwater lighting variations.' },
  { icon: 'flip_camera_android', title: 'Augmentations', desc: 'Random horizontal flip, small rotations, mild blur; avoid changing organism orientation semantics if any.' },
  { icon: 'grid_on', title: 'Normalization', desc: 'Normalize to ImageNet means/std or model-specific processor (e.g., AutoImageProcessor for ConvNeXt).' }
]

// Placeholder images (you can swap with real examples/assets)
const placeholderImgs = [
'src/assets/scallop_ex1.jpg',
'src/assets/roundfish_ex1.jpg',
'src/assets/crab_ex1.jpg',
'src/assets/whelk_ex1.jpg',
'src/assets/skate_ex1.jpg',
  'src/assets/flatfish_ex1.jpg',
  
  
  'src/assets/eel_ex2.jpg',
  
  

]

const placeholderScenes = [
  'https://picsum.photos/seed/reef1/960/540',
  'https://picsum.photos/seed/reef2/960/540',
  'https://picsum.photos/seed/reef3/960/540'
]

const detSplits = [
  { split: 'Train', images: 1931, objects: 2058, avg: 1.07 },
  { split: 'Val', images: 551, objects: 575, avg: 1.04 },
  { split: 'Test', images: 277, objects: 299, avg: 1.08 }
]

const detClassDist = [
  { id: 0, species: 'Crab', train: 291, val: 89, test: 45, total: 425 },
  { id: 1, species: 'Eel', train: 275, val: 89, test: 43, total: 407 },
  { id: 2, species: 'Flatfish', train: 209, val: 62, test: 26, total: 297 },
  { id: 3, species: 'Roundfish', train: 287, val: 82, test: 38, total: 407 },
  { id: 4, species: 'Scallop', train: 419, val: 109, test: 69, total: 597 },
  { id: 5, species: 'Skate', train: 295, val: 76, test: 39, total: 410 },
  { id: 6, species: 'Whelk', train: 282, val: 68, test: 39, total: 389 }
]

const id2label = {
  0: 'Crab',
  1: 'Eel',
  2: 'Flatfish',
  3: 'Roundfish',
  4: 'Scallop',
  5: 'Skate',
  6: 'Whelk'
}


const shareTips = [
  { icon: 'commit', title: 'Record Git commit', desc: 'Pin code and config to a commit hash for exact provenance.' },
  { icon: 'lock', title: 'Freeze Environment', desc: 'Export conda env or pip requirements; note CUDA/cudnn if applicable.' },
  { icon: 'dns', title: 'Hash Artifacts', desc: 'Publish MD5/SHA256 for zips/labels so others can verify integrity.' },
  { icon: 'hub', title: 'Model Cards', desc: 'Include training details, intended use, and known limitations.' }
]
</script>

<style scoped lang="scss">
.dataset-page { background: #f7f9fb; }

/* Container */
.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }

/* HERO */
.hero { position: relative; padding: 64px 0 32px; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; }
.hero-grad { position: absolute; inset: 0; background: linear-gradient(135deg, #0575E6 0%, #021B79 100%); opacity: .9; }
.hero-pattern { position: absolute; inset: 0;
  background: url('data:image/svg+xml,<svg width="60" height="60" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="g" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1"/></pattern></defs><rect width="60" height="60" fill="url(%23g)" /></svg>');
  opacity: .5;
}
.hero-inner { position: relative; z-index: 1; text-align: center; color: #fff; }
.badge { display: inline-flex; gap:.5rem; align-items:center; background: rgba(255,255,255,.2); padding:.5rem 1rem; border-radius: 999px; border:1px solid rgba(255,255,255,.35); }
.title { font-size: clamp(2.2rem, 4.6vw, 3.2rem); margin: 1rem 0 .5rem; font-weight: 800; letter-spacing:-.02em; }
.subtitle { font-size: 1.1rem; opacity:.95; max-width: 800px; margin: 0 auto; }
.stats { display:flex; gap:1.25rem; justify-content:center; align-items:center; margin-top: 1.25rem; flex-wrap: wrap; }
.stat { text-align:center; }
.stat-value { font-size: 1.8rem; font-weight: 800; line-height: 1; }
.stat-label { opacity:.95; }
.divider { width:1px; height:32px; background: rgba(255,255,255,.4); }
.waves { position:absolute; left:0; right:0; bottom:0; height:60px; background: linear-gradient(180deg, rgba(255,255,255,.0), rgba(255,255,255,1)); }

/* Cards & Sections */
.glass { background: rgba(255,255,255,.98); border-radius: 18px; box-shadow: 0 10px 36px rgba(2,27,121,0.07); }
.glass-lite { background: rgba(248,250,252, .6); border-radius: 12px; }
.section-header { display:flex; gap:12px; align-items:center; margin-bottom: 12px; }
.h2 { font-size: 1.6rem; font-weight: 800; }
.h3 { font-size: 1.3rem; font-weight: 800; }
.muted { color:#6b7280; }

.chip-row { display:flex; gap:.5rem; flex-wrap: wrap; margin-top: .5rem; }
/* ---- YOLO label format table ---- */
.yolo-table {
  width: 100%;
  border-radius: 8px;
  background: #0f172a; /* dark background for readability */
  color: #e5e7eb;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 0.9rem;
  border: 1px solid rgba(255, 255, 255, 0.1);

  th {
    background: #1e293b;
    color: #f8fafc;
    font-weight: 600;
    text-align: center;
    padding: 6px 10px;
  }

  td {
    text-align: center;
    padding: 6px 10px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
  }

  code {
    background: transparent;
    color: #93c5fd; /* light blue accent for values */
  }
}

/* Tabs */
.tabs { background: #fff; border-radius: 14px; padding: .25rem .5rem; box-shadow: 0 4px 20px rgba(0,0,0,.06); }
.panels { background: transparent; }

/* Code blocks */
.code, .code-wrap { background: #0b1020; color: #e6f1ff; border-radius: 10px; overflow: auto; }
.code { padding: 12px; }
.code-wrap pre { margin: 0; padding: 12px; color: #e6f1ff; }

/* Grids */
.grid { display:grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
.grid-img { border-radius: 12px; overflow: hidden; }

/* Responsive */
@media (max-width: 768px) {
  .stats { gap:.75rem; }
  .divider { display:none; }
}
</style>
