code = """import json
import os

# MongoDB result
mongo_res = locals()['var_function-call-7343253709634976495']
if isinstance(mongo_res, str) and os.path.exists(mongo_res):
    with open(mongo_res, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_res

# SQLite result (this one was stated to be a file)
sqlite_res = locals()['var_function-call-13725744379955539795']
if isinstance(sqlite_res, str) and os.path.exists(sqlite_res):
    with open(sqlite_res, 'r') as f:
        sqlite_citations = json.load(f)
else:
    sqlite_citations = sqlite_res

print("Mongo docs count:", len(mongo_docs))
print("SQLite citations count:", len(sqlite_citations))

mongo_filenames = set(d['filename'] for d in mongo_docs)
sqlite_titles = set(c['title'] + ".txt" for c in sqlite_citations)

intersection = mongo_filenames.intersection(sqlite_titles)
print("Intersection count:", len(intersection))

print("__RESULT__:")
print(json.dumps(list(intersection)))"""

env_args = {'var_function-call-13725744379955539795': 'file_storage/function-call-13725744379955539795.json', 'var_function-call-16281852908939748059': 158, 'var_function-call-7061098653727589076': 'file_storage/function-call-7061098653727589076.json', 'var_function-call-7343253709634976495': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
