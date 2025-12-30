code = """import json

# Load citations
citations_path = locals()['var_function-call-8331430492114871094']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load filenames
filenames_path = locals()['var_function-call-4296707544942016588']
with open(filenames_path, 'r') as f:
    paper_docs = json.load(f)

# Create a set of citation titles
citation_titles = {c['title'] for c in citations}

# Find filenames that match (filename = title + ".txt")
matching_filenames = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    if title in citation_titles:
        matching_filenames.append(doc['filename'])

print(f"Total matching papers: {len(matching_filenames)}")
print("__RESULT__:")
print(json.dumps(matching_filenames))"""

env_args = {'var_function-call-8331430492114871094': 'file_storage/function-call-8331430492114871094.json', 'var_function-call-1820504185663630141': ['paper_docs'], 'var_function-call-16553614299134381618': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3493281973132824763': 'file_storage/function-call-3493281973132824763.json', 'var_function-call-14960290961413987657': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-13728953187963276153': 5, 'var_function-call-4296707544942016588': 'file_storage/function-call-4296707544942016588.json'}

exec(code, env_args)
