code = """import pandas as pd
import json

file_path = locals()['var_function-call-17345096948690760045']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

univ_california_patents = set()
for index, row in df.iterrows():
    patents_info = row['Patents_info']
    if 'assignee_harmonized: UNIV CALIFORNIA' in patents_info:
        # Extract publication number from Patents_info
        # The format is like '...publication number US-XXXXXXXX-XX...'
        try:
            pub_number_start = patents_info.find('publication number ') + len('publication number ')
            pub_number_end = patents_info.find('.', pub_number_start)
            publication_number = patents_info[pub_number_start:pub_number_end].strip()
            univ_california_patents.add(publication_number)
        except Exception:
            pass # Skip if publication number not found in expected format

citing_assignees_info = []

for index, row in df.iterrows():
    citation_str = row['citation']
    citations = json.loads(citation_str) if citation_str else []
    
    cites_univ_california = False
    for citation in citations:
        if citation.get('publication_number') in univ_california_patents:
            cites_univ_california = True
            break
            
    if cites_univ_california:
        patents_info = row['Patents_info']
        assignee_start = patents_info.find('assignee_harmonized: ') + len('assignee_harmonized: ')
        assignee_end = patents_info.find(',', assignee_start)
        if assignee_end == -1:
            assignee_end = patents_info.find(' ', assignee_start) # Fallback if comma not found
            if assignee_end == -1:
                assignee_end = len(patents_info) # Fallback if space not found
        
        citing_assignee = patents_info[assignee_start:assignee_end].strip()
        
        if citing_assignee != 'UNIV CALIFORNIA':
            cpc_str = row['cpc']
            cpc_codes = json.loads(cpc_str) if cpc_str else []
            primary_cpc = None
            for cpc_item in cpc_codes:
                if cpc_item.get('first'):
                    primary_cpc = cpc_item.get('code')
                    break
            
            if primary_cpc:
                citing_assignees_info.append({
                    'assignee': citing_assignee,
                    'primary_cpc': primary_cpc
                })

result = pd.DataFrame(citing_assignees_info).to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-6464706059766972960': [], 'var_function-call-17345096948690760045': 'file_storage/function-call-17345096948690760045.json'}

exec(code, env_args)
