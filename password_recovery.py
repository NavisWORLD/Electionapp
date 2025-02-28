# password_recovery.py

import hashlib
from typing import Dict, Union
from authentication import users

# Dictionary to store password recovery tokens
recovery_tokens: Dict[str, str] = {}


def generate_recovery_token(username: str) -> Union[str, None]:
    """
    Generate a password recovery token for the specified user.

    Parameters:
    - username (str): The username of the user.

    Returns:
    - str: The recovery token if the user is found, otherwise None.

    Raises:
    - ValueError: If the username is empty.
    """
    if not username:
        raise ValueError("Username cannot be empty")

    if username in users:
        # For simplicity, we'll use a hashed username as the token
        token = hashlib.sha256(username.encode()).hexdigest()
        recovery_tokens[token] = username
        return token
    else:
        return "User not found."


def reset_password(token: str, new_password: str) -> str:
    """
    Reset the password for the user associated with the given token.

    Parameters:
    - token (str): The password recovery token.
    - new_password (str): The new password for the user.

    Returns:
    - str: Status message indicating success or failure.

    Raises:
    - ValueError: If the token or new password is empty.
    """
    if not token or not new_password:
        raise ValueError("Token and new password cannot be empty")

    username = recovery_tokens.get(token)
    if username:
        hashed_pw = hashlib.sha256(new_password.encode()).hexdigest()
        users[username] = hashed_pw
        del recovery_tokens[token]
        return "Password reset successful."
    else:
        return "Invalid recovery token."
