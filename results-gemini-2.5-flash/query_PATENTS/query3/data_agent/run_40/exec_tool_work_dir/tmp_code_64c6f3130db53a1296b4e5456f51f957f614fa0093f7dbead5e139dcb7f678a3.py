code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-373891586094066339'], 'r') as f:
    publication_data = json.load(f)

df_publications = pd.DataFrame(publication_data)

def extract_assignee(patents_info):
    # Patterns to capture assignee names more broadly
    patterns = [
        r'assignee_harmonized: ([^,;.]+)',
        r'owned by ([^,;.]+)',
        r'assigned to ([^,;.]+)',
        r'holds the US patent (?:application|filing) \([^)]+\),? with publication number [^,;.]+'
        r'holds the US (?:application|patent filing) \([^)]+\),? with publication number [^,;.]+'
        r'held by ([^,;.]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            # For the last two patterns, the assignee is often the first part of the string
            if 'holds the US patent' in pattern or 'holds the US application' in pattern or 'held by' in pattern:
                # This specific case needs to be handled carefully, as the assignee is at the beginning
                # Let's try to capture the name before "holds" or "owned by" if those patterns are used
                if re.match(r'^([^,]+) holds the US', patents_info, re.IGNORECASE):
                    return re.match(r'^([^,]+) holds the US', patents_info, re.IGNORECASE).group(1).strip()
                elif re.match(r'^In US, the application \([^)]+\) is owned by ([^,;.]+)', patents_info, re.IGNORECASE):
                    return re.match(r'^In US, the application \([^)]+\) is owned by ([^,;.]+)', patents_info, re.IGNORECASE).group(1).strip()
                elif re.match(r'^In US, the patent filing \([^)]+\) is assigned to ([^,;.]+)', patents_info, re.IGNORECASE):
                    return re.match(r'^In US, the patent filing \([^)]+\) is assigned to ([^,;.]+)', patents_info, re.IGNORECASE).group(1).strip()
                elif re.match(r'^Patent application \([^)]+\) from US, owned by ([^,;.]+)', patents_info, re.IGNORECASE):
                    return re.match(r'^Patent application \([^)]+\) from US, owned by ([^,;.]+)', patents_info, re.IGNORECASE).group(1).strip()

            return match.group(1).strip()
    return None

def extract_publication_number(patents_info):
    match = re.search(r'publication number ([^,;.]+)', patents_info)
    if match:
        return match.group(1).strip()
    return None

df_publications['assignee_harmonized'] = df_publications['Patents_info'].apply(extract_assignee)
df_publications['publication_number'] = df_publications['Patents_info'].apply(extract_publication_number)

univ_california_patents = df_publications[
    (df_publications['assignee_harmonized'].astype(str).str.contains('UNIV CALIFORNIA', na=False, case=False))
]

univ_california_publication_numbers = univ_california_patents['publication_number'].dropna().unique().tolist()

citing_patents_info = []
for _, row in df_publications.iterrows():
    citing_assignee = row['assignee_harmonized']
    if citing_assignee and 'UNIV CALIFORNIA' not in citing_assignee.upper():
        citations = json.loads(row['citation']) if pd.notna(row['citation']) else []
        for citation in citations:
            if citation.get('publication_number') in univ_california_publication_numbers:
                cpc_codes = json.loads(row['cpc']) if pd.notna(row['cpc']) else []
                primary_cpc = None
                for cpc_item in cpc_codes:
                    if cpc_item.get('first') == True:
                        primary_cpc = cpc_item.get('code')
                        break
                if primary_cpc:
                    citing_patents_info.append({'assignee': citing_assignee, 'primary_cpc': primary_cpc})

result_df = pd.DataFrame(citing_patents_info).drop_duplicates()

unique_cpc_codes = result_df['primary_cpc'].unique().tolist()

print('__RESULT__:')
print(json.dumps(unique_cpc_codes))"""

env_args = {'var_function-call-15453717939236819502': [], 'var_function-call-373891586094066339': 'file_storage/function-call-373891586094066339.json', 'var_function-call-2533390639764278579': [], 'var_function-call-16095269943222012598': [None], 'var_function-call-13949763096847288352': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}], 'var_function-call-16757069480458435073': 'file_storage/function-call-16757069480458435073.json'}

exec(code, env_args)
