<template>
  <q-page class="dataset-page">
    <!-- HERO -->
    <section class="hero-section">
      <div class="hero-background">
        <div class="hero-pattern"></div>
        <div class="hero-gradient"></div>
      </div>
      <div class="hero-content">
        <div class="container">
          <div class="hero-inner">
            <div class="hero-badge">
              <q-icon name="inventory_2" size="18px" />
              <span>Dataset & Reproducibility</span>
            </div>
            <h1 class="hero-title">
              BenthicAI Datasets
            </h1>
            <p class="hero-subtitle">
              Everything you need to train, evaluate, and reproduce results for
              <strong>Image Classification</strong> and <strong>Object Detection</strong> on underwater benthic species.
            </p>

            <div class="hero-stats">
              <div class="stat-pill">
                <q-icon name="image" size="20px" />
                <span>10,500 Classification Images</span>
              </div>
              <div class="stat-pill">
                <q-icon name="radar" size="20px" />
                <span>2,759 Detection Images</span>
              </div>
              <div class="stat-pill">
                <q-icon name="pets" size="20px" />
                <span>7 Species</span>
              </div>
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

    <div class="content-wrapper">
      <div class="container">

        <!-- OVERVIEW -->
        <q-card flat bordered class="overview-card q-mb-xl">
          <div class="card-header">
            <div class="icon-wrapper gradient-blue">
              <q-icon name="science" size="32px" color="white" />
            </div>
            <div>
              <h2 class="card-title">Overview</h2>
              <div class="card-subtitle">Comprehensive benthic species datasets</div>
            </div>
          </div>

          <div class="card-content">
            <p class="overview-text">
              The primary task is <strong>Image Classification</strong>: develop robust models using a
              comprehensive dataset of <strong>10,500</strong> images to identify 7 benthic species
              (Scallop, Roundfish, Crab, Whelk, Skate, Flatfish, Eel) from single-organism underwater images.
            </p>
            <p class="overview-text">
              As an advanced extension, we chose to tackle <strong>Object Detection</strong>: building systems
              to locate and identify multiple organisms within complex seafloor scenes using a smaller
              supplementary dataset.
            </p>
            <p class="overview-text muted">
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
          class="dataset-tabs q-mb-lg"
          active-color="primary"
          indicator-color="primary"
        >
          <q-tab name="cls" icon="category" label="Dataset 1 — Classification" />
          <q-tab name="det" icon="radar" label="Dataset 2 — Detection (YOLO)" />
          <q-tab name="repro" icon="published_with_changes" label="Reproducibility" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="tab-panels">

          <!-- CLASSIFICATION -->
          <q-tab-panel name="cls" class="q-pa-none">
            <q-card flat bordered class="content-card">

              <div class="card-header">
                <div class="icon-wrapper gradient-blue">
                  <q-icon name="image" size="28px" color="white" />
                </div>
                <div>
                  <h3 class="card-title">Dataset 1: Classification</h3>
                  <div class="card-subtitle">Single-organism images with 7 class/order labels</div>
                </div>
              </div>

              <div class="card-content">
                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="folder" size="20px" color="primary" />
                    <span>Structure</span>
                  </div>
                  <q-markup-table dense flat bordered class="data-table">
                    <tbody>
                      <tr>
                        <td class="table-label">Folder</td>
                        <td class="table-value"><code>data/classification_dataset/</code></td>
                      </tr>
                      <tr>
                        <td class="table-label">Contents</td>
                        <td class="table-value">
<pre><code>classification_dataset/
├── images/
│   ├── 2015_image001.jpg
│   ├── 2022_image002.jpg
│   └── ...
└── labels.txt</code></pre>
                        </td>
                      </tr>
                      <tr>
                        <td class="table-label">Label file</td>
                        <td class="table-value">
<pre><code># labels.txt
2015_image001.jpg Scallop
2022_image002.jpg Eel
...</code></pre>
                        </td>
                      </tr>
                    </tbody>
                  </q-markup-table>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="bar_chart" size="20px" color="primary" />
                    <span>Statistics</span>
                  </div>
                  <q-markup-table flat bordered square class="stats-table">
                    <thead>
                      <tr>
                        <th>Species</th>
                        <th class="text-right">Images</th>
                        <th>Source Years</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="row in clsTable" :key="row.species">
                        <td class="species-cell">{{ row.species }}</td>
                        <td class="text-right number-cell">{{ row.images.toLocaleString() }}</td>
                        <td class="year-cell">{{ row.years }}</td>
                      </tr>
                      <tr class="total-row">
                        <td class="species-cell">Total</td>
                        <td class="text-right number-cell">{{ (10500).toLocaleString() }}</td>
                        <td></td>
                      </tr>
                    </tbody>
                  </q-markup-table>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="auto_fix_high" size="20px" color="primary" />
                    <span>Recommended Preprocessing</span>
                  </div>
                  <q-list bordered separator class="feature-list">
                    <q-item v-for="(it, i) in clsPreproc" :key="i" class="feature-item">
                      <q-item-section avatar>
                        <div class="feature-icon-bg gradient-blue-soft">
                          <q-icon :name="it.icon" color="primary" size="24px" />
                        </div>
                      </q-item-section>
                      <q-item-section>
                        <q-item-label class="feature-item-title">{{ it.title }}</q-item-label>
                        <q-item-label caption class="feature-item-desc">{{ it.desc }}</q-item-label>
                      </q-item-section>
                    </q-item>
                  </q-list>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="photo_library" size="20px" color="primary" />
                    <span>Example Photos</span>
                  </div>
                  <div class="image-grid">
                    <q-img
                      v-for="(p, i) in placeholderImgs"
                      :key="i"
                      :ratio="4/3"
                      :src="p"
                      class="grid-image cursor-pointer"
                      @click="openViewer(i)"
                    >
                      <div class="image-overlay">
                        <div class="image-label">{{ classes[i] }}</div>
                      </div>
                    </q-img>
                  </div>
                </div>

                <!-- Lightbox dialog -->
                <q-dialog v-model="viewerOpen" persistent maximized transition-show="slide-up" transition-hide="slide-down">
                  <q-card class="viewer-card">
                    <div class="viewer-header">
                      <div class="viewer-title">{{ classes[selectedIndex] || 'Preview' }}</div>
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
                      class="viewer-carousel"
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
                          <div class="viewer-image-label">
                            Example {{ i + 1 }} — {{ classes[i] || 'Sample' }}
                          </div>
                        </q-img>
                      </q-carousel-slide>
                    </q-carousel>
                  </q-card>
                </q-dialog>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="analytics" size="20px" color="primary" />
                    <span>Baselines</span>
                  </div>
                  <q-markup-table flat bordered square class="baseline-table">
                    <thead>
                      <tr>
                        <th>Model</th>
                        <th>Input Size</th>
                        <th>Augmentations</th>
                        <th>Optimizer</th>
                        <th>Epochs</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><strong>ConvNeXt-Tiny</strong></td>
                        <td><code>224×224</code></td>
                        <td>RandAugment, ColorJitter, RandomResizedCrop</td>
                        <td><code>AdamW</code> (lr=5e-4, wd=0.05)</td>
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
            <q-card flat bordered class="content-card">

              <div class="card-header">
                <div class="icon-wrapper gradient-teal">
                  <q-icon name="sensors" size="28px" color="white" />
                </div>
                <div>
                  <h3 class="card-title">Dataset 2: Detection (YOLO format)</h3>
                  <div class="card-subtitle">Multi-object scenes with bounding boxes</div>
                </div>
              </div>

              <div class="card-content">
                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="folder" size="20px" color="teal" />
                    <span>Structure</span>
                  </div>
                  <q-markup-table dense flat bordered class="data-table">
                    <tbody>
                      <tr>
                        <td class="table-label">Folders</td>
                        <td class="table-value">
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
                        <td class="table-label">Label Format (YOLO)</td>
                        <td class="table-value">
                          <q-markup-table flat bordered dense class="yolo-format-table">
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
                          <div class="format-note">
                            <q-icon name="info" size="16px" color="grey-7" />
                            All values are normalized between <code>0</code> and <code>1</code>.
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <td class="table-label">data.yaml</td>
                        <td class="table-value">
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

                <div class="two-column-grid">
                  <div class="section-block">
                    <div class="subheader">
                      <q-icon name="splitscreen" size="20px" color="teal" />
                      <span>Dataset Splits</span>
                    </div>
                    <q-markup-table flat bordered square class="stats-table">
                      <thead>
                        <tr>
                          <th>Split</th>
                          <th class="text-right">Images</th>
                          <th class="text-right">Objects</th>
                          <th class="text-right">Avg Obj/Image</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="row in detSplits" :key="row.split">
                          <td class="species-cell">{{ row.split }}</td>
                          <td class="text-right number-cell">{{ row.images.toLocaleString() }}</td>
                          <td class="text-right number-cell">{{ row.objects.toLocaleString() }}</td>
                          <td class="text-right number-cell">{{ row.avg.toFixed(2) }}</td>
                        </tr>
                        <tr class="total-row">
                          <td class="species-cell">Total</td>
                          <td class="text-right number-cell">2,759</td>
                          <td class="text-right number-cell">2,932</td>
                          <td class="text-right number-cell">1.06</td>
                        </tr>
                      </tbody>
                    </q-markup-table>
                  </div>

                  <div class="section-block">
                    <div class="subheader">
                      <q-icon name="pie_chart" size="20px" color="teal" />
                      <span>Class Distribution</span>
                    </div>
                    <q-markup-table flat bordered square class="stats-table compact-table">
                      <thead>
                        <tr>
                          <th>ID</th>
                          <th>Species</th>
                          <th class="text-right">Train</th>
                          <th class="text-right">Val</th>
                          <th class="text-right">Test</th>
                          <th class="text-right">Total</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="row in detClassDist" :key="row.id">
                          <td class="id-cell">{{ row.id }}</td>
                          <td class="species-cell">{{ row.species }}</td>
                          <td class="text-right number-cell small">{{ row.train }}</td>
                          <td class="text-right number-cell small">{{ row.val }}</td>
                          <td class="text-right number-cell small">{{ row.test }}</td>
                          <td class="text-right number-cell small total">{{ row.total }}</td>
                        </tr>
                      </tbody>
                    </q-markup-table>
                  </div>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="code" size="20px" color="teal" />
                    <span>Recommended Training (Ultralytics YOLO)</span>
                  </div>
                  <div class="code-block">
<pre><code># Train
yolo task=detect mode=train model=yolo11n.pt data=detection_dataset/data.yaml \
  imgsz=640 epochs=100 batch=16 amp=True

# Validate
yolo task=detect mode=val data=detection_dataset/data.yaml model=runs/detect/train/weights/best.pt

# Predict
yolo task=detect mode=predict model=best.pt source=path/to/images/ conf=0.25 iou=0.45</code></pre>
                  </div>
                </div>
              </div>
            </q-card>
          </q-tab-panel>

          <!-- REPRODUCIBILITY -->
          <q-tab-panel name="repro" class="q-pa-none">
            <q-card flat bordered class="content-card">

              <div class="card-header">
                <div class="icon-wrapper gradient-orange">
                  <q-icon name="manage_history" size="28px" color="white" />
                </div>
                <div>
                  <h3 class="card-title">Reproducibility & Best Practices</h3>
                  <div class="card-subtitle">Make your experiments exact and comparable</div>
                </div>
              </div>

              <div class="card-content">
                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="cloud" size="20px" color="deep-orange" />
                    <span>1) Environment Setup</span>
                  </div>
                  <div class="code-block">
<pre><code># Conda (CPU)
conda create -n benthicai python=3.10 -y
conda activate benthicai
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics transformers timm pillow scikit-learn numpy pandas pyyaml

# (Optional) GPU builds of PyTorch/Ultralytics as appropriate to your CUDA</code></pre>
                  </div>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="lock" size="20px" color="deep-orange" />
                    <span>2) Determinism & Seed Setting</span>
                  </div>
                  <div class="code-block">
<pre><code>import os, random, numpy as np, torch
seed = 42
random.seed(seed); np.random.seed(seed)
torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
os.environ["PYTHONHASHSEED"] = str(seed)</code></pre>
                  </div>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="call_split" size="20px" color="deep-orange" />
                    <span>3) Train/Val/Test Splits</span>
                  </div>
                  <q-list bordered separator class="feature-list">
                    <q-item class="feature-item">
                      <q-item-section avatar>
                        <div class="feature-icon-bg gradient-blue-soft">
                          <q-icon name="category" color="primary" size="24px" />
                        </div>
                      </q-item-section>
                      <q-item-section>
                        <q-item-label class="feature-item-title">Classification Dataset</q-item-label>
                        <q-item-label caption class="feature-item-desc">Use stratified splits by species (e.g., 70/15/15). Maintain year balance if temporal leakage is a concern (2015 vs 2022).</q-item-label>
                      </q-item-section>
                    </q-item>
                    <q-item class="feature-item">
                      <q-item-section avatar>
                        <div class="feature-icon-bg gradient-teal-soft">
                          <q-icon name="radar" color="teal" size="24px" />
                        </div>
                      </q-item-section>
                      <q-item-section>
                        <q-item-label class="feature-item-title">Detection Dataset</q-item-label>
                        <q-item-label caption class="feature-item-desc">Use the provided splits (Train/Val/Test). Keep YOLO label/image pairing intact.</q-item-label>
                      </q-item-section>
                    </q-item>
                  </q-list>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="assessment" size="20px" color="deep-orange" />
                    <span>4) Evaluation Metrics</span>
                  </div>
                  <q-markup-table flat bordered square class="metrics-table">
                    <thead>
                      <tr>
                        <th>Task</th>
                        <th>Metrics</th>
                        <th>Notes</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td class="task-cell"><strong>Classification</strong></td>
                        <td class="metric-cell">Top-1 Acc, Macro F1, Confusion Matrix</td>
                        <td class="notes-cell">Report per-class precision/recall; inspect confusions between Flatfish/Roundfish.</td>
                      </tr>
                      <tr>
                        <td class="task-cell"><strong>Detection</strong></td>
                        <td class="metric-cell">mAP@0.5, mAP@0.5:0.95</td>
                        <td class="notes-cell">Include per-class AP, PR curves; track FN on small/occluded organisms.</td>
                      </tr>
                    </tbody>
                  </q-markup-table>
                </div>

                <div class="section-block">
                  <div class="subheader">
                    <q-icon name="save" size="20px" color="deep-orange" />
                    <span>5) Saving & Sharing Results</span>
                  </div>
                  <q-list bordered separator class="feature-list">
                    <q-item v-for="(tip, i) in shareTips" :key="i" class="feature-item">
                      <q-item-section avatar>
                        <div class="feature-icon-bg gradient-orange-soft">
                          <q-icon :name="tip.icon" color="deep-orange" size="24px" />
                        </div>
                      </q-item-section>
                      <q-item-section>
                        <q-item-label class="feature-item-title">{{ tip.title }}</q-item-label>
                        <q-item-label caption class="feature-item-desc">{{ tip.desc }}</q-item-label>
                      </q-item-section>
                    </q-item>
                  </q-list>
                </div>

                <q-banner class="info-banner">
                  <template v-slot:avatar>
                    <q-icon name="tips_and_updates" color="primary" size="28px" />
                  </template>
                  <div class="banner-content">
                    <strong>Pro Tip:</strong> Keep a <code>RUN.md</code> per experiment with the exact
                    command, seed, environment, git commit, and dataset hashes for full reproducibility.
                  </div>
                </q-banner>
              </div>
            </q-card>
          </q-tab-panel>
        </q-tab-panels>

        <!-- DOWNLOAD / LINKS -->
        <q-card flat bordered class="download-card q-mt-xl">
          <div class="card-header">
            <div class="icon-wrapper gradient-purple">
              <q-icon name="download" size="28px" color="white" />
            </div>
            <div>
              <h3 class="card-title">Downloads & Resources</h3>
              <div class="card-subtitle">Access the complete datasets on Google Drive</div>
            </div>
          </div>
          <div class="card-content">
            <div class="download-grid">
              <!-- Classification Dataset -->
              <q-btn 
                unelevated 
                size="lg"
                color="primary" 
                icon="folder_zip" 
                label="Classification Dataset" 
                class="download-btn"
                href="https://drive.google.com/drive/folders/1n9VzTJuUgD0fug8VcoseVcmRoHNLM_Uz?usp=drive_link"
                target="_blank"
                type="a"
              >
                <q-badge color="white" text-color="primary" floating>10,500</q-badge>
                <q-tooltip>10,500 images with 7 species labels</q-tooltip>
              </q-btn>
              
              <!-- Detection Dataset -->
              <q-btn 
                unelevated 
                size="lg"
                color="teal" 
                icon="radar" 
                label="Detection Dataset (YOLO)" 
                class="download-btn"
                href="https://drive.google.com/drive/folders/1tMz4YWS-hQpafpMSx7RxNkl4EwYHpsY0?usp=drive_link"
                target="_blank"
                type="a"
              >
                <q-badge color="white" text-color="teal" floating>2,759</q-badge>
                <q-tooltip>2,759 images with YOLO format annotations</q-tooltip>
              </q-btn>
              
              <!-- Documentation -->
              <q-btn 
                unelevated 
                size="lg"
                color="deep-orange" 
                icon="description" 
                label="Documentation" 
                class="download-btn"
                href="https://drive.google.com/file/d/1iJ4snyyMEcc8InoquA4BmUNkriAwxxey/view?usp=drive_link"
                target="_blank"
                type="a"
              >
                <q-tooltip>README, data cards, and citation info</q-tooltip>
              </q-btn>
            </div>
            
            <!-- Info Banner -->
            <div class="download-info q-mt-lg">
              <q-icon name="info" color="primary" size="24px" />
              <div class="info-text">
                <strong>How to download:</strong> Click a dataset button above to open the Google Drive folder. 
                Then use the three-dot menu (⋮) at the top right and select "Download" to get all files as a ZIP archive.
              </div>
            </div>

            <!-- Download Instructions Expandable -->
            <q-expansion-item
              icon="terminal"
              label="Command Line Download (Advanced)"
              class="q-mt-md command-expansion"
            >
              <q-card flat class="q-pa-md bg-grey-1">
                <div class="q-mb-md">
                  <div class="method-header">
                    <q-icon name="code" color="primary" size="20px" />
                    <span class="text-weight-bold">Using gdown</span>
                  </div>
                  <div class="code-block q-mt-sm">
<pre><code># Install gdown
pip install gdown

# Download Classification Dataset
gdown --folder https://drive.google.com/drive/folders/1n9VzTJuUgD0fug8VcoseVcmRoHNLM_Uz

# Download Detection Dataset
gdown --folder https://drive.google.com/drive/folders/1tMz4YWS-hQpafpMSx7RxNkl4EwYHpsY0</code></pre>
                  </div>
                </div>

                <q-separator class="q-my-md" />

                <div>
                  <div class="method-header">
                    <q-icon name="integration_instructions" color="teal" size="20px" />
                    <span class="text-weight-bold">Python Script</span>
                  </div>
                  <div class="code-block q-mt-sm">
<pre><code>import gdown

# Download Classification Dataset
cls_url = 'https://drive.google.com/drive/folders/1n9VzTJuUgD0fug8VcoseVcmRoHNLM_Uz'
gdown.download_folder(cls_url, output='classification_dataset/', quiet=False)

# Download Detection Dataset
det_url = 'https://drive.google.com/drive/folders/1tMz4YWS-hQpafpMSx7RxNkl4EwYHpsY0'
gdown.download_folder(det_url, output='detection_dataset/', quiet=False)</code></pre>
                  </div>
                </div>
              </q-card>
            </q-expansion-item>
          </div>
        </q-card>

      </div>
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

const placeholderImgs = [
  'src/assets/scallop_ex1.jpg',
  'src/assets/roundfish_ex1.jpg',
  'src/assets/crab_ex1.jpg',
  'src/assets/whelk_ex1.jpg',
  'src/assets/skate_ex1.jpg',
  'src/assets/flatfish_ex1.jpg',
  'src/assets/eel_ex2.jpg',
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

const shareTips = [
  { icon: 'commit', title: 'Record Git commit', desc: 'Pin code and config to a commit hash for exact provenance.' },
  { icon: 'lock', title: 'Freeze Environment', desc: 'Export conda env or pip requirements; note CUDA/cudnn if applicable.' },
  { icon: 'dns', title: 'Hash Artifacts', desc: 'Publish MD5/SHA256 for zips/labels so others can verify integrity.' },
  { icon: 'hub', title: 'Model Cards', desc: 'Include training details, intended use, and known limitations.' }
]
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
$gradient-purple: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
$gradient-ocean: linear-gradient(135deg, #0575E6 0%, #021B79 100%);

.dataset-page {
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
  
  @media (max-width: 768px) {
    min-height: 450px;
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
  background: $gradient-ocean;
}

.hero-content {
  position: relative;
  z-index: 1;
  width: 100%;
  padding: 3rem 0;
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
  margin-bottom: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: fadeInDown 0.8s ease-out;
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  font-weight: 800;
  color: white;
  line-height: 1.2;
  margin: 0 0 1rem 0;
  letter-spacing: -0.02em;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.hero-subtitle {
  font-size: clamp(1rem, 2vw, 1.25rem);
  color: rgba(255, 255, 255, 0.95);
  max-width: 700px;
  margin: 0 auto 2rem;
  line-height: 1.6;
  font-weight: 400;
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
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

// WAVES (matching HomePage)
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

// CONTENT WRAPPER
.content-wrapper {
  padding: 4rem 0;
  background: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  
  @media (max-width: 768px) {
    padding: 0 1.5rem;
  }
}

// CARDS
.overview-card,
.content-card,
.download-card {
  background: white;
  border-radius: 24px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  
  &:hover {
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
  }
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 2rem;
  border-bottom: 1px solid #f0f0f0;
}

.icon-wrapper {
  width: 64px;
  height: 64px;
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
    background: $gradient-purple;
  }
}

.card-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.01em;
}

.card-subtitle {
  font-size: 0.9375rem;
  color: #666;
  margin-top: 0.25rem;
}

.card-content {
  padding: 2rem;
}

// SECTION BLOCKS
.section-block {
  margin-bottom: 2.5rem;
  
  &:last-child {
    margin-bottom: 0;
  }
}

.subheader {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  font-size: 1.125rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #f0f0f0;
}

.overview-text {
  font-size: 1.0625rem;
  line-height: 1.8;
  color: #333;
  margin-bottom: 1.25rem;
  
  &.muted {
    color: #666;
    font-size: 1rem;
  }
  
  &:last-child {
    margin-bottom: 0;
  }
  
  strong {
    color: #1a1a1a;
    font-weight: 600;
  }
}

// TABS
.dataset-tabs {
  background: white;
  border-radius: 16px;
  padding: 0.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 1px solid #e0e0e0;
}

.tab-panels {
  background: transparent;
}

// TABLES
.data-table,
.stats-table,
.baseline-table,
.metrics-table,
.mapping-table,
.checksum-table {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  
  thead tr {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    
    th {
      font-weight: 700;
      color: #1a1a1a;
      padding: 1rem;
      font-size: 0.9375rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      border-bottom: 2px solid #dee2e6;
    }
  }
  
  tbody tr {
    transition: background 0.2s;
    
    &:hover {
      background: #f8f9fa;
    }
    
    td {
      padding: 0.875rem 1rem;
      color: #333;
      border-bottom: 1px solid #f0f0f0;
    }
    
    &:last-child td {
      border-bottom: none;
    }
  }
}

.table-label {
  background: #f8f9fa;
  font-weight: 600;
  color: #1a1a1a;
  width: 160px;
  vertical-align: top;
}

.table-value {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  
  code {
    background: #f1f3f5;
    padding: 0.125rem 0.375rem;
    border-radius: 4px;
    color: #0575E6;
    font-size: 0.875rem;
  }
  
  pre {
    margin: 0;
    padding: 0.75rem;
    background: #0b1020;
    color: #e6f1ff;
    border-radius: 8px;
    overflow-x: auto;
    
    code {
      background: transparent;
      padding: 0;
      color: #e6f1ff;
    }
  }
}

.species-cell {
  font-weight: 600;
  color: #1a1a1a;
}

.number-cell {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-weight: 600;
  
  &.small {
    font-size: 0.9375rem;
  }
  
  &.total {
    color: $primary;
  }
}

.year-cell {
  color: #666;
  font-size: 0.9375rem;
}

.id-cell {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-weight: 600;
  color: #666;
  text-align: center;
}

.total-row {
  background: #f8f9fa;
  font-weight: 700;
  
  td {
    border-top: 2px solid #dee2e6;
  }
}

.task-cell {
  font-weight: 600;
  color: #1a1a1a;
}

.metric-cell {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.9375rem;
  color: #333;
}

.notes-cell {
  color: #666;
  font-size: 0.9375rem;
  line-height: 1.6;
}

// YOLO FORMAT TABLE
.yolo-format-table {
  background: #0b1020;
  color: #e6f1ff;
  border-radius: 8px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.875rem;
  margin-top: 0.5rem;
  
  thead tr {
    background: #1e293b;
    
    th {
      color: #f8fafc;
      font-weight: 600;
      text-align: center;
      padding: 0.625rem 0.875rem;
      text-transform: none;
      letter-spacing: normal;
    }
  }
  
  tbody tr {
    &:hover {
      background: rgba(255, 255, 255, 0.05);
    }
    
    td {
      text-align: center;
      padding: 0.625rem 0.875rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      
      code {
        color: #93c5fd;
        background: transparent;
        padding: 0;
      }
    }
  }
}

.format-note {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.75rem;
  font-size: 0.875rem;
  color: #666;
  
  code {
    background: #f1f3f5;
    padding: 0.125rem 0.375rem;
    border-radius: 4px;
    color: #0575E6;
  }
}

// CODE BLOCKS
.code-block {
  background: #0b1020;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  
  pre {
    margin: 0;
    padding: 1.25rem;
    overflow-x: auto;
    
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      color: #e6f1ff;
      font-size: 0.9375rem;
      line-height: 1.6;
    }
  }
}

// FEATURE LIST
.feature-list {
  border-radius: 12px;
  overflow: hidden;
  background: white;
}

.feature-item {
  padding: 1.25rem;
  transition: background 0.2s;
  
  &:hover {
    background: #f8f9fa;
  }
}

.feature-icon-bg {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  
  &.gradient-blue-soft {
    background: rgba(102, 126, 234, 0.1);
  }
  
  &.gradient-teal-soft {
    background: rgba(0, 137, 123, 0.1);
  }
  
  &.gradient-orange-soft {
    background: rgba(255, 111, 0, 0.1);
  }
}

.feature-item-title {
  font-size: 1.0625rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.25rem;
}

.feature-item-desc {
  font-size: 0.9375rem;
  color: #666;
  line-height: 1.6;
}

// IMAGE GRID
.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  
  &.scene-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
}

.grid-image {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.15);
  }
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
  padding: 1rem;
}

.image-label {
  color: white;
  font-weight: 600;
  font-size: 0.9375rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

// VIEWER (LIGHTBOX)
.viewer-card {
  background: #000;
}

.viewer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
}

.viewer-title {
  color: white;
  font-size: 1.125rem;
  font-weight: 600;
}

.viewer-carousel {
  background: #000;
}

.viewer-image-label {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(8px);
  color: white;
  padding: 0.75rem 1rem;
  font-size: 0.9375rem;
}

// TWO COLUMN GRID
.two-column-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  
  @media (max-width: 968px) {
    grid-template-columns: 1fr;
  }
}

.compact-table {
  font-size: 0.9375rem;
  
  th, td {
    padding: 0.625rem 0.875rem;
  }
}

// INFO BANNER
.info-banner {
  background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
  border-radius: 12px;
  padding: 1.25rem;
  border: 1px solid #90caf9;
  
  .banner-content {
    font-size: 1rem;
    color: #1a1a1a;
    line-height: 1.6;
    
    strong {
      font-weight: 700;
    }
    
    code {
      background: rgba(255, 255, 255, 0.6);
      padding: 0.125rem 0.375rem;
      border-radius: 4px;
      color: #0575E6;
      font-weight: 600;
    }
  }
}

// DOWNLOAD SECTION
.download-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.download-btn {
  height: 64px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: none;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  
  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  }
  
  .q-badge {
    font-weight: 700;
    font-size: 0.75rem;
  }
}

.download-info {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.25rem;
  background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
  border-radius: 12px;
  border: 1px solid #bbdefb;
  
  .info-text {
    flex: 1;
    font-size: 0.9375rem;
    line-height: 1.6;
    color: #333;
    
    strong {
      font-weight: 700;
      color: #1a1a1a;
    }
  }
}

.command-expansion {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
  
  :deep(.q-item) {
    background: white;
    
    &:hover {
      background: #f8f9fa;
    }
  }
}

.method-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  margin-bottom: 0.5rem;
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

// RESPONSIVE
@media (max-width: 768px) {
  .hero-stats {
    gap: 0.75rem;
  }
  
  .image-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 0.75rem;
  }
  
  .card-header {
    padding: 1.5rem;
  }
  
  .card-content {
    padding: 1.5rem;
  }
  
  .icon-wrapper {
    width: 56px;
    height: 56px;
  }
}
</style>
