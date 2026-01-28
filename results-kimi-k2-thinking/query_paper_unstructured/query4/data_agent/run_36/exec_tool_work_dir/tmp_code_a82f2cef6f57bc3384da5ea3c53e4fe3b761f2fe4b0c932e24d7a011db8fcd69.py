code = """import json
import re
import pandas as pd

# Load the full data
citations_path = locals()['var_functions.query_db:6']
citations_df = pd.read_json(citations_path)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'], errors='coerce')
citations_df = citations_df[citations_df['total_citations'].notnull()]

papers_path = locals()['var_functions.query_db:7']
papers_df = pd.read_json(papers_path)

# More comprehensive paper processing
paper_info = []
domain_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'steps', 'workout', 'walking', 'running']

for idx, paper in papers_df.iterrows():
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - multiple attempts
    year = None
    
    # Look for conference/journal headers
    text_start = text[:3000]
    
    # Look for year patterns
    year_patterns = [
        # Conference headers like "CHI 2016"
        r'(?:CHI|CHI Conference|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*[\'"\s]?\s*(2016)',
        # Year anywhere
        r'\b(2016)\b'
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text_start, re.IGNORECASE)
        if matches:
            year = int(matches[0])
            break
    
    # Check for physical activity domain
    text_lower = text.lower()
    is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
    
    if title and year == 2016 and is_physical_activity:
        paper_info.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

paper_info_df = pd.DataFrame(paper_info)

if not paper_info_df.empty:
    # Merge with citations
    merged_df = paper_info_df.merge(
        citations_df[['title', 'total_citations']], 
        on='title', 
        how='left'
    )
    merged_df['total_citations'] = merged_df['total_citations'].fillna(0).astype(int)
    result_df = merged_df.sort_values('total_citations', ascending=False)
    output = result_df.to_dict('records')
    output_message = f'Found {len(paper_info_df)} papers from 2016 in physical activity domain'
else:
    # Debug: Find all 2016 papers and all physical activity papers
    all_2016 = []
    all_pa = []
    
    for idx, paper in papers_df.iterrows():
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        title = filename.replace('.txt', '') if filename else ''
        
        text_start = text[:3000]
        year = 2016 if re.search(r'\b(2016)\b', text_start) else None
        
        text_lower = text.lower()
        is_pa = any(keyword in text_lower for keyword in domain_keywords)
        
        if year == 2016:
            all_2016.append(title)
        if is_pa:
            all_pa.append(title)
    
    output = {
        'message': 'No 2016 physical activity papers found',
        'papers_2016_count': len(all_2016),
        'pa_papers_count': len(all_pa),
        'papers_2016_sample': all_2016[:10],
        'pa_papers_sample': all_pa[:10]
    }

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'total_papers_checked': 5, 'papers_from_2016': 0, 'physical_activity_papers': 5, 'physical_activity_2016': 0, 'sample_2016_papers': [], 'sample_pa_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity': True}], 'sample_pa_2016_papers': []}}

exec(code, env_args)
