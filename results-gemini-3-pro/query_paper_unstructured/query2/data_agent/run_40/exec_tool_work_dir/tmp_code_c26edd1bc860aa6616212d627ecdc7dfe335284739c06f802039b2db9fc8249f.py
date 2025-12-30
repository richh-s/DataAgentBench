code = """import json

citations_path = locals()['var_function-call-7399957863239035507']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

docs_path = locals()['var_function-call-3533404645208889558']
with open(docs_path, 'r') as f:
    paper_docs = json.load(f)

citation_lookup = {c['title']: int(c['citation_count']) for c in citations_data}

acm_counts_5000 = []
acm_counts_2000 = []
ieee_overlap = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        if title in citation_lookup:
            text = doc.get('text', '')
            
            is_acm_5000 = "ACM" in text[:5000] or "Association for Computing Machinery" in text[:5000]
            is_acm_2000 = "ACM" in text[:2000] or "Association for Computing Machinery" in text[:2000]
            
            is_ieee_2000 = "IEEE" in text[:2000]

            if is_acm_5000:
                acm_counts_5000.append(citation_lookup[title])
            
            if is_acm_2000:
                acm_counts_2000.append(citation_lookup[title])
                if is_ieee_2000:
                    ieee_overlap.append(title)

print(f"ACM (5000 chars): {len(acm_counts_5000)} papers, Avg: {sum(acm_counts_5000)/len(acm_counts_5000) if acm_counts_5000 else 0}")
print(f"ACM (2000 chars): {len(acm_counts_2000)} papers, Avg: {sum(acm_counts_2000)/len(acm_counts_2000) if acm_counts_2000 else 0}")
print(f"Papers with both ACM and IEEE in first 2000 chars: {len(ieee_overlap)}")
if ieee_overlap:
    print(f"Sample overlap: {ieee_overlap[:3]}")

print("__RESULT__:")
print(json.dumps({"avg_5000": sum(acm_counts_5000)/len(acm_counts_5000) if acm_counts_5000 else 0}))"""

env_args = {'var_function-call-10677751840676979687': ['paper_docs'], 'var_function-call-10677751840676979600': ['Citations', 'sqlite_sequence'], 'var_function-call-7399957863239035507': 'file_storage/function-call-7399957863239035507.json', 'var_function-call-7399957863239036828': 'file_storage/function-call-7399957863239036828.json', 'var_function-call-2139143517697208341': {'average_citation_count': 68.5, 'count_papers': 2}, 'var_function-call-5835197415723081262': {'num_citations': 158, 'num_docs': 5, 'num_matched': 2, 'num_acm': 2, 'sample_non_acm': []}, 'var_function-call-16190191439772045651': 'file_storage/function-call-16190191439772045651.json', 'var_function-call-13217026804725367555': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-3533404645208889558': 'file_storage/function-call-3533404645208889558.json', 'var_function-call-3491883231450755483': {'average_citations': 59.75471698113208}}

exec(code, env_args)
