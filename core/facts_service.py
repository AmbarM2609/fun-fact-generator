import requests

API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    """
    Fetches a random fact from the external API.
    Returns:
        str: The fact text.
    Raises:
        RuntimeError: If API request fails.
    """
    try:
        response = requests.get(API_URL , timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("text"," Fact not found.")
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch random fact: {e}")
    except ValueError as e:
        raise RuntimeError(f"Failed to parse API response: {e}")