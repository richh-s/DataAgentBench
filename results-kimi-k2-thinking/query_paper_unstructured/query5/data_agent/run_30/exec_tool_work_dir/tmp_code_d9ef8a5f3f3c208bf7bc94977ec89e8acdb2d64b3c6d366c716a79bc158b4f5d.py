code = """import json

# Load the full citations data for 2020
citations_path = var_functions.query_db:7
if isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = var_functions.query_db:7

# Load the paper documents data
papers_path = var_functions.query_db:9
if isinstance(papers_path, str) and papers_path.endswith('.json'):
    with open(papers_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:9

# Create citation map
citation_map = {}
for item in citations_2020:
    title = item.get('title', '')
    count = int(item.get('citation_count', 0))
    citation_map[title.lower()] = count

# Find CHI papers
chi_titles = []
for paper in paper_docs:
    text = paper.get('text', '').lower()
    # Look for CHI venue indicators
    if 'chi' in text[:2000]:  # Check first part of document
        # More specific checks to avoid false positives
        if any(marker in text[:2000] for marker in ['proceedings of chi', 'chi conference', 'acm chi', "chi '" ]):
            title = paper.get('filename', '').replace('.txt', '')
            chi_titles.append(title.lower())

# Match CHI papers with citations
matched_citations = {}
for chi_title in chi_titles:
    if chi_title in citation_map:
        matched_citations[chi_title] = citation_map[chi_title]
    else:
        # Try partial matching
        for cite_title, count in citation_map.items():
            if chi_title in cite_title or cite_title in chi_title:
                if len(chi_title) > 20:  # Only for reasonably long titles
                    matched_citations[chi_title] = count
                    break

total_citations = sum(matched_citations.values())
num_papers = len(matched_citations)

result = {
    "total_citation_count": total_citations,
    "chi_papers_cited_in_2020": num_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_cited_in_2020': 0, 'sample_papers': []}}

exec(code, env_args)
