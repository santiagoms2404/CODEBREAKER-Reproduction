import requests


def fetch_secure_data(url):
    """
    A secure function that properly validates SSL certificates.
    """
    try:
        # SAFE: verify=True is the default, ensuring SSL validation.
        # We explicitly set it here for clarity.
        response = requests.get(url, timeout=5, verify=True)
        return response.status_code
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print(fetch_secure_data("https://example.com"))
