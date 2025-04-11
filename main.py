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
    if r.status_code == 200:
        return r.json()
    else:
        print(f"Erreur lors de la récupération des commits : {r.status_code} - {r.text}")
        return []

def get_pulls():
    r = requests.get(f"https://api.github.com/repos/{REPO}/pulls", headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"Erreur lors de la récupération des pull requests : {r.status_code} - {r.text}")
        return []

def get_runs():
    r = requests.get(f"https://api.github.com/repos/{REPO}/actions/runs", headers=headers)
    if r.status_code == 200:
        return r.json().get("workflow_runs", [])
    else:
        print(f"Erreur lors de la récupération des executions de pipelines : {r.status_code} - {r.text}")
        return []

def print_report():
    print("Commits:", len(get_commits()))
    print("Pull Requests:", len(get_pulls()))
    print("Executions de pipeline:", len(get_runs()))

if __name__ == "__main__":
    print_report()
