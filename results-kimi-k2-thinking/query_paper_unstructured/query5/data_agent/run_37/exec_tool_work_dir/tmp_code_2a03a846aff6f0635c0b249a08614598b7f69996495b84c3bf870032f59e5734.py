code = """import json
import re

# Read the full citations data from file path stored in variable
citations_file = '/tmp/tmpt9f7xy1o.json'
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents data from file path stored in variable  
papers_file = '/tmp/tmpf3y3n8l_.json'
paper_docs = []
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Process paper documents to extract CHI papers
chi_titles_set = set()
for doc in paper_docs:
    text = doc.get("text", "")
    filename = doc.get("filename", "")
    
    # Look for CHI venue patterns in the text
    chi_patterns = [
        r'CHI\s+[\'\"]?\d{2}\'?\d{2}?',  # CHI 'YY or CHI "YY
        r'\bCHI\b.*?\d{4}',  # CHI ... YYYY
        r'Proceedings of CHI',  # Proceedings of CHI
        r'CHI\s+Conference'  # CHI Conference
    ]
    
    has_chi = any(re.search(pattern, text, re.IGNORECASE) for pattern in chi_patterns)
    
    if has_chi:
        # Extract title from filename (remove .txt extension)
        title = filename.replace(".txt", "")
        chi_titles_set.add(title)

# Match citations with CHI papers and sum citation counts
total_citations = 0
matched_papers = []

for citation in citations_data:
    cite_title = citation.get("title", "")
    cite_count = int(citation.get("citation_count", 0))
    
    if cite_title in chi_titles_set:
        total_citations += cite_count
        matched_papers.append({"title": cite_title, "citations": cite_count})

# Sort by citation count
matched_papers.sort(key=lambda x: x["citations"], reverse=True)

result = {
    "total_citation_count": total_citations,
    "number_of_chi_papers_cited": len(matched_papers),
    "top_cited_chi_papers": matched_papers[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
