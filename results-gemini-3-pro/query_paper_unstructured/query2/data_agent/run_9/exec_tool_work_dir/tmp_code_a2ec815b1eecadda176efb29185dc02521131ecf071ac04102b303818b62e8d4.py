code = """import json

# Load citation filenames
file_path = locals()['var_function-call-17911279335149474793']
with open(file_path, 'r') as f:
    filenames = json.load(f)

# Batch 1: 0 to 80
batch1 = filenames[:80]

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

env_args = {'var_function-call-18015536077059182288': 'file_storage/function-call-18015536077059182288.json', 'var_function-call-869791821563470546': 158, 'var_function-call-17911279335149474793': 'file_storage/function-call-17911279335149474793.json', 'var_function-call-8120018053668087895': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-11498474745731372473': 5, 'var_function-call-18030763288875008701': 'file_storage/function-call-18030763288875008701.json', 'var_function-call-886812679702357317': 'file_storage/function-call-886812679702357317.json', 'var_function-call-4904106200708187765': 'file_storage/function-call-4904106200708187765.json'}

exec(code, env_args)
