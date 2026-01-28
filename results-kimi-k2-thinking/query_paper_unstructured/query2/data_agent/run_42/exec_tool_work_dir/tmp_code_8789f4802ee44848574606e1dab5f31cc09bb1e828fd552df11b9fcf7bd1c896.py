code = """import json
import re

# Load the citations and papers data
citations_file = locals()['var_functions.query_db:0']
papers_file = locals()['var_functions.query_db:2']

with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded {} citation records for 2018'.format(len(citations_2018)))
print('Loaded {} paper documents'.format(len(papers)))

# Find ACM papers
acm_paper_titles = set()
for paper in papers:
    if 'acm' in paper['text'].lower():
        title = paper['filename'].replace('.txt', '').lower()
        acm_paper_titles.add(title)

print('Found {} ACM papers'.format(len(acm_paper_titles)))

# Match with citations
acm_citations = []
for citation in citations_2018:
    title = citation['title'].lower()
    if title in acm_paper_titles:
        acm_citations.append(int(citation['citation_count']))

print('Found {} ACM papers cited in 2018'.format(len(acm_citations)))

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    print('Average citation count: {:.2f}'.format(avg_citations))
    print('Result ready for output')
else:
    print('No ACM papers found with 2018 citations')

# Prepare result for JSON output
result = {'average_citation_count': avg_citations if acm_citations else 0}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
