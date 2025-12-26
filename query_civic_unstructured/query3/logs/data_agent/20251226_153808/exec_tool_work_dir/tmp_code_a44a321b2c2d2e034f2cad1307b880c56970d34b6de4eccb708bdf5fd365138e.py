code = """import json, re, os

funding = var_call_DGRCZDX110DTY4gUivyXNyUe

def load_result(var):
    if isinstance(var, str) and var.endswith('.json') and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

records1 = load_result(var_call_O8HL1cNpcu5mycff1GaKKkO6)
records2 = load_result(var_call_Q3aM7WyVmNUCFiRmiqRtR1aa)

# Collect texts
texts = []
for rec in (records1 or []):
    if isinstance(rec, dict) and 'text' in rec:
        texts.append(rec['text'])
for rec in (records2 or []):
    if isinstance(rec, dict) and 'text' in rec:
        texts.append(rec['text'])

section_status = {
    'capital improvement projects (design)': 'design',
    'disaster projects (design)': 'design',
    'capital improvement projects (not started)': 'not started',
    'disaster projects (not started)': 'not started',
    'capital improvement projects (completed)': 'completed',
    'disaster projects (completed)': 'completed'
}

# Function to infer status from docs

def infer_status(project_keywords):
    # project_keywords: list of keywords to search (lowercase)
    for txt in texts:
        tl = txt.lower()
        # find any occurrence of all keywords in order
        pattern = r"\b" + r"\s+".join([re.escape(k) for k in project_keywords]) + r"\b"
        for m in re.finditer(pattern, tl):
            pos = m.start()
            # look back for nearest section header
            back = tl[max(0, pos-5000):pos]
            best_pos = -1
            best_status = None
            for header, st in section_status.items():
                idx = back.rfind(header)
                if idx > best_pos:
                    best_pos = idx
                    best_status = st
            if best_status:
                return best_status
    return None

results = []
for f in funding:
    pname = f['Project_Name']
    amount = f['Amount']
    try:
        amount_val = int(amount)
    except Exception:
        amount_val = amount
    # default status based on name
    status = None
    if ' - Design' in pname or 'Design' in pname:
        status = 'design'
    else:
        # try infer from docs for 'outdoor warning sirens' and 'outdoor warning signs' (sometimes phrased that way)
        status = infer_status(['outdoor', 'warning', 'sirens'])
        if not status:
            status = infer_status(['outdoor', 'warning', 'signs'])
    results.append({
        'Project_Name': pname,
        'Funding_Source': f['Funding_Source'],
        'Amount': amount_val,
        'Status': status
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_cH4C7fJd2xZs7fWLL5rhWdlZ': ['Funding'], 'var_call_XsEnhovQo3j1WNnCiDI1xqfP': 'file_storage/call_XsEnhovQo3j1WNnCiDI1xqfP.json', 'var_call_DGRCZDX110DTY4gUivyXNyUe': [{'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}], 'var_call_4sAsUUhE036JPkFHo8mr6EEY': ['civic_docs'], 'var_call_XRufoQylMP1TSUPMfklkzWQr': 'file_storage/call_XRufoQylMP1TSUPMfklkzWQr.json', 'var_call_NpJiLr4tT7FScaJ8TlQ3pQqa': 'file_storage/call_NpJiLr4tT7FScaJ8TlQ3pQqa.json', 'var_call_Xj5f3A1xhCePGEZbHKmCmUmm': 'file_storage/call_Xj5f3A1xhCePGEZbHKmCmUmm.json', 'var_call_Q3aM7WyVmNUCFiRmiqRtR1aa': 'file_storage/call_Q3aM7WyVmNUCFiRmiqRtR1aa.json', 'var_call_O8HL1cNpcu5mycff1GaKKkO6': 'file_storage/call_O8HL1cNpcu5mycff1GaKKkO6.json'}

exec(code, env_args)
