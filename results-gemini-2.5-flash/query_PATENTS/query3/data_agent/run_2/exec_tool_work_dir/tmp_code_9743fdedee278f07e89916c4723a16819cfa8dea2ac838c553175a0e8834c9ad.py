code = """import json
import pandas as pd
import numpy as np

with open(locals()['var_function-call-718955595413545914'], 'r') as f:
    all_publication_data = json.load(f)

univ_california_patent_numbers = set()
all_patent_assignees = {}
all_patent_cpcs = {}
patent_citations_mapping = {} # Key: citing_patent_number, Value: list of cited_patent_numbers

for record in all_publication_data:
    patent_info = record.get('Patents_info', '')
    citations_raw = record.get('citation', '[]')
    cpc_codes_raw = record.get('cpc', '[]')

    # Extract publication number for the current patent
    publication_number = None
    pub_num_match_series = pd.Series([patent_info]).str.extract(r'pub\. number (US-[\w-]+(?:-[A-Z]\d)?|WO-[\w-]+(?:-[A-Z]\d)?|EP-[\w-]+(?:-[A-Z]\d)?|JP-[\w-]+(?:-[A-Z]\d)?)')
    if not pub_num_match_series.empty and pub_num_match_series.iloc[0, 0] is not None:
        publication_number = str(pub_num_match_series.iloc[0, 0]).strip()

    # Extract assignee for the current patent
    assignee_harmonized = None
    assignee_match_series = pd.Series([patent_info]).str.extract(r'(?:assigned to |owned by |holds the )([A-Z0-9\s&.-]+?)(?: and has| with| holds| patent| application| filing| app| publication| published| publication| pub|$)')
    if not assignee_match_series.empty and assignee_match_series.iloc[0, 0] is not None:
        assignee_harmonized = str(assignee_match_series.iloc[0, 0]).strip()

    if publication_number and assignee_harmonized:
        all_patent_assignees[publication_number] = assignee_harmonized
        if 'UNIV CALIFORNIA' in assignee_harmonized.upper(): # Case-insensitive check
            univ_california_patent_numbers.add(publication_number)
        
    if publication_number:
        try:
            cpc_codes_list = json.loads(cpc_codes_raw)
            primary_cpc_codes = [cpc['code'] for cpc in cpc_codes_list if cpc.get('first') == True]
            if primary_cpc_codes:
                all_patent_cpcs[publication_number] = primary_cpc_codes
        except json.JSONDecodeError:
            pass # Handle cases where cpc is not valid JSON

    # Extract citations from this patent
    if publication_number and citations_raw:
        try:
            citations_list = json.loads(citations_raw)
            cited_by_current_patent = [citation_entry.get('publication_number') for citation_entry in citations_list if citation_entry.get('publication_number')]
            if cited_by_current_patent:
                patent_citations_mapping[publication_number] = cited_by_current_patent
        except json.JSONDecodeError:
            pass # Handle cases where citation is not valid JSON

# Now, identify patents that cite 'UNIV CALIFORNIA' patents, excluding 'UNIV CALIFORNIA' itself
citing_assignees_and_cpcs_data = []

for citing_pub_num, cited_pub_numbers in patent_citations_mapping.items():
    for cited_pub_num in cited_pub_numbers:
        if cited_pub_num in univ_california_patent_numbers: # This citation is to a UNIV CALIFORNIA patent
            citing_assignee = all_patent_assignees.get(citing_pub_num)
            if citing_assignee and 'UNIV CALIFORNIA' not in citing_assignee.upper(): # Exclude UNIV CALIFORNIA itself, case-insensitive
                citing_cpc_codes = all_patent_cpcs.get(citing_pub_num, [])
                for cpc_code in citing_cpc_codes:
                    citing_assignees_and_cpcs_data.append({'assignee': citing_assignee, 'cpc_code': cpc_code})


# Get unique CPC codes for definition lookup
unique_cpc_codes = list(set([item['cpc_code'] for item in citing_assignees_and_cpcs_data]))

print('__RESULT__:')
print(json.dumps({'citing_assignees_and_cpcs': citing_assignees_and_cpcs_data, 'unique_cpc_codes': unique_cpc_codes}))"""

env_args = {'var_function-call-4989284733204990727': ['publicationinfo'], 'var_function-call-6439696821773378279': 'file_storage/function-call-6439696821773378279.json', 'var_function-call-12633100993076752375': {'citing_assignees_and_cpcs': [], 'unique_cpc_codes': []}, 'var_function-call-718955595413545914': 'file_storage/function-call-718955595413545914.json'}

exec(code, env_args)
