import streamlit as st
import requests
import random

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="AI Image Studio",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 AI Image Studio")
st.markdown("Create stunning AI-generated images from your imagination!")

# ==========================
# Sidebar
# ==========================
st.sidebar.header("⚙️ Settings")

art_style = st.sidebar.selectbox(
    "🎭 Select Art Style",
    [
        "Photorealistic",
        "Anime",
        "Vintage Victorian",
        "Sketch",
        "3D Render"
    ]
)

width = st.sidebar.slider(
    "📏 Image Width",
    min_value=256,
    max_value=1024,
    value=768,
    step=64
)

height = st.sidebar.slider(
    "📐 Image Height",
    min_value=256,
    max_value=1024,
    value=768,
    step=64
)

# ==========================
# Task 3 - Magic Enhance
# ==========================
magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")

# ==========================
# Surprise Prompt List
# ==========================
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon reading books inside a futuristic library",
    "A floating island made entirely of candy",
    "A robot painting the sunset on a beach"
]

# ==========================
# User Prompt
# ==========================
user_prompt = st.text_input(
    "🖊️ Describe the image you want to generate"
)

# ==========================
# Buttons
# ==========================
col1, col2 = st.columns(2)

generate = col1.button("🚀 Generate Image")
surprise = col2.button("🎲 Surprise Me!")

# ==========================
# Surprise Me Logic
# ==========================
if surprise:
    user_prompt = random.choice(surprise_prompts)
    st.info(f"🎲 Surprise Prompt:\n\n**{user_prompt}**")
    generate = True

# ==========================
# Generate Image
# ==========================
if generate:

    if user_prompt:

        with st.spinner("🎨 Creating your masterpiece..."):

            full_prompt = f"{user_prompt}, make the art style: {art_style}"

            # Task 3
            if magic_enhance:
                full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

            # Task 1
            url = (
                f"https://image.pollinations.ai/prompt/"
                f"{full_prompt}"
                f"?width={width}&height={height}"
            )

            response = requests.get(url)

            if response.status_code == 200:

                st.success("✅ Image Generated Successfully!")

                st.image(
                    response.content,
                    caption=full_prompt,
                    use_container_width=True
                )

                # Task 2
                st.download_button(
                    label="⬇️ Download Image",
                    data=response.content,
                    file_name=f"{art_style}_image.png",
                    mime="image/png"
                )

            else:
                st.error("❌ Unable to generate image. Please try again.")

    else:
        st.warning("⚠️ Please enter a prompt first.")