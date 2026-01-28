code = """import json
import re

# Access stored data using locals()
# The previous query results are stored with specific keys
citations_data = locals().get('var_functions.query_db:7')
papers_data = locals().get('var_functions.query_db:9')

# Handle file paths if data is too large
import os
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Build citation map for 2020
citation_map = {}
for item in citations_2020:
    if 'title' in item and 'citation_count' in item:
        citation_map[item['title']] = int(item['citation_count'])

# Extract CHI papers from MongoDB documents
chi_titles = []
chi_paper_data = []

for paper in paper_docs:
    title = paper.get('filename', '').replace('.txt', '')
    text = paper.get('text', '')
    
    # Check if CHI venue is mentioned
    if re.search(r'\bCHI\b', text):
        chi_titles.append(title)
        chi_paper_data.append({
            'title': title,
            'text': text
        })

# Match CHI papers with citation data
matched_citations = {}

# First pass: direct exact matches (case-insensitive)
for chi_title in chi_titles:
    for cite_title, count in citation_map.items():
        if chi_title.lower() == cite_title.lower():
            matched_citations[chi_title] = count
            break

# Second pass: partial matches for titles that weren't exact matches
unmatched_chi = [t for t in chi_titles if t not in matched_citations]
for chi_title in unmatched_chi:
    chi_main = chi_title.split(':')[0].strip().lower()
    
    for cite_title, count in citation_map.items():
        cite_main = cite_title.split(':')[0].strip().lower()
        
        # Check if main parts match or one contains the other
        if chi_main == cite_main or chi_main in cite_main or cite_main in chi_main:
            # Verify it's a reasonable match
            if len(chi_main) > 10 and len(cite_main) > 10:
                matched_citations[chi_title] = count
                break

# Sum total citations
total_citations = sum(matched_citations.values())
num_papers = len(matched_citations)

# Prepare result
result = {
    "total_citation_count": total_citations,
    "chi_papers_cited_in_2020": num_papers,
    "sample_papers": list(matched_citations.items())[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
