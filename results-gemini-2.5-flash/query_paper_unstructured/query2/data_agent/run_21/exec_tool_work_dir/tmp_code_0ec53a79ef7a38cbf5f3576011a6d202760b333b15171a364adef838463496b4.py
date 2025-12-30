code = """import json

citations_data = json.load(open(locals()['var_function-call-8215253681165722155'], 'r'))
paper_docs_data = json.load(open(locals()['var_function-call-8418810907700332722'], 'r'))

paper_sources = []
for doc in paper_docs_data:
    title = doc['filename'].replace('.txt', '')
    source = 'Unknown'
    if 'ACM' in doc['text']:
        source = 'ACM'
    paper_sources.append({'title': title, 'source': source})

acm_papers = [paper for paper in paper_sources if paper['source'] == 'ACM']
acm_titles = {paper['title'] for paper in acm_papers}

acm_citations = []
for citation in citations_data:
    if citation['title'] in acm_titles:
        acm_citations.append(int(citation['citation_count']))


if len(acm_citations) > 0:
    average_citation_count = sum(acm_citations) / len(acm_citations)
else:
    average_citation_count = 0

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-8215253681165722155': 'file_storage/function-call-8215253681165722155.json', 'var_function-call-8418810907700332722': 'file_storage/function-call-8418810907700332722.json'}

exec(code, env_args)
