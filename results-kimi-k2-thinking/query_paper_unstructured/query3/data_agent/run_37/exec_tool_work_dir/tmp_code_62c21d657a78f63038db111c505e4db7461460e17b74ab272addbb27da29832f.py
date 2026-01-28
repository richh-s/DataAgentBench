code = """import json, re

# Load paper data
mongo_file = var_functions.query_db:2
with open(mongo_file, 'r') as f:
    papers = json.load(f)

print('Papers loaded:', len(papers))

empirical_paper_data = []

for paper in papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    # Extract year - look for 4-digit year patterns
    year = None
    # Try venue patterns first
    patterns = [
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)[\s\'"]+(\d{2})(\d{2})?',
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s+(20\d{2})'
    ]
    
    first_part = text[:3000]
    for pattern in patterns:
        m = re.search(pattern, first_part, re.IGNORECASE)
        if m:
            # Extract full year
            year_str = m.group(0)
            year_match = re.search(r'20\d{2}', year_str)
            if year_match:
                year = int(year_match.group())
                break
    
    if not year:
        # Fallback: any 4-digit year starting with 20
        m = re.search(r'20\d{2}', first_part)
        if m:
            year = int(m.group())
    
    if not year or year <= 2016:
        continue
    
    # Check for empirical contribution
    search_text = text[:8000].lower()
    has_empirical = False
    
    # Simple check for empirical in contribution context
    if 'empirical' in search_text and 'contribution' in search_text:
        has_empirical = True
    elif 'empirical study' in search_text or 'empirical research' in search_text:
        has_empirical = True
    elif 'empirical' in search_text:
        # Check if empirical appears multiple times (more likely to be empirical contribution)
        empirical_count = search_text.count('empirical')
        if empirical_count >= 3:
            has_empirical = True
    
    if has_empirical:
        empirical_paper_data.append({'title': title, 'year': year})

print('Empirical papers after 2016:', len(empirical_paper_data))
print('Sample:', empirical_paper_data[:3])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:22': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
