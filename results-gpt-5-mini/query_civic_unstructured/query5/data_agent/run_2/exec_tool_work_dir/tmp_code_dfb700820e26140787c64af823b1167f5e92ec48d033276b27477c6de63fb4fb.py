code = """import json, re
with open(var_call_XTpGdeOUqBGKrql77n109P0x, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_8iO6IE1pAFY52osRikfHN8xI, 'r', encoding='utf-8') as f:
    funding = json.load(f)

def to_int(x):
    try:
        return int(x)
    except:
        try:
            return int(float(x))
        except:
            return 0

funding_map = {}
for rec in funding:
    name = rec.get('Project_Name','')
    amt = to_int(rec.get('Amount',0))
    funding_map.setdefault(name,0)
    funding_map[name] += amt

disaster_tokens_in_name = ['fema','caloes','caljpia']
other_disaster_tokens = ['disaster','fire','woolsey','fema','caloes','caljpia']

matched = []
for name, amt in funding_map.items():
    name_l = name.lower()
    name_has_disaster_token = any(tok in name_l for tok in disaster_tokens_in_name)
    found_2022 = False
    found_disaster_context = False

    # Search exact occurrences of project name in civic docs
    for doc in civic_docs:
        text = doc.get('text','')
        txt = text.lower()
        idx = txt.find(name_l)
        if idx != -1:
            # examine window
            start = max(0, idx-400)
            end = min(len(txt), idx+400)
            window = txt[start:end]
            if '2022' in window:
                found_2022 = True
            if any(tok in window for tok in other_disaster_tokens):
                found_disaster_context = True
        # also, if name not found exactly, maybe it appears with minor punctuation; use word-sequence match
        else:
            # create word pattern from name with spaces/punct
            words = [w for w in re.split(r'[^a-z0-9]+', name_l) if w]
            if words:
                # require first and last word present within 100 chars
                first = words[0]
                last = words[-1]
                pos = txt.find(first)
                while pos != -1:
                    window = txt[max(0,pos-200): pos+800]
                    if last in window and all(w in window for w in words[:5]):
                        if '2022' in window:
                            found_2022 = True
                        if any(tok in window for tok in other_disaster_tokens):
                            found_disaster_context = True
                        break
                    pos = txt.find(first, pos+1)

    # Decide if disaster-related and started in 2022
    is_disaster = False
    if name_has_disaster_token:
        # if name itself indicates disaster, require 2022 found near occurrence in docs
        if found_2022:
            is_disaster = True
        else:
            # If name has disaster token but no civic doc match, still consider it disaster if funding source indicates federal? Skip for now
            is_disaster = False
    else:
        # if name doesn't have disaster token, require civic doc context mentioning disaster tokens and 2022
        if found_disaster_context and found_2022:
            is_disaster = True

    if is_disaster:
        matched.append({'Project_Name': name, 'Amount': amt})

total = sum(x['Amount'] for x in matched)
print("__RESULT__:")
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_call_XTpGdeOUqBGKrql77n109P0x': 'file_storage/call_XTpGdeOUqBGKrql77n109P0x.json', 'var_call_8iO6IE1pAFY52osRikfHN8xI': 'file_storage/call_8iO6IE1pAFY52osRikfHN8xI.json', 'var_call_31kWt76n1FWNy5CpQXbGodgQ': 'file_storage/call_31kWt76n1FWNy5CpQXbGodgQ.json'}

exec(code, env_args)
