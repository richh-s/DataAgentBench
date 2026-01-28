code = """import json

with open(locals()['var_function-call-2106421940036629061'], 'r') as f:
    citations_data = json.load(f)

titles = [record['title'] for record in citations_data]
filenames = [t + ".txt" for t in titles]

# Construct MongoDB query
# We want: {"filename": {"$in": filenames}}
# We need to ensure it's a valid JSON string.
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2106421940036629061': 'file_storage/function-call-2106421940036629061.json', 'var_function-call-10975034147027654622': {'count': 188, 'filenames_preview': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"]}}

exec(code, env_args)
