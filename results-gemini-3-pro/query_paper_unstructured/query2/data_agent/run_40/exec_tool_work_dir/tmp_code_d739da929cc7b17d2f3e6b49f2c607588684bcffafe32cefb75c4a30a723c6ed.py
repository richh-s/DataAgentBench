code = """import json

# Load citations
citations_path = locals()['var_function-call-7399957863239035507']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load paper docs
docs_path = locals()['var_function-call-3533404645208889558']
with open(docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Loaded {len(citations_data)} citation records.")
print(f"Loaded {len(paper_docs)} paper documents.")

citation_lookup = {c['title']: int(c['citation_count']) for c in citations_data}

acm_counts = []
matched_count = 0

for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        if title in citation_lookup:
            matched_count += 1
            text = doc.get('text', '')
            # Check for ACM
            # Look in the first 5000 chars
            header = text[:5000]
            if "ACM" in header or "Association for Computing Machinery" in header:
                acm_counts.append(citation_lookup[title])

print(f"Matched titles: {matched_count}")
print(f"ACM papers found: {len(acm_counts)}")

if len(acm_counts) > 0:
    avg_citations = sum(acm_counts) / len(acm_counts)
    print("__RESULT__:")
    print(json.dumps({"average_citations": avg_citations}))
else:
    print("__RESULT__:")
    print(json.dumps({"average_citations": 0}))"""

env_args = {'var_function-call-10677751840676979687': ['paper_docs'], 'var_function-call-10677751840676979600': ['Citations', 'sqlite_sequence'], 'var_function-call-7399957863239035507': 'file_storage/function-call-7399957863239035507.json', 'var_function-call-7399957863239036828': 'file_storage/function-call-7399957863239036828.json', 'var_function-call-2139143517697208341': {'average_citation_count': 68.5, 'count_papers': 2}, 'var_function-call-5835197415723081262': {'num_citations': 158, 'num_docs': 5, 'num_matched': 2, 'num_acm': 2, 'sample_non_acm': []}, 'var_function-call-16190191439772045651': 'file_storage/function-call-16190191439772045651.json', 'var_function-call-13217026804725367555': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-3533404645208889558': 'file_storage/function-call-3533404645208889558.json'}

exec(code, env_args)
