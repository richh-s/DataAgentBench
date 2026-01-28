code = """import json, re
papers_file = var_functions.query_db:12
with open(papers_file, 'r') as f:
    all_papers = json.load(f)
print('Loaded', len(all_papers), 'papers')
papers_2016_pa = []
for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    if not filename:
        continue
    title = filename.replace('.txt', '')
    year = None
    lines = text.split('\n')[:50]
    for line in lines:
        if '2016' in line:
            year = 2016
            break
        matches = re.findall(r'20\d{2}', line)
        for match in matches:
            if match == '2016':
                year = 2016
                break
        if year:
            break
    if year != 2016:
        continue
    text_lower = text.lower()
    title_lower = title.lower()
    keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'step count', 'activity tracking', 'walking', 'running', 'sports', 'fitbit', 'fitness tracker']
    in_title = any(kw in title_lower for kw in keywords)
    count_in_text = sum(text_lower.count(kw) for kw in keywords)
    if in_title or count_in_text >= 3:
        papers_2016_pa.append(title)
print('Found', len(papers_2016_pa), 'papers')
result = {'titles': papers_2016_pa}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
