code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_qhebnCaD1s96wvrGHtfmMRTd, 'r') as f:
    funding_records = json.load(f)
with open(var_call_adu40HKquiSiZPCnhlp9jLxY, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame
fund_df = pd.DataFrame(funding_records)
# Normalize Amount to int
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Identify candidate disaster-related funding records by name keywords
import re
keywords = [r'FEMA', r'CalOES', r'CalJPIA', r'FEMA/CalOES', r'CalJPIA/FEMA', r'FEMA\)', r'CalOES\)', r'CalJPIA\)', r'FEMA\(', r'fire', r'Woolsey']
pattern = re.compile('|'.join(keywords), flags=re.IGNORECASE)
fund_df['is_disaster_name'] = fund_df['Project_Name'].str.contains(pattern)

candidate_funds = fund_df[fund_df['is_disaster_name']].copy()

# For each candidate project, search civic documents for occurrences and look for 2022 near start-related keywords
start_keywords = ['begin construction', 'begin construction:', 'advertise:', 'advertise', 'complete construction', 'complete construction:', 'construction was completed', 'project schedule', 'project schedule:', 'begin construction -', 'begin construction -']

# function to check if a project has a start-related 2022 mention

def project_started_in_2022(project_name, docs):
    pname = project_name
    pname_lower = pname.lower()
    for doc in docs:
        text = doc.get('text','')
        text_lower = text.lower()
        # find occurrences of project name or its core without disaster suffixes
        if pname_lower in text_lower:
            # for each occurrence, take window
            start = 0
            idx = text_lower.find(pname_lower, start)
            while idx != -1:
                window_start = max(0, idx-300)
                window_end = min(len(text_lower), idx+300)
                window = text_lower[window_start:window_end]
                # check for 2022 in same window near start keywords
                if '2022' in window:
                    # ensure a start-related keyword appears in window as well
                    for sk in start_keywords:
                        if sk in window:
                            return True
                    # Also consider lines following the project name (next 5 lines) for dates
                    tail = text_lower[idx: idx+500]
                    if '2022' in tail:
                        for sk in ['begin', 'start', 'advertis', 'construction', 'schedule', 'complete']:
                            if sk in tail:
                                return True
                # next occurrence
                idx = text_lower.find(pname_lower, idx+1)
    return False

# Also attempt to strip disaster suffixes and match base name
import re

def strip_suffix(name):
    # remove parentheses suffixes like (FEMA Project) etc.
    return re.sub(r"\s*\([^\)]*\)", "", name).strip()

# Determine which candidate funding records correspond to projects that started in 2022
started_flags = []
for _, row in candidate_funds.iterrows():
    pname = row['Project_Name']
    base = strip_suffix(pname)
    started = project_started_in_2022(pname, civic_docs) or project_started_in_2022(base, civic_docs)
    started_flags.append(started)

candidate_funds = candidate_funds.assign(started_in_2022=started_flags)

# Sum amounts where started_in_2022 is True
total = int(candidate_funds.loc[candidate_funds['started_in_2022'], 'Amount'].sum())

# As a fallback: if total is zero, try a broader heuristic: any disaster-name funding where any '2022' appears anywhere in civic docs lines mentioning the project
if total == 0:
    broader_flags = []
    for _, row in candidate_funds.iterrows():
        pname = row['Project_Name']
        base = strip_suffix(pname)
        found = False
        for doc in civic_docs:
            text = doc.get('text','').lower()
            if pname.lower() in text or base.lower() in text:
                if '2022' in text:
                    found = True
                    break
        broader_flags.append(found)
    candidate_funds = candidate_funds.assign(started_in_2022_broad=broader_flags)
    total = int(candidate_funds.loc[candidate_funds['started_in_2022_broad'], 'Amount'].sum())

# Prepare result
result = {"total_disaster_funding_started_in_2022": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qhebnCaD1s96wvrGHtfmMRTd': 'file_storage/call_qhebnCaD1s96wvrGHtfmMRTd.json', 'var_call_L0ybKHzTOLEpeYq9s9Zxi6qF': ['civic_docs'], 'var_call_adu40HKquiSiZPCnhlp9jLxY': 'file_storage/call_adu40HKquiSiZPCnhlp9jLxY.json'}

exec(code, env_args)
