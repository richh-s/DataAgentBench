code = """import json
import re

# Load citations data from the actual file
# Find the correct file path for citations
citation_files = [
    '/tmp/var_functions.query_db:44',
    '/tmp/var_functions.query_db:16',
    '/tmp/var_functions.query_db:42'
]

citations_2020 = []
for path in citation_files:
    if os.path.exists(path):
        with open(path, 'r') as f:
            citations_2020 = json.load(f)
        break

print('Loaded citations for 2020, count:', len(citations_2020))

# Load papers data
papers_path = '/tmp/var_functions.query_db:2'
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Loaded papers, count:', len(papers))

# Extract CHI papers by analyzing text
chi_paper_titles = set()
chi_details = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Look for CHI venue in the text (case-insensitive)
    # Check first 100 lines for header information
    lines = text.split('\n')[:100]
    is_chi = False
    year = None
    
    for line in lines:
        line_upper = line.upper()
        # Look for CHI with various patterns
        if 'CHI' in line_upper:
            # Check for year patterns like CHI '20, CHI 2020, etc.
            year_match = re.search(r"CHI\s*['’]?\s*(20\d{2}|\d{2})\b|\b(20\d{2})\s*CHI", line, re.IGNORECASE)
            if year_match:
                yr = year_match.group(1) or year_match.group(2) or year_match.group(3)
                if yr:
                    if len(yr) == 2:
                        year = int('20' + yr)
                    else:
                        year = int(yr)
                    is_chi = True
                    break
            # Also check for CHI in proceedings/conference context
            elif any(indicator in line_upper for indicator in ['PROCEEDINGS', 'CONFERENCE', 'PAPER', 'SESSION']):
                # Extract year from nearby
                year_match = re.search(r'\b(20\d{2})\b', line)
                if year_match:
                    year = int(year_match.group(1))
                    is_chi = True
                    break
    
    if is_chi and year:
        chi_paper_titles.add(title.lower())
        chi_details.append({'title': title, 'year': year})

print('Found CHI papers:', len(chi_paper_titles))
print('Sample CHI papers:', list(chi_paper_titles)[:10])

# Match with citations and sum counts
total_citations = 0
matched_chi_citations = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_paper_titles:
        count = int(cite.get('citation_count', 0))
        total_citations += count
        matched_chi_citations.append({
            'title': cite_title,
            'citations_2020': count
        })

# Sort by citation count
matched_chi_citations.sort(key=lambda x: x['citations_2020'], reverse=True)

result = {
    'total_citation_count_for_chi_papers': total_citations,
    'number_of_chi_papers_cited': len(matched_chi_citations),
    'top_chi_papers_by_citations': matched_chi_citations[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
