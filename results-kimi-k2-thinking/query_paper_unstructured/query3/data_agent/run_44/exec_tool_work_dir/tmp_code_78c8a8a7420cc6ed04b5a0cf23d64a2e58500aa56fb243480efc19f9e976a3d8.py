code = """import json

papers_path = locals()['var_functions.query_db:6']
with open(papers_path, 'r') as f:
    papers = json.load(f)

citations_path = locals()['var_functions.query_db:5']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Count unique titles in citations
unique_titles = set(cite['title'] for cite in citations)

# Final verification - iterate through all papers and check criteria
matching_papers = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    # Extract year
    import re
    year = None
    
    # Try multiple patterns
    patterns = [
        r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'(\d{2})",
        r'\b(20\d{2})\b',
        r'Copyright\s+(\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            if pattern == patterns[0]:
                year = 2000 + int(match.group(2))
            else:
                year = int(match.group(1) if match.group(1).startswith('20') else match.group(2))
            break
    
    # Calculate total citations
    total_citations = sum(int(cite['citation_count']) for cite in citations if cite['title'] == title)
    
    # Check if meets criteria
    if year and year > 2016 and has_empirical:
        matching_papers.append({
            'title': title,
            'year': year,
            'total_citation_count': total_citations
        })

# Also check what years we have for empirical papers
empirical_papers = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    if 'empirical' in text.lower():
        import re
        year = None
        patterns = [
            r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'(\d{2})",
            r'\b(20\d{2})\b',
            r'Copyright\s+(\d{4})'
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if pattern == patterns[0]:
                    year = 2000 + int(match.group(2))
                else:
                    year = int(match.group(1) if match.group(1).startswith('20') else match.group(2))
                break
        
        total_citations = sum(int(cite['citation_count']) for cite in citations if cite['title'] == title)
        
        empirical_papers.append({
            'title': title,
            'year': year,
            'total_citations': total_citations
        })

result = {
    'matching_papers': matching_papers,
    'all_empirical_papers': empirical_papers,
    'total_citation_records': len(citations),
    'citation_database_unique_titles': len(unique_titles),
    'mongo_db_papers': len(papers)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'num_citations': 1405, 'num_papers': 5}, 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'filtered_results': [], 'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 'unknown', 'contribution': [], 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 'unknown', 'contribution': [], 'citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 'unknown', 'contribution': [], 'citations': 452}]}, 'var_functions.execute_python:28': [], 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:34': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year_found': 'venue_pattern', 'year': 2015, 'has_empirical': False, 'meets_criteria': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year_found': 'copyright', 'year': 2010, 'has_empirical': False, 'meets_criteria': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True, 'meets_criteria': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_found': 'venue_pattern', 'year': 2014, 'has_empirical': True, 'meets_criteria': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_found': 'venue_pattern', 'year': 2011, 'has_empirical': False, 'meets_criteria': False}], 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json'}

exec(code, env_args)
