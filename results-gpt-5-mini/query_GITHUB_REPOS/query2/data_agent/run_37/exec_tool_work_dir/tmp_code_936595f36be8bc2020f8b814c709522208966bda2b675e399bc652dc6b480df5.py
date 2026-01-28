code = """import json, re

# Load the contents query result stored in the file path variable
path = var_call_q8fwIyRYAp5c5Hv1wl7PRIyZ
with open(path, 'r') as f:
    data = json.load(f)

# Parse the repo_data_description to extract copy counts
results = []
for rec in data:
    desc = rec.get('repo_data_description') or ''
    # look for patterns like 'copied 12 times', 'appearing 12 times', 'duplicated 12 times', 'repeated 12 times', 'seen 12 times'
    m = re.search(r"(copied|appearing|duplicated|repeated|seen)\s+(\d+)\s+times", desc, re.IGNORECASE)
    if not m:
        # sometimes 'appears 9 times'
        m = re.search(r"(appears)\s+(\d+)\s+times", desc, re.IGNORECASE)
    if not m:
        # fallback: find any number followed by 'times'
        m = re.search(r"(\d+)\s+times", desc)
    copies = int(m.group(2)) if m and m.lastindex>=2 else (int(m.group(1)) if m and m.lastindex==1 else None)
    results.append({
        'id': rec.get('id'),
        'sample_repo_name': rec.get('sample_repo_name'),
        'sample_path': rec.get('sample_path'),
        'repo_data_description': desc,
        'copies': copies
    })

# Filter to valid copies and find max
valid = [r for r in results if r['copies'] is not None]
if not valid:
    out = {'error': 'no copy counts parsed'}
else:
    maxcopies = max(r['copies'] for r in valid)
    top = [r for r in valid if r['copies']==maxcopies]
    out = {'max_copies': maxcopies, 'top_files': top}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_oSkPWzXihTqO9vvcpWCglOps': [], 'var_call_rbHOFgBtBvkb2IDJvshCTvd0': ['commits', 'contents', 'files'], 'var_call_R1k4AIpVxOEdsxHIEMKDMRNy': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'copies': '4'}, {'id': 'd67714b2a25908fbc4e6b00531862cc62265bf75', 'copies': '2'}, {'id': '0191f88060e6994e1095478da21798fd2c0a9dcb', 'copies': '2'}, {'id': 'e94c45ffe619fbd39e7f5df78a590bd33893d64a', 'copies': '2'}, {'id': 'a1615a71d1bdbb036d1dde0a94b8285fa8fca084', 'copies': '2'}, {'id': '53496cde05c660feb3ab3335e825b363aa68a51a', 'copies': '2'}, {'id': 'd1b6baa8d0bd3ac28e0765482e204e33340ccf8c', 'copies': '2'}, {'id': '8af9111216436874eecfaa475d5c2f3ac650e3bc', 'copies': '2'}, {'id': '6066caa5e76b60fbd0f7bc2a096c6fd7c023609f', 'copies': '2'}, {'id': '3252bbf919d2fb7d0f3fd9a3841f44f5f699c0c2', 'copies': '2'}, {'id': 'f260ac370354b6dc8e5fb92da276cf587dd2d4d7', 'copies': '2'}, {'id': 'f64ee245678dcb26d658600708e2996a7608fc6e', 'copies': '2'}, {'id': '731d202c0c486ce8daf377f2c6a7389cc9bc20fa', 'copies': '2'}, {'id': '75c9123b0b91ca99402ed40efe80d21cb6bc3f90', 'copies': '2'}, {'id': '49f5eda9ac693bf61324ee7f65a15d704f7f3411', 'copies': '2'}, {'id': 'a1a7098f21fbd20afe3098e33bb8e0c93b14179e', 'copies': '1'}, {'id': 'b577774bae4db39fa8a2a5c8e4b61b654085919d', 'copies': '1'}, {'id': '37104c1cea94b28d00a2c564dcd09e8f542f5ef6', 'copies': '1'}, {'id': 'ef1ba022ec64bc9c7fdbba5156a7d6eec3068e33', 'copies': '1'}, {'id': '89a00ca864c3e205b522deb9533c921cf3c1243d', 'copies': '1'}], 'var_call_59Hcnp9AAdp0opDoiQpoStl8': [], 'var_call_SVjJRBCzTSAwIFjZy3Lm8Ers': [], 'var_call_4Hs4co1epdSoWn1wbwNko0Jp': [], 'var_call_q8fwIyRYAp5c5Hv1wl7PRIyZ': 'file_storage/call_q8fwIyRYAp5c5Hv1wl7PRIyZ.json'}

exec(code, env_args)
