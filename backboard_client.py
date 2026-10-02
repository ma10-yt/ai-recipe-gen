import os
import requests

BACKBOARD_API_URL = "https://app.backboard.io/api/threads/messages"
BACKBOARD_API_KEY = os.getenv("BACKBOARD_API_KEY")

RECIPE_SYSTEM_PROMPT = """
You are an AI cooking assistant.

Your job is to help users decide what to cook and then teach them how to cook it.

Always consider:
- ingredients available to the user
- ingredients identified from uploaded images
- dietary preferences
- allergies
- cuisine preference
- serving size
- cooking time

Never recommend an ingredient that conflicts with a stated allergy or dietary restriction.

Keep recipes realistic, practical, and suitable for a home kitchen.
"""


def send_to_backboard(prompt, image_file=None):
    if not BACKBOARD_API_KEY:
        raise ValueError("BACKBOARD_API_KEY is not configured.")

    # ---------------------------------------------------------
    # Normal text request
    # ---------------------------------------------------------
    if image_file is None:
        response = requests.post(
            BACKBOARD_API_URL,
            headers={
                "X-API-Key": BACKBOARD_API_KEY,
                "Content-Type": "application/json",
            },
            json={
                "content": prompt,
                "system_prompt": RECIPE_SYSTEM_PROMPT,
                "llm_provider": "openrouter",
                "model_name": "moonshotai/kimi-k2.6",
                "memory": "Auto",
                "stream": False,
            },
            timeout=120,
        )

    # ---------------------------------------------------------
    # Image + text request
    # ---------------------------------------------------------
    else:
        image_bytes = image_file.getvalue()

        response = requests.post(
            BACKBOARD_API_URL,
            headers={
                "X-API-Key": BACKBOARD_API_KEY,
            },
            data={
                "content": prompt,
                "system_prompt": RECIPE_SYSTEM_PROMPT,
                "llm_provider": "openrouter",
                "model_name": "moonshotai/kimi-k2.6",
                "memory": "Auto",
                "stream": "false",
            },
            files=[
                (
                    "files",
                    (
                        image_file.name,
                        image_bytes,
                        image_file.type or "image/jpeg",
                    ),
                )
            ],
            timeout=120,
        )

    if not response.ok:
        raise RuntimeError(
            f"Backboard error {response.status_code}: {response.text}"
        )

    return response.json()


def get_recipe_suggestions(
    ingredients,
    dietary_preferences="None",
    cuisine="Any",
    servings=2,
    cooking_time="Any",
    image_file=None,
):
    if image_file:
        prompt = f"""
Look carefully at the uploaded image and identify the food ingredients
that are visible.

The user also provided these ingredients:
{ingredients if ingredients.strip() else "None"}

Combine the ingredients you identify from the image with the ingredients
provided by the user.

Dietary preference/restriction:
{dietary_preferences}

Preferred cuisine:
{cuisine}

Servings:
{servings}

Maximum cooking time:
{cooking_time}

Suggest exactly 5 different recipes that can realistically be made
using the available ingredients.

IMPORTANT:
Return ONLY the 5 suggestions.

Use exactly this format:

1. Recipe Name | One short description
2. Recipe Name | One short description
3. Recipe Name | One short description
4. Recipe Name | One short description
5. Recipe Name | One short description

Do not provide cooking instructions yet.
Do not add any text before or after the 5 suggestions.
"""
    else:
        prompt = f"""
The user has these ingredients:

{ingredients}

Dietary preference/restriction:
{dietary_preferences}

Preferred cuisine:
{cuisine}

Servings:
{servings}

Maximum cooking time:
{cooking_time}

Suggest exactly 5 different recipes that the user could make.

IMPORTANT:
Return ONLY the 5 suggestions.

Use exactly this format:

1. Recipe Name | One short description
2. Recipe Name | One short description
3. Recipe Name | One short description
4. Recipe Name | One short description
5. Recipe Name | One short description

Do not provide cooking instructions yet.
Do not add any text before or after the 5 suggestions.
"""

    data = send_to_backboard(prompt, image_file=image_file)

    return {
        "content": data.get("content", ""),
        "thread_id": data.get("thread_id"),
        "assistant_id": data.get("assistant_id"),
    }


def get_recipe_details(
    recipe_name,
    ingredients,
    dietary_preferences="None",
    cuisine="Any",
    servings=2,
    cooking_time="Any",
):
    prompt = f"""
The user selected this recipe:

{recipe_name}

Available ingredients:
{ingredients}

Dietary preference/restriction:
{dietary_preferences}

Preferred cuisine:
{cuisine}

Servings:
{servings}

Maximum cooking time:
{cooking_time}

Now provide the COMPLETE recipe.

Use this structure:

# Recipe Name

## Description

## Ingredients
- ingredient with quantity
- ingredient with quantity

## Preparation Time

## Cooking Time

## Instructions
1. Step one
2. Step two
3. Step three

## Substitutions
Mention useful substitutions when appropriate.

## Cooking Tip
Give one useful tip.

Do not suggest another recipe.
Give instructions only for the selected recipe.
"""

    data = send_to_backboard(prompt)

    return {
        "content": data.get("content", ""),
        "thread_id": data.get("thread_id"),
        "assistant_id": data.get("assistant_id"),
    }