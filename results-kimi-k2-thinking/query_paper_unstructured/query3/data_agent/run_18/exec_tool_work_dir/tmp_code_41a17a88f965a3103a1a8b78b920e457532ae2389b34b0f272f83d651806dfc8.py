code = """import json, os, re, sys

# Get stored variable key for papers
papers_var = 'var_functions.query_db:18'
# This should be the file path string
papers_file = globals().get(papers_var)
if not papers_file:
    papers_file = locals().get(papers_var)

print('Papers file path:', papers_file)

# If not found, try to infer from tmp directory
if not papers_file or not isinstance(papers_file, str):
    tmp_files = [f for f in os.listdir('/tmp') if f.startswith('tmp') and f.endswith('.json')]
    if tmp_files:
        papers_file = os.path.join('/tmp', tmp_files[0])
        print('Inferred file path:', papers_file)

# Load papers data
if papers_file and os.path.exists(papers_file):
    with open(papers_file, 'r') as f:
        papers = json.load(f)
else:
    papers = []
    print('No papers file found')

print('Number of papers:', len(papers))

# Function to extract paper metadata
def extract_paper_metadata(paper):
    title = paper.get('filename', '').replace('.txt', '')
    text = paper.get('text', '')
    # Extract year - look in first part of text
    year_match = re.search(r'\b(20[0-9]{2})\b', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    return {'title': title, 'year': year, 'has_empirical': has_empirical}

# Extract metadata for all papers
paper_metadata = [extract_paper_metadata(p) for p in papers]

# Filter papers: after 2016 and has empirical contribution
filtered = [p for p in paper_metadata if p['year'] and p['year'] > 2016 and p['has_empirical']]

print('Filtered papers count:', len(filtered))

# Output result as JSON
result = json.dumps(filtered)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:28': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}, {'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 'total_citations': '91'}, {'title': 'Affordances for Self-tracking Wearable Devices', 'total_citations': '195'}, {'title': 'An Anxious Alliance', 'total_citations': '370'}, {'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}, {'title': 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities', 'total_citations': '317'}, {'title': 'Balancing Accuracy and Fun: Designing Camera Based Mobile Games for Implicit Heart Rate Monitoring', 'total_citations': '345'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'total_citations': '270'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': '306'}]}

exec(code, env_args)
