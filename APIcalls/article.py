from operator import itemgetter
import requests
import json

#Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f" Status code : {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    #Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} \status : {r.status_code}")
    response_dict = r.json()


    # Build a dictionary for each article
    submission_dict = {

        'title' : response_dict['title'],
        'link' :  f"http://news.ycombinator.com/item?id={submission_id}",
        'comments' : response_dict['descendants'],

        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\n Title : {submission_dict['title']}")
    print(f"Discussion link : {submission_dict['link']}")
    print(f"Comments : {submission_dict['comments']}")








# Explore structure of json data

#response_dict = r.json()
#readable_file = 'readable_data.json'
#with open(readable_file, 'w') as f:
#    json.dump(response_dict, f, indent=4)
