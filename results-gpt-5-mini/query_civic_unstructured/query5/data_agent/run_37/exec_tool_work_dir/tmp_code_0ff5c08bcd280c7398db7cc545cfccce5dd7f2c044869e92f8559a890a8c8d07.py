code = """import json
import re

# Load previous tool results from storage paths
with open(var_call_xYjxDFVtmV0T7uhUW6fn1MPb, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_saf1zSumCBClpwwtOFQoyZwV, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Prepare
funding_records = funding_rows

# Heuristics
disaster_indicators = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'fema/caloes', 'fire', 'woolsey', 'disaster', 'emergency', 'flood']

def is_disaster_by_name(name):
    if not name:
        return False
    ln = name.lower()
    for kw in disaster_indicators:
        if kw in ln:
            return True
    return False

# Search civic docs for context around project name
def find_contexts_for_project(name, docs, window=200):
    contexts = []
    if not name:
        return contexts
    name_escaped = re.escape(name)
    pattern = re.compile(name_escaped, re.IGNORECASE)
    for doc in docs:
        text = doc.get('text','')
        for m in pattern.finditer(text):
            start = max(0, m.start()-window)
            end = min(len(text), m.end()+window)
            contexts.append(text[start:end])
    return contexts

# Also try fuzzy by splitting project name into important tokens (drop small words)
stopwords = set(['and','the','of','at','in','project','improvements','repair','repairs','road','roadway','roadway/retaining','retaining','improvement','phase','design'])

def token_based_contexts(name, docs, window=200):
    contexts = []
    if not name:
        return contexts
    tokens = [t for t in re.split('[^A-Za-z0-9]+', name.lower()) if t and t not in stopwords and len(t)>=4]
    if not tokens:
        return contexts
    # require at least two tokens to match
    for doc in docs:
        text = doc.get('text','').lower()
        for i in range(len(text)):
            pass
        # simple approach: check if all tokens appear within a slice of text length 400
        for i in range(len(text)):
            pass
        # Instead, find first token occurrence and check nearby for others
        for t in tokens:
            for m in re.finditer(re.escape(t), text):
                start = max(0, m.start()-window)
                end = min(len(text), m.end()+window)
                slice_ = text[start:end]
                if all(tok in slice_ for tok in tokens[:min(3,len(tokens))]):
                    contexts.append(slice_)
    return contexts

# Determine if a context indicates start in 2022

def context_has_2022_and_start_indicators(ctx):
    if not ctx:
        return False
    if '2022' in ctx:
        # Check for 'begin', 'start', 'advertise', or 'construction' near 2022
        # If 2022 appears anywhere in context, accept
        return True
    return False

# Now evaluate each funding record
total = 0
matched_records = []
for rec in funding_records:
    name = rec.get('Project_Name')
    amount_raw = rec.get('Amount',0)
    try:
        amount = int(amount_raw)
    except:
        try:
            amount = int(float(amount_raw))
        except:
            amount = 0
    disaster_name_flag = is_disaster_by_name(name)
    started_2022_flag = False

    # If project name itself contains 2022, mark started_2022
    if name and '2022' in name:
        started_2022_flag = True

    # search civic docs for contexts
    contexts = find_contexts_for_project(name, civic_docs)
    if not contexts:
        # try token based contexts
        contexts = token_based_contexts(name, civic_docs)

    # analyze contexts
    for ctx in contexts:
        low = ctx.lower()
        if '2022' in low:
            started_2022_flag = True
        # check if context mentions disaster indicators
        if not disaster_name_flag:
            for kw in disaster_indicators:
                if kw in low:
                    disaster_name_flag = True
                    break
    # Final decision: require both flags
    if disaster_name_flag and started_2022_flag:
        total += amount
        matched_records.append({'Project_Name': name, 'Amount': amount})

# Additionally, there may be projects listed in civic docs under Disaster Recovery Projects heading without FEMA tag but disaster-related.
# Attempt to extract simple list of projects in civic docs that are within a 'Disaster Recovery Projects' section and contain 2022
for doc in civic_docs:
    text = doc.get('text','')
    low = text.lower()
    if 'disaster recovery projects' in low or 'disaster recovery' in low:
        # extract lines around that heading
        idx = low.find('disaster recovery')
        snippet = text[idx: idx+5000]
        # find project-like lines: lines with 'Project' or title-cased lines followed by updates
        lines = re.split('\n+', snippet)
        for ln in lines:
            if len(ln.strip())<5:
                continue
            if 'project' in ln.lower() or 'repairs' in ln.lower() or 'improvements' in ln.lower():
                # try to match this line to a funding record
                for rec in funding_records:
                    pname = rec.get('Project_Name','')
                    if pname.lower() in ln.lower() or ln.lower() in pname.lower():
                        # if this snippet contains 2022
                        if '2022' in snippet:
                            try:
                                amt = int(rec.get('Amount',0))
                            except:
                                amt = 0
                            # if not already counted and appears disaster-related in name or snippet
                            already = any(r['Project_Name']==pname and r['Amount']==amt for r in matched_records)
                            disaster_flag = is_disaster_by_name(pname) or any(kw in snippet.lower() for kw in disaster_indicators)
                            if disaster_flag and not already:
                                total += amt
                                matched_records.append({'Project_Name': pname, 'Amount': amt})

# Prepare result
result = {'total_disaster_funding_started_2022': total, 'matched_records': matched_records}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5UWQMcOPol6UzCwliXq5ldyo': ['civic_docs'], 'var_call_9NLdNOA90UOg67wMOYnq3dvj': ['Funding'], 'var_call_xYjxDFVtmV0T7uhUW6fn1MPb': 'file_storage/call_xYjxDFVtmV0T7uhUW6fn1MPb.json', 'var_call_saf1zSumCBClpwwtOFQoyZwV': 'file_storage/call_saf1zSumCBClpwwtOFQoyZwV.json'}

exec(code, env_args)
