code = """import json
import re

# Get the papers data from storage
papers_data = locals()['var_functions.query_db:5']

# Check what it is first
print("Starting to process papers data...")

# Load if it's a file path
if isinstance(papers_data, str):
    print(f"Reading from file: {papers_data}")
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

print(f"Processing {len(papers_data)} papers")

# Extract paper information
def extract_paper_info(text, filename):
    # Get title from filename
    title = filename.replace('.txt', '').strip()
    
    # Extract year with multiple pattern matching
    year = None
    years = []
    
    # Pattern 1: Full years (2015, 2016, etc.)
    year_matches = re.findall(r'(?:20|19)\d{2}', text)
    for ym in year_matches:
        y = int(ym)
        if 1900 <= y <= 2100:
            years.append(y)
    
    # Pattern 2: Short form years ('15, '16, etc. - usually publication year)
    short_year_matches = re.findall(r"\'(\d{2})", text)
    for sm in short_year_matches:
        y = 2000 + int(sm) if int(sm) < 50 else 1900 + int(sm)
        if 1900 <= y <= 2100:
            years.append(y)
    
    if years:
        year = max(years)  # Usually the publication year is the newest one
    
    # Check for empirical contribution
    has_empirical = False
    
    # Pattern 1: Direct mention of "empirical"
    if bool(re.search(r'\bempirical\b', text, re.IGNORECASE)):
        has_empirical = True
    
    # Pattern 2: Other empirical study indicators
    if not has_empirical:
        empirical_indicators = [
            r'\buser study\b', r'\bfield study\b', r'\binterview[s]?\b',  
            r'\bsurvey of\b', r'\bquestionnaire[s]?\b', r'\bevaluation\b',
            r'\bexperiment[s]?\b', r'\bparticipants\b', r'\bcase study\b',
            r'\bdata collected\b', r'\bempirical data\b', r'\bqualitative study\b'
        ]
        for indicator in empirical_indicators:
            if bool(re.search(indicator, text, re.IGNORECASE)):
                has_empirical = True
                break
    
    return {'title': title, 'year': year, 'has_empirical': has_empirical}

# Process all papers
papers_with_info = []
for paper in papers_data:
    info = extract_paper_info(paper.get('text', ''), paper.get('filename', ''))
    # Only keep papers with title and year
    if info['title'] and info['year']:
        papers_with_info.append(info)

print(f"Successfully processed {len(papers_with_info)} papers")

# Filter for papers after 2016 with empirical contribution
empirical_papers_after_2016 = []
for p in papers_with_info:
    if p['year'] > 2016 and p['has_empirical']:
        empirical_papers_after_2016.append(p)

print(f"Found {len(empirical_papers_after_2016)} empirical papers after 2016")

# Show some samples
print(f"Sample empirical papers after 2016:")
for p in empirical_papers_after_2016[:5]:
    print(f"- {p['title']} (Year: {p['year']}, Empirical: {p['has_empirical']})")

# Create JSON response
result_data = {
    'total_processed': len(papers_with_info),
    'empirical_after_2016': len(empirical_papers_after_2016),
    'sample_empirical': empirical_papers_after_2016[:10]
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
