code = """import json
import re

# Load data from storage paths
with open(var_call_5EwovTJ4SinqHtiXuZdxh9NN, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_ZNZi3TGRHzg810xT0A41N95d, 'r') as f:
    funding = json.load(f)

# Prepare
disaster_keywords = ['fema', 'caloes', 'caljpia', 'caloes', 'disaster', 'fire', 'woolsey', 'fema/caloes', 'fema project', 'caloes project', '(fema', '(caloes', 'disaster recovery']
start_indicators = ['begin construction', 'begin', 'start', 'project schedule', 'advertise', 'complete design', 'construction was', 'construction was completed', 'construction started']

matched = {}

for rec in funding:
    pname = rec.get('Project_Name', '')
    amount_str = rec.get('Amount', '0')
    try:
        amount = int(amount_str)
    except:
        try:
            amount = int(float(amount_str))
        except:
            amount = 0
    pname_low = pname.lower()
    found_match = False
    # Search in civic docs texts for the project name
    for doc in civic_docs:
        text = doc.get('text', '')
        text_low = text.lower()
        idx = text_low.find(pname_low)
        if idx == -1:
            continue
        # get window
        start = max(0, idx-300)
        end = min(len(text_low), idx+len(pname_low)+300)
        window = text_low[start:end]
        # check if 2022 is in window
        if '2022' in window:
            # determine if disaster-related by checking keywords in name or window
            is_disaster = any(kw in pname_low for kw in disaster_keywords) or any(kw in window for kw in disaster_keywords)
            # also consider funding source keywords? (not available here)
            if is_disaster:
                matched[pname] = matched.get(pname, 0) + amount
                found_match = True
                break
    # If not found by exact name, try matching after stripping suffixes like parentheses
    if not found_match:
        # try simple token match for shorter forms (split on parentheses)
        pname_simple = re.split(r"\(|\-", pname)[0].strip().lower()
        if len(pname_simple) > 5 and pname_simple != pname_low:
            for doc in civic_docs:
                text_low = doc.get('text', '').lower()
                idx = text_low.find(pname_simple)
                if idx == -1:
                    continue
                start = max(0, idx-300)
                end = min(len(text_low), idx+len(pname_simple)+300)
                window = text_low[start:end]
                if '2022' in window:
                    is_disaster = any(kw in pname_simple for kw in disaster_keywords) or any(kw in window for kw in disaster_keywords)
                    if is_disaster:
                        matched[pname] = matched.get(pname, 0) + amount
                        found_match = True
                        break

# Sum unique matched amounts
total = sum(matched.values())

# Prepare output
result = {
    'total': total,
    'matched_projects': [{'Project_Name': k, 'Amount': v} for k, v in matched.items()]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_b52KfjzGZYAZvJdS6irAH9g9': ['civic_docs'], 'var_call_aFHekwAG1QNPRjG56qqjqpqs': ['Funding'], 'var_call_5EwovTJ4SinqHtiXuZdxh9NN': 'file_storage/call_5EwovTJ4SinqHtiXuZdxh9NN.json', 'var_call_ZNZi3TGRHzg810xT0A41N95d': 'file_storage/call_ZNZi3TGRHzg810xT0A41N95d.json'}

exec(code, env_args)
