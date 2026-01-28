code = """import json, os, re

funding = var_call_DGRCZDX110DTY4gUivyXNyUe

# Only consider FEMA-related emergency warning projects (sirens)
projects = [f for f in funding if ('Warning' in f['Project_Name'] and 'FEMA' in f['Project_Name'])]

# Load full results for relevant civic docs queries
paths = [var_call_O8HL1cNpcu5mycff1GaKKkO6, var_call_Q3aM7WyVmNUCFiRmiqRtR1aa, var_call_n7ElYfWMCkC5VPCbzm93dCtR]

def load_records(path_or_list):
    if isinstance(path_or_list, str) and path_or_list.endswith('.json') and os.path.exists(path_or_list):
        with open(path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif isinstance(path_or_list, list):
        return path_or_list
    else:
        return []

records = []
for p in paths:
    records.extend(load_records(p))

# Build searchable corpus
corpus = []
for rec in records:
    if isinstance(rec, dict) and 'text' in rec:
        corpus.append(rec['text'])

# Map document section headers to normalized status
header_status_map = {
    'capital improvement projects (design)': 'design',
    'disaster projects (design)': 'design',
    'capital improvement projects (not started)': 'not started',
    'disaster projects (not started)': 'not started',
    'capital improvement projects (completed)': 'completed',
    'disaster projects (completed)': 'completed'
}

# Helper to find status near a given keyword phrase

def find_status_for_phrase(phrase):
    phrase_l = phrase.lower()
    for text in corpus:
        tl = text.lower()
        # find all occurrences
        for m in re.finditer(re.escape(phrase_l), tl):
            pos = m.start()
            # look back up to 5000 chars for the last section header
            back = tl[max(0, pos-5000):pos]
            best = None
            best_idx = -1
            for header, status in header_status_map.items():
                idx = back.rfind(header)
                if idx > best_idx:
                    best_idx = idx
                    best = status
            if best:
                return best
    return None

# Also try generic 'outdoor warning sirens'

def infer_status_for_project_name(pname):
    # If the name itself contains 'Design', set design
    if 'design' in pname.lower():
        return 'design'
    # Try exact phrase search first (without parentheses content)
    base = re.sub(r"\s*\(.*?\)", "", pname).strip()
    status = find_status_for_phrase(base)
    if status:
        return status
    # Try generic
    status = find_status_for_phrase('outdoor warning sirens')
    if status:
        return status
    # Try with potential typo 'outdoor warningn sirens'
    status = find_status_for_phrase('outdoor warningn sirens')
    return status

results = []
for f in projects:
    status = infer_status_for_project_name(f['Project_Name'])
    # Convert amount to int if possible
    amt = f['Amount']
    try:
        amt_val = int(amt)
    except Exception:
        amt_val = amt
    results.append({
        'Project_Name': f['Project_Name'],
        'Funding_Source': f['Funding_Source'],
        'Amount': amt_val,
        'Status': status
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_cH4C7fJd2xZs7fWLL5rhWdlZ': ['Funding'], 'var_call_XsEnhovQo3j1WNnCiDI1xqfP': 'file_storage/call_XsEnhovQo3j1WNnCiDI1xqfP.json', 'var_call_DGRCZDX110DTY4gUivyXNyUe': [{'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}], 'var_call_4sAsUUhE036JPkFHo8mr6EEY': ['civic_docs'], 'var_call_XRufoQylMP1TSUPMfklkzWQr': 'file_storage/call_XRufoQylMP1TSUPMfklkzWQr.json', 'var_call_NpJiLr4tT7FScaJ8TlQ3pQqa': 'file_storage/call_NpJiLr4tT7FScaJ8TlQ3pQqa.json', 'var_call_Xj5f3A1xhCePGEZbHKmCmUmm': 'file_storage/call_Xj5f3A1xhCePGEZbHKmCmUmm.json', 'var_call_Q3aM7WyVmNUCFiRmiqRtR1aa': 'file_storage/call_Q3aM7WyVmNUCFiRmiqRtR1aa.json', 'var_call_O8HL1cNpcu5mycff1GaKKkO6': 'file_storage/call_O8HL1cNpcu5mycff1GaKKkO6.json', 'var_call_EkMZkcDvGNiIT4jmosYFrXdS': [{'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': None}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': None}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'design'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'design'}], 'var_call_n7ElYfWMCkC5VPCbzm93dCtR': 'file_storage/call_n7ElYfWMCkC5VPCbzm93dCtR.json'}

exec(code, env_args)
