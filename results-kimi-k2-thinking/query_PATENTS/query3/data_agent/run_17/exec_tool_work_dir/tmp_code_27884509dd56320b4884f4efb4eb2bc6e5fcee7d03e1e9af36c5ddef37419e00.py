code = """import json
import re
from collections import defaultdict

# Access the file path that was stored
result_key = 'var_functions.query_db:12'
if result_key in locals():
    file_path = locals()[result_key]
    print(f"Retrieved file path: {file_path}")
    
    # Load the data
    with open(file_path, 'r') as f:
        univ_california_patents = json.load(f)
    
    print(f"Total UNIV CALIFORNIA patents: {len(univ_california_patents)}")
    
    # Extract publication numbers of UNIV CALIFORNIA patents
    uc_pub_numbers = set()
    for patent in univ_california_patents:
        patents_info = patent.get('Patents_info', '')
        # Extract publication number from Patents_info
        if 'pub. number' in patents_info or 'publication number' in patents_info:
            # Look for pattern like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
            match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[^\s]+)', patents_info)
            if match:
                uc_pub_numbers.add(match.group(1))
    
    print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
    print("Sample:", list(uc_pub_numbers)[:5])
    
    # Now get the file path for citations to UNIV CALIFORNIA
    citations_key = 'var_functions.query_db:5'
    if citations_key in locals():
        citations_file = locals()[citations_key]
        print(f"\nCitations file path: {citations_file}")
        
        with open(citations_file, 'r') as f:
            citing_patents = json.load(f)
        
        print(f"Total patents citing UNIV CALIFORNIA: {len(citing_patents)}")
        
        # Extract assignees from these citing patents
        citing_assignees = defaultdict(list)
        
        for patent in citing_patents:
            patents_info = patent.get('Patents_info', '')
            citations = patent.get('citation', '[]')
            
            if not patents_info or patents_info == '':
                continue
                
            # Check if this patent cites UNIV CALIFORNIA
            cites_uc = False
            try:
                citation_list = json.loads(citations) if isinstance(citations, str) else citations
                for citation in citation_list:
                    pub_num = citation.get('publication_number', '')
                    if pub_num in uc_pub_numbers:
                        cites_uc = True
                        break
            except:
                pass
            
            if cites_uc:
                # Extract assignee from Patents_info (exclude UNIV CALIFORNIA itself)
                match = re.search(r'(?:is owned by|is assigned to|is belonging to|belongs to)\s+([^,.]+)', patents_info)
                if match:
                    assignee = match.group(1).strip()
                    if 'UNIV CALIFORNIA' not in assignee.upper():
                        # Get CPC codes for this patent
                        cpc_data = patent.get('cpc', '[]')
                        try:
                            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                            primary_cpcs = [cpc.get('code') for cpc in cpc_list if cpc.get('inventive', False)]
                            if primary_cpcs:
                                citing_assignees[assignee].extend(primary_cpcs)
                        except:
                            pass
        
        print(f"\nFound {len(citing_assignees)} unique citing assignees (excluding UNIV CALIFORNIA)")
        print("Assignees:", list(citing_assignees.keys())[:10])
        
        # Format results
        results = []
        for assignee, cpcs in citing_assignees.items():
            unique_cpcs = list(set(cpcs))
            results.append({
                'assignee': assignee,
                'cpc_codes': unique_cpcs,
                'count': len(cpcs)
            })
        
        # Sort by count
        results.sort(key=lambda x: x['count'], reverse=True)
        
        print("\n__RESULT__:")
        print(json.dumps(results[:20], indent=2))
else:
    print("Could not find result key")
    print("Available variables:", [k for k in locals().keys() if k.startswith('var_')])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
