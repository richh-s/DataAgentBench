code = """import json
import re
import os

# Get the file path for papers from the variable key
papers_key = 'var_functions.query_db:18'
citations_key = 'var_functions.query_db:28'

# Read the papers data (it's in the format '/tmp/...')
papers_file = '/tmp/tmpld3w_0o1.json'
if os.path.exists(papers_file):
    with open(papers_file, 'r') as f:
        papers = json.load(f)
else:
    # Try alternative paths
    papers_file = '/tmp/tmp4w0_0h5.json'
    if os.path.exists(papers_file):
        with open(papers_file, 'r') as f:
            papers = json.load(f)
    else:
        papers = []

print('Papers loaded:', len(papers))

# Read citations data (already in variable)
citations = var_functions.query_db:28
print('Citations loaded:', len(citations))

# Function to extract year from text
def extract_year(text):
    year_matches = re.findall(r'\b(20[0-9]{2})\b', text)
    if year_matches:
        return int(year_matches[0])
    return None

# Function to extract contribution type
def extract_contribution(text):
    text_lower = text.lower()
    contributions = []
    
    if 'empirical' in text_lower:
        contributions.append('empirical')
    if 'artifact' in text_lower:
        contributions.append('artifact')
    if 'theoretical' in text_lower:
        contributions.append('theoretical')
    if 'survey' in text_lower:
        contributions.append('survey')
    if 'methodological' in text_lower:
        contributions.append('methodological')
    
    return contributions

# Extract information from each paper
paper_info = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    year = extract_year(paper['text'])
    contributions = extract_contribution(paper['text'])
    
    paper_info.append({
        'title': title,
        'year': year,
        'contributions': contributions
    })

# Filter for papers after 2016 with empirical contribution
empirical_papers = [
    p for p in paper_info 
    if p['year'] and p['year'] > 2016 and 'empirical' in p['contributions']
]

print('Empirical papers after 2016:', len(empirical_papers))

# Create a dictionary of titles for lookup
titles_dict = {p['title'].lower(): p for p in empirical_papers}

# Find matching citations
results = []
for citation in citations:
    cit_title = citation['title']
   
title_lower = cit_title.lower()
    
    if title_lower in titles_dict:
        paper = titles_dict[title_lower]
        results.append({
            'title': cit_title,
            'total_citations': int(citation['total_citations'])
        })

print('Matching papers found:', len(results))

# Print results
if results:
    for r in results[:10]:
        print(f"{r['title']}: {r['total_citations']} citations")

result_json = json.dumps(results)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:28': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Affordances for Self-tracking Wearable Devices', 'total_citations': '195'}, {'title': 'An Anxious Alliance', 'total_citations': '370'}, {'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}, {'title': 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities', 'total_citations': '317'}, {'title': 'Balancing Accuracy and Fun: Designing Camera Based Mobile Games for Implicit Heart Rate Monitoring', 'total_citations': '345'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': '306'}]}

exec(code, env_args)
