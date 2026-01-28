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

# Build a comprehensive CHI detection
chi_papers = {}

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    title_key = title.lower().strip()
    
    # Check multiple locations in the text for CHI
    # Check header, footer, and body
    text_upper = text.upper()
    
    # Look for CHI with conference context
    chi_conference_indicators = [
        'PROCEEDINGS OF THE CHI',
        'PROCEEDINGS OF THE ACM CHI',
        'CHI CONFERENCE',
        'CHI \'1',  # CHI '14, CHI '15, etc
        'CHI 20',   # CHI 2014, CHI 2015, etc
        'CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS'
    ]
    
    is_chi = any(indicator in text_upper for indicator in chi_conference_indicators)
    
    # Also check specific pattern: CHI followed by year near conference/proceedings
    if not is_chi:
        # Find CHI and check surrounding context
        chi_positions = [m.start() for m in re.finditer('CHI', text_upper)]
        for pos in chi_positions:
            context_start = max(0, pos - 200)
            context_end = min(len(text_upper), pos + 200)
            context = text_upper[context_start:context_end]
            
            if any(word in context for word in ['CONFERENCE', 'PROCEEDINGS', 'PAPER']):
                # Make sure it's not a citation or reference to another work
                if 'REFERENCE' not in context and 'CITATION' not in context:
                    # Check for year pattern (4 digits)
                    year_match = re.search(r'\d{4}', context)
                    if year_match:
                        year = int(year_match.group())
                        if 2000 <= year <= 2025:  # Reasonable year range
                            is_chi = True
                            break
    
    # Add to CHI papers if identified
    if is_chi:
        chi_papers[title_key] = {
            'original_title': title,
            'is_chi': True
        }

# Match citations with CHI papers
total_citation_count = 0
chi_papers_cited = []

for citation in citations_data:
    cite_title = citation['title'].lower().strip()
    citation_count = int(citation['citation_count'])
    
    if cite_title in chi_papers:
        total_citation_count += citation_count
        chi_papers_cited.append({
            'title': citation['title'],
            'citations_2020': citation_count
        })

result = {
    'total_citations': total_citation_count,
    'chi_papers_cited_count': len(chi_papers_cited)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'total_citation_count': 243, 'chi_papers_identified': 4, 'sample_chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16, 'venue': 'CHI'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77, 'venue': 'CHI'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52, 'venue': 'CHI'}]}, 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_count': 0}, 'var_functions.execute_python:14': {'total_citation_count': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:16': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'matched_papers_sample': []}, 'var_functions.execute_python:20': {'total_citation_count': 0, 'papers_analyzed': 188, 'chi_papers_identified': 0, 'chi_papers': []}, 'var_functions.execute_python:22': {'total_citations_for_chi_papers_in_2020': 0, 'number_of_chi_papers_cited': 0}, 'var_functions.execute_python:26': {'citation_titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'], 'paper_filenames_sample': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'total_citations': 188, 'total_papers': 5}}

exec(code, env_args)
