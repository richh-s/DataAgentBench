code = """import json
import re

# Read the paper documents file
papers_file = var_functions.query_db:0
with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Process papers to extract information
processed_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    year = None
    
    # Pattern 1: Look for year in venue header (common format: VENUE 'YY, MONTH DATE, YYYY)
    venue_match = re.search(r"[A-Z]+\s+'\d{2},\s+\w+\s+\d{1,2}\D{1,3}\d{4}", text)
    if venue_match:
        # Extract 4-digit year from the match
        year_str = re.search(r'(\d{4})', venue_match.group(0))
        if year_str:
            y_int = int(year_str.group(1))
            if 2010 <= y_int <= 2025:
                year = y_int
    
    # If not found, look for 4-digit years in the first 20 lines
    if not year:
        lines = text.split('\n')[:20]
        for line in lines:
            year_matches = re.findall(r'(?:20|19)\d{2}', line)
            for y in year_matches:
                y_int = int(y)
                if 2010 <= y_int <= 2025:
                    year = y_int
                    break
            if year:
                break
    
    # Extract domain information - check for physical activity
    domain = None
    text_lower = text.lower()
    title_lower = title.lower()
    
    # Physical activity keywords
    physical_activity_keywords = [
        'physical activity', 'fitness', 'exercise', 'workout', 'step count',
        'activity tracking', 'walking', 'running', 'sports', 'fitbit'
    ]
    
    # Count occurrences
    score = 0
    for keyword in physical_activity_keywords:
        if keyword in text_lower or keyword in title_lower:
            score += 1
    
    # If significant evidence, classify as physical activity
    if score >= 2:
        domain = 'physical activity'
    elif score == 1 and any(kw in title_lower for kw in ['physical activity', 'fitness', 'exercise']):
        domain = 'physical activity'
    
    # Check if paper is from 2016 and physical activity domain
    if title and year == 2016 and domain == 'physical activity':
        processed_papers.append({
            'title': title,
            'year': year,
            'domain': domain,
            'filename': filename
        })

print(f"Papers from 2016 in physical activity domain: {len(processed_papers)}")
for p in processed_papers:
    print(f"  - {p['title']}")

# Return result
result = {
    'physical_activity_papers_2016': processed_papers,
    'count': len(processed_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
