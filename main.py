import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "CICDHEXA/hello_world"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_commits():
    r = requests.get(f"https://api.github.com/repos/{REPO}/commits", headers=headers)
    return r.json()

def get_pulls():
    r = requests.get(f"https://api.github.com/repos/{REPO}/pulls", headers=headers)
    return r.json()

def get_runs():
    r = requests.get(f"https://api.github.com/repos/{REPO}/actions/runs", headers=headers)
    return r.json()

def print_report():
    print("Commits:", len(get_commits()))
    print("Pull Requests:", len(get_pulls()))
    print("Executions de pipeline:", len(get_runs()))

if __name__ == "__main__":
    print_report()
