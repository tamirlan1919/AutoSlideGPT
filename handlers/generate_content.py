# utils/generate_content.py
import openai
import os


openai.api_key = os.getenv('OPENAI_API_KEY')

async def generate_presentation_content(topic):
    prompt = f"Создай план презентации по теме '{topic}'. Разбей презентацию на слайды, укажи заголовок и краткое содержание для каждого слайда."

    response = await openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    content = response.choices[0].text.strip()
    return content
