code = """import json
from pathlib import Path
p = Path(var_call_UGXRs02smPa8XIJInYASS4bD)
records = json.loads(p.read_text())
result_titles = []
for rec in records:
    filename = rec.get('filename','')
    text = rec.get('text','')
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # check domain mention
    if 'physical activity' in text.lower():
        # check publication year 2016 present in text
        if '2016' in text:
            result_titles.append(title)
# deduplicate
result_titles = sorted(list(dict.fromkeys(result_titles)))
import json
print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_call_UGXRs02smPa8XIJInYASS4bD': 'file_storage/call_UGXRs02smPa8XIJInYASS4bD.json'}

exec(code, env_args)
