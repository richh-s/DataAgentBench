code = """import json
# Load the previous result to get filenames
citations_path = locals()['var_function-call-16918491452103176986']
with open(citations_path, 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-16918491452103176986': 'file_storage/function-call-16918491452103176986.json', 'var_function-call-2065725143731253530': 'file_storage/function-call-2065725143731253530.json', 'var_function-call-338667310084266534': {'count': 158, 'filenames_sample': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}}

exec(code, env_args)
