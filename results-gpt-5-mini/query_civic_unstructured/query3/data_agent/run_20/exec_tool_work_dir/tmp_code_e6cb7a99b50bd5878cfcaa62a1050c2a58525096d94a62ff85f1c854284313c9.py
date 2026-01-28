code = """import json
import re

# Load data
with open(var_call_PiVO4fMjvPZ9Ri2Sq3DmNv40, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_VWfCe7d7cKITCZHoI1fqcWri, 'r', encoding='utf-8') as f:
    funding = json.load(f)

texts = [doc.get('text','') for doc in civic_docs]

results = []
seen = set()

def base_name(name):
    return re.sub(r"\s*\(.*?\)\s*$", "", name, flags=re.IGNORECASE).strip().lower()

status_keywords = [
    ('under construction', 'under construction'),
    ('construction was completed', 'completed'),
    ('complete construction', 'completed'),
    ('complete design', 'design complete'),
    ('preliminary design', 'preliminary design'),
    ('in the preliminary design phase', 'preliminary design'),
    ('awaiting final fema', 'awaiting FEMA approval'),
    ('awaiting final fema/caloes approval', 'awaiting FEMA/CalOES approval'),
    ('awaiting final fema/caloes approval for scope modification', 'awaiting FEMA/CalOES approval for scope modification'),
    ('advertise', 'advertising/solicitation'),
    ('begin construction', 'begin construction'),
    ('design', 'design')
]

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_l = pname.lower()
    matched = False
    status = None

    # direct name contains fema or emergency
    if 'fema' in pname_l or 'emergency' in pname_l:
        matched = True

    # search in civic texts
    if not matched:
        base = base_name(pname)
        pats = [pname.lower(), base]
        for txt in texts:
            low = txt.lower()
            for pat in pats:
                if not pat:
                    continue
                idx = low.find(pat)
                if idx != -1:
                    start = max(0, idx-200)
                    end = min(len(low), idx+len(pat)+200)
                    window = low[start:end]
                    if any(k in window for k in ['fema', 'caloes', 'emergency', 'outdoor warning', 'sirens']):
                        matched = True
                        # find status by keywords in window
                        for kw, label in status_keywords:
                            if kw in window:
                                status = label
                                break
                        if not status:
                            status = 'status not found in nearby text'
                        break
            if matched:
                break

    if matched:
        key = (pname, rec.get('Funding_Source'), rec.get('Amount'))
        if key in seen:
            continue
        seen.add(key)
        amt = rec.get('Amount')
        try:
            amt_conv = int(amt)
        except Exception:
            amt_conv = amt
        results.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': amt_conv,
            'Status': status if status else 'status not found in documents'
        })

# Sort
results = sorted(results, key=lambda x: x['Project_Name'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_PiVO4fMjvPZ9Ri2Sq3DmNv40': 'file_storage/call_PiVO4fMjvPZ9Ri2Sq3DmNv40.json', 'var_call_VWfCe7d7cKITCZHoI1fqcWri': 'file_storage/call_VWfCe7d7cKITCZHoI1fqcWri.json', 'var_call_VEl1viGQxcXHTw2tm7MVOTBD': {'civic': 'file_storage/call_PiVO4fMjvPZ9Ri2Sq3DmNv40.json', 'fund': 'file_storage/call_VWfCe7d7cKITCZHoI1fqcWri.json'}}

exec(code, env_args)
