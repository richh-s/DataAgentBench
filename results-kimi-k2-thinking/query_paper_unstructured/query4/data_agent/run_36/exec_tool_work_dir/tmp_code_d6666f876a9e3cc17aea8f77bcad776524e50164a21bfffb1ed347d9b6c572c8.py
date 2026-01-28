code = """import json
import re
import pandas as pd

# Load the citations data
citations_path = var_functions.query_db:6
citations_df = pd.read_json(citations_path)
try:
    citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'], errors='coerce')
    citations_df = citations_df[citations_df['total_citations'].notnull()]
except Exception as e:
    print(f'Error processing citations: {e}')

# Load the paper documents
papers_path = var_functions.query_db:7
papers_df = pd.read_json(papers_path)

# Extract paper information
paper_info = []
for _, paper in papers_df.iterrows():
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text (look for patterns like '2016', 'CHI 2016', etc.)
    year = None
    year_patterns = [
        r'\b(20\d{2})\b',  # Year 2000-2099
        r'(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*[\'"]?\s*(20\d{2})'
    ]
    
    text_start = text[:2000]  # Look in first 2000 chars
    for pattern in year_patterns:
        matches = re.findall(pattern, text_start)
        if matches:
            for match in matches:
                if 2010 <= int(match) <= 2023:  # Reasonable range
                    year = int(match)
                    break
        if year:
            break
    
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

# If we have papers, join with citations
if not paper_info_df.empty:
    # Merge with citations
    merged_df = paper_info_df.merge(
        citations_df[['title', 'total_citations']], 
        on='title', 
        how='left'
    )
    
    # Fill NaN citations with 0
    merged_df['total_citations'] = merged_df['total_citations'].fillna(0).astype(int)
    
    # Sort by citations descending
    result_df = merged_df.sort_values('total_citations', ascending=False)
    
    output = result_df.to_dict('records')
else:
    # Check if we need to examine the data more carefully
    sample_papers = []
    for i, (_, paper) in enumerate(papers_df.iterrows()):
        if i >= 20:  # Check first 20 papers
            break
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        title = filename.replace('.txt', '')
        
        # Extract year
        year_match = re.search(r'\b(20\d{2})\b', text[:2000])
        year = int(year_match.group(1)) if year_match else None
        
        # Check for physical activity
        text_lower = text.lower()
        is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
        
        sample_papers.append({
            'title': title,
            'year': year,
            'is_physical_activity': is_physical_activity
        })
    
    # Check if any are from 2016 and physical activity
    papers_2016_pa = [p for p in sample_papers if p['year'] == 2016 and p['is_physical_activity']]
    
    if papers_2016_pa:
        # Process all papers again with this approach
        paper_info = []
        for _, paper in papers_df.iterrows():
            filename = paper.get('filename', '')
            text = paper.get('text', '')
            
            title = filename.replace('.txt', '') if filename else ''
            
            # Extract year
            year_match = re.search(r'\b(20\d{2})\b', text[:2000])
            year = int(year_match.group(1)) if year_match else None
            
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
        
        # Merge with citations
        merged_df = paper_info_df.merge(
            citations_df[['title', 'total_citations']], 
            on='title', 
            how='left'
        )
        
        merged_df['total_citations'] = merged_df['total_citations'].fillna(0).astype(int)
        result_df = merged_df.sort_values('total_citations', ascending=False)
        
        output = result_df.to_dict('records')
    else:
        output = f"No papers found for 2016 physical activity domain. Sample checked: {len(sample_papers)} papers.\nPapers from 2016: {[p for p in sample_papers if p['year'] == 2016][:5]}\nPhysical activity papers: {[p for p in sample_papers if p['is_physical_activity']][:5]}"

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
