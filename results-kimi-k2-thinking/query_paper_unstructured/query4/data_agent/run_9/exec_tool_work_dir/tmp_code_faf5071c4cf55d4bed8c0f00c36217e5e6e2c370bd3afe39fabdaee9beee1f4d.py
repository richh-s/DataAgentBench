code = """import json

# Read the paper data from MongoDB query result_path = var_functions.query_db:40
with open(var_functions.query_db:40, 'r') as f:
    papers_from_mongo = json.load(f)

# Read citation data from SQLite query result_path = var_functions.query_db:42
with open(var_functions.query_db:42, 'r') as f:
    citations_from_sql = json.load(f)

# Extract titles from papers
pa_titles = []
for paper in papers_from_mongo:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    pa_titles.append(title)

# Create citation map (normalized title to citation count)
citation_map = {}
for item in citations_from_sql:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    citation_map[title.strip().lower()] = citations

# Match papers with citations
matched_results = []
for title in pa_titles:
    if not title:
        continue
    normalized_title = title.strip().lower()
    total_cites = citation_map.get(normalized_title, 0)
    matched_results.append({
        'title': title,
        'total_citations': total_cites
    })

# Sort by citation count descending
final_results = sorted(matched_results, key=lambda x: x['total_citations'], reverse=True)

# Print results
print('Papers from 2016 in physical activity domain:')
for paper in final_results:
    print(f"{paper['title']}: {paper['total_citations']} total citations")

# Return as JSON
output = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
