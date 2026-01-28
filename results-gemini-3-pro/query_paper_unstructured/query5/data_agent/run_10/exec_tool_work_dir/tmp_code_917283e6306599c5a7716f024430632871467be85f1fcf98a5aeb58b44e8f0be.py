code = """import json

# Load citations from the original query result file
file_path = locals()['var_function-call-17184037719659309695']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Extract titles and create filenames
titles = [c['title'] for c in citations]
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-17184037719659309695': 'file_storage/function-call-17184037719659309695.json', 'var_function-call-575482602016470720': {'count': 188, 'sample_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_function-call-15651807627207268888': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-14454467224535404411': 5, 'var_function-call-15124095079000885129': 'file_storage/function-call-15124095079000885129.json', 'var_function-call-17358706496144615783': 'file_storage/function-call-17358706496144615783.json'}

exec(code, env_args)
