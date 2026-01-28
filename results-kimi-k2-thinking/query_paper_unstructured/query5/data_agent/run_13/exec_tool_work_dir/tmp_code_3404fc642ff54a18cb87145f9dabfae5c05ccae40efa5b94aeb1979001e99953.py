code = """import json
import pandas as pd
import re
import os

# Get citation data from storage
citations_key = 'var_functions.query_db:5'
citations_data = locals().get(citations_key, [])

# If it's a string path, read the file
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

# Get paper data from storage
papers_key = 'var_functions.query_db:6'
papers_data = locals().get(papers_key, [])

# If it's a string path, read the file
if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

print('Data loaded: %d papers, %d citations' % (len(papers_data), len(citations_data)))

# Function to clean titles for matching
def clean_title(title):
    if not isinstance(title, str):
        return ''
    # Remove file extension
    title = title.replace('.txt', '')
    # Remove punctuation and normalize
    cleaned = re.sub(r'[^\w\s]', ' ', title.lower())
    cleaned = re.sub(r'\s+', ' ', cleaned.strip())
    # Remove common stop words
    stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from'}
    words = [w for w in cleaned.split() if w not in stop_words]
    return ' '.join(words)

# Find CHI papers and extract info
chi_papers = []
for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if CHI conference
    is_chi = False
    if re.search(r'CHI', text):
        is_chi = True
    elif re.search(r'Human Factors in Computing Systems', text):
        is_chi = True
    
    if is_chi:
        title = filename.replace('.txt', '') if filename else ''
        # Extract year
        year = None
        year_matches = re.findall(r'CHI\s*[\'?]?(\d{4})', text)
        if year_matches:
            year = int(year_matches[0])
        else:
            # Look for any 4-digit year in the text
            year_matches = re.findall(r'\b(20\d{2})\b', text)
            if year_matches:
                year = int(year_matches[0])
        
        chi_papers.append({
            'title': title,
            'title_clean': clean_title(title),
            'year': year,
            'venue': 'CHI'
        })

print('Found %d CHI papers' % len(chi_papers))

# Prepare citations data
citations_list = []
for citation in citations_data:
    if isinstance(citation, dict):
        title = citation.get('title', '')
        citations_list.append({
            'title': title,
            'title_clean': clean_title(title),
            'citation_count': int(citation.get('citation_count', 0)),
            'citation_year': int(citation.get('citation_year', 0))
        })

# Convert to DataFrames
chi_df = pd.DataFrame(chi_papers)
citations_df = pd.DataFrame(citations_list)

# Filter citations for year 2020
citations_2020 = citations_df[citations_df['citation_year'] == 2020]

print('2020 citations count: %d' % len(citations_2020))

# Merge on clean titles
merged = pd.merge(chi_df, citations_2020, on='title_clean', how='inner')

# Remove duplicates (keep first occurrence)
merged_unique = merged.drop_duplicates(subset=['title_x'])

print('Matches found: %d' % len(merged_unique))

# Calculate total citations
total_citations = merged_unique['citation_count'].sum()
print('Total citations: %d' % total_citations)

# Prepare result
result = {
    'total_citations': int(total_citations),
    'papers_matched': int(len(merged_unique))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
