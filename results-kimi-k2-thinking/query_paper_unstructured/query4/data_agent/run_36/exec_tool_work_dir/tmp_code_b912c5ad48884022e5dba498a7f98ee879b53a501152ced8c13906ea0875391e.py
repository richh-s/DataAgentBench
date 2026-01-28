code = """import json
import re
import pandas as pd

# Load the data using proper variable references
citations_path = locals()['var_functions.query_db:6']
citations_df = pd.read_json(citations_path)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'], errors='coerce')
citations_df = citations_df[citations_df['total_citations'].notnull()]

papers_path = locals()['var_functions.query_db:7']
papers_df = pd.read_json(papers_path)

# Extract paper information
paper_info = []
for _, paper in papers_df.iterrows():
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    year = None
    year_match = re.search(r'\b(20\d{2})\b', text[:2000])
    if year_match:
        potential_year = int(year_match.group(1))
        if 2010 <= potential_year <= 2023:
            year = potential_year
    
    # Check for physical activity domain
    domain_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'steps']
    text_lower = text.lower()
    is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
    
    if title and year == 2016 and is_physical_activity:
        paper_info.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

paper_info_df = pd.DataFrame(paper_info)

# Merge with citation data
if not paper_info_df.empty:
    merged_df = paper_info_df.merge(
        citations_df[['title', 'total_citations']], 
        on='title', 
        how='left'
    )
    merged_df['total_citations'] = merged_df['total_citations'].fillna(0).astype(int)
    result_df = merged_df.sort_values('total_citations', ascending=False)
    output = result_df.to_dict('records')
else:
    # More thorough search for debugging
    sample_results = []
    for _, paper in papers_df.iterrows():
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        title = filename.replace('.txt', '') if filename else ''
        
        # Get year
        year_match = re.search(r'\b(20\d{2})\b', text[:2000])
        year = int(year_match.group(1)) if year_match else None
        
        # Check for physical activity
        domain_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'steps']
        text_lower = text.lower()
        is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
        
        sample_results.append({
            'title': title,
            'year': year,
            'is_physical_activity': is_physical_activity
        })
    
    papers_2016 = [p for p in sample_results if p['year'] == 2016]
    pa_papers = [p for p in sample_results if p['is_physical_activity']]
    pa_2016 = [p for p in sample_results if p['year'] == 2016 and p['is_physical_activity']]
    
    debug_info = {
        'total_papers_checked': len(sample_results),
        'papers_from_2016': len(papers_2016),
        'physical_activity_papers': len(pa_papers),
        'physical_activity_2016': len(pa_2016),
        'sample_2016_papers': papers_2016[:5],
        'sample_pa_papers': pa_papers[:5],
        'sample_pa_2016_papers': pa_2016
    }
    output = debug_info

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
