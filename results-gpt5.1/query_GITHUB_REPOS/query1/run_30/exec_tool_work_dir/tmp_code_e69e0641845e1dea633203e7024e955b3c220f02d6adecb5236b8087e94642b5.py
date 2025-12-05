code = """import json, pandas as pd

readme_meta_path = var_call_sninqBPE2bhsTyUkAUgrIju3
langs_path = var_call_4aLLA4dvTVTqrO03GuHfQPOX
readme_contents_path = var_call_pPSsbpUTewWWDqfX0IV3Sko

readme_meta = pd.read_json(readme_meta_path)
langs = pd.read_json(langs_path)
readme_contents = pd.read_json(readme_contents_path)

langs_no_py = langs[~langs['language_description'].str.contains('Python', case=False, na=False)]

readme_meta_no_py = readme_meta[readme_meta['sample_repo_name'].isin(langs_no_py['repo_name'])]

readmes_no_py = readme_meta_no_py.merge(readme_contents, on='id', how='left')

copyright_mask = readmes_no_py['content'].str.contains('copyright', case=False, na=False)

total = int(len(readmes_no_py))
with_copyright = int(copyright_mask.sum())
prop = with_copyright / total if total > 0 else None

result = {
  'total_readmes_non_python_repos': total,
  'readmes_with_copyright_info': with_copyright,
  'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_sninqBPE2bhsTyUkAUgrIju3': 'file_storage/call_sninqBPE2bhsTyUkAUgrIju3.json', 'var_call_4aLLA4dvTVTqrO03GuHfQPOX': 'file_storage/call_4aLLA4dvTVTqrO03GuHfQPOX.json', 'var_call_pPSsbpUTewWWWDqfX0IV3Sko': 'file_storage/call_pPSsbpUTewWWWDqfX0IV3Sko.json'}

exec(code, env_args)
