---
title: AI Image Generator
emoji: 🎨
colorFrom: red
colorTo: purple
sdk: streamlit
sdk_version: "1.28.0"
app_file: app.py
pinned: false
---

# AI Image Generator 🎨

A professional web application that generates stunning AI images from text descriptions using HuggingFace's FLUX.1-schnell model and Streamlit.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- **🎭 Multiple Art Styles**: Choose from 10 different artistic styles
  - Realistic, Cartoon, Anime, Oil Painting, Watercolor
  - 3D Render, Digital Art, Sketch, Cyberpunk, Fantasy

- **🖼️ Image History Gallery**: View and manage up to 10 generated images
  - Grid layout with thumbnails
  - Individual download buttons
  - Prompt reuse functionality
  - Session-based storage

- **⚡ Fast Generation**: Powered by FLUX.1-schnell model (10-30 seconds per image)

- **💾 Download Functionality**: Save images with timestamped filenames

- **🎨 Intuitive UI**: Clean, responsive interface with real-time feedback

- **🔧 Advanced Options**: Toggle style modifiers, view full prompts

## 🚀 Technologies Used

- **Python 3.8+**
- **Streamlit** - Web interface framework
- **HuggingFace Inference API** - AI model hosting
- **FLUX.1-schnell** - State-of-the-art image generation model
- **Pillow (PIL)** - Image processing
- **python-dotenv** - Environment management

## 📋 Prerequisites

- Python 3.8 or higher
- HuggingFace account (free)
- HuggingFace API token with Write permissions

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CodeCubCA/ai-image-generator-candyna5.git
cd ai-image-generator-candyna5
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get HuggingFace API Token

1. Go to [HuggingFace Settings - Tokens](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Name it (e.g., "image-generator")
4. Select **Write** permissions
5. Copy the token (starts with `hf_...`)

### 5. Configure Environment

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your token
HUGGINGFACE_TOKEN=hf_your_actual_token_here
```

## 🎮 Usage

### Start the Application

```bash
streamlit run app.py
```

The app will automatically open at `http://localhost:8501`

### Generate Your First Image

1. **Select a Style**: Choose from 10 artistic styles in the left panel
2. **Enter Description**: Type what you want to generate
3. **Click Generate**: Wait 10-30 seconds for AI magic
4. **Download & Save**: Images appear in the gallery below

## 💡 Example Prompts

- "A serene mountain landscape at sunset with a crystal-clear lake"
- "A cute robot reading a book in a cozy library"
- "Abstract geometric patterns in vibrant colors"
- "A futuristic city with flying cars and neon lights"
- "A watercolor painting of a peaceful garden with butterflies"

## 🎭 Available Styles

| Style | Description |
|-------|-------------|
| Realistic | Photorealistic, highly detailed, 8K quality |
| Cartoon | Animated, colorful, playful illustration |
| Anime | Manga style, vibrant colors, detailed art |
| Oil Painting | Artistic brush strokes, fine art |
| Watercolor | Soft colors, flowing paint effect |
| 3D Render | Cinematic lighting, high-quality CGI |
| Digital Art | Concept art, artstation quality |
| Sketch | Hand-drawn, detailed linework |
| Cyberpunk | Neon lights, futuristic sci-fi |
| Fantasy | Magical, ethereal, dreamlike |

## 🖼️ Image History Features

- **Auto-save**: All generated images saved to session history
- **Grid View**: Clean 3-column layout
- **Download Individual**: Each image has its own download button
- **Reuse Prompts**: Click "🔄 Reuse" to regenerate similar images
- **Clear History**: Remove all images with one click
- **Max 10 Images**: Automatic memory management

## ⚠️ Troubleshooting

### Authentication Error (401)
- Verify token is correctly copied in `.env`
- Ensure token has Write permissions
- Token may be revoked - create a new one

### Rate Limit Error (429)
- Free tier has limited requests per hour
- Wait a few minutes before retrying
- Consider HuggingFace Pro for higher limits

### Model Loading Error (503)
- Model is warming up (first use after idle period)
- Wait 1-2 minutes and try again

### Token Not Found
- Ensure `.env` file is in the project root
- Variable name must be exactly `HUGGINGFACE_TOKEN`
- Restart application after modifying `.env`

## 📊 Rate Limits

**Free Tier:**
- Limited requests per hour
- May experience slower generation during peak times

**For Production:**
- Consider [HuggingFace Pro](https://huggingface.co/pricing) for higher limits
- Better performance and reliability

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Credits

- Built with [Streamlit](https://streamlit.io/)
- Powered by [HuggingFace](https://huggingface.co/)
- FLUX.1-schnell model by [Black Forest Labs](https://huggingface.co/black-forest-labs)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/CodeCubCA/ai-image-generator-candyna5/issues)
- **HuggingFace Status**: [status.huggingface.co](https://status.huggingface.co/)

---

Made with ❤️ using AI and Streamlit
