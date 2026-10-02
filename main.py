import re
import streamlit as st

from backboard_client import (
    get_recipe_suggestions,
    get_recipe_details,
)


st.set_page_config(
    page_title="AI Recipe Generator",
    page_icon="🍳",
    layout="centered",
)


st.title("🍳 AI Recipe Generator")
st.write(
    "Tell me what ingredients you have, or upload a photo of them."
)


# ---------------------------------------------------------
# User inputs
# ---------------------------------------------------------

ingredients = st.text_area(
    "🥕 What ingredients do you have?",
    placeholder="Example: chicken, onion, garlic, tomato, rice",
)


uploaded_image = st.file_uploader(
    "📷 Upload a photo of your ingredients (optional)",
    type=["jpg", "jpeg", "png", "webp"],
    help="Take a photo of your fridge, ingredients, or groceries.",
)


if uploaded_image:
    st.image(
        uploaded_image,
        caption="Uploaded ingredients",
        use_container_width=True,
    )


dietary_preferences = st.selectbox(
    "🥗 Dietary preference",
    [
        "None",
        "Vegetarian",
        "Vegan",
        "Halal",
        "Gluten-Free",
        "Keto",
        "Low-Carb",
    ],
)


cuisine = st.selectbox(
    "🌎 Cuisine",
    [
        "Any",
        "Indian",
        "Italian",
        "Mexican",
        "Chinese",
        "American",
        "Mediterranean",
    ],
)


servings = st.number_input(
    "👥 Servings",
    min_value=1,
    max_value=12,
    value=2,
)


cooking_time = st.selectbox(
    "⏱️ Maximum cooking time",
    [
        "Any",
        "15 minutes",
        "30 minutes",
        "45 minutes",
        "60 minutes",
    ],
)


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------

if "recipe_suggestions" not in st.session_state:
    st.session_state.recipe_suggestions = []

if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None

if "recipe_details" not in st.session_state:
    st.session_state.recipe_details = None


# ---------------------------------------------------------
# Find recipes
# ---------------------------------------------------------

if st.button("🔎 Find Recipes", use_container_width=True):

    if not ingredients.strip() and uploaded_image is None:
        st.warning(
            "Please enter some ingredients or upload a photo."
        )
        st.stop()

    st.session_state.recipe_suggestions = []
    st.session_state.selected_recipe = None
    st.session_state.recipe_details = None

    try:
        with st.spinner("🔍 Looking at your ingredients..."):

            result = get_recipe_suggestions(
                ingredients=ingredients,
                dietary_preferences=dietary_preferences,
                cuisine=cuisine,
                servings=servings,
                cooking_time=cooking_time,
                image_file=uploaded_image,
            )

        raw_content = result["content"]

        pattern = r"^\s*(\d+)\.\s*(.*?)\s*\|\s*(.*?)\s*$"

        suggestions = []

        for line in raw_content.splitlines():
            match = re.match(pattern, line)

            if match:
                suggestions.append(
                    {
                        "number": match.group(1),
                        "name": match.group(2).strip(),
                        "description": match.group(3).strip(),
                    }
                )

        if len(suggestions) < 5:
            st.error(
                "The AI returned an unexpected format. "
                "Please try again."
            )
        else:
            st.session_state.recipe_suggestions = suggestions[:5]

    except Exception as e:
        st.error(f"Something went wrong: {e}")


# ---------------------------------------------------------
# Recipe suggestions
# ---------------------------------------------------------

if st.session_state.recipe_suggestions:

    st.markdown("---")

    st.subheader("🍽️ Choose a Recipe")

    recipe_options = [
        f"{recipe['number']}. {recipe['name']}"
        for recipe in st.session_state.recipe_suggestions
    ]

    selected_option = st.radio(
        "Which one would you like to cook?",
        recipe_options,
    )

    selected_index = recipe_options.index(selected_option)

    selected_recipe = st.session_state.recipe_suggestions[
        selected_index
    ]

    st.info(selected_recipe["description"])


    if st.button(
        "👨‍🍳 Give Me the Recipe",
        use_container_width=True,
    ):

        try:
            with st.spinner(
                f"Preparing {selected_recipe['name']}..."
            ):

                result = get_recipe_details(
                    recipe_name=selected_recipe["name"],
                    ingredients=ingredients,
                    dietary_preferences=dietary_preferences,
                    cuisine=cuisine,
                    servings=servings,
                    cooking_time=cooking_time,
                )

            st.session_state.selected_recipe = (
                selected_recipe["name"]
            )

            st.session_state.recipe_details = result["content"]

        except Exception as e:
            st.error(f"Something went wrong: {e}")


# ---------------------------------------------------------
# Final recipe
# ---------------------------------------------------------

if st.session_state.recipe_details:

    st.markdown("---")

    st.markdown("## 👨‍🍳 Your Recipe")

    st.markdown(
        st.session_state.recipe_details
    )


    if st.button("🔄 Choose Another Recipe"):

        st.session_state.selected_recipe = None
        st.session_state.recipe_details = None

        st.rerun()