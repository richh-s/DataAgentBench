code = """import json
import pandas as pd
import re
import os

# Get the file path from storage
file_path = locals()['var_functions.query_db:2']

# Check if file exists and load it
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f"Total records loaded: {len(data)}")
    
    # Extract UNIV CALIFORNIA patents and their publication numbers
    uc_patents = []
    for record in data:
        patents_info = record.get('Patents_info', '')
        if 'UNIV CALIFORNIA' in patents_info:
            # Extract publication number from Patents_info
            pub_num_match = re.search(r'(?:pub\. number|publication number|has pub\. number|pub\. number is)\s+([A-Z]{2}-[^\s,]+)', patents_info)
            if pub_num_match:
                pub_num = pub_num_match.group(1)
                uc_patents.append({
                    'publication_number': pub_num,
                    'patents_info': patents_info,
                    'citation': record.get('citation', '[]')
                })
    
    print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")
    
    # Create a set of UC publication numbers for easy lookup
    uc_pub_numbers = {p['publication_number'] for p in uc_patents}
    print(f"UC publication numbers sample: {list(uc_pub_numbers)[:5]}")
    
    # Now find all patents that cite UC patents and get their assignees
    citing_patents = []
    
    for record in data:
        citations_str = record.get('citation', '[]')
        if citations_str and citations_str != '[]':
            try:
                citations = json.loads(citations_str)
                for citation in citations:
                    cited_pub_num = citation.get('publication_number')
                    if cited_pub_num and cited_pub_num in uc_pub_numbers:
                        # This patent cites a UC patent
                        patents_info = record.get('Patents_info', '')
                        if patents_info and 'UNIV CALIFORNIA' not in patents_info:
                            citing_patents.append({
                                'citing_patent_info': patents_info,
                                'cited_uc_patent': cited_pub_num,
                                'citation': citations_str
                            })
            except:
                continue
    
    print(f"Found {len(citing_patents)} patents that cite UC patents (excluding UC)")
    
    # Extract assignees from citing patents
    assignee_citations = {}
    for cp in citing_patents:
        patents_info = cp['citing_patent_info']
        # Extract assignee from patents_info
        assignee_match = re.search(r'(?:owned by|assigned to|is owned by|is assigned to)\s+([A-Z][^,\s\)]*(?:\s+[A-Z][^,\s\)]*)*)', patents_info)
        if assignee_match:
            assignee = assignee_match.group(1).strip()
            if assignee != 'UNIV CALIFORNIA':
                if assignee not in assignee_citations:
                    assignee_citations[assignee] = []
                assignee_citations[assignee].append(cp['cited_uc_patent'])
    
    print(f"Found {len(assignee_citations)} unique assignees (excluding UNIV CALIFORNIA)")
    print(f"Assignees: {list(assignee_citations.keys())[:10]}")
    
    result = {
        'uc_patents_count': len(uc_patents),
        'citing_patents_count': len(citing_patents),
        'assignee_citations': assignee_citations
    }
    
else:
    result = {'error': 'File not found', 'file_path': file_path}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
