code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_function-call-13041768272351243081']))
civic_docs = json.load(open(locals()['var_function-call-13041768272351241682']))

# Extract Project Names for matching
project_names = set(item['Project_Name'] for item in funding_data)

# Helper function to check if a date string is Spring 2022
def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower().strip()
    
    # Check for "2022"
    if '2022' not in date_str:
        return False
    
    # Check for "Spring"
    if 'spring' in date_str:
        return True
    
    # Check for months
    months = ['march', 'april', 'may']
    for m in months:
        if m in date_str:
            return True
            
    # Check numeric months if formatted like 2022-03, 03/2022, etc.
    # Simple regex for 03, 04, 05 with 2022
    # 2022-03, 2022-04, 2022-05
    if re.search(r'2022\D0[345]', date_str):
        return True
    if re.search(r'0[345]\D2022', date_str):
        return True
        
    return False

# Extraction logic
projects_found = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    # Find positions of all known project names in the text
    # We store (start_index, project_name)
    positions = []
    for pname in project_names:
        # Simple find. Could use regex for boundary safety but exact string match is likely intended based on hints.
        # But wait, text might have newlines or extra spaces.
        # Let's try to match exact first.
        idx = text.find(pname)
        if idx != -1:
            positions.append((idx, pname))
    
    # Sort by position
    positions.sort()
    
    # Iterate through found projects and define chunks
    for i in range(len(positions)):
        start_idx, pname = positions[i]
        # End index is the start of the next project or end of text
        if i < len(positions) - 1:
            end_idx = positions[i+1][0]
        else:
            end_idx = len(text)
            
        chunk = text[start_idx:end_idx]
        
        # Extract Start Date / Begin Construction
        # Pattern: "Begin Construction: <date>" or "Start Date: <date>"
        # Looking at sample: "(cid:131) Begin Construction: Fall 2023"
        # We'll look for "Begin Construction" and capture until end of line
        
        match = re.search(r'Begin [Cc]onstruction[:\s]+([^\n\r]+)', chunk)
        date_str = None
        if match:
            date_str = match.group(1)
        else:
            # Fallback: Check "Advertise:" if considered start? 
            # Prompt says "st: Start time/date". 
            # Usually "Begin Construction" is the main one. 
            # Let's also check for "Start:" just in case.
            match_start = re.search(r'Start[:\s]+([^\n\r]+)', chunk)
            if match_start:
                date_str = match_start.group(1)
        
        if date_str:
            if is_spring_2022(date_str):
                projects_found.add(pname)

# Now join with funding data
total_funding = 0
count = 0
matched_projects = []

for pname in projects_found:
    # Find funding info
    # Assuming one record per project, but Funding table might have duplicates? 
    # Prompt says "Funding_ID" is unique. Project Name seems unique in Funding table sample.
    records = [f for f in funding_data if f['Project_Name'] == pname]
    for r in records:
        try:
            amt = float(r['Amount'])
            total_funding += amt
            count += 1
            matched_projects.append({'name': pname, 'amount': amt})
        except:
            pass

result = {
    "count": count,
    "total_funding": total_funding,
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11615212228094692141': 'file_storage/function-call-11615212228094692141.json', 'var_function-call-11615212228094691266': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13041768272351241682': 'file_storage/function-call-13041768272351241682.json', 'var_function-call-13041768272351243081': 'file_storage/function-call-13041768272351243081.json'}

exec(code, env_args)
