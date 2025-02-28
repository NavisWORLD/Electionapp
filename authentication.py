# authentication.py

import hashlib
from typing import Dict

# Dictionary to store user credentials
users: Dict[str, str] = {}


def register_user(username: str, password: str) -> str:
    """
    Register a new user.

    Parameters:
    - username (str): The username of the new user.
    - password (str): The password of the new user.

    Returns:
    - str: Status message indicating success or failure.

    Raises:
    - ValueError: If username or password is empty.
    """
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")

    if username in users:
        return "Username already exists."
    else:
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_pw
        return "User registered successfully."


def login_user(username: str, password: str) -> str:
    """
    Log in a user.

    Parameters:
    - username (str): The username of the user.
    - password (str): The password of the user.

    Returns:
    - str: Login status message.

    Raises:
    - ValueError: If username or password is empty.
    """
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")

    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == hashed_pw:
        return "Login successful."
    else:
        return "Invalid credentials."


def logout_user() -> str:
    """
    Log out the user.

    Returns:
    - str: Logout status message.
    """
    return "User logged out successfully."
