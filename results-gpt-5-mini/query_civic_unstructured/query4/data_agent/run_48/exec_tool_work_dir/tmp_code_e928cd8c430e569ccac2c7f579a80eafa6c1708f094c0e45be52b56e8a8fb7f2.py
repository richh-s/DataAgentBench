code = """import json
path = var_call_p0BJfJnAHeSkmth79jwrGCCJ
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# convert Amounts to integers
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

# Save processed funding to output
out = funding
print('__RESULT__:')
print(json.dumps(out[:200]))  # print first 200 records for brevity"""

env_args = {'var_call_BbHlkOS5ptYiDuPuA4GtohCC': 'file_storage/call_BbHlkOS5ptYiDuPuA4GtohCC.json', 'var_call_wzdYOCoVDSdfZqe0nUNWVPJq': [], 'var_call_GlrSSShezpsTLg3CJ6gEOWVe': 'file_storage/call_GlrSSShezpsTLg3CJ6gEOWVe.json', 'var_call_p0BJfJnAHeSkmth79jwrGCCJ': 'file_storage/call_p0BJfJnAHeSkmth79jwrGCCJ.json'}

exec(code, env_args)
