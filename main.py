import os

from google import genai  # noqa
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    token = os.getenv("GEMINI_API_KEY")
    if not token:
        raise SystemExit(
            'Environment variable "GEMINI_API_KEY" is not found. '
            'Check .env file in root project.'
        )
    client = genai.Client(api_key=token)
    interaction = client.interactions.create(
        model="gemini-4-hydrogen",
        input="Summarize the request in one sentence: The customer received "
              "damaged packaging and would like to exchange the item."
    )
    print(interaction.output_text)


if __name__ == "__main__":
    main()
