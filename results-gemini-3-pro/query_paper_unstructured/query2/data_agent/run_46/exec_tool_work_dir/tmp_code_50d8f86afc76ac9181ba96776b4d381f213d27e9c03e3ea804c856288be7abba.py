code = """import json
file_path = locals()['var_function-call-6474308532486273444']
with open(file_path, 'r') as f:
    filenames = json.load(f)

# Split into 2 batches
batch1 = filenames[:80]
batch2 = filenames[80:]

query1 = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": batch1},
        "text": {"$regex": "ACM"}
    },
    "projection": {"filename": 1}
}

query2 = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": batch2},
        "text": {"$regex": "ACM"}
    },
    "projection": {"filename": 1}
}

print("__RESULT__:")
print(json.dumps([json.dumps(query1), json.dumps(query2)]))"""

env_args = {'var_function-call-4970464269223372421': 'file_storage/function-call-4970464269223372421.json', 'var_function-call-6474308532486273444': 'file_storage/function-call-6474308532486273444.json', 'var_function-call-8662636658253547831': 158, 'var_function-call-2887577120062876127': 'file_storage/function-call-2887577120062876127.json', 'var_function-call-1763755718692513152': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-9878315296097800506': 'file_storage/function-call-9878315296097800506.json', 'var_function-call-9092742365924836319': 'file_storage/function-call-9092742365924836319.json', 'var_function-call-7113279303859906017': 'file_storage/function-call-7113279303859906017.json', 'var_function-call-15100215538405544922': 'file_storage/function-call-15100215538405544922.json', 'var_function-call-14168744166593217509': 'file_storage/function-call-14168744166593217509.json'}

exec(code, env_args)
