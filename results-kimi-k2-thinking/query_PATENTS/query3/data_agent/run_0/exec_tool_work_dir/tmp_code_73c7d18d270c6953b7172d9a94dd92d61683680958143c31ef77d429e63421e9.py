code = """import json

# Load the UNIV CALIFORNIA data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    univ_california_data = json.load(f)

# Extract all unique cited publication numbers
all_cited_pubs = set()
for row in univ_california_data:
    citation_str = row['citation']
    if citation_str:
        try:
            citations = json.loads(citation_str)
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                if pub_num:
                    all_cited_pubs.add(pub_num)
        except:
            continue

print('__RESULT__:')
print(json.dumps({
    'total_cited_publications': len(all_cited_pubs),
    'sample_pubs': list(all_cited_pubs)[:20]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_records': 169, 'total_citations': 1308, 'sample': [{'publication_number': 'US-4599677-A', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2015129765-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'FR-3105380-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-11466906-B2', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2001053519-A1', 'source_patent': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}]}}

exec(code, env_args)
