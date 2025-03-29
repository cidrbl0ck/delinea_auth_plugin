# Python module for an Ansible AWX custom credential type for Delinea or Thycotic Secret Server
from typing import Callable, NamedTuple
import os
from ss_token_plugin import exceptions

# Initialize required inputs
#api_url = os.environ.get('SS_API_URL', '')  # Base API URL
auth_endpoint = '/oauth2/token'  # Authentication endpoint
secrets_endpoint = '/api/v1/secrets/'  # Secrets endpoint
#api_username = os.environ.get('SS_API_USERNAME', '')  # Default API username
#api_password = os.environ.get('SS_API_PASSWORD', '')  # Default API password
api_test_secret = os.environ.get('SS_SECRET_ID', '')  # Default secret ID for testing

class CredentialPlugin(NamedTuple):
    name: str
    inputs: dict
    backend: Callable

ss_app_inputs = {
    "fields": [
        {"id": "api_url", "type": "string", "label": "API URL", "required": True},
        {"id": "api_username", "type": "string", "label": "API Username", "required": True},
        {"id": "api_password", "type": "string", "label": "API Password", "required": True, "secret": True},
    ],
    "required": ["api_url", "api_username", "api_password"],  # Required fields for the credential
}

def ss_auth_backend(api_url, api_username, api_password):
    auth_url = f"{api_url}{auth_endpoint}"
    #print(f"DEBUG: Authenticating with URL: {auth_url}")  # Debugging info

    try:
        response = requests.post(
            auth_url,
            data={
                'username': api_username,
                'password': api_password,
                'grant_type': 'password',
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
        )
        response.raise_for_status()
        token = response.json().get('access_token')
        if not token:
            raise Exception("Authentication failed: No access token returned.")
        #print(f"DEBUG: Authentication successful. Access token: {token}")  # Debugging info
        return token
    except Exception as e:
        #print(f"DEBUG: Authentication failed: {str(e)}")  # Debugging info
        raise Exception(f"Authentication failed: {str(e)}")

    return token

delinea_auth_plugin = CredentialPlugin("Delinea Secret Server Auth", inputs=ss_app_inputs, backend=ss_auth_backend)

#def test_secret_lookup(api_url, token, secret_id):
#    secrets_url = f"https://YourSecretServerURLHere.com"
#   print(f"DEBUG: Retrieving secrets from URL: {secrets_url}")  # Debugging info

#    try:
#        secrets_response = requests.get(
#            secrets_url,
#            headers={'Authorization': f"Bearer {token}"},
#        )
#        secrets_response.raise_for_status()
#        secrets = secrets_response.json()
#        print(f"DEBUG: Retrieved secrets: {secrets}")  # Debugging info
#        return secrets
#    except Exception as e:
#       print(f"DEBUG: Failed to retrieve secrets: {str(e)}")  # Debugging info
#       raise Exception(f"Failed to retrieve secrets: {str(e)}")


# DEBUGGING Main block to execute the script
#if __name__ == "__main__":
#    try:
        # Authenticate and retrieve the token
#        token = ss_auth_backend(
#            api_url=api_url,
#            api_username=api_username,
#            api_password=api_password,
#        )
#        print(f"DEBUG: Returned token is {token}")

        # Optional: Test secret lookup
#        secrets = test_secret_lookup(
#           api_url=api_url,
#            token=token,
#           secret_id=api_test_secret,
#        )
#        print(f"DEBUG: Retrieved test secret: {secrets}")
#    except Exception as e:
#        print(f"ERROR: {str(e)}")
