code = """import json
import os
import glob
import re

# Load citations data
citation_files = glob.glob('/tmp/*query_db*44*')
if citation_files:
    with open(citation_files[0], 'r') as f:
        all_citations = json.load(f)
else:
    # Try alternative file patterns
    alt_files = glob.glob('/tmp/*query_db*42*') + glob.glob('/tmp/*query_db*')
    if alt_files:
        with open(alt_files[0], 'r') as f:
            all_citations = json.load(f)
    else:
        all_citations = []

print('Loaded', len(all_citations), 'total citations (all years)')

# Filter for 2020
citations_2020 = [c for c in all_citations if str(c.get('citation_year', '')) == '2020']
print('Filtered to', len(citations_2020), 'citations from 2020')

# Load papers
paper_files = glob.glob('/tmp/*query_db*2*')
with open(paper_files[0], 'r') as f:
    papers = json.load(f)

print('Loaded', len(papers), 'papers')

# Use a comprehensive pattern to identify CHI papers
chi_paper_titles = set()
chi_papers_full = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Look for CHI venue indicators in the first 200 lines
    lines = text.split('\n')[:200]
    is_chi_paper = False
    year = None
    
    for line in lines:
        line_clean = line.strip()
        
        # Pattern 1: CHI with year (e.g., CHI 2020, CHI '20)
        match1 = re.search(r"CHI\s*['’]?\s*(20\d{2}|\d{2})\b|\b(20\d{2})\s*CHI", line_clean, re.IGNORECASE)
        
        # Pattern 2: CHI in conference context
        if 'CHI' in line_clean.upper():
            # Check if line has conference indicators
            has_conference_context = any(word in line_clean.upper() for word in [
                'PROCEEDINGS', 'CONFERENCE', 'PAPER', 'ACM', 'ISBN', 'DOI', 'SESSION'
            ])
            
            # Check if there's a year in the line
            year_match = re.search(r'\b(20\d{2})\b', line_clean)
            
            if match1:
                # Extract year from match1
                yr = match1.group(1) or match1.group(2)
                if yr:
                    year = int(yr) if len(yr) == 4 else int('20' + yr)
                    is_chi_paper = True
                    break
            elif has_conference_context and year_match:
                year = int(year_match.group(1))
                is_chi_paper = True
                break
    
    if is_chi_paper:
        chi_paper_titles.add(title.lower())
        chi_papers_full.append({
            'title': title,
            'year': year,
            'venue': 'CHI'
        })

print('Identified', len(chi_paper_titles), 'CHI papers by venue analysis')
print('Sample CHI papers:', list(chi_paper_titles)[:5])

# Match citations with CHI papers
total_citation_count = 0
matched_papers = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title:
        cite_title_lower = cite_title.lower()
        if cite_title_lower in chi_paper_titles:
            count = int(cite.get('citation_count', 0))
            total_citation_count += count
            matched_papers.append({
                'title': cite_title,
                'citations_in_2020': count
            })

# Sort by citation count
matched_papers.sort(key=lambda x: x['citations_in_2020'], reverse=True)

result = {
    'total_citation_count_for_chi_papers': total_citation_count,
    'number_of_chi_papers_cited_in_2020': len(matched_papers),
    'top_cited_chi_papers': matched_papers[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}}

exec(code, env_args)
