code = """import json
import re

# Get citations data
citations_2020 = locals()['var_functions.query_db:0']
citations_count_info = locals()['var_functions.query_db:2']

# Get MongoDB file path and load papers
mongo_file_path = locals()['var_functions.query_db:8']
with open(mongo_file_path, 'r') as f:
    all_papers = json.load(f)

print('Loaded data:')
print(f'- Citations in 2020: {len(citations_2020)} records')
print(f'- Total papers in MongoDB: {len(all_papers)}')
print(f'- Total citations count in 2020: {citations_count_info[0]["total_2020_citations"]}')

# Create a set of paper titles from citations for fast lookup
citation_titles = set(c['title'] for c in citations_2020)
print(f'- Unique papers cited in 2020: {len(citation_titles)}')

# Find CHI papers in MongoDB
chi_paper_titles = []
chi_papers_full = []

for doc in all_papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Check if this appears to be a CHI paper
    text_lower = text.lower()
    
    # Simple check for CHI venue indicators
    if 'chi' in text_lower:
        if any(keyword in text_lower for keyword in ['proceedings', 'conference', 'acm']):
            # Additional verification - look for year patterns
            if re.search(r'chi\s*["\'\s]*(?:20\d{2}|\d{2})', text_lower, re.IGNORECASE):
                chi_paper_titles.append(title)
                chi_papers_full.append({
                    'title': title,
                    'text_preview': text[:200]
                })

print(f'- Papers identified as CHI: {len(chi_paper_titles)}')

# Now match CHI papers with 2020 citations
chi_citations_2020 = []
total_citations = 0

for citation in citations_2020:
    cite_title = citation['title']
    cite_count = int(citation['citation_count'])
    
    # Check if this paper is in our CHI papers list
    if cite_title in chi_paper_titles:
        chi_citations_2020.append({
            'title': cite_title,
            'citation_count': cite_count,
            'citation_year': 2020
        })
        total_citations += cite_count

print(f'- CHI papers cited in 2020: {len(chi_citations_2020)}')
print(f'- Total citations for CHI papers in 2020: {total_citations}')

# Save results
result = {
    'total_chi_papers_identified': len(chi_paper_titles),
    'chi_papers_cited_in_2020': len(chi_citations_2020),
    'total_citation_count_2020': total_citations,
    'detailed_citations': chi_citations_2020[:20]  # First 20 for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:2': [{'total_2020_citations': '188'}], 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
