code = """import json
import re

# Load funding data (> $50,000)
funding_path = locals()['var_functions.query_db:84']
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:82']
with open(civic_path) as f:
    civic_documents = json.load(f)

# Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Not Started|$)'
    match = re.search(design_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section = match.group(1)
        # Split into potential project entries
        # Projects are typically separated by blank lines or start with project names
        entries = re.split(r'\n\s*\n', section)
        
        for entry in entries:
            entry = entry.strip()
            if not entry:
                continue
                
            # Get the first line which is typically the project name
            lines = entry.split('\n')
            first_line = lines[0].strip()
            
            # Clean up the line
            # Remove leading markers like numbers, letters, bullets
            clean_name = re.sub(r'^[0-9A-Z]+[.)]\s*', '', first_line)
            clean_name = clean_name.replace('•', '').replace('■', '').replace('●', '').strip()
            
            # Skip if too short or contains certain keywords
            if len(clean_name) < 10 or 'Project Schedule' in clean_name or 'Updates:' in clean_name:
                continue
                
            # Check if it looks like a project name based on keywords
            keywords = ['road', 'beach', 'park', 'storm', 'drain', 'bridge', 'median', 'crosswalk', 
                       'repair', 'improvement', 'project', 'structure', 'facility', 'signal']
            if any(k in clean_name.lower() for k in keywords):
                # Skip if it's a heading (all caps, short)
                if not (clean_name.isupper() and len(clean_name.split()) <= 3):
                    design_capital_projects.append({
                        'Project_Name': clean_name,
                        'status': 'design',
                        'type': 'capital'
                    })

# Remove obvious duplicates (exact matches)
unique_design_projects = []
seen_names = set()
for proj in design_capital_projects:
    name = proj['Project_Name']
    if name not in seen_names:
        seen_names.add(name)
        unique_design_projects.append(proj)

# Get high funding project names
high_funding_names = set()
high_funding_details = {}
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        name = rec['Project_Name']
        high_funding_names.add(name)
        high_funding_details[name] = amount

# Normalize function for better matching
def normalize_name(name):
    # Convert to lowercase, remove extra spaces, remove common suffixes/prefixes
    name = name.lower()
    name = ' '.join(name.split())  # Normalize whitespace
    # Remove common project suffixes that might differ
    name = re.sub(r'\s*(\(fema[^)]*\)|\(caloes[^)]*\)|\(caljpia[^)]*\)|project)', '', name)
    return name.strip()

# Find matches between design projects and high funding projects
matches = []

# Build normalized mapping of high funding projects
high_funding_normalized = {}
for name in high_funding_names:
    norm = normalize_name(name)
    high_funding_normalized[norm] = name

# Try to match each design project with funding
for design_proj in unique_design_projects:
    design_name = design_proj['Project_Name']
    design_norm = normalize_name(design_name)
    
    # Direct match check
    if design_norm in high_funding_normalized:
        original_fund_name = high_funding_normalized[design_norm]
        matches.append({
            'Project_Name': original_fund_name,
            'Amount': high_funding_details[original_fund_name],
            'Status': 'design',
            'Type': 'capital'
        })
    else:
        # Fuzzy matching - check if design name is contained in funding name or vice versa
        for fund_norm, original_name in high_funding_normalized.items():
            # Check for substring matches
            if (design_norm in fund_norm or fund_norm in design_norm) and len(design_norm) > 8:
                # Additional check: ensure it's not a false positive
                # The match should be meaningful (not just a single word)
                common_words = set(design_norm.split()) & set(fund_norm.split())
                if len(common_words) >= 2 or (len(design_norm.split()) <= 2 and design_norm in fund_norm):
                    if not any(m['Project_Name'] == original_name for m in matches):
                        matches.append({
                            'Project_Name': original_name,
                            'Amount': high_funding_details[original_name],
                            'Status': 'design',
                            'Type': 'capital'
                        })
                    break

# Remove duplicate matches
cleaned_matches = []
seen_names_final = set()
for match in matches:
    if match['Project_Name'] not in seen_names_final:
        seen_names_final.add(match['Project_Name'])
        cleaned_matches.append(match)

# Count matches
final_count = len(cleaned_matches)

# Prepare result
result = {
    'total_design_capital_projects': len(unique_design_projects),
    'total_high_funding_projects': len(high_funding_names),
    'matched_projects_count': final_count,
    'sample_matched_projects': cleaned_matches[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}, 'var_functions.list_db:58': ['Funding'], 'var_functions.list_db:76': ['civic_docs'], 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
