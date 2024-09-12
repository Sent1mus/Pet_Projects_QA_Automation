import os
import logging
from dotenv import load_dotenv
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GITHUB_API_URL = "https://api.github.com"

def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    logger.info(f"GITHUB_TOKEN: {'***' if token else 'Not set'}")
    if not token:
        raise ValueError("GitHub token is not set in environment variables")
    return token

def get_username():
    username = os.getenv("GITHUB_USERNAME")
    logger.info(f"GITHUB_USERNAME: {'***' if username else 'Not set'}")
    if not username:
        raise ValueError("GitHub username is not set in environment variables")
    return username

def get_repo_name():
    repo_name = os.getenv("REPO_NAME")
    logger.info(f"REPO_NAME: {repo_name}")
    if not repo_name:
        raise ValueError("Repository name is not set in environment variables")
    return repo_name

def create_repository(repo_name):
    token = get_github_token()
    username = get_username()

    url = f"{GITHUB_API_URL}/user/repos"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    data = {
        "name": repo_name,
        "description": "Test repository",
        "private": False,
        "auto_init": True
    }

    try:
        logger.info(f"Creating repository {repo_name}...")
        response = requests.post(url, json=data, headers=headers)

        logger.info(f"Response status code: {response.status_code}")

        if response.status_code == 201:
            logger.info(f"Repository {repo_name} created successfully")
            return True
        elif response.status_code == 422:
            logger.error("Unprocessable Entity error occurred")
            logger.error(f"Response content: {response.text}")
        else:
            logger.error(f"Unexpected status code: {response.status_code}")
            logger.error(f"Response content: {response.text}")

        return False

    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating repository: {e}")
        return False

def check_repository_exists(repo_name):
    token = get_github_token()
    username = get_username()

    url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Repository {repo_name} exists")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Error checking repository: {e}")
        return False

def delete_repository(repo_name):
    token = get_github_token()
    username = get_username()

    url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Repository {repo_name} deleted successfully")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Error deleting repository: {e}")
        return False

def main():
    try:
        load_dotenv()

        logger.info("Checking environment variables:")
        for var in ["GITHUB_TOKEN", "GITHUB_USERNAME", "REPO_NAME"]:
            value = os.getenv(var)
            logger.info(f"{var}: {'***' if value else 'Not set'}")

        # Get the repository name from environment variables
        repo_name = get_repo_name()

        logger.info(f"Using repository name: {repo_name}")

        if check_repository_exists(repo_name):
            logger.info(f"Repository {repo_name} already exists.")
            return  # Exit or handle as needed

        if create_repository(repo_name):
            logger.info(f"Repository {repo_name} created successfully.")
            if check_repository_exists(repo_name):
                logger.info(f"Repository {repo_name} has been verified to exist.")
                if delete_repository(repo_name):
                    logger.info(f"Repository {repo_name} deleted successfully.")
                else:
                    logger.error(f"Failed to delete repository {repo_name}.")
            else:
                logger.error(f"Repository {repo_name} does not exist after creation.")
        else:
            logger.error(f"Failed to create repository {repo_name}.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()