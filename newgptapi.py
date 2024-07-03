import openai

def get_joke(prompt, api_key):
    """
    Request a joke from OpenAI API.

    Parameters:
    prompt (str): The prompt to send to the API.
    api_key (str): The OpenAI API key.

    Returns:
    str: The joke returned by the API.
    """
    # Set the OpenAI API key
    openai.api_key = api_key

    try:
        # Make a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=50
        )

        # Extract and return the response text
        return response['choices'][0]['message']['content'].strip()

    except openai.error.OpenAIError as e:
        # Handle any errors that occur
        print(f"An error occurred: {e}")
        return None

def main():
    # Define your API key (replace with your actual API key)
    api_key = 'sk-proj-knhjFYo4MTf7oxUrtfKMT3BlbkFJWwrnaIAp9LcBVrPPPJuL'

    # Define the prompt
    prompt = "Tell me a joke."

    # Get a joke from the API
    joke = get_joke(prompt, api_key)

    # Print the joke
    if joke:
        print("Here's a joke for you:", joke)

if __name__ == "__main__":
    main()
