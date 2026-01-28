code = """import json
import re

# Load the patents data from the file
all_patents = var_functions.query_db:32

print(f"Total patents loaded: {len(all_patents)}")

# Step 1: Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        uc_patents.append(patent)
        # Extract publication number
        pub_match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]*)', patents_info)
        if pub_match:
            uc_pub_numbers.add(pub_match.group(1))
        else:
            # Try alternative pattern
            alt_match = re.search(r'([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]*)', patents_info)
            if alt_match:
                uc_pub_numbers.add(alt_match.group(1))

print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")
print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print(f"Sample UC pub numbers: {list(uc_pub_numbers)[:10]}")

# Step 2: Find citing patents and extract assignees
# We'll look at all patents that have citations and check if they cite UC patents
citing_assignees = {}  # assignee -> set of CPC codes
uc_pub_numbers_list = list(uc_pub_numbers)

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    citation_str = patent.get('citation', '[]')
    cpc_str = patent.get('cpc', '[]')
    
    # Skip if this is a UNIV CALIFORNIA patent
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    try:
        citations = json.loads(citation_str)
        cpc_codes = json.loads(cpc_str)
        
        # Check if any citation matches a UC publication number
        cites_uc = False
        for citation in citations:
            pub_num = citation.get('publication_number', '')
            if pub_num in uc_pub_numbers:
                cites_uc = True
                break
        
        if cites_uc:
            # Extract assignee from patents_info
            # Look for patterns like "COMPANY holds", "COMPANY is assigned", etc.
            assignee_match = re.search(r'^(.*?)\s+(holds|is assigned to|is owned by|is belonging to|from).*?\s+(the patent filing|the patent application|patent filing|patent application|application|the application)', patents_info)
            
            if assignee_match:
                assignee = assignee_match.group(1).strip()
                # Clean up assignee name
                assignee = re.sub(r'^(In|From|The|A|An)\s+', '', assignee, flags=re.IGNORECASE)
                
                # Skip if it's still UNIV CALIFORNIA
                if 'UNIV CALIFORNIA' in assignee.upper():
                    continue
                    
                # Extract CPC codes (just the primary codes for now - inventive=true or first=true)
                cpc_codes_list = []
                for cpc in cpc_codes:
                    if isinstance(cpc, dict):
                        code = cpc.get('code', '')
                        # Get first 4 characters for subclass (e.g., A61K from A61K31/357)
                        if code and len(code) >= 4:
                            subclass = code[:4]
                            cpc_codes_list.append(subclass)
                
                # Add to our mapping
                if assignee not in citing_assignees:
                    citing_assignees[assignee] = set()
                citing_assignees[assignee].update(cpc_codes_list)
                
    except json.JSONDecodeError:
        continue

print(f"\nFound {len(citing_assignees)} unique citing assignees")
print("Sample citing assignees:")
for assignee in list(citing_assignees.keys())[:10]:
    print(f"  {assignee}: {list(citing_assignees[assignee])[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'total_patents': '169'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:40': [], 'var_functions.list_db:42': ['cpc_definition'], 'var_functions.query_db:44': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}]}

exec(code, env_args)
