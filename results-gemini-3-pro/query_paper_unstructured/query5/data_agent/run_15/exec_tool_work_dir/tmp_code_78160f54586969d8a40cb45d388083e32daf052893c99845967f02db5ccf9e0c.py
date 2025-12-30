code = """import json

# Load citations
with open(locals()['var_function-call-15646429060027290344'], 'r') as f:
    citations = json.load(f)

# Extract titles and create filenames
filenames = [c['title'] + ".txt" for c in citations]

# Construct MongoDB query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-173807103424142885': ['Citations', 'sqlite_sequence'], 'var_function-call-173807103424140732': ['paper_docs'], 'var_function-call-173807103424142675': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-173807103424140522': 'file_storage/function-call-173807103424140522.json', 'var_function-call-17670429279864850901': [{'COUNT(*)': '188'}], 'var_function-call-5884279522157261639': 'file_storage/function-call-5884279522157261639.json', 'var_function-call-15646429060027290344': 'file_storage/function-call-15646429060027290344.json'}

exec(code, env_args)
