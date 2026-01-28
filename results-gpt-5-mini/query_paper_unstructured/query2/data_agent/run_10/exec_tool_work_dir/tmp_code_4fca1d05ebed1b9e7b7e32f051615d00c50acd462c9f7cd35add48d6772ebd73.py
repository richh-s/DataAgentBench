code = """import json
# Load the large citations result from the provided JSON file path
with open(var_call_WXMWXkxD6OZaPZYTlkk5zTo6, 'r') as f:
    citations = json.load(f)

# Load the paper filenames from the MongoDB query result (already in memory)
papers_docs = var_call_1exOBJY9zqCRE4CaMH3XBcO1

# Extract titles from filenames by stripping the .txt extension
paper_titles = [d['filename'].rsplit('.txt', 1)[0] for d in papers_docs]

# Find matching citation records for these titles for 2018
matches = []
for rec in citations:
    title = rec.get('title')
    cc = rec.get('citation_count')
    try:
        count = int(cc)
    except Exception:
        try:
            count = float(cc)
        except Exception:
            continue
    if title in paper_titles:
        matches.append({'title': title, 'citation_count': count})

if len(matches) == 0:
    avg = None
else:
    avg = sum(m['citation_count'] for m in matches) / len(matches)

out = {'average_citation_count': avg, 'num_papers': len(matches), 'papers': matches}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_WXMWXkxD6OZaPZYTlkk5zTo6': 'file_storage/call_WXMWXkxD6OZaPZYTlkk5zTo6.json', 'var_call_hBl8y7o9ToeaGxLxyMvviXIg': ['paper_docs'], 'var_call_1exOBJY9zqCRE4CaMH3XBcO1': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
