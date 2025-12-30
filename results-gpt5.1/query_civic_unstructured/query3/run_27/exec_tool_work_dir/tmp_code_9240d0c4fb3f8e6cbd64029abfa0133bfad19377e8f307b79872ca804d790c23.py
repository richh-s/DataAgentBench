code = """import re, json

funding = var_call_efwyv9vmeNCegB3c7611ouON
civic = var_call_HqHppt51ZAHDqNUlZFIR1TQ3

project_status = {}
for doc in civic:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if len(line) < 120 and re.search(r'[A-Za-z]', line):
            window = ' '.join(lines[i:i+5]).lower()
            if ('emergency' in window) or ('fema' in window):
                status = 'unknown'
                wlow = window
                if ('currently under construction' in wlow) or ('construction was completed' in wlow) or ('complete construction' in wlow):
                    status = 'completed'
                if 'not started' in wlow:
                    status = 'not started'
                if ('design' in wlow) or ('preliminary design' in wlow):
                    status = 'design'
                project_status[line] = status

results = []
for row in funding:
    name = row['Project_Name']
    lname = name.lower()
    if ('fema' in lname) or ('emergency' in lname):
        status = 'unknown'
        for pname, st in project_status.items():
            pl = pname.lower()
            if (pl in lname) or (lname in pl):
                status = st
                break
        results.append({'Project_Name': name, 'Funding_Source': row['Funding_Source'], 'Amount': int(row['Amount']), 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_efwyv9vmeNCegB3c7611ouON': 'file_storage/call_efwyv9vmeNCegB3c7611ouON.json', 'var_call_HqHppt51ZAHDqNUlZFIR1TQ3': 'file_storage/call_HqHppt51ZAHDqNUlZFIR1TQ3.json'}

exec(code, env_args)
