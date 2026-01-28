code = """import json

# Load citations
with open(locals()['var_function-call-1625930341030172972'], 'r') as f:
    citations = json.load(f)

# Load paper filenames
with open(locals()['var_function-call-5147705068000109282'], 'r') as f:
    paper_docs = json.load(f)

# Create a set of filenames from paper_docs
available_filenames = set(d['filename'] for d in paper_docs)

# Identify which citations have a matching paper
matches = []
files_to_fetch = []

for c in citations:
    fname = c['title'] + ".txt"
    if fname in available_filenames:
        matches.append(c)
        files_to_fetch.append(fname)

print(f"Total citations in 2018: {len(citations)}")
print(f"Matches found in paper_docs: {len(matches)}")

# Construct query to fetch text for these files
# We need to fetch 'text' and 'filename' (to map back)
query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": files_to_fetch}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-1625930341030172972': 'file_storage/function-call-1625930341030172972.json', 'var_function-call-13977181496462038220': 'file_storage/function-call-13977181496462038220.json', 'var_function-call-12384276026889794839': 'file_storage/function-call-12384276026889794839.json', 'var_function-call-15504972561961046607': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-4599745652298373250': {'count': 5, 'first_doc': {'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}}, 'var_function-call-5147705068000109282': 'file_storage/function-call-5147705068000109282.json'}

exec(code, env_args)
