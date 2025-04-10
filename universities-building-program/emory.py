# ============================================================
# Emory University Challenge: Implement the "joke" command.
#
# When a user sends a message containing "joke",
# your agent should fetch a random joke from an external API.
#
# Hints:
# 1. Use the 'requests' library to perform an HTTP GET request.
# 2. A commonly used endpoint is:
#    https://official-joke-api.appspot.com/random_joke
# 3. Check that the response is successful (status code 200).
# 4. Parse the JSON to extract the "setup" and "punchline".
#
# Useful resources:
# - Requests documentation: https://docs.python-requests.org/en/latest/
# - Official Joke API info: https://official-joke-api.appspot.com/
# ============================================================

import requests

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif "joke" in message:
        # TODO: Implement the joke command.
        # Steps:
        #   1. Make a GET request to the joke API.
        #   2. Verify the response status.
        #   3. Parse the JSON data to extract "setup" and "punchline".
        #   4. Return the joke as a formatted string.
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        if response.status_code == 200:
            joke_data = response.json()
            setup = joke_data.get('setup', '')
            punchline = joke_data.get('punchline', '')
            return f"{setup}\n{punchline}"
        else:
            return "Sorry, I couldn't fetch a joke at the moment. Please try again later."
        #pass
    else:
        return "I'm sorry, I didn't understand your message."

if __name__ == "__main__":
    user_input = input("Enter a message for the agent: ")
    print(handle_message(user_input))
