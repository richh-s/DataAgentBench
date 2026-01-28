code = """import json

# Load the citation data
with open(var_functions.query_db:42, 'r') as f:
    citations_data = json.load(f)

# Load the paper data (2016, physical activity)
with open(var_functions.query_db:40, 'r') as f:
    papers_2016_pa = json.load(f)

print(f"Total papers from 2016 in physical activity: {len(papers_2016_pa)}")
print(f"Total papers in citations database: {len(citations_data)}")

# Extract titles from 2016 physical activity papers
pa_titles = []
for paper in papers_2016_pa:
    filename = paper.get('filename', '')
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    pa_titles.append(title)

print(f"Paper titles found: {pa_titles}")

# Match with citation data - need to normalize titles
def normalize_title(title):
    return title.strip().lower()

# Create a mapping of normalized titles to citation counts
citation_map = {}
for item in citations_data:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    norm_title = normalize_title(title)
    citation_map[norm_title] = citations

# Find matches
results = []
for title in pa_titles:
    norm_title = normalize_title(title)
    if norm_title in citation_map:
        results.append({
            'title': title,
            'total_citations': citation_map[norm_title]
        })
    else:
        # Try to find partial matches
        matches = []
        for cit_title, citations in citation_map.items():
            if norm_title in cit_title or cit_title in norm_title:
                matches.append((cit_title, citations))
        
        if matches:
            # Take the best match (longest title match)
            best_match = max(matches, key=lambda x: len(x[0]))
            results.append({
                'title': title,
                'total_citations': best_match[1]
            })

# Sort by citation count
top_results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print(f"\nFound {len(top_results)} papers with citation data:")
for paper in top_results:
    print(f"  {paper['title']}: {paper['total_citations']} citations")

# Return results
output = json.dumps(top_results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
