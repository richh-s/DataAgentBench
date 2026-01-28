code = """import json
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_function-call-15165357656390883116']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)
df_funding = pd.DataFrame(funding_records)

# Load civic docs
docs_path = locals()['var_function-call-13981208063081827307']
with open(docs_path, 'r') as f:
    docs = json.load(f)

projects = []

status_map = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

keywords = ['park', 'road', 'emergency', 'FEMA', 'capital', 'fire', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail']
target_keywords = ['emergency', 'FEMA']

for doc in docs:
    text = doc['text']
    
    sections = []
    for header, status_code in status_map.items():
        idx = text.find(header)
        if idx != -1:
            sections.append((idx, header, status_code))
    
    sections.sort(key=lambda x: x[0])
    
    for i in range(len(sections)):
        start_idx = sections[i][0] + len(sections[i][1])
        status = sections[i][2]
        
        end_idx = sections[i+1][0] if i + 1 < len(sections) else len(text)
        section_text = text[start_idx:end_idx]
        
        # Split by the pattern that indicates a project update block
        # Pattern: \n[Name]\n(cid:190) Updates:
        # We'll split by "(cid:190) Updates:" or "(cid:190) Project Description:"
        # But we need the name which is before it.
        
        # Let's iterate line by line to be safer?
        # Or use regex finditer.
        # The name is usually non-empty line before the marker.
        
        # Regex: Capture the line before the marker
        # We need to be careful about newlines.
        # (?:^|\n)\s*(?P<name>[^\n]+?)\s*\n+\s*\(cid:190\)\s*(?:Updates|Project Description):
        
        pattern = re.compile(r"(?:^|\n)\s*(?P<name>[^\n]+?)\s*\n+\s*\(cid:190\)\s*(?:Updates|Project Description):")
        
        matches = list(pattern.finditer(section_text))
        
        for j, match in enumerate(matches):
            proj_name = match.group('name').strip()
            
            # Content is from match end to next match start
            content_start = match.end()
            content_end = matches[j+1].start() if j + 1 < len(matches) else len(section_text)
            proj_content = section_text[content_start:content_end]
            
            # Determine refined status
            current_status = status
            if status == 'construction':
                if 'Construction was completed' in proj_content or 'Notice of completion filed' in proj_content:
                    current_status = 'completed'
                # If 'under construction', keep as 'construction' (or 'design' if forced, but let's stick to accurate extraction first)
            
            # Topics
            found_topics = [kw for kw in keywords if kw.lower() in (proj_name + " " + proj_content).lower()]
            
            # Relevance
            combined = (proj_name + " " + proj_content).lower()
            is_relevant = any(kw.lower() in combined for kw in target_keywords)
            
            projects.append({
                "Project_Name": proj_name,
                "Status": current_status,
                "Topics": found_topics,
                "Is_Relevant_Text": is_relevant,
                "raw_text": proj_content
            })

df_projects = pd.DataFrame(projects)

# Prepare join keys
df_funding['join_key'] = df_funding['Project_Name'].str.lower().str.strip()
df_projects['join_key'] = df_projects['Project_Name'].str.lower().str.strip()

# Merge
# Note: Extracted names might have extra chars or slight diffs.
# "Corral Canyon Culvert Repairs" vs "Corral Canyon Culvert Repairs (FEMA Project)"
# The text extraction usually gives the base name.
# We should try to match: extracted_name in funding_name OR funding_name in extracted_name
# But pandas merge only does exact.
# Let's do exact merge first.
merged = pd.merge(df_projects, df_funding, on='join_key', how='inner')

# If exact merge misses, we might need fuzzy matching.
# Let's check how many we got.
if len(merged) < len(df_projects):
    # Try finding funding where funding name contains extracted name
    # We can iterate through df_projects and find match in df_funding
    
    # Create a mapping dictionary
    mapping = {}
    funding_names = df_funding['join_key'].unique()
    
    for pname in df_projects['join_key'].unique():
        # Check if pname is substring of any funding name or vice versa
        # Actually, extracted name "Latigo Canyon Road Retaining Wall Repair Project" 
        # Funding name might be "Latigo Canyon Road Retaining Wall Repair Project" or with suffix.
        
        match = None
        for fname in funding_names:
            if pname == fname:
                match = fname
                break
            # Try substring
            if pname in fname: # Text name is substring of funding name (e.g. "Project" vs "Project (FEMA)")
                match = fname # Prefer the funding name as it might have more info? Or just link them.
                # Only if it's a strong match.
                # "Park" in "Bluffs Park" -> Bad.
                # "Corral Canyon Culvert Repairs" in "Corral Canyon Culvert Repairs (FEMA Project)" -> Good.
                if len(pname) > 10: 
                    match = fname
                    break
            if fname in pname:
                if len(fname) > 10:
                    match = fname
                    break
        
        if match:
            mapping[pname] = match

    df_projects['join_key_mapped'] = df_projects['join_key'].map(mapping)
    merged_fuzzy = pd.merge(df_projects, df_funding, left_on='join_key_mapped', right_on='join_key', how='inner', suffixes=('', '_funding'))
    
    # Combine exact and fuzzy results?
    # Actually, the mapping covers exact matches too if logic included it.
    final_merged = merged_fuzzy
else:
    final_merged = merged

# Filter for relevance
# Is_Relevant_Text is True OR Funding Name has keywords
final_merged['Is_Relevant_Funding'] = final_merged['Project_Name_funding'].astype(str).str.contains('emergency|FEMA', case=False, regex=True)
final_merged['Is_Relevant'] = final_merged['Is_Relevant_Text'] | final_merged['Is_Relevant_Funding']

result = final_merged[final_merged['Is_Relevant']].copy()

# Select columns
# Status from text is likely more up to date or accurate than nothing.
# Funding details from funding DB.
columns = ['Project_Name_funding', 'Funding_Source', 'Amount', 'Status']
result['Project_Name'] = result['Project_Name_funding']

print("__RESULT__:")
print(result[columns].to_json(orient='records'))"""

env_args = {'var_function-call-4192215151994041760': 'file_storage/function-call-4192215151994041760.json', 'var_function-call-15165357656390883116': 'file_storage/function-call-15165357656390883116.json', 'var_function-call-13981208063081827307': 'file_storage/function-call-13981208063081827307.json'}

exec(code, env_args)
