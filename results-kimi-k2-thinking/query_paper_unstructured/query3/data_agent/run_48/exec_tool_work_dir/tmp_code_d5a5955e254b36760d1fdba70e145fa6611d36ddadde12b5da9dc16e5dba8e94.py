code = """import json
import os
import re

# First, let's see what's available in the environment
available_vars = [name for name in dir() if 'var_' in name or 'query' in name]
print("Available variables:", available_vars)

# Check if var_functions.query_db:2 exists and contains the file path
if 'var_functions.query_db:2' in dir():
    paper_docs_path = locals()['var_functions.query_db:2']
    print(f"Paper docs path: {paper_docs_path}")
    
    # Read the paper documents
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
    
    print(f"Loaded {len(paper_docs)} paper documents")
    
    # Extract information
    papers_info = []
    for doc in paper_docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        # Extract title
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        
        # Extract year
        year = None
        year_match = re.search(r"(20[12][0-9])", text[:1000])
        if year_match:
            year = int(year_match.group(1))
        
        # Extract contribution type
        contribution = None
        text_lower = text.lower()
        if 'empirical' in text_lower:
            contribution = 'empirical'
        elif 'theoretical' in text_lower:
            contribution = 'theoretical'
        elif 'survey' in text_lower:
            contribution = 'survey'
        elif 'system' in text_lower or 'prototype' in text_lower:
            if 'design' in text_lower or 'develop' in text_lower:
                contribution = 'artifact'
        
        papers_info.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })
    
    # Filter empirical papers after 2016
    empirical_papers = [p for p in papers_info if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]
    
    print(f"Empirical papers after 2016: {len(empirical_papers)}")
    for p in empirical_papers[:5]:
        print(f"  {p['title']} ({p['year']})")
    
else:
    print("var_functions.query_db:2 not found")
    # List all variables to see what's available
    for name, value in locals().items():
        if 'functions' in str(name):
            print(f"{name}: {value}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
