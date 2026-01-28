code = """import json

# Load citations
citations_path = locals()['var_function-call-16918491452103176986']
with open(citations_path, 'r') as f:
    citations = json.load(f)
# Create a set of target filenames
target_filenames = set([c['title'] + ".txt" for c in citations])

# Load all paper docs filenames
paper_list_path = locals()['var_function-call-12990868199474423311']
with open(paper_list_path, 'r') as f:
    paper_list = json.load(f)

# Find IDs
ids = []
for p in paper_list:
    if p['filename'] in target_filenames:
        ids.append(p['_id'])

print(f"Found {len(ids)} matching papers.")
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-16918491452103176986': 'file_storage/function-call-16918491452103176986.json', 'var_function-call-2065725143731253530': 'file_storage/function-call-2065725143731253530.json', 'var_function-call-338667310084266534': {'count': 158, 'filenames_sample': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}, 'var_function-call-12839390599410482913': 'file_storage/function-call-12839390599410482913.json', 'var_function-call-12990868199474423311': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
