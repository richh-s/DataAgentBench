code = """import json

with open(locals()['var_function-call-161273639758194169'], 'r') as f:
    citations_2018 = json.load(f)

filenames = [c['title'] + ".txt" for c in citations_2018]
query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": filenames}},
    "projection": {"filename": 1, "text": 1} 
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-161273639758194169': 'file_storage/function-call-161273639758194169.json', 'var_function-call-161273639758192992': 'file_storage/function-call-161273639758192992.json', 'var_function-call-13120840873059324966': {'count': 158, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set']}}

exec(code, env_args)
