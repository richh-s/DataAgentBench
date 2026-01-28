code = """import json

# Load citations data for 2020
citations_file = locals()['var_functions.query_db:26']
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load all papers from MongoDB
papers_file = locals()['var_functions.query_db:8']
with open(papers_file, 'r') as f:
    all_papers = json.load(f)

print(f"Loaded {len(citations_2020)} citation records for 2020")
print(f"Loaded {len(all_papers)} papers from MongoDB")

# Create a set of titles that have 2020 citations
citation_titles = {c['title'] for c in citations_2020}

# Identify CHI papers and create a mapping
candidate_chi_papers = []
for doc in all_papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text_lower = text.lower()
    
    # Check if this is likely a CHI paper
    if 'chi' in text_lower:
        # Look for conference/proceedings indicators
        if 'conference' in text_lower or 'proceedings' in text_lower or 'acm' in text_lower:
            # Check if title matches any cited paper
            if title in citation_titles:
                candidate_chi_papers.append(title)

print(f"Found {len(candidate_chi_papers)} CHI papers with 2020 citations")

# Calculate total citations
chi_paper_citations = []
total_citation_count = 0

for citation in citations_2020:
    if citation['title'] in candidate_chi_papers:
        count = int(citation['citation_count'])
        chi_paper_citations.append({
            'title': citation['title'],
            'citation_count': count
        })
        total_citation_count += count

result = {
    'total_citation_count_2020': total_citation_count,
    'chi_papers_count': len(chi_paper_citations),
    'sample_papers': chi_paper_citations[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:2': [{'total_2020_citations': '188'}], 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': {'status': 'loaded', 'citations_count': 10, 'papers_count': 5}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
