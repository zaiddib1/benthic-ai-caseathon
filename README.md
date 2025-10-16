<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<br />
<div align="center">
  <a href="https://ai-caseathon.web.app/">
    <img src="icons/waves.svg" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">BenthicAI</h2>

  <p align="center">
    AI-Powered Image Classification and Object Detection for Underwater Marine Life
    <br />
    <a href="https://ai-caseathon.web.app/"><strong>Explore the Site »</strong></a>
    <br />
    <br />
    <a href="https://huggingface.co/spaces/dshi01/benthic_classification">ConvNeXt Demo</a>
    &middot;
    <a href="https://huggingface.co/spaces/dshi01/benthic_obj_detect">YOLO Demo</a>
    &middot;
    <a href="https://github.com/your_username/benthicai/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/your_username/benthicai/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

---

## 🧭 About The Project

BenthicAI is an interactive Quasar web application that embeds Gradio interfaces for two state-of-the-art computer vision models designed for marine conservation and education:

- 🐠 **ConvNeXt Tiny (Classification)** – Classifies single-organism underwater images into seven benthic species: *Eel, Scallop, Crab, Flatfish, Roundfish, Skate, and Whelk.*
- 🦀 **YOLOv8 (Object Detection)** – Detects and localizes multiple benthic organisms in seafloor scenes.

### Purpose
BenthicAI supports:
- **Marine Conservation** – Enables rapid, scalable underwater image analysis.
- **Biodiversity Monitoring** – Assists researchers in long-term ecosystem tracking.
- **STEM Education** – Demonstrates how AI aids marine science and outreach.

Built using Gradio Spaces and integrated into a responsive Quasar interface, it provides users with hands-on AI exploration for underwater ecosystems.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚙️ Built With

**Frontend**
- Quasar / Vue.js  
- TailwindCSS  
- [Gradio]([url](https://gradio.app/))

**Backend & Models**
- Python  
- PyTorch  
- [Hugging Face Transformers]([url](https://huggingface.co/models))  
- [Ultralytics YOLO]([url](https://github.com/ultralytics/ultralytics)) 

**Deployment**
- [Hugging Face Spaces]([url](https://huggingface.co/spaces))  
- [Firebase Hosting]([url](https://firebase.google.com/docs/hosting))  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🚀 Getting Started

To run locally:

### Prerequisites
```
node >= 18
npm >= 9
python >= 3.9
```

Install Quasar CLI:
```
npm install -g @quasar/cli
```

### Installation

1. Clone the repository  
```
git clone https://github.com/zaiddib1/benthic-ai-caseathon
cd benthic-ai-caseathon
```

2. Install dependencies  
```
npm install
```

3. Configure Gradio embed URLs in `/src/pages/ModelsPage.vue`  
```js
const classificationEmbed = "https://huggingface.co/spaces/username/convnext-benthic";
const detectionEmbed = "https://huggingface.co/spaces/username/yolo-benthic";
```

4. Run the app locally  
```
quasar dev
```

5. Build for production  
```
quasar build
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🖼️ Usage

### 🔹 ConvNeXt Classification
Upload a cropped underwater organism image (e.g., crab, eel).  
Model outputs:
- Predicted species  
- Confidence score  
- Visual overlay  

### 🔹 YOLOv8 Detection
Upload a full underwater scene.  
Model outputs:
- Bounding boxes  
- Class names  
- Confidence levels  

**Live demos:**
- [ConvNeXt Classifier](https://huggingface.co/spaces/dshi01/benthic_classification)
- [YOLO Detector](https://huggingface.co/spaces/dshi01/benthic_obj_detect)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🗺️ Roadmap

- [x] Deploy ConvNeXt classification  
- [x] Deploy YOLO detection  
- [x] Integrate Gradio embeds into Quasar  
- [ ] Add dashboard for biodiversity visualization  
- [ ] Add coral segmentation support  
- [ ] Add multilingual support (EN, KR, ES)  
- [ ] Connect to live ROV camera feeds  

See [open issues](https://github.com/dshi01/benthic-ai-caseathon/issues) for current progress.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project  
2. Create a branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)  
4. Push (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

Top contributors:  
<a href="https://github.com/your_username/benthicai/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=your_username/benthicai" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📬 Contact

**Daniel Shi**  
dshi01@wm.edu <br> 
**Zaid Dib**<br>
zmdib@wm.edu<br>
**Michael Martinez**<br>
mcmartinez@wm.edu

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🙏 Acknowledgments

- [Hugging Face Spaces](https://huggingface.co/spaces)  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- [ConvNeXt Paper](https://arxiv.org/abs/2201.03545)  
- [Gradio](https://gradio.app)  
- [Quasar Framework](https://quasar.dev)  
- Prof. Yi He  
- William and Mary AI Club  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

[contributors-shield]: https://img.shields.io/github/contributors/your_username/benthicai.svg?style=for-the-badge
[contributors-url]: https://github.com/your_username/benthicai/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/your_username/benthicai.svg?style=for-the-badge
[forks-url]: https://github.com/your_username/benthicai/network/members
[stars-shield]: https://img.shields.io/github/stars/your_username/benthicai.svg?style=for-the-badge
[stars-url]: https://github.com/your_username/benthicai/stargazers
[issues-shield]: https://img.shields.io/github/issues/your_username/benthicai.svg?style=for-the-badge
[issues-url]: https://github.com/your_username/benthicai/issues
[license-shield]: https://img.shields.io/github/license/your_username/benthicai.svg?style=for-the-badge
[license-url]: https://github.com/your_username/benthicai/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/yourprofile
