code = """import json

# Load the database results
db_path = var_functions.query_db:5
with open(db_path, 'r') as f:
    univ_california_data = json.load(f)

# Process citations
all_citations = []
for row in univ_california_data:
    patents_info = row['Patents_info']
    citation_str = row['citation']
    
    if citation_str:
        try:
            citations = json.loads(citation_str)
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                if pub_num:
                    all_citations.append({
                        'publication_number': pub_num,
                        'source_patent': patents_info
                    })
        except:
            continue

# Print the first few to debug
print('__RESULT__:')
print(json.dumps({
    'total_records': len(univ_california_data),
    'total_citations': len(all_citations),
    'sample': all_citations[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
