code = """import json
import re
import random

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

print(f"Total docs: {len(paper_docs)}")

# Print 3 random headers
print("--- Random Headers ---")
for doc in paper_docs[:3]:
    print(f"Title: {doc['filename']}")
    print(f"Header: {doc['text'][:300]}")
    print("---")

# Count occurrences of "CHI"
chi_counts = 0
chi_matches = []
for doc in paper_docs:
    if "CHI" in doc['text']:
        chi_counts += 1
        # Try to validate if it's the venue
        if re.search(r"CHI\s*['\u2019]?\d{2}", doc['text'][:500]):
            chi_matches.append(doc['filename'])

print(f"Docs containing 'CHI': {chi_counts}")
print(f"Docs with 'CHI YY' pattern in header: {len(chi_matches)}")
print(f"Sample CHI papers: {chi_matches[:5]}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16, 'var_function-call-17271081787061420733': 16, 'var_function-call-10439916293815859342': {'total_citations': 0, 'count': 0, 'titles': []}}

exec(code, env_args)
