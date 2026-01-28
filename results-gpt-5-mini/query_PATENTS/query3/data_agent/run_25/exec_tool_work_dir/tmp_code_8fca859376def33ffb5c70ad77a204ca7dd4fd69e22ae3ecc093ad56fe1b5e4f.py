code = """import json
# clean up assignee names heuristically: remove leading phrases like 'The US patent filing (application number US-4007205-A)'
ass_map = var_call_JqBy4NKHg2XiJ8kO60aKjHpt
cleaned = {}
for k,v in ass_map.items():
    orig = k
    # try to find known patterns and extract proper assignee
    # If name is all caps and short, keep. Otherwise, try to parse before verbs like 'holds' etc
    if k.isupper() and len(k.split())<=4:
        name = k
    else:
        # attempt to extract entity-like substring before ' holds ' or ' holds the ' or ' is ' etc
        import re
        m = re.match(r"^([A-Z0-9 &,.\-]{2,80}?)\s+(?:holds|is|owns|with|holds the|assigned|assigned to|has|keeps)", k, re.IGNORECASE)
        if m:
            name = m.group(1).strip()
        else:
            # fallback: if contains 'patent' or 'application', skip those leading words
            name = re.sub(r"^The\s+.*?\b(?:patent|application|filing)\b.*?[:\)]?\s*", "", k, flags=re.IGNORECASE)
            name = name.strip()
            if not name:
                name = k
    cleaned[name] = v
print('__RESULT__:')
print(json.dumps(cleaned))"""

env_args = {'var_call_6s5RpImgm3iTcGaGq8ohXGZr': 'file_storage/call_6s5RpImgm3iTcGaGq8ohXGZr.json', 'var_call_gG2899rItsLZOgaJaeMhanfU': [], 'var_call_l3Wv2stVqubRXfB59zoHvWq0': 'file_storage/call_l3Wv2stVqubRXfB59zoHvWq0.json', 'var_call_CseUXkBYEh0x7C6OSnU7kxDL': {'assignee_to_cpcs': {'The US patent filing (application number US-4007205-A)': ['G01V1/01'], 'The US patent application (no. US-201715785968-A) is': ['H01M4/9066', 'H01M8/2425'], 'The US application (ID US-201414520615-A)': ['C30B11/003', 'C30B25/10', 'C30B25/16'], 'SCHOWALTER LEO J': ['H01L21/0262']}, 'cpc_codes': ['C30B11/003', 'C30B25/10', 'C30B25/16', 'G01V1/01', 'H01L21/0262', 'H01M4/9066', 'H01M8/2425'], 'num_pub_with_identified_pubnum': 277082}, 'var_call_EVz8z9z1vdgSDYsvIxpwnXrP': [{'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}, {'symbol': 'C30B25/10', 'titleFull': 'Heating of the reaction chamber or the substrate'}, {'symbol': 'C30B25/16', 'titleFull': 'Controlling or regulating'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}], 'var_call_JqBy4NKHg2XiJ8kO60aKjHpt': {'The US patent filing (application number US-4007205-A)': ['Measuring or predicting earthquakes'], 'The US patent application (no. US-201715785968-A) is': ['Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets', 'High-temperature cells with solid electrolytes'], 'The US application (ID US-201414520615-A)': ['Heating or cooling of the melt or the crystallised material', 'Heating of the reaction chamber or the substrate', 'Controlling or regulating'], 'SCHOWALTER LEO J': ['Reduction or decomposition of gaseous compounds, e.g. CVD']}}

exec(code, env_args)
