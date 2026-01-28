code = """import json
import re

# Load data from storage variables
def load_from_storage():
    civic_docs = None
    funding_data = None
    
    # Try to access storage variables
    if 'var_functions.query_db:2' in locals():
        civic_docs = locals()['var_functions.query_db:2']
    if 'var_functions.query_db:5' in locals():
        funding_data = locals()['var_functions.query_db:5']
    
    return civic_docs, funding_data

civic_docs, funding_data = load_from_storage()

if not civic_docs or not funding_data:
    print('__RESULT__:')
    print(json.dumps({"error": "Could not load data from storage"}))
else:
    # Build funding lookup
    funding_dict = {}
    for record in funding_data:
        try:
            name = record.get('Project_Name', '').lower()
            amount_str = record.get('Amount', '0')
            amount = int(amount_str) if isinstance(amount_str, str) and amount_str.isdigit() else int(amount_str)
            if name and amount > 0:
                funding_dict[name] = amount
        except:
            continue
    
    # Extract disaster projects from civic docs
    disaster_2022_projects = []
    
    for doc in civic_docs:
        text = doc.get('text', '')
        
        # Find lines that might be project names containing disaster indicators
        for line in text.split('\n'):
            line = line.strip()
            if not line or len(line) < 5:
                continue
                
            # Skip common headers
            if any(line.startswith(x) for x in ['Public Works', 'Commission', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Capital Improvement', 'Page']):
                continue
            if 'cid:' in line:
                continue
            
            # Check if this is a disaster project
            lower_line = line.lower()
            is_disaster = any(marker in lower_line for marker in ['fema', 'caljpia', 'caloes'])
            
            if is_disaster:
                # Look for 2022 in nearby text (within 10 lines after)
                lines_after = text.split('\n')
                line_index = text.split('\n').index(line)
                context_window = min(line_index + 15, len(lines_after))
                
                has_2022 = False
                for j in range(line_index, context_window):
                    if '2022' in lines_after[j]:
                        has_2022 = True
                        break
                
                if has_2022:
                    disaster_2022_projects.append(line)
    
    # Remove duplicates
    disaster_2022_projects = list(set(disaster_2022_projects))
    
    # Match with funding
    total_funding = 0
    matched_projects = []
    
    for proj_name in disaster_2022_projects:
        proj_lower = proj_name.lower()
        
        # Try direct match
        if proj_lower in funding_dict:
            amount = funding_dict[proj_lower]
            total_funding += amount
            matched_projects.append({"project": proj_name, "amount": amount})
        else:
            # Try substring matching - look for the base project name
            # Remove suffixes like (FEMA Project) for matching
            base_name = re.sub(r'\s*\([^)]*\)\s*$', '', proj_name).strip().lower()
            
            # Look for funding projects containing this base name
            for fund_name, amount in funding_dict.items():
                if base_name in fund_name or fund_name in base_name:
                    total_funding += amount
                    matched_projects.append({
                        "project": proj_name,
                        "matched_funding": fund_name,
                        "amount": amount
                    })
                    break
    
    output = {
        "total_funding": total_funding,
        "matched_projects": matched_projects,
        "disaster_projects_count": len(disaster_2022_projects)
    }
    
    print('__RESULT__:')
    print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:28': [{'total_funding': '1410000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
