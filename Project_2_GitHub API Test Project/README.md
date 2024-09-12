# GitHub API Test Project

This project creates an automated test for interacting with the GitHub API using Python. It demonstrates creating,
checking, and deleting a repository on GitHub.

## Installation

1. Clone the repository:
   git clone https://github.com/Sent1mus/Pet_Projects_QA_Automation

   cd Pet_Projects_QA_Automation


2. Create a virtual environment (optional but recommended):
   python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate


3. Install dependencies:
   pip install -r requirements.txt


4. Replace `your_github_personal_access_token` with a valid GitHub Personal Access Token and `your_github_username` with
your GitHub username.

## Running the Test

To run the test, simply execute the script:

python test_api.py

## Expected Output

The script will attempt to:

1. Create a new public repository named `test-repo-for-api-test` (or whatever you specified in the REPO_NAME variable).
2. Check if the repository exists.
3. Delete the repository.

If everything goes well, you should see log messages indicating each step's success.