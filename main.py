import os

from google import genai  # noqa
from openai import OpenAI
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    token = os.getenv('GPT_API_KEY')
    if not token:
        raise SystemExit(
            'Environment variable "GPT_API_KEY" is not found. '
            'Check .env file in root project.'
        )
    client = OpenAI(api_key=token)
    response = client.chat.completions.create(
        model=os.getenv('MODEL'),
        messages=[
            {
                'role': 'user',
                'content': 'Resume in short: The client paid for the same order twice.'
            }
        ]
    )
    choice = response.choices[0]
    answer = choice.message.content

    print('Result: ')
    print(answer or 'Model did not return any answer')

    print('\nStatistics:')
    print(f'Response ID: {response.id}')
    print(f'Model: {response.model}')
    print(f'Причина завершения: {choice.finish_reason}')
    if response.usage:
        print(f'Input Tokens: {response.usage.prompt_tokens}')
        print(f'Output Tokens: {response.usage.completion_tokens}')
        print(f'Total Tokens: {response.usage.total_tokens}')
    else:
        print('The provider did not return token statistics')


# def main() -> None:
#     load_dotenv()
#
#     token = os.getenv("GEMINI_API_KEY")
#     if not token:
#         raise SystemExit(
#             'Environment variable "GEMINI_API_KEY" is not found. '
#             'Check .env file in root project.'
#         )
#     client = genai.Client(api_key=token)
#     interaction = client.interactions.create(
#         model='gemini-4-hydrogen',
#         input='Resume in short: The client paid for the same order twice.'
#     )
#
#     print('Result: ')
#     print(interaction.output_text)
#
#     print('\nStatistics:')
#     print(f'Response ID: {interaction.id}')
#     print(f'Model: {interaction.model}')
#     if interaction.usage:
#         print(f'Input Tokens: {interaction.usage.initial_input_tokens}')
#         print(f'Output Tokens: {interaction.usage.total_output_tokens}')
#         print(f'Total Tokens: {interaction.usage.total_tokens}')
#     else:
#         print('The provider did not return token statistics')


if __name__ == "__main__":
    main()
