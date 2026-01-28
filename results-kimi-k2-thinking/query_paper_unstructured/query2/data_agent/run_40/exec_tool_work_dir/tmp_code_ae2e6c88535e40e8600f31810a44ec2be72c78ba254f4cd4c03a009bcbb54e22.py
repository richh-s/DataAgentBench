code = """import json
import re

# Read the citation data for 2018
citations_file = var_functions.query_db:0
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = var_functions.query_db:0

# Read the paper documents
papers_file = var_functions.query_db:2
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:2

# Convert to DataFrames for easier processing
import pandas as pd

citations_df = pd.DataFrame(citations_2018)
# Convert citation_count to numeric
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Extract paper title from filename and extract source information
papers_list = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for ACM in the text (common patterns)
    source = None
    
    # Check for ACM references in text
    acm_patterns = [
        r'ACM\s+Classification',
        r'Copyright\s+\d{4}\s+ACM',
        r'ACM\s+[^\s]*\d{4}',
        r'Association for Computing Machinery',
        r'ACM\s+Digital Library',
        r'Permission[^.]*ACM[^.]*\.'
    ]
    
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            source = 'ACM'
            break
    
    # Also check for venue patterns that indicate ACM
    if not source:
        acm_venues = ['CHI', 'CSCW', 'DIS', 'UbiComp', 'TEI', 'IUI']
        for venue in acm_venues:
            # Look for venue mentions that are likely ACM conferences
            if re.search(rf'\b{venue}\b.*?\d{{4}}', text):
                # Check if it's ACM by proximity
                nearby_text = text[max(0, text.find(venue)-200):text.find(venue)+200]
                if 'ACM' in nearby_text or 'Association for Computing Machinery' in nearby_text:
                    source = 'ACM'
                    break
    
    papers_list.append({
        'title': title,
        'source': source,
        'text_preview': text[:500]  # First 500 chars for debugging
    })

papers_df = pd.DataFrame(papers_list)

# Count papers by source
source_counts = papers_df['source'].value_counts()
print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers_df),
    'papers_with_acm': int(source_counts.get('ACM', 0)),
    'sample_papers': papers_df[papers_df['source'] == 'ACM'][['title', 'source']].head(5).to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
