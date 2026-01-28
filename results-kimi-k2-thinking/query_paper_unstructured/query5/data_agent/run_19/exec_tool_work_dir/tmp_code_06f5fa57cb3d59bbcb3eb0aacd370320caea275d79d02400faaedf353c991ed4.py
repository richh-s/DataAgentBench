code = """import json

# Read citations data for 2020
citations_file = globals().get('var_functions.query_db:2')
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Read CHI papers data
chi_papers_file = globals().get('var_functions.query_db:14')
with open(chi_papers_file, 'r') as f:
    chi_papers_raw = json.load(f)

# Process CHI papers to extract title (from filename) and venue info
chi_papers = []
for paper in chi_papers_raw:
    filename = paper.get('filename', '')
    # Remove .txt extension to get title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    chi_papers.append({
        'title': title,
        'venue': 'CHI'  # These are all CHI papers from the regex query
    })

# Create a dictionary of CHI papers for fast lookup
chi_titles = {paper['title']: paper for paper in chi_papers}

# Find citations for CHI papers and sum them
total_citations = 0
matched_citations = []

for citation in citations_2020:
    title = citation.get('title', '')
    if title in chi_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        matched_citations.append({
            'title': title,
            'citation_count': count
        })

print('__RESULT__:')
print(json.dumps({
    'total_chi_citations_2020': total_citations,
    'chi_papers_count': len(chi_papers),
    'matched_citations_count': len(matched_citations),
    'sample_matched': matched_citations[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'is_string': True, 'is_list': False}, 'var_functions.execute_python:10': {'total_citations_2020': 188, 'sample_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
