code = """import json
import re

# Load data
citations_path = locals()['var_function-call-10128853651664279531']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

acm_papers_path = locals()['var_function-call-2153954921317662099']
with open(acm_papers_path, 'r') as f:
    acm_papers_data = json.load(f)

# Helper to normalize
def normalize(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

# Map normalized title to (original title, citation count)
# Handling potential duplicates? (unlikely for title)
citation_map = {}
for item in citations_data:
    norm = normalize(item['title'])
    citation_map[norm] = int(item['citation_count'])

matched_counts = []
matched_details = []

for paper in acm_papers_data:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        norm_title = normalize(title)
        
        if norm_title in citation_map:
            count = citation_map[norm_title]
            matched_counts.append(count)
            matched_details.append((title, count))
        else:
            # Check if it was close?
            pass

print("__RESULT__:")
print(json.dumps({
    "matches": len(matched_counts),
    "average": sum(matched_counts)/len(matched_counts) if matched_counts else 0,
    "details": matched_details
}))"""

env_args = {'var_function-call-10128853651664279531': 'file_storage/function-call-10128853651664279531.json', 'var_function-call-13767594165860701791': 'file_storage/function-call-13767594165860701791.json', 'var_function-call-447385373725122589': 'file_storage/function-call-447385373725122589.json', 'var_function-call-2153954921317662099': 'file_storage/function-call-2153954921317662099.json', 'var_function-call-2779362211671997774': {'matched_papers_count': 2, 'average_citations': 68.5}, 'var_function-call-18204126579925751486': {'count_citations_2018': 158, 'count_acm_papers_returned': 5, 'count_intersection': 2, 'sample_citation_titles': ['Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Problematising Upstream Technology Through Speculative Design: The Case of Quantified Cats and Dogs', 'Quantified Construction of Self: Numbers, Narratives and the Modern Individual', 'Supporting Learning by Considering Emotions: Tracking and Visualization a Case Study', 'Understanding the Cost of Driving Trips'], 'sample_acm_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Stage-based Model of Personal Informatics Systems', 'A Lived Informatics Model of Personal Informatics', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-1895846447207820443': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5330953167614813920': ['paper_docs']}

exec(code, env_args)
