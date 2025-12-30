code = """import json
import re
import pandas as pd

def extract_paper_info(paper_text, filename):
    title = filename.replace(".txt", "")
    year = None
    is_empirical = False

    # Extract year: look for 4-digit numbers starting with 19 or 20 anywhere in the text
    year_matches = re.findall(r'\b(19|20)\d{2}\b', paper_text)
    if year_matches:
        # Assuming the first found year is the publication year
        year = int(year_matches[0])

    # Check if 'empirical' is in the text (case-insensitive)
    if 'empirical' in paper_text.lower():
        is_empirical = True

    return {'title': title, 'year': year, 'is_empirical': is_empirical}

file_path = locals()['var_function-call-17384357217489800854']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

all_papers_extracted_info = []
for doc in paper_docs:
    info = extract_paper_info(doc['text'], doc['filename'])
    all_papers_extracted_info.append(info)

# Analyze the extracted data
years = [p['year'] for p in all_papers_extracted_info if p['year'] is not None]
empirical_papers_count = sum(1 for p in all_papers_extracted_info if p['is_empirical'])
papers_after_2016_count = sum(1 for p in all_papers_extracted_info if p['year'] is not None and p['year'] > 2016)

# Filter papers based on year and empirical contribution
filtered_papers = []
for paper in all_papers_extracted_info:
    if paper['year'] is not None and paper['year'] > 2016 and paper['is_empirical']:
        filtered_papers.append(paper)

# Convert to DataFrame for easier merging
filtered_papers_df = pd.DataFrame(filtered_papers)

# Load citation data
citation_file_path = locals()['var_function-call-505378774442661286']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

citations_df = pd.DataFrame(citation_data)
citations_df['total_citation_count'] = citations_df['total_citation_count'].astype(int)

# Merge the two dataframes if filtered_papers_df is not empty
if not filtered_papers_df.empty:
    merged_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')
    result = merged_df[['title', 'total_citation_count']].to_json(orient='records')
else:
    result = json.dumps([]) # Return empty list if no papers match criteria

print("__RESULT__:")
print(json.dumps({
    "extracted_info_sample": all_papers_extracted_info[:5],
    "unique_years": sorted(list(set(years))) if years else [],
    "empirical_papers_count": empirical_papers_count,
    "papers_after_2016_count": papers_after_2016_count,
    "filtered_papers_count": len(filtered_papers),
    "final_result": json.loads(result)
}))"""

env_args = {'var_function-call-8876707072609632946': ['Citations', 'sqlite_sequence'], 'var_function-call-9424252978014940020': ['paper_docs'], 'var_function-call-17384357217489800854': 'file_storage/function-call-17384357217489800854.json', 'var_function-call-13031117097295312790': [], 'var_function-call-505378774442661286': 'file_storage/function-call-505378774442661286.json', 'var_function-call-1634136829314383703': {'filtered_papers_df_columns': [], 'citations_df_columns': ['title', 'total_citation_count']}}

exec(code, env_args)
