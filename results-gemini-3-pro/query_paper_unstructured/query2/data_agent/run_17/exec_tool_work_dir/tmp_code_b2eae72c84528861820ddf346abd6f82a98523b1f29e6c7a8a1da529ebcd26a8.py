code = """import json
import os

# Load citations
with open(locals()['var_function-call-161273639758194169'], 'r') as f:
    citations_2018 = json.load(f)

# Load papers
with open(locals()['var_function-call-4266321762780779682'], 'r') as f:
    papers = json.load(f)

# Create a dictionary of title -> citation_count for 2018
# Note: citations_2018 is a list of dicts: {'title': ..., 'citation_count': ...}
citation_map = {c['title']: int(c['citation_count']) for c in citations_2018}

acm_citation_counts = []

for p in papers:
    # Extract title from filename
    filename = p.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if this paper was cited in 2018
    if title in citation_map:
        # Check if published by ACM
        # Heuristic: 'ACM' in text (first 2000 chars)
        text = p.get('text', '')
        if 'ACM' in text:
            acm_citation_counts.append(citation_map[title])

# Calculate average
if len(acm_citation_counts) > 0:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps({"average_citations": avg_citations, "count_acm_papers": len(acm_citation_counts), "total_citations_2018_papers": len(citation_map)}))"""

env_args = {'var_function-call-161273639758194169': 'file_storage/function-call-161273639758194169.json', 'var_function-call-161273639758192992': 'file_storage/function-call-161273639758192992.json', 'var_function-call-13120840873059324966': {'count': 158, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set']}, 'var_function-call-447886293380607187': 'file_storage/function-call-447886293380607187.json', 'var_function-call-7481131308563480348': 'file_storage/function-call-7481131308563480348.json', 'var_function-call-4266321762780779682': 'file_storage/function-call-4266321762780779682.json'}

exec(code, env_args)
