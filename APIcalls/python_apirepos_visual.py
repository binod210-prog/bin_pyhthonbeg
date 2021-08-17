import requests
import json

from plotly.graph_objs import Bar
from plotly import offline

# Make API calls and store responses

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f"Status code : {r.status_code}")


# process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links,stars, labels = [], [], []  # Adding clickable links to graph
for repo_dict in repo_dicts:

    repo_name = repo_dict['name']
    #repo_names.append(repo_dict['name'])
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])


# Make visualization

data = [{
    'type': 'bar',
    'x' : repo_links,
    'y' : stars

    }]

my_layout = {
    'title' : ' Most starred python projects on github',
    'xaxis' : {'title' :'Repository'},
    'yaxis' : {'title' : 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')
