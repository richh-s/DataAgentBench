code = """import json
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-6920317979161454102'], 'r') as f:
    publication_data = json.load(f)

# Convert to DataFrame for easier processing
df_publications = pd.DataFrame(publication_data)

# Function to extract assignee_harmonized from Patents_info
def extract_assignee(patents_info):
    if isinstance(patents_info, str):
        # The assignee_harmonized is typically before "holds the US patent application" or "is assigned"
        # This is a heuristic and might need refinement based on actual data variations
        if "holds the US patent application" in patents_info:
            return patents_info.split("holds the US patent application")[0].strip()
        elif "is assigned" in patents_info:
            return patents_info.split("is assigned")[0].strip()
        elif "publication number" in patents_info:
            # Try to find assignee from the start of the string before the first patent info
            parts = patents_info.split(" ")
            assignee_parts = []
            for part in parts:
                if part.startswith("US-") or part.startswith("WO-") or part.startswith("JP-") or part.startswith("KR-"):
                    break
                assignee_parts.append(part)
            assignee = " ".join(assignee_parts).replace(",", "").strip()
            if assignee:
                return assignee
    return None

# Extract assignee and publication number
df_publications['assignee_harmonized'] = df_publications['Patents_info'].apply(extract_assignee)
df_publications['publication_number'] = df_publications['Patents_info'].str.extract(r'(US-\d{11}-\w{1,2}|US-\d{7}-\w{1,2}|WO-\d{11}-\w{1,2}|JP-H\d{8}-\w{1,2}|JP-\d{10}-\w{1,2}|KR-\d{11}-\w{1,2})')

# Identify patents assigned to UNIV CALIFORNIA
univ_california_patents = df_publications[df_publications['assignee_harmonized'].str.contains('UNIV CALIFORNIA', na=False)]['publication_number'].dropna().tolist()

# Find citing patents and their assignees and primary CPCs
citing_assignees_cpc = []

for index, row in df_publications.iterrows():
    citations_str = row['citation']
    if pd.isna(citations_str) or citations_str == '[]':
        continue

    citations = json.loads(citations_str)
    current_assignee = row['assignee_harmonized']

    if current_assignee is None or "UNIV CALIFORNIA" in current_assignee:
        continue

    cited_univ_california = False
    for citation in citations:
        if citation.get('publication_number') in univ_california_patents:
            cited_univ_california = True
            break
    
    if cited_univ_california:
        cpc_codes_str = row['cpc']
        if pd.isna(cpc_codes_str) or cpc_codes_str == '[]':
            continue
        
        cpc_codes = json.loads(cpc_codes_str)
        primary_cpc_codes = [cpc['code'] for cpc in cpc_codes if cpc.get('first') == True]
        
        for cpc_code in primary_cpc_codes:
            citing_assignees_cpc.append({'assignee': current_assignee, 'cpc_code': cpc_code})

print('__RESULT__:')
print(json.dumps(citing_assignees_cpc))"""

env_args = {'var_function-call-11185114347300340884': ['publicationinfo'], 'var_function-call-6920317979161454102': 'file_storage/function-call-6920317979161454102.json'}

exec(code, env_args)
