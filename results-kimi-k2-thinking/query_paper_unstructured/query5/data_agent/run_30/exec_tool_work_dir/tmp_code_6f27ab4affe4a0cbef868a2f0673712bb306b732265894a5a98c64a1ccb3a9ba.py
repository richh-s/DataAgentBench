code = """import json
import re
from pathlib import Path

# Read the query results
# The citations for 2020 is stored in a file (too large), need to load it
if isinstance(var_functions.query_db:7, str) and var_functions.query_db:7.endswith('.json'):
    with open(var_functions.query_db:7, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = var_functions.query_db:7

# Load paper data from MongoDB
if isinstance(var_functions.query_db:9, str) and var_functions.query_db:9.endswith('.json'):
    with open(var_functions.query_db:9, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:9

# Create a mapping from title to citation count for 2020
citation_map = {item['title']: int(item['citation_count']) for item in citations_2020}

# Function to extract venue from paper text
# CHI papers typically have CHI mentioned in the header
chi_papers = []
chi_titles = []

for paper in paper_docs:
    # The title is the filename without .txt
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Check if this is a CHI paper by looking for CHI mentions
    # Common patterns: CHI 'XX, CHI, Proceedings of CHI, etc.
    if re.search(r'\bCHI\b', text, re.IGNORECASE):
        chi_papers.append(paper)
        chi_titles.append(title)

# Filter citations to only CHI papers and sum them
chi_citations = []
total_citations = 0

for title in chi_titles:
    if title in citation_map:
        count = citation_map[title]
        chi_citations.append((title, count))
        total_citations += count

# Also check for partial matches, in case titles differ slightly
citations_list = list(citation_map.items())
matched_citations = []
for title, count in citations_list:
    # Look for this title in CHI papers
    for chi_paper in chi_papers:
        chi_title = chi_paper['filename'].replace('.txt', '')
        if title.lower() == chi_title.lower():
            if (chi_title, count) not in matched_citations:
                matched_citations.append((chi_title, count))
            break
        # Also check if title is a substring or has fuzzy match
        parts = title.split(":")[0] if ":" in title else title
        if len(parts) > 5 and parts.lower() in chi_title.lower():
            if (chi_title, count) not in matched_citations:
                matched_citations.append((chi_title, count))
            break

# Sum unique matched citations
unique_citations = {}
for title, count in matched_citations:
    unique_citations[title] = count

total = sum(unique_citations.values())

result = {
    "total_citation_count": total,
    "chi_papers_with_citations_2020_count": len(unique_citations),
    "sample_papers": list(unique_citations.items())[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
