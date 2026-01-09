code = """import json, pandas as pd

# load filenames list
food_files = var_call_Y4KXBc0oIuetUNE6IdPbJFio
food_titles = [d['filename'].removesuffix('.txt') for d in food_files]

# load citations records
cit_path_or_list = var_call_25Hi6GegtOSCGQVzvrAZUEsO
if isinstance(cit_path_or_list, str):
    with open(cit_path_or_list, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_path_or_list

# sum citation_count for matching titles
food_set = set(food_titles)

total = 0
for r in citations:
    if r.get('title') in food_set:
        try:
            total += int(r.get('citation_count', 0))
        except Exception:
            pass

out = {"domain":"food", "total_citation_count": total, "paper_count": len(food_set)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5ZlwqXjtr1V1PpxZnVuqeDFo': 'file_storage/call_5ZlwqXjtr1V1PpxZnVuqeDFo.json', 'var_call_25Hi6GegtOSCGQVzvrAZUEsO': 'file_storage/call_25Hi6GegtOSCGQVzvrAZUEsO.json', 'var_call_Y4KXBc0oIuetUNE6IdPbJFio': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt'}]}

exec(code, env_args)
