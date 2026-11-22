import os
from time import perf_counter

import openai
from dotenv import load_dotenv
from openai import OpenAI


def summarize_request(client: OpenAI, user_text: str) -> None:
    text = user_text.strip()
    if not text:
        print('Error: Message must not be empty.')
        return

    started_at = perf_counter()

    try:
        response = client.chat.completions.create(
            model=os.getenv('MODEL'),
            messages=[
                {
                    'role': 'user',
                    'content': 'Summarize the content of the message in '
                               'a single sentence. Do not include any facts '
                               'that are not present in the text.\n\n'
                               f'Message: {text}'
                }
            ]
        )
    except openai.AuthenticationError:
        print('Authorization error. Check API Key is available.')
    except openai.PermissionDeniedError:
        print('Permission denied error. Check API Key permissions.')
    except openai.RateLimitError:
        print('Rate limit exceeded. Please try again later.')
    except openai.APITimeoutError:
        print(
            "Timeout error. The provider didn't manage to answer within "
            "the allotted time."
        )
    except openai.APIConnectionError:
        print('Connection error. Check the network.')
    except openai.APIStatusError as e:
        if e.status_code == 429:
            print('Credit balance exhausted or organization limit exceeded.')
        else:
            print(f'The API returned an error with a status {e.status_code}')
        if e.request_id:
            print(f'Request ID: {e.request_id}')
    except openai.APIError as e:
        print(f'API error occurred: {e}')

    else:
        elapsed_seconds = perf_counter() - started_at
        choice = response.choices[0]
        answer = choice.message.content

        print('Result: ')
        print(answer or 'Model did not return any answer')

        print('\nStatistics:')
        print(f'Response ID: {response.id}')
        print(f'Model: {response.model}')
        print(f'Finish Reason: {choice.finish_reason}')
        print(f'Time: {elapsed_seconds:.2f} seconds')
        if response.usage:
            print(f'Input Tokens: {response.usage.prompt_tokens}')
            print(f'Output Tokens: {response.usage.completion_tokens}')
            print(f'Total Tokens: {response.usage.total_tokens}')
        else:
            print('The provider did not return token statistics')


def main() -> None:
    load_dotenv()

    token = os.getenv('GPT_API_KEY')
    if not token:
        raise SystemExit(
            'Environment variable "GPT_API_KEY" is not found. '
            'Check .env file in root project.'
        )
    client = OpenAI(api_key=token)
    user_text = input('Enter yor text message...')
    summarize_request(client, user_text)


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
