code = """import json

def norm(x):
    return None if x is None else str(x).replace('#','').strip()

opp = var_call_I9gIINqF5RKNkWPf019kbSpx
prod = {norm(r['Id']): r for r in var_call_LZlpOhg9jxQQi4i41BgSmidz}

# choose product that best matches 'AI processing unit' intent; only one has AI in name
candidates = []
for r in opp:
    pid = norm(r['Product2Id'])
    p = prod.get(pid)
    name = (p.get('Name') if p else '') or ''
    desc = (p.get('Description') if p else '') or ''
    text = (name + ' ' + desc).lower()
    score = 0
    if 'ai' in text: score += 2
    if 'unit' in text or 'processing' in text: score += 1
    if 'chip' in text or 'accelerator' in text: score += 1
    candidates.append((score, pid))

# pick highest score; tie-breaker arbitrary
candidates.sort(reverse=True)
answer = candidates[0][1] if candidates else None

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_uvbWSyFehHJHxPjbkCh20mUO': [{'Product2Id': '01tWt000006hV8LIAU', 'EffectiveDate': '2021-06-15'}, {'Product2Id': '01tWt000006hTUkIAM', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV57IAE', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-06-01'}], 'var_call_afDyPj95J9XyA9uVnUrtqPda': [], 'var_call_I9gIINqF5RKNkWPf019kbSpx': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_qPpXKLx7H3a4mLrF6b1SKxdZ': [], 'var_call_eg2XKTjBOacA0yJIzWQdpvlS': [], 'var_call_LZlpOhg9jxQQi4i41BgSmidz': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer', 'Description': 'Cloud-based design collaboration tool enhancing team productivity across global projects.'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite', 'Description': 'Comprehensive security and compliance modules with integrated data protection features.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}]}

exec(code, env_args)
