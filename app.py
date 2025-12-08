import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Configuration
MODEL_NAME = "black-forest-labs/FLUX.1-schnell"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Page configuration
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #FF5252;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎨 AI Image Generator")
st.markdown("Generate stunning images from text descriptions using AI")

# Check if API token is configured
if not HUGGINGFACE_TOKEN:
    st.error("⚠️ HuggingFace API token not found!")
    st.info("""
    **Setup Instructions:**
    1. Go to https://huggingface.co/settings/tokens
    2. Create a new token with **Write** permissions
    3. Create a `.env` file in the project directory
    4. Add: `HUGGINGFACE_TOKEN=your_token_here`
    5. Restart the application
    """)
    st.stop()

# Initialize the HuggingFace Inference Client
@st.cache_resource
def get_client():
    """Initialize and cache the InferenceClient"""
    try:
        return InferenceClient(token=HUGGINGFACE_TOKEN)
    except Exception as e:
        st.error(f"Failed to initialize HuggingFace client: {str(e)}")
        return None

client = get_client()

# Main interface
st.markdown("---")

# Style selection
st.subheader("🎭 Choose Image Style")
style_options = {
    "Realistic": "photorealistic, highly detailed, 8k, professional photography",
    "Cartoon": "cartoon style, animated, colorful, fun, playful illustration",
    "Anime": "anime style, manga, vibrant colors, detailed anime art",
    "Oil Painting": "oil painting style, artistic, brush strokes, fine art",
    "Watercolor": "watercolor painting, soft colors, artistic, flowing paint",
    "3D Render": "3D render, octane render, cinematic lighting, high quality CGI",
    "Digital Art": "digital art, concept art, detailed, artstation quality",
    "Sketch": "pencil sketch, hand drawn, artistic sketch, detailed linework",
    "Cyberpunk": "cyberpunk style, neon lights, futuristic, sci-fi aesthetic",
    "Fantasy": "fantasy art, magical, ethereal, dreamlike, mystical"
}

selected_style = st.selectbox(
    "Select a style:",
    options=list(style_options.keys()),
    index=0,
    help="Choose the artistic style for your generated image"
)

# Display style description
st.caption(f"✨ **Style modifier:** {style_options[selected_style]}")

st.markdown("---")

# Text input for prompt
prompt = st.text_area(
    "Enter your image description:",
    placeholder="Example: A serene mountain landscape at sunset with a crystal-clear lake",
    height=100
)

# Advanced options (optional)
with st.expander("⚙️ Advanced Options"):
    st.info(f"Current Model: **{MODEL_NAME}**")
    st.caption("FLUX.1-schnell is optimized for fast, high-quality image generation")

    # Option to disable style modifier
    use_style = st.checkbox("Apply style modifier to prompt", value=True,
                           help="Uncheck to use only your prompt without style modifiers")

# Generate button
generate_button = st.button("🚀 Generate Image", type="primary")

# Image generation logic
if generate_button:
    if not prompt.strip():
        st.warning("⚠️ Please enter a description for your image")
    elif not client:
        st.error("❌ HuggingFace client not initialized. Please check your API token.")
    else:
        try:
            # Construct the final prompt with style modifier
            final_prompt = prompt
            if use_style and selected_style in style_options:
                final_prompt = f"{prompt}, {style_options[selected_style]}"

            # Show loading spinner
            with st.spinner("🎨 Generating your image... This may take 10-30 seconds"):
                # Display the prompt being used
                with st.expander("📝 View Full Prompt"):
                    st.code(final_prompt, language=None)

                # Generate image using InferenceClient
                image = client.text_to_image(
                    prompt=final_prompt,
                    model=MODEL_NAME
                )

                # Display the generated image
                st.success("✅ Image generated successfully!")
                st.image(image, caption=prompt, use_container_width=True)

                # Convert PIL Image to bytes for download
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                byte_im = buf.getvalue()

                # Download button
                st.download_button(
                    label="⬇️ Download Image",
                    data=byte_im,
                    file_name="generated_image.png",
                    mime="image/png"
                )

        except Exception as e:
            error_message = str(e)

            # Handle specific error cases
            if "401" in error_message or "authentication" in error_message.lower():
                st.error("❌ Authentication failed!")
                st.info("""
                **Possible issues:**
                - Invalid API token
                - Token doesn't have the required permissions
                - Token has been revoked

                **Solution:**
                - Go to https://huggingface.co/settings/tokens
                - Create a new token with **Write** permissions (or at minimum "Make calls to the serverless Inference API")
                - Update your `.env` file with the new token
                """)
            elif "429" in error_message or "rate limit" in error_message.lower():
                st.error("❌ Rate limit exceeded!")
                st.info("""
                **You've hit the API rate limit.**
                - Free tier has limited requests per hour
                - Please wait a few minutes and try again
                - Consider upgrading to HuggingFace Pro for higher limits
                """)
            elif "503" in error_message or "loading" in error_message.lower():
                st.error("❌ Model is loading!")
                st.info("""
                **The model is currently loading.**
                - This happens when the model hasn't been used recently
                - Please wait 1-2 minutes and try again
                """)
            else:
                st.error(f"❌ Error generating image: {error_message}")
                st.info("Please try again or check your internet connection.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Powered by HuggingFace 🤗 | Model: FLUX.1-schnell</p>
    <p style='font-size: 0.8rem;'>Free tier has rate limits. For production use, consider HuggingFace Pro.</p>
</div>
""", unsafe_allow_html=True)
