code = """import json

# Load knowledge articles from storage file path var_call_w1moNA8s4G1hUxzaq61kJOlr
path = var_call_w1moNA8s4G1hUxzaq61kJOlr
with open(path, 'r') as f:
    kas = json.load(f)

# Normalize IDs: remove leading # and strip
def normalize(idv):
    if idv is None:
        return None
    s = str(idv).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Look for knowledge articles that might be linked to the case id or related issue
# First, check for any article where faq_answer__c, title, or summary contain the case id (unlikely)
case_id = '500Wt00000DDyznIAD'

matches = []
for k in kas:
    nid = normalize(k.get('id'))
    if nid is None:
        continue
    # direct match
    if case_id.lower() == nid.lower():
        matches.append(k)
    # if case id substring appears anywhere in text fields
    for field in ['title','faq_answer__c','summary','urlname']:
        val = k.get(field,'')
        if val and case_id.lower() in str(val).lower():
            if k not in matches:
                matches.append(k)

# If no matches, we may need to look up the Case and see issueid__c then match issue to knowledge article
# Load the matching case from previous result
case_matches = json.loads(open(var_call_KqqxXCXZiRLgSMU0umFBHiMF).read())
# var_call_KqqxXCXZiRLgSMU0umFBHiMF contains printed output format, so it's JSON list string
# The content is a printed JSON string. Let's parse it properly.

# Actually var_call_KqqxXCXZiRLgSMU0umFBHiMF is a small JSON file that contains the print outputs.
# To be safe, open the original case file and find the case entry
cases_path = var_call_81qCXhrIirIMkLjSQmtstroQ
with open(cases_path, 'r') as f:
    cases = json.load(f)

# find case with id matching (normalize)
found_case = None
for c in cases:
    cid = normalize(c.get('id'))
    if cid and cid.lower() == case_id.lower():
        found_case = c
        break
    # also check if matches with leading #
    if ('#'+case_id).lower() == str(c.get('id','')).strip().lower():
        found_case = c
        break

result = None
if found_case:
    # get issueid__c and see if it maps to a knowledge article via title/summary
    issueid = found_case.get('issueid__c')
    # search knowledge articles for issue name or description
    if issueid:
        # query issue__c table
        # but we cannot call query_db here; we will just search local kas for issueid
        for k in kas:
            # maybe urlname or summary contains issueid
            for field in ['title','summary','faq_answer__c','urlname']:
                val = k.get(field,'')
                if val and issueid.lower() in str(val).lower():
                    matches.append(k)

# If matches found, prepare their normalized ids
match_ids = [normalize(m.get('id')) for m in matches]

print('__RESULT__:')
print(json.dumps(match_ids))"""

env_args = {'var_call_s1lNhDjFiycvs4aDFcZmLIc4': [], 'var_call_81qCXhrIirIMkLjSQmtstroQ': 'file_storage/call_81qCXhrIirIMkLjSQmtstroQ.json', 'var_call_KqqxXCXZiRLgSMU0umFBHiMF': ['#500Wt00000DDyznIAD'], 'var_call_NEBXdFJ8Pz3n00XbC4nqWDw2': [], 'var_call_w1moNA8s4G1hUxzaq61kJOlr': 'file_storage/call_w1moNA8s4G1hUxzaq61kJOlr.json'}

exec(code, env_args)
