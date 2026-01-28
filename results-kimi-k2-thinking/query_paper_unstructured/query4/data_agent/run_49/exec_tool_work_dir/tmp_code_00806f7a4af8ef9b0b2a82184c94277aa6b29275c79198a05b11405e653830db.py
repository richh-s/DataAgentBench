code = """import json
import re
from pathlib import Path

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
    # Look for patterns like: YYYY, 'YY, or venue years
    year = None
    
    # Pattern 1: Look for 4-digit years around 2010-2020
    year_patterns = [
        r'(?:20|19)\d{2}',  # 4-digit years
        r"'\d{2}",  # 2-digit years with apostrophe
    ]
    
    # First, try to find year in venue header (common format: VENUE 'YY, ...)
    venue_match = re.search(r"[A-Z]+\s+'(\d{2}),\s+(\d{4})", text)
    if venue_match:
        year_str = venue_match.group(2)
        if 2010 <= int(year_str) <= 2025:
            year = int(year_str)
    
    # If not found, look for 4-digit years in the first few lines
    if not year:
        lines = text.split('\n')[:10]  # Check first 10 lines
        for line in lines:
            year_matches = re.findall(r'(?:20|19)\d{2}', line)
            for y in year_matches:
                y_int = int(y)
                if 2010 <= y_int <= 2025:
                    year = y_int
                    break
            if year:
                break
    
    # Extract domain information
    # Look for domain keywords in the text
    domain = None
    text_lower = text.lower()
    
    # Check for physical activity domain
    physical_activity_keywords = [
        'physical activity', 'fitness', 'exercise', 'workout', 'step count',
        'activity tracking', 'physical', 'walking', 'running', 'sports'
    ]
    
    # Also check the title
    title_lower = title.lower()
    
    # Count occurrences of physical activity keywords
    physical_activity_score = 0
    for keyword in physical_activity_keywords:
        if keyword in text_lower or keyword in title_lower:
            physical_activity_score += 1
    
    # If we find multiple physical activity keywords, classify as physical activity domain
    if physical_activity_score >= 2:
        domain = 'physical activity'
    elif physical_activity_score == 1 and any(kw in title_lower for kw in ['physical activity', 'fitness', 'exercise']):
        domain = 'physical activity'
    
    if title and year == 2016 and domain == 'physical activity':
        processed_papers.append({
            'title': title,
            'year': year,
            'domain': domain,
            'filename': filename
        })

print(f"Papers from 2016 in physical activity domain: {len(processed_papers)}")
for p in processed_papers[:5]:
    print(f"  - {p['title']}")

# Save results for next step
result = {
    'physical_activity_papers_2016': processed_papers,
    'count': len(processed_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
