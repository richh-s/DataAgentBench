code = """import json
import pandas as pd
import re

# Read citations data
citations_path = 'storage/cbf0e9f7f7ee2b36.json'  # This should be the path to the citations file
try:
    with open(citations_path, 'r') as f:
        citations_data = json.load(f)
except:
    # Fallback - try to get from storage variable
    citations_data = locals().get('var_functions.query_db:5', [])

# Ensure citations_data is a list, not a string path
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

# Convert citations to DataFrame
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Read paper documents data
papers_path = 'storage/f9ccddcd0eaa8bf4.json'  # This should be the path to the papers file
try:
    with open(papers_path, 'r') as f:
        papers_data = json.load(f)
except:
    papers_data = locals().get('var_functions.query_db:6', [])

# Ensure papers_data is a list
if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

print(f"Total papers in database: {len(papers_data)}")
print(f"Total citations in 2020: {len(citations_df)}")

# Extract CHI papers
chi_papers = []
for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if it's a CHI paper by looking for CHI venue indicators
    # Look for CHI in the text (conference name, headers, etc.)
    if re.search(r'\bCHI\b|\bHuman Factors in Computing Systems\b', text, re.IGNORECASE):
        # Try to extract year
        year_match = re.search(r'(CHI\s*\'?\d{2,4}|\b(20\d{2})\b)', text)
        year = None
        if year_match:
            year_str = year_match.group(0)
            # Extract 4-digit year
            year_match_4 = re.search(r'20\d{2}', year_str)
            if year_match_4:
                year = int(year_match_4.group(0))
        
        chi_papers.append({
            'title': title,
            'year': year,
            'venue': 'CHI',
            'text': text[:500]  # Store first 500 chars for debugging
        })

print(f"Found {len(chi_papers)} CHI papers")

# Convert to DataFrame
chi_df = pd.DataFrame(chi_papers)

# Join with citations - exact title match
citations_df['title'] = citations_df['title'].str.strip()
chi_df['title'] = chi_df['title'].str.strip()

# Merge on title
merged_df = pd.merge(chi_df, citations_df, on='title', how='inner')

print(f"CHI papers with 2020 citations: {len(merged_df)}")

if len(merged_df) > 0:
    total_citations = merged_df['citation_count'].sum()
    print(f"Total citations: {total_citations}")
    print("\nFirst few matched papers:")
    print(merged_df[['title', 'citation_count', 'citation_year']].head())
else:
    print("No matches found. Let's check some titles...")
    print("Sample CHI titles:", chi_df['title'].head(10).tolist())
    print("Sample citation titles:", citations_df['title'].head(10).tolist())

# Try fuzzy matching if exact matching failed
from collections import defaultdict

# Create a mapping of cleaned titles
def clean_title(title):
    # Remove common words, normalize case
    if not isinstance(title, str):
        return ""
    import re
    # Remove punctuation and extra spaces
    cleaned = re.sub(r'[^\w\s]', ' ', title.lower())
    cleaned = re.sub(r'\s+', ' ', cleaned.strip())
    # Remove common words
    stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    words = [w for w in cleaned.split() if w not in stop_words]
    return ' '.join(words)

citations_df['title_clean'] = citations_df['title'].apply(clean_title)
chi_df['title_clean'] = chi_df['title'].apply(clean_title)

# Try matching on cleaned titles
merged_clean_df = pd.merge(chi_df, citations_df, on='title_clean', how='inner')
print(f"\nCHI papers with 2020 citations (clean match): {len(merged_clean_df)}")

if len(merged_clean_df) > 0:
    total_citations_clean = merged_clean_df['citation_count'].sum()
    print(f"Total citations (clean match): {total_citations_clean}")
    # Remove duplicates if any
    merged_clean_df = merged_clean_df.drop_duplicates(subset=['title_x'])
    total_citations_clean_unique = merged_clean_df['citation_count'].sum()
    print(f"Total citations (clean match, unique): {total_citations_clean_unique}")
    
    # Store result in proper format
    result = {
        'total_citations': int(total_citations_clean_unique),
        'papers_count': int(len(merged_clean_df)),
        'sample_papers': merged_clean_df[['title_x', 'citation_count']].head(5).to_dict('records')
    }
else:
    result = {'total_citations': 0, 'papers_count': 0, 'message': 'No matches found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
