code = """import json, re, os

# Load funding entries
funding = var_call_DGRCZDX110DTY4gUivyXNyUe

# Ensure read docs results fully; they might be file paths (strings) or lists

def load_result(var):
    if isinstance(var, str) and var.endswith('.json') and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

records1 = load_result(var_call_O8HL1cNpcu5mycff1GaKKkO6)
records2 = load_result(var_call_Q3aM7WyVmNUCFiRmiqRtR1aa)

# Combine unique docs by filename
docs = {}
for rec in (records1 or []):
    docs[rec['filename']] = rec['text']
for rec in (records2 or []):
    docs[rec['filename']] = rec['text']

# Helper to infer status from surrounding headers
section_status_map = {
    'capital improvement projects (design)': 'design',
    'disaster projects (design)': 'design',
    'capital improvement projects (construction)': 'completed',  # could be under construction; but statuses expected are 'design', 'completed', 'not started'. We'll map construction to 'design'? But use 'design'/'not started'/'completed'. However we can mark 'design' if design; 'completed' only if in completed section; 'not started' if in Not Started.
    'capital improvement projects (not started)': 'not started',
    'disaster projects (construction)': 'completed',
    'disaster projects (not started)': 'not started',
    'capital improvement projects (completed)': 'completed',
    'disaster projects (completed)': 'completed'
}

# We adjust: treat '(construction)' as neither completed nor design; but the allowed statuses given are only design, completed, not started. The doc may contain construction. We'll map 'construction' to 'design'? That is not accurate. Better map 'construction' to 'design' doesn't fit. The problem statement says statuses are 3. We'll map 'construction' to 'design'? Hmm. We'll avoid mapping 'construction' unless needed. We'll only map to 'design', 'not started', or 'completed'. For construction, we leave as None and will prefer other sections.
section_status_map_specific = {
    'capital improvement projects (design)': 'design',
    'disaster projects (design)': 'design',
    'capital improvement projects (not started)': 'not started',
    'disaster projects (not started)': 'not started',
    'capital improvement projects (completed)': 'completed',
    'disaster projects (completed)': 'completed'
}

# For each funding entry, try to find status
results = []
for f in funding:
    pname = f['Project_Name']
    # normalize search key
    base = pname
    # remove content in parentheses and extra hyphen detail ' - Design'
    base = re.sub(r"\s*\(.*?\)", "", base).strip()
    base = base.replace(' - Design', '').strip()
    base = re.sub(r"\s+", " ", base)
    status_found = None
    evidence = []
    for fname, text in docs.items():
        # Lowercase for search
        t = text
        tl = t.lower()
        # find occurrences of 'outdoor warning sirens' regardless of base details
        if 'outdoor warning sirens' in tl:
            # identify positions
            for m in re.finditer(r"outdoor\s+warning\s+sirens", tl):
                pos = m.start()
                # find the nearest section header above
                # scan up to 2000 chars back
                start = max(0, pos - 4000)
                context = tl[start:pos]
                # find last occurrence of a section header pattern like '\n... Projects (Something)'
                # We'll search all header keys and pick the last match
                header_pos = -1
                header_status = None
                for header, stat in section_status_map_specific.items():
                    idx = context.rfind(header)
                    if idx > header_pos:
                        header_pos = idx
                        header_status = stat
                if header_status:
                    status_found = header_status
                    evidence.append({"filename": fname, "status": header_status})
                    break
            if status_found:
                break
    results.append({
        'Project_Name': pname,
        'Funding_Source': f['Funding_Source'],
        'Amount': int(f['Amount']) if isinstance(f['Amount'], (int, float, str)) and str(f['Amount']).isdigit() else f['Amount'],
        'Status': status_found
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_cH4C7fJd2xZs7fWLL5rhWdlZ': ['Funding'], 'var_call_XsEnhovQo3j1WNnCiDI1xqfP': 'file_storage/call_XsEnhovQo3j1WNnCiDI1xqfP.json', 'var_call_DGRCZDX110DTY4gUivyXNyUe': [{'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}], 'var_call_4sAsUUhE036JPkFHo8mr6EEY': ['civic_docs'], 'var_call_XRufoQylMP1TSUPMfklkzWQr': 'file_storage/call_XRufoQylMP1TSUPMfklkzWQr.json', 'var_call_NpJiLr4tT7FScaJ8TlQ3pQqa': 'file_storage/call_NpJiLr4tT7FScaJ8TlQ3pQqa.json', 'var_call_Xj5f3A1xhCePGEZbHKmCmUmm': 'file_storage/call_Xj5f3A1xhCePGEZbHKmCmUmm.json', 'var_call_Q3aM7WyVmNUCFiRmiqRtR1aa': 'file_storage/call_Q3aM7WyVmNUCFiRmiqRtR1aa.json', 'var_call_O8HL1cNpcu5mycff1GaKKkO6': 'file_storage/call_O8HL1cNpcu5mycff1GaKKkO6.json'}

exec(code, env_args)
