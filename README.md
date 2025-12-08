# AI Image Generator

A beautiful web application that generates images from text descriptions using AI, powered by HuggingFace's Inference API and Streamlit.

## Features

- Simple and intuitive web interface
- Generate high-quality images from text descriptions
- Powered by FLUX.1-schnell model (fast and high-quality)
- Download generated images
- Real-time error handling and user feedback
- Loading indicators during generation

## Prerequisites

- Python 3.8 or higher
- HuggingFace account (free)
- HuggingFace API token with appropriate permissions

## Installation

1. **Clone or download this project**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your HuggingFace API token**

   a. Go to [HuggingFace Settings - Tokens](https://huggingface.co/settings/tokens)

   b. Click "New token"

   c. Give it a name (e.g., "image-generator")

   d. Select **Write** permissions (or at minimum "Make calls to the serverless Inference API")

   e. Copy the generated token (starts with `hf_...`)

5. **Create your `.env` file**
   ```bash
   # Copy the example file
   copy .env.example .env    # Windows
   cp .env.example .env      # macOS/Linux
   ```

6. **Edit the `.env` file and add your token**
   ```
   HUGGINGFACE_TOKEN=hf_your_actual_token_here
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't, manually navigate to that URL

3. **Generate images**
   - Enter a description of the image you want to create
   - Click "Generate Image"
   - Wait 10-30 seconds for the AI to create your image
   - Download the image if you like it!

## Example Prompts

Try these prompts to get started:

- "A serene mountain landscape at sunset with a crystal-clear lake"
- "A cute robot reading a book in a cozy library"
- "Abstract geometric patterns in vibrant colors"
- "A futuristic city with flying cars and neon lights"
- "A watercolor painting of a peaceful garden with butterflies"

## Troubleshooting

### Authentication Error (401)
- Check that your token is correctly copied in the `.env` file
- Ensure your token has the correct permissions (Write or Inference API access)
- Token might be revoked - create a new one

### Rate Limit Error (429)
- You've exceeded the free tier limits
- Wait a few minutes before trying again
- Consider upgrading to HuggingFace Pro for higher limits

### Model Loading Error (503)
- The model is warming up (happens when not used recently)
- Wait 1-2 minutes and try again

### Token Not Found
- Make sure the `.env` file is in the same directory as `app.py`
- Check that the variable name is exactly `HUGGINGFACE_TOKEN`
- Restart the application after creating/modifying the `.env` file

## Technologies Used

- **Streamlit**: Web interface framework
- **HuggingFace Hub**: AI model inference
- **FLUX.1-schnell**: State-of-the-art image generation model
- **Python-dotenv**: Environment variable management
- **Pillow**: Image processing

## Models

The application uses `black-forest-labs/FLUX.1-schnell` by default. This model is:
- Fast (generates images in 10-30 seconds)
- High quality
- Publicly accessible on HuggingFace

### Alternative Models

You can modify the `MODEL_NAME` in `app.py` to use other models:
- `stabilityai/stable-diffusion-xl-base-1.0`
- `runwayml/stable-diffusion-v1-5`

## Rate Limits

The free HuggingFace tier has rate limits:
- Limited number of requests per hour
- May experience slower generation during peak times
- For production use, consider HuggingFace Pro

## License

This project is open source and available for personal and educational use.

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your API token is valid and has correct permissions
3. Check [HuggingFace Status](https://status.huggingface.co/) for service issues
4. Review the error messages in the application

## Credits

- Built with [Streamlit](https://streamlit.io/)
- Powered by [HuggingFace](https://huggingface.co/)
- Uses FLUX.1-schnell model by [Black Forest Labs](https://huggingface.co/black-forest-labs)
