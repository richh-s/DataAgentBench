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

# Keywords to look for
keywords = ['park', 'road', 'emergency', 'FEMA', 'capital', 'fire', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail']
target_keywords = ['emergency', 'FEMA']

status_map = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction", # Will refine
    "Capital Improvement Projects (Not Started)": "not started"
}

for doc in docs:
    text = doc['text']
    # Split text by sections
    # Sections seem to be denoted by "Capital Improvement Projects (...)"
    # We can find the indices of these headers
    
    sections = []
    for header, status_code in status_map.items():
        if header in text:
            sections.append((text.find(header), header, status_code))
    
    sections.sort() # Sort by position
    
    for i in range(len(sections)):
        start_idx = sections[i][0]
        header = sections[i][1]
        base_status = sections[i][2]
        
        end_idx = sections[i+1][0] if i + 1 < len(sections) else len(text)
        section_text = text[start_idx + len(header):end_idx]
        
        # Now parse projects within section text
        # Projects seem to start with a Name line followed by (cid:190) Updates: or (cid:190) Project Description:
        # Regex: Look for a line that is followed by the marker
        
        # Split by the marker, but keep the preceding line?
        # Alternative: The text uses (cid:190) which is likely a bullet point character.
        # Project structure:
        # [Project Name]
        # (cid:190) Updates: ...
        # ...
        
        # Let's find all occurrences of (cid:190) Updates: or (cid:190) Project Description:
        # and take the line before it as the Project Name.
        
        # regex to find the split points
        # pattern = r"\n\n(.*?)\n\n\(cid:190\) (Updates|Project Description):"
        # The text format in preview:
        # "2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:"
        
        # We can iterate through matches
        pattern = re.compile(r"(?:\n|^)(?P<name>[^\n]+)\n+(?:\(cid:190\)|●|▪|\u2022)\s*(?:Updates|Project Description):", re.MULTILINE)
        
        matches = list(pattern.finditer(section_text))
        
        for j in range(len(matches)):
            match = matches[j]
            proj_name = match.group("name").strip()
            
            # The content of the project is from the start of this match (or end of header) to the start of next match
            content_start = match.end()
            content_end = matches[j+1].start() if j + 1 < len(matches) else len(section_text)
            proj_content = section_text[content_start:content_end]
            
            # Refine status
            status = base_status
            if base_status == "construction":
                if "Construction was completed" in proj_content or "Notice of completion filed" in proj_content:
                    status = "completed"
                elif "Project is currently under construction" in proj_content:
                    status = "design" # User prompt says only 3 statuses. Active construction is closest to 'design' (in progress) or maybe I should output 'completed' only if done?
                    # Actually, let's keep it as "construction" or "design" but wait, the prompt explicitly listed statuses.
                    # "design" (planning/design), "completed", "not started".
                    # If I MUST pick one, maybe "design" fits "underway"? Or "completed" fits "funded"? 
                    # Let's check if I can just output "under construction". The prompt says "Projects have three statuses...". This implies the answer should likely use these.
                    # But if I report "construction", it's factual.
                    # Let's look at the result: "Capital Improvement Projects (Design)" -> "design".
                    # Let's output "design" for under construction? No that's misleading.
                    # I will assume "design" covers "in progress" or the prompt is just listing examples.
                    # Let's stick to "construction" if strictly "under construction", but map to "completed" if finished.
                    pass 
            
            # Topics
            found_topics = []
            combined_text = (proj_name + " " + proj_content).lower()
            for kw in keywords:
                if kw.lower() in combined_text:
                    found_topics.append(kw)
            
            # Extract Dates (st, et)
            # Look for "Complete Design:", "Begin Construction:", "Complete Construction:", "Advertise:"
            # Regex for dates
            date_matches = re.findall(r"(Complete Design|Begin Construction|Complete Construction|Advertise|Final Design):?\s*([A-Za-z0-9,\s]+)", proj_content)
            # Store dates as a list or dict
            dates = {k.strip(): v.strip() for k, v in date_matches}
            
            # Check if relevant (emergency or FEMA)
            is_relevant = False
            for kw in target_keywords:
                if kw.lower() in combined_text:
                    is_relevant = True
                    break
            
            # Also check if funding project name has FEMA
            # (We will do this after joining or here if we fuzzy match)
            
            projects.append({
                "Project_Name": proj_name,
                "Status": status,
                "Topics": found_topics,
                "Dates": dates,
                "Is_Relevant_Text": is_relevant,
                "Full_Text": proj_content # for debugging or further checks
            })

df_projects = pd.DataFrame(projects)

# Now join with funding
# Funding names might differ. Let's try exact match first, then substring.
# Normalized join column
df_funding['join_key'] = df_funding['Project_Name'].str.lower().str.strip()
df_projects['join_key'] = df_projects['Project_Name'].str.lower().str.strip()

# Merge
merged = pd.merge(df_projects, df_funding, on='join_key', how='left', suffixes=('', '_funding'))

# Fill Is_Relevant based on Funding Name too
merged['Is_Relevant_Funding'] = merged['Project_Name_funding'].astype(str).str.contains('emergency|FEMA', case=False, regex=True)
merged['Is_Relevant'] = merged['Is_Relevant_Text'] | merged['Is_Relevant_Funding']

# Filter
result_df = merged[merged['Is_Relevant']].copy()

# Formatting result
final_columns = ['Project_Name', 'Funding_Source', 'Amount', 'Status', 'Topics', 'Dates']
# Use Project_Name from funding if available (it's cleaner usually), else extracted
result_df['Project_Name'] = result_df['Project_Name_funding'].fillna(result_df['Project_Name'])

print("__RESULT__:")
print(result_df[final_columns].to_json(orient='records'))"""

env_args = {'var_function-call-4192215151994041760': 'file_storage/function-call-4192215151994041760.json', 'var_function-call-15165357656390883116': 'file_storage/function-call-15165357656390883116.json', 'var_function-call-13981208063081827307': 'file_storage/function-call-13981208063081827307.json'}

exec(code, env_args)
