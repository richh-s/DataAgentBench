code = """import json

papers = locals()['var_functions.query_db:2']
citations = locals()['var_functions.query_db:5']

print('Papers loaded:', len(papers))
print('Citations loaded:', len(citations))

food_papers = []
paper_title_map = {}

for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        paper_title_map[title] = paper
        
        text = paper.get('text', '').lower()
        if 'food' in text:
            food_papers.append(title)

print('Food papers found:', len(food_papers))

food_citations = []
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_papers:
        food_citations.append({
            'title': cit_title,
            'count': int(citation.get('citation_count', 0)),
            'year': citation.get('citation_year')
        })

total_citations = sum(fc['count'] for fc in food_citations)
print('Total food citations:', total_citations)

if food_citations:
    print('\nTop cited food papers:')
    sorted_papers = sorted(food_citations, key=lambda x: x['count'], reverse=True)
    for paper in sorted_papers[:5]:
        print(f"  {paper['title']}: {paper['count']} citations")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
