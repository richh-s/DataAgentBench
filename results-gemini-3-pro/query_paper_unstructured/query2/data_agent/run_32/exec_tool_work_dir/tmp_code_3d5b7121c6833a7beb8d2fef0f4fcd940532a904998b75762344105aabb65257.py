code = """import json

# MongoDB filenames
file_path_mongo = locals()['var_function-call-7343253709634976495']
with open(file_path_mongo, 'r') as f:
    mongo_docs = json.load(f)

# SQLite citations
file_path_sqlite = locals()['var_function-call-13725744379955539795']
with open(file_path_sqlite, 'r') as f:
    sqlite_citations = json.load(f)

print("Mongo docs count:", len(mongo_docs))
print("SQLite citations count:", len(sqlite_citations))

# Find intersection
mongo_filenames = set(d['filename'] for d in mongo_docs)
sqlite_titles = set(c['title'] + ".txt" for c in sqlite_citations)

intersection = mongo_filenames.intersection(sqlite_titles)
print("Intersection count:", len(intersection))

# Store intersection filenames for next step
print("__RESULT__:")
print(json.dumps(list(intersection)))"""

env_args = {'var_function-call-13725744379955539795': 'file_storage/function-call-13725744379955539795.json', 'var_function-call-16281852908939748059': 158, 'var_function-call-7061098653727589076': 'file_storage/function-call-7061098653727589076.json', 'var_function-call-7343253709634976495': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
