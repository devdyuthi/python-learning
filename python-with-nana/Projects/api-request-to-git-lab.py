import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

nana_projects = response.json()

for project in nana_projects:
    print(f"Project Name: {project['name']}\n Project URL: {project['web_url']}\n")


