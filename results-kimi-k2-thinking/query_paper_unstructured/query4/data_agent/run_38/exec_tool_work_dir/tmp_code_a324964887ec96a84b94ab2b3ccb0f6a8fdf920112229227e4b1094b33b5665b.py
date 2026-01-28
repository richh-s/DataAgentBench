code = """import json
import re
import pandas as pd

# Get file paths
paper_docs_file = locals()['var_functions.query_db:8']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract years and basic info from all papers
years_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Try multiple patterns for year extraction
    year = None
    
    # Pattern 1: Look for 4-digit years in first 5000 chars
    year_matches = re.findall(r"\b(20\d{2})\b", text[:5000])
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    # Pattern 2: Look for conference year notation like '16 or "16
    if not year:
        conf_matches = re.findall(r"[\'\"](\d{2})[\'\"]", text[:2000])
        for match in conf_matches:
            year_int = 2000 + int(match)
            if 2010 <= year_int <= 2025:
                year = year_int
                break
    
    # Pattern 3: Look for explicit year mentions
    if not year:
        year_patterns = re.findall(r"(?:year|Year|YEAR)\s*[:]?\s*(20\d{2})", text[:2000])
        if year_patterns:
            year = int(year_patterns[0])
    
    years_info.append({
        'title': title,
        'year': year
    })

# Analyze years
df_years = pd.DataFrame(years_info)
print("Year distribution:")
print(df_years['year'].value_counts().sort_index())

# Check for 2016 papers
papers_2016 = df_years[df_years['year'] == 2016]
print(f"\nFound {len(papers_2016)} papers from 2016")

# Check first few 2016 papers
if not papers_2016.empty:
    print("\nFirst few 2016 papers:")
    for _, paper in papers_2016.head(10).iterrows():
        print(f"  - {paper['title'][:80]}...")

# Also check for physical activity papers across all years
all_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Check for physical activity domain (more lenient)
    text_lower = text.lower()
    has_physical_activity = any(keyword in text_lower for keyword in 
                                ['physical activity', 'fitness', 'exercise', 
                                 'step count', 'walking', 'running', 'activity tracker'])
    
    if has_physical_activity:
        # Extract year for these papers
        year_matches = re.findall(r"\b(20\d{2})\b", text[:5000])
        year = None
        if year_matches:
            valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
            if valid_years:
                year = min(valid_years)
        
        all_papers.append({
            'title': title,
            'year': year,
            'has_pa': has_physical_activity
        })

df_pa = pd.DataFrame(all_papers)
print(f"\n\nFound {len(df_pa)} papers with physical activity content across all years")
print("Year distribution for physical activity papers:")
print(df_pa['year'].value_counts().sort_index())

# Check 2016 specifically
pa_2016 = df_pa[df_pa['year'] == 2016]
print(f"\nPhysical activity papers from 2016: {len(pa_2016)}")

output = pa_2016.to_dict('records')
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': []}

exec(code, env_args)
