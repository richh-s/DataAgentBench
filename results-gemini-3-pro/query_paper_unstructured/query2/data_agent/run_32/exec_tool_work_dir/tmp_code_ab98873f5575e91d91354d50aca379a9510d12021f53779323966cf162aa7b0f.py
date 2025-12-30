code = """import json
import os

# MongoDB result (filenames)
mongo_res = locals()['var_function-call-16257406837857240081']
with open(mongo_res, 'r') as f:
    mongo_docs = json.load(f)

# SQLite result (citations)
sqlite_res = locals()['var_function-call-13725744379955539795']
with open(sqlite_res, 'r') as f:
    sqlite_citations = json.load(f)

mongo_filenames = set(d['filename'] for d in mongo_docs)
sqlite_titles = {c['title'] + ".txt": c['citation_count'] for c in sqlite_citations}

intersection_files = list(mongo_filenames.intersection(sqlite_titles.keys()))
print("Intersection count:", len(intersection_files))

# I will print the list of filenames to use in the next query
print("__RESULT__:")
print(json.dumps(intersection_files))"""

env_args = {'var_function-call-13725744379955539795': 'file_storage/function-call-13725744379955539795.json', 'var_function-call-16281852908939748059': 158, 'var_function-call-7061098653727589076': 'file_storage/function-call-7061098653727589076.json', 'var_function-call-7343253709634976495': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-8333179605566181681': ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-16257406837857240081': 'file_storage/function-call-16257406837857240081.json'}

exec(code, env_args)
