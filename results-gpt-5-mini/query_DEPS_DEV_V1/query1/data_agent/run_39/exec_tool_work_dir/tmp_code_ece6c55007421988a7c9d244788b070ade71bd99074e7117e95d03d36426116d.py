code = """import json
# read results
res = var_call_elaX5VvPiH29hX9bLvl2gYq4
# Prepare final answer string
lines = []
for i,r in enumerate(res, start=1):
    pkg = r.get('package')
    ver = r.get('version')
    stars = r.get('stars')
    proj = r.get('project')
    lines.append(f"{i}. {pkg} ({ver}) — {stars} stars — repo: {proj}")
ans = "Top 5 NPM packages (latest release versions) by GitHub stars:\n" + "\n".join(lines)
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_odEChWwbyx3ZSKtoFlIj7SPR': 'file_storage/call_odEChWwbyx3ZSKtoFlIj7SPR.json', 'var_call_cX7ZObtVcMBUYFPZ5bTHIOB4': 'file_storage/call_cX7ZObtVcMBUYFPZ5bTHIOB4.json', 'var_call_eQzyT8z7ifD8VFtKdZCFk1cg': 'file_storage/call_eQzyT8z7ifD8VFtKdZCFk1cg.json', 'var_call_f9EegKMFs4uCCzbPvb1PZAYw': 'file_storage/call_f9EegKMFs4uCCzbPvb1PZAYw.json', 'var_call_elaX5VvPiH29hX9bLvl2gYq4': [{'package': '@easyprogram/easyregexp', 'version': '1.0.0', 'stars': 111144, 'project': 'sky111144/easyregexp'}, {'package': '@dylanvann/svelte', 'version': '3.25.4', 'stars': 73499, 'project': 'sveltejs/svelte'}, {'package': '@dumc11/tailwindcss', 'version': '0.4.0', 'stars': 73464, 'project': 'tailwindcss/tailwindcss'}, {'package': '@dman777/shadow-dom-quill-temp', 'version': '1.0.0', 'stars': 42407, 'project': 'quilljs/quill'}, {'package': '@dynasty/styled-components', 'version': '3.2.1', 'stars': 39660, 'project': 'styled-components/styled-components'}]}

exec(code, env_args)
