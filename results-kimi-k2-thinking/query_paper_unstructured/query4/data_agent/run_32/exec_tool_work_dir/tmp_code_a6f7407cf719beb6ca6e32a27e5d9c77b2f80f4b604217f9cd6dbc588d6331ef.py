code = """import json, re

paper_docs_file = locals()['var_functions.query_db:2']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Count total papers and papers per year
years_count = {}
year_papers = {}
domain_papers = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    year_match = re.search(r'(\b(20|19)\d{2})\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    domains = []
    domain_keywords = ['physical activity', 'food', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    for keyword in domain_keywords:
        if keyword in text.lower():
            domains.append(keyword)
    
    if year:
        years_count[year] = years_count.get(year, 0) + 1
        if year not in year_papers:
            year_papers[year] = []
        year_papers[year].append({'title': title, 'domains': domains})
    
    if 'physical activity' in text.lower():
        domain_papers['physical activity'] = domain_papers.get('physical activity', 0) + 1

# Check papers from 2016 and physical activity
papers_2016 = year_papers.get(2016, [])
physical_activity_papers = [p for p in papers_2016 if 'physical activity' in p['domains']]

debug_info = {
    'total_papers': len(paper_docs),
    'years_distribution': {k: v for k, v in sorted(years_count.items())},
    'papers_2016_count': len(papers_2016),
    'physical_activity_count': sum(1 for p in paper_docs if 'physical activity' in p.get('text', '').lower()),
    'physical_activity_2016_count': len(physical_activity_papers),
    'sample_papers_2016_physical_activity': physical_activity_papers[:5]
}

print('__RESULT__:')
print(json.dumps(debug_info, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:21': []}

exec(code, env_args)
