code = """import json

# Read MongoDB filenames
with open(locals()['var_function-call-5679702400551775489'], 'r') as f:
    mongo_docs = json.load(f)
mongo_filenames = set(d['filename'] for d in mongo_docs)

# Read SQLite citations
with open(locals()['var_function-call-3465492661884944588'], 'r') as f:
    citations = json.load(f)

# Intersect
# SQLite has titles, Mongo has filenames = title + ".txt"
# Need to match title + ".txt"
target_filenames = []
for r in citations:
    fname = r['title'] + ".txt"
    if fname in mongo_filenames:
        target_filenames.append(fname)
    else:
        # Check if maybe there's a mismatch?
        pass

print(f"Found {len(target_filenames)} matching papers out of {len(citations)} citations.")

# Split into chunks of 50
chunks = []
chunk_size = 50
for i in range(0, len(target_filenames), chunk_size):
    chunks.append(target_filenames[i:i+chunk_size])

print("__RESULT__:")
print(json.dumps(chunks))"""

env_args = {'var_function-call-3465492661884944588': 'file_storage/function-call-3465492661884944588.json', 'var_function-call-5093555136357275627': 'file_storage/function-call-5093555136357275627.json', 'var_function-call-9313904331850907827': {'count': 158, 'filenames_preview': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}, 'var_function-call-13887185202303649787': 'file_storage/function-call-13887185202303649787.json', 'var_function-call-5679702400551775489': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
