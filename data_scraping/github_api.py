import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_API_TOKEN}"}

def get_random_repositories(num = 10):
    repositories_data = []
    page = 1
    while len(repositories_data) < num:
        response = requests.get(f"https://api.github.com/search/repositories?q=stars:>0&sort=updated&per_page=100&page={page}",
        headers=HEADERS)

        if response.status_code != 200:
            print("Error: ", response.json())
            break

        repositories = response.json().get("items", [])
        random.shuffle(repositories)

        for repo in repositories:
            repositories_data.append(repo)
            if len(repositories_data) >= num:
                break

    page += 1

    return repositories_data[:num]

random_repos = get_random_repositories()

print(random_repos)
