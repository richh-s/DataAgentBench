code = """import json
import re
import os

# Access the file containing patents that cite UNIV CALIFORNIA
citing_patents_file = locals()['var_functions.query_db:18']

# Read the data
with open(citing_patents_file, 'r') as f:
    citing_patents = json.load(f)

print('Total patents that cite UNIV CALIFORNIA:', len(citing_patents))

# Initialize data structures
citing_assignees_map = {}  # Map of patent number to citing assignee
cited_california_patents = set()

# Process the citing patents data
for patent in citing_patents:
    patent_info = patent.get('Patents_info', '')
    citation_json = patent.get('citation', '')
    
    # Extract assignee from patent info
    try:
        if 'owned by' in patent_info:
            assignee_part = patent_info.split('owned by')[1].split('and has')[0].strip()
        elif 'belongs to' in patent_info:
            assignee_part = patent_info.split('belongs to')[1].split('and has')[0].strip()
        elif 'assigned to' in patent_info:
            assignee_part = patent_info.split('assigned to')[1].split('and has')[0].strip()
        else:
            assignee_part = ''
        
        citing_assignee = assignee_part.strip()
        if citing_assignee == 'UNIV CALIFORNIA':
            continue  # Skip self-citations
    except:
        citing_assignee = ''
    
    if not citing_assignee or citing_assignee == 'UNIV CALIFORNIA':
        continue
    
    # Parse citations to find UNIV CALIFORNIA patents
    try:
        if citation_json and citation_json != '[]':
            citations = json.loads(citation_json) if isinstance(citation_json, str) else citation_json
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                # Check if this is a UNIV CALIFORNIA patent (would need proper matching)
                # For now, we'll collect all citations and match later
                if pub_num:
                    if pub_num not in citing_assignees_map:
                        citing_assignees_map[pub_num] = []
                    citing_assignees_map[pub_num].append(citing_assignee)
    except:
        continue

# Load the previously saved UNIV CALIFORNIA patent data
california_data_result = locals()['var_functions.execute_python:16']

# Get the CPC subclass data from previous analysis
import os
analysis_dir = './analysis_output'
cpc_file = os.path.join(analysis_dir, 'california_cpc_codes.json')

with open(cpc_file, 'r') as f:
    california_cpc_subclasses = json.load(f)

# Now find which citations match UNIV CALIFORNIA patents
california_patents_file = os.path.join(analysis_dir, 'california_citations.json')
with open(california_patents_file, 'r') as f:
    california_citations_data = json.load(f)

# Extract all UNIV CALIFORNIA patent numbers from the citations data
california_patent_numbers = set()
for item in california_citations_data:
    cal_patent_info = item['california_patent_info']
    # Extract the publication number from the patent info
    try:
        if 'pub. number' in cal_patent_info:
            pub_part = cal_patent_info.split('pub. number')[1].strip()
        elif 'publication number' in cal_patent_info:
            pub_part = cal_patent_info.split('publication number')[1].strip()
        elif 'publication no' in cal_patent_info:
            pub_part = cal_patent_info.split('publication no')[1].strip()
        else:
            continue
        
        # Extract the actual patent number
        pub_num = pub_part.split('.')[0].split(',')[0].strip()
        california_patent_numbers.add(pub_num)
    except:
        continue

# Now cross-reference: find which citing patents cited UNIV CALIFORNIA patents
cross_reference_results = []
california_patents_file = os.path.join(analysis_dir, 'california_citations.json')
with open(california_patents_file, 'r') as f:
    california_citations = json.load(f)

# Create a set of cited UNIV CALIFORNIA patent numbers
university_cited_patents = set(item['cited_patent_number'] for item in california_citations)

# Cross-reference to find which citing patents cite these UNIV CALIFORNIA patents
citing_to_california = {}
for cited_patent_num, citing_assignees in citing_assignees_map.items():
    if cited_patent_num in university_cited_patents:
        citing_to_california[cited_patent_num] = list(set(citing_assignees))

output = {
    'total_citing_patents_processed': len(citing_patents),
    'unique_citing_assignees': len(set([assignee for assignees in citing_to_california.values() for assignee in assignees])),
    'university_patents_cited': len(citing_to_california),
    'sample_citations': dict(list(citing_to_california.items())[:5])
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_california_patents': 169, 'total_citations_found': 1308, 'unique_cpc_subclasses': 436, 'sample_cpc_codes': ['Y10S436', 'B01D53', 'B64G1', 'Y02E60', 'C07K1', 'C12Q2600', 'C07D323', 'C12M21', 'A23V2002', 'A61N5'], 'sample_citations': [{'cited_patent_number': 'US-4599677-A', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'US-2015129765-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'cited_patent_number': 'FR-3105380-A1', 'california_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
