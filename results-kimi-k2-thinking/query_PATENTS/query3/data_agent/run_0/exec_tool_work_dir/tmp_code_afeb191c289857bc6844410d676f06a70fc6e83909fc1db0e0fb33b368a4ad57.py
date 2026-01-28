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

# Write the list of publication numbers to a file
with open('cited_pubs.json', 'w') as f:
    json.dump(list(all_cited_pubs), f)

print('__RESULT__:')
print(json.dumps({
    'message': 'Created cited_pubs.json with all cited publication numbers',
    'count': len(all_cited_pubs)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_records': 169, 'total_citations': 1308, 'sample': [{'publication_number': 'US-4599677-A', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2015129765-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'FR-3105380-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-11466906-B2', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2001053519-A1', 'source_patent': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}]}, 'var_functions.execute_python:10': {'total_cited_publications': 1112, 'sample_pubs': ['WO-2013025632-A1', 'US-2020023209-A1', 'US-6200265-B1', 'EP-2694154-A1', 'US-9974593-B2', 'US-5366770-A', 'US-8865406-B2', 'US-2006105322-A1', 'US-7757565-B2', 'US-2014356956-A1', 'JP-H11261169-A', 'US-2016242650-A1', 'US-2014356867-A1', 'WO-2014093712-A1', 'US-8080523-B2', 'WO-2013169802-A1', 'WO-2010144578-A2', 'EP-2515996-A2', 'US-2011281288-A1', 'US-2012065087-A1']}}

exec(code, env_args)
