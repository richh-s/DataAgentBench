code = """import json
import pandas as pd
import re
import os

# Access the paper data variable
paper_data_file = locals()['var_functions.query_db:8']
print(f"Loading paper data from: {paper_data_file}")

if not os.path.exists(paper_data_file):
    print(f"File not found: {paper_data_file}")
else:
    with open(paper_data_file, 'r') as f:
        papers = json.load(f)
    
    print(f"Loaded {len(papers)} papers")
    
    # Extract paper information
    paper_extract_list = []
    for paper in papers:
        title = paper['filename'].replace('.txt', '')
        text = paper['text']
        
        # Extract year - look for patterns that match conference years
        year = None
        year_matches = re.findall(r"'(\d{2})\b|201(\d)|202(\d)", text)
        if year_matches:
            # Flatten the matches and look for valid years
            years = []
            for match in year_matches:
                for item in match:
                    if item:
                        if len(item) == 2:  # '15 format
                            year_num = int('20' + item)
                            if 2010 <= year_num <= 2030:
                                years.append(year_num)
                        else:  # 2015 or 2020 format
                            year_num = int('201' + item if item in '0123456789' else item)
                            if 2010 <= year_num <= 2030:
                                years.append(year_num)
            
            if years:
                year = max(years)  # Take the most recent year found
        
        # Check for empirical contribution in text
        contribution = 'unknown'
        text_lower = text.lower()
        if 'empirical' in text_lower:
            contribution = 'empirical'
        elif 'this empirical' in text_lower or 'an empirical' in text_lower:
            contribution = 'empirical'
            
        paper_extract_list.append({
            'title': title,
            'year': year,
            'contribution': contribution,
            'has_empirical': 'empirical' in text_lower
        })
    
    # Create DataFrame
    df_papers = pd.DataFrame(paper_extract_list)
    print(f"Papers with empirical in text: {df_papers['has_empirical'].sum()}")
    print(f"Year distribution: {df_papers['year'].value_counts().sort_index().head(10).to_dict()}")
    
    # Filter for empirical papers after 2016
    empirical_papers_2017plus = df_papers[
        (df_papers['has_empirical'] == True) & 
        (df_papers['year'] > 2016)
    ]
    
    print(f"Empirical papers after 2016: {len(empirical_papers_2017plus)}")
    
    if len(empirical_papers_2017plus) > 0:
        print("Sample papers:")
        for idx, paper in empirical_papers_2017plus.head(5).iterrows():
            print(f"  - {paper['title']} ({paper['year']})")
    
    result = empirical_papers_2017plus[['title', 'year']].to_dict('records')
    print(f"__RESULT__:")
    print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
