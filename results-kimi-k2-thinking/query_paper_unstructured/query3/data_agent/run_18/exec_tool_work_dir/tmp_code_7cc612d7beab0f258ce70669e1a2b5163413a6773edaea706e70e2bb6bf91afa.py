code = """import json
import os
import re

# Load citations data
citations_file = var_functions.query_db:44
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load papers data
papers_file = var_functions.query_db:41
with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f'Loaded {len(citations)} citation records and {len(papers)} papers')

# Extract unique citation titles for lookup
citation_titles = {c['title'].lower().strip(): {'title': c['title'], 'total_citations': int(c['total_citations'])} for c in citations}

def extract_paper_info(paper):
    """Extract title, year, and contribution type from paper document"""
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '').strip()
    text = paper.get('text', '')
    text_lower = text.lower()
    
    # Extract year - pattern matching for publication year in text
    year = None
    year_matches = re.findall(r'\b(20[0-9]{2})\b', text)
    if year_matches:
        # Use the earliest year found (publication year)
        year = int(min(year_matches))
    
    # Extract contribution type
    contribution = []
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower:
        contribution.append('methodological')
    
    return {
        'title': title,
        'year': year,
        'contributions': contribution
    }

# Process all papers
paper_info_list = [extract_paper_info(p) for p in papers]

# Filter papers: after 2016 and has empirical contribution
empirical_papers = [p for p in paper_info_list if p['year'] and p['year'] > 2016 and 'empirical' in p['contributions']]

print(f'Found {len(empirical_papers)} empirical papers after 2016')

# Find matching citations for these papers
results = []
for paper in empirical_papers:
    paper_title_lower = paper['title'].lower()
    
    # Check for exact match first
    if paper_title_lower in citation_titles:
        citation_data = citation_titles[paper_title_lower]
        results.append({
            'title': citation_data['title'],
            'total_citations': citation_data['total_citations']
        })
    else:
        # Try partial matching for similar titles
        for cit_title_lower, citation_data in citation_titles.items():
            if paper_title_lower in cit_title_lower or cit_title_lower in paper_title_lower:
                results.append({
                    'title': paper['title'],  # Use original paper title
                    'total_citations': citation_data['total_citations']
                })
                break

# Sort results by citation count descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print(f'Matched {len(results_sorted)} papers with citation data')

# Format output for result
output = '\n'.join([f"{r['title']}: {r['total_citations']} citations" for r in results_sorted])

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:28': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Affordances for Self-tracking Wearable Devices', 'total_citations': '195'}, {'title': 'An Anxious Alliance', 'total_citations': '370'}, {'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}, {'title': 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities', 'total_citations': '317'}, {'title': 'Balancing Accuracy and Fun: Designing Camera Based Mobile Games for Implicit Heart Rate Monitoring', 'total_citations': '345'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': '306'}], 'var_functions.execute_python:38': [], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:41': 'file_storage/functions.query_db:41.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
