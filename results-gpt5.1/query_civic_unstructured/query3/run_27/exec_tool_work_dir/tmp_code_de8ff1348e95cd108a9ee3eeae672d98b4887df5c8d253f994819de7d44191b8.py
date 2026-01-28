code = """import re, json

funding = var_call_efwyv9vmeNCegB3c7611ouON
civic = var_call_HqHppt51ZAHDqNUlZFIR1TQ3

# Extract project names and simple statuses from civic text
project_status = {}
for doc in civic:
    text = doc['text']
    # find lines that look like project titles followed by updates or project description
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        # heuristic: title case line, not too long
        if len(line) < 120 and re.search(r'[A-Za-z]', line):
            # check for nearby keywords emergency or FEMA in window
            window = ' '.join(lines[i:i+5]).lower()
            if 'emergency' in window or 'fema' in window:
                status = 'unknown'
                wlow = window
                if 'currently under construction' in wlow or 'construction was completed' in wlow or 'complete construction' in wlow:
                    status = 'completed'
                if 'not started' in wlow:
                    status = 'not started'
                if 'design' in wlow or 'preliminary design' in wlow:
                    status = 'design'
                project_status[line] = status

# match funding projects either containing FEMA/emergency or matching civic project names with those topics
results = []
for row in funding:
    name = row['Project_Name']
    lname = name.lower()
    if 'fema' in lname or 'emergency' in lname:
        status = 'unknown'
        # try direct match or prefix match against civic project names
        for pname, st in project_status.items():
            if pname.lower() in lname or lname in pname.lower():
                status = st
                break
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_efwyv9vmeNCegB3c7611ouON': 'file_storage/call_efwyv9vmeNCegB3c7611ouON.json', 'var_call_HqHppt51ZAHDqNUlZFIR1TQ3': 'file_storage/call_HqHppt51ZAHDqNUlZFIR1TQ3.json'}

exec(code, env_args)
