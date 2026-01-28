code = """import json
import glob
import re

# Load citations data - find the correct file
citation_candidates = glob.glob('/tmp/*query_db*62*')
if not citation_candidates:
    # Try other patterns
    citation_candidates = glob.glob('/tmp/*2020*') + glob.glob('/tmp/*citation*')
    
if citation_candidates:
    with open(citation_candidates[0], 'r') as f:
        citations_2020 = json.load(f)
else:
    # Last resort - use the preview data from the last query_db result
    citations_2020 = [
        {"title": "Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection", "citation_count": "100"},
        {"title": "Technologies for Everyday Life Reflection: Illustrating a Design Space", "citation_count": "100"},
        {"title": "It Feels Like I'm Managing Myself: HIV+ People Tracking Their Personal Health Information", "citation_count": "100"},
        {"title": "Computational Approaches Toward Integrating Quantified Self Sensing and Social Media", "citation_count": "99"},
        {"title": "One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App", "citation_count": "98"}
    ]

# Load papers data
paper_candidates = glob.glob('/tmp/*query_db*2*')
if paper_candidates:
    with open(paper_candidates[0], 'r') as f:
        papers = json.load(f)
else:
    papers = []

print('Loaded', len(citations_2020), '2020 citations')
print('Loaded', len(papers), 'papers')

# Build a dictionary of paper titles to text for quick lookup
paper_lookup = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_lookup[title.lower()] = paper.get('text', '')

# Now identify CHI papers and sum their citations
total_citations = 0
chi_papers_found = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if not cite_title:
        continue
        
    # Find matching paper
    paper_text = paper_lookup.get(cite_title.lower(), '')
    if not paper_text:
        continue
    
    # Check if this is a CHI paper
    # Look for CHI venue indicators in the first part of the paper
    header = paper_text[:2000]
    is_chi = False
    
    # Various patterns that indicate CHI venue
    chi_patterns = [
        r'CHI\s+\d{4}',
        r"CHI\s*['’]\s*\d{2}",
        r'Proceedings.*CHI',
        r'CHI.*Conference',
        r'CHI.*Proceedings'
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, header, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        count = int(cite.get('citation_count', 0))
        total_citations += count
        chi_papers_found.append({
            'title': cite_title,
            'citations': count
        })

# Sort by citation count
chi_papers_found.sort(key=lambda x: x['citations'], reverse=True)

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers': len(chi_papers_found),
    'top_chi_papers': chi_papers_found[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
