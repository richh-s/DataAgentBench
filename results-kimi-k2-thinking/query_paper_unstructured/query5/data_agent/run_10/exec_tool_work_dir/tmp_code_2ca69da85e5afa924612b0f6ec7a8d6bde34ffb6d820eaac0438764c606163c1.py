code = """import json

# Get file paths from storage using locals()
citations_path = locals()['var_functions.query_db:5']
papers_path = locals()['var_functions.query_db:8']

print('Citations file path: ' + citations_path)
print('Papers file path: ' + papers_path)

# Load the data
with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Loaded ' + str(len(citations)) + ' citations from 2020')
print('Loaded ' + str(len(papers)) + ' papers')

# Build venue mapping
paper_venues = {}
venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    venue = None
    for v in venues:
        if v.lower() in text.lower():
            venue = v
            break
    paper_venues[title] = venue

# Count CHI papers and their citations
total_citations = 0
chi_count = 0

for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    if title in paper_venues and paper_venues[title] == 'CHI':
        total_citations += count
        chi_count += 1

result = {'total_citations_2020': total_citations, 'chi_papers_count': chi_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
