code = """import json

# Load citations again
path = locals()['var_function-call-4972033907989994002']
with open(path, 'r') as f:
    citations = json.load(f)

titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

# Batch 1: 0 to 100
batch1 = filenames[:100]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": batch1}
    },
    "projection": {
        "filename": 1,
        "text": 1
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-909056177594673317': ['Citations', 'sqlite_sequence'], 'var_function-call-909056177594674086': ['paper_docs'], 'var_function-call-4972033907989994002': 'file_storage/function-call-4972033907989994002.json', 'var_function-call-217871320813389592': {'count': 188, 'sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_function-call-10698500835932062431': 'file_storage/function-call-10698500835932062431.json', 'var_function-call-8173241189317845158': 'file_storage/function-call-8173241189317845158.json'}

exec(code, env_args)
