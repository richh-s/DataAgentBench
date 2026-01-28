code = """import json
import re

# Get the papers data from storage
papers_raw = locals()['var_functions.query_db:18']

# Parse the papers data
papers_data = json.loads(papers_raw) if isinstance(papers_raw, str) else papers_raw

print(f"Processing {len(papers_data)} papers")

# Function to extract paper info and check for empirical contribution
def extract_paper_info(paper):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Get title from filename
    title = filename.replace('.txt', '').strip() if filename else ''
    
    # Extract year with multiple approaches
    year = None
    years = []
    
    # Look for 4-digit years (1900-2099) that are likely publication years
    year_matches = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    for ym in year_matches:
        y = int(ym)
        if 1900 <= y <= 2100:
            years.append(y)
    
    # Look for short years like '15, '16 etc.
    short_year_matches = re.findall(r"'\s*(\d{2})\s*[,\]]", text)
    for sm in short_year_matches:
        y = 2000 + int(sm) if int(sm) < 50 else 1900 + int(sm)
        if 1900 <= y <= 2100:
            years.append(y)
    
    if years:
        year = max(years)
    
    # Check if paper has empirical contribution
    has_empirical = False
    
    # Pattern 1: Direct mention of empirical
    if bool(re.search(r'\bempirical\b', text, re.IGNORECASE)):
        has_empirical = True
    
    # Pattern 2: Other empirical study indicators (more comprehensive)
    if not has_empirical:
        empirical_indicators = [
            r'\buser stud(?:y|ies)\b', r'\bfield stud(?:y|ies)\b', 
            r'\binterview[s]?\s*\([^)]*\d+[^)]*\)', r'\binterview[s]?\b(?!\s*\w)', 
            r'\bsurvey of\b', r'\bquestionnaire[s]?\b', 
            r'\bevaluation\b(?!\s*\w)', r'\bevaluated\b', 
            r'\bexperiment[s]?\b', r'\bexperimental\b', 
            r'\bparticipants?\b', r'\bsubjects?\b', 
            r'\bcase stud(?:y|ies)\b', r'\bqualitative stud(?:y|ies)\b',
            r'\bfollow[-\s]up stud(?:y|ies)\b', r'\blongitudinal stud(?:y|ies)\b',
            r'\bdesign stud(?:y|ies)\b', r'\bfocus group[s]?\b',
            r'\buser[\s-]centered\b', r'\bhuman[\s-]centered\b',
            r'\busability test[s]?\b', r'\bempirical data\b',
            r'\bdata collected\b', r'\bdata was gathered\b',
            r'\bstatistical analysis\b', r'\bhypothesis test[s]?\b'
        ]
        for pattern in empirical_indicators:
            if bool(re.search(pattern, text, re.IGNORECASE)):
                has_empirical = True
                break
    
    # Pattern 3: Check for study indicators in the text overall
    if not has_empirical:
        total_indicators = len(text.split())
        if any(word in text.lower() for word in ['study', 'evaluation', 'experiment']):
            study_indicators = []
            if 'study' in text.lower():
                # Count study mentions
                study_count = len(re.findall(r'\bstudy\b', text, re.IGNORECASE))
                study_indicators.append(study_count)
            if 'participant' in text.lower() or 'user' in text.lower():
                has_empirical = True
    
    return {
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'filename': filename
    }

# Process all papers
papers_info = []
for paper in papers_data:
    info = extract_paper_info(paper)
    if info['title'] and info['year']:
        papers_info.append(info)

# Filter for papers after 2016 with empirical contribution
empirical_papers = [p for p in papers_info if p['year'] > 2016 and p['has_empirical']]

print(f"Total papers processed: {len(papers_info)}")
print(f"Empirical papers after 2016: {len(empirical_papers)}")

# Show first few empirical papers
print("\nSample empirical papers after 2016:")
for p in empirical_papers[:10]:
    print(f"- {p['title']} (Year: {p['year']})")

# Prepare result for JSON output
result_data = {
    'papers_total': len(papers_info),
    'empirical_papers_after_2016_count': len(empirical_papers),
    'empirical_papers': [{'title': p['title'], 'year': p['year']} for p in empirical_papers]
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'total_processed': 99, 'empirical_after_2016': 0, 'sample_empirical': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
