code = """import json

with open(locals()['var_function-call-789985204037697992'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
# Print titles and check if 'food' is in text
debug_info = []
for p in papers[:5]:
    debug_info.append({
        "title": p['filename'],
        "has_food_in_text": "food" in p['text'].lower(),
        "snippet": p['text'][:500]
    })
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4706990439072147394': 'file_storage/function-call-4706990439072147394.json', 'var_function-call-4706990439072147581': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-789985204037697992': 'file_storage/function-call-789985204037697992.json', 'var_function-call-10038520539297588104': 'file_storage/function-call-10038520539297588104.json', 'var_function-call-6756475489867741448': 0}

exec(code, env_args)
