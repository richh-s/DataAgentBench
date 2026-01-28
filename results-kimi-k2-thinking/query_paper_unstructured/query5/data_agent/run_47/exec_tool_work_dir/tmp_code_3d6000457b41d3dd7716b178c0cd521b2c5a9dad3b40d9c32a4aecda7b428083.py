code = """import json
import re

# Load all data
citations_file = locals()['var_functions.query_db:0']
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

papers_file = locals()['var_functions.query_db:4']
papers_data = []
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Build dictionary of CHI papers
chi_papers = {}

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Look for CHI conference patterns in the text
    text_upper = text.upper()
    
    # Patterns that indicate CHI conference paper
    chi_patterns = [
        'PROCEEDINGS OF THE CHI',
        'PROCEEDINGS OF THE ACM CHI',
        'CHI CONFERENCE',
        'CHI 20',
        'CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if pattern in text_upper:
            # Extra verification: look for year
            year_match = re.search(r'(20\d{2})', text_upper)
            if year_match:
                year = int(year_match.group(1))
                if 2010 <= year <= 2025:
                    is_chi = True
                    break
    
    if is_chi:
        title_key = title.lower().strip()
        chi_papers[title_key] = title

# Match citations with CHI papers
total_citations = 0
matched_chi_papers = []

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    cite_count = int(citation['citation_count'])
    
    if cite_title in chi_papers:
        total_citations += cite_count
        matched_chi_papers.append({
            'title': citation['title'],
            'citations': cite_count
        })

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': len(matched_chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:16': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'matched_papers_sample': []}, 'var_functions.execute_python:20': {'total_citation_count': 0, 'papers_analyzed': 188, 'chi_papers_identified': 0, 'chi_papers': []}, 'var_functions.execute_python:22': {'total_citations_for_chi_papers_in_2020': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:26': {'citation_titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'], 'paper_filenames_sample': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'total_citations': 188, 'total_papers': 5}}

exec(code, env_args)
