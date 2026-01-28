code = """import json

file_path = locals()['var_function-call-3465492661884944588']
with open(file_path, 'r') as f:
    citations = json.load(f)

filenames = [r['title'] + ".txt" for r in citations]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3465492661884944588': 'file_storage/function-call-3465492661884944588.json', 'var_function-call-5093555136357275627': 'file_storage/function-call-5093555136357275627.json', 'var_function-call-9313904331850907827': {'count': 158, 'filenames_preview': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}}

exec(code, env_args)
