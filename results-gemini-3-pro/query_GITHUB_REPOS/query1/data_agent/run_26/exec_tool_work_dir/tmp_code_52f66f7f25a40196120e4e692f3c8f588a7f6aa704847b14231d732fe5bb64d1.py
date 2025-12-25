code = """import pandas as pd
import json

# Load languages
with open(locals()['var_function-call-8536059397377604475'], 'r') as f:
    languages_data = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for entry in languages_data:
    repo = entry['repo_name']
    desc = entry.get('language_description', '')
    # Check if 'Python' is mentioned. Case sensitive 'Python' is standard for language names.
    if 'Python' not in desc: 
        non_python_repos.add(repo.lower())

# Load README data
with open(locals()['var_function-call-17452844990187727134'], 'r') as f:
    readme_data = json.load(f)

# Filter and count
total_readme_non_python = 0
copyright_readme_non_python = 0

filtered_repos = []

for entry in readme_data:
    repo = entry['sample_repo_name']
    has_copyright = int(entry['has_copyright'])
    
    if repo.lower() in non_python_repos:
        total_readme_non_python += 1
        if has_copyright == 1:
            copyright_readme_non_python += 1
        filtered_repos.append(repo)

proportion = 0.0
if total_readme_non_python > 0:
    proportion = copyright_readme_non_python / total_readme_non_python

print("__RESULT__:")
print(json.dumps({
    "total_non_python_readmes": total_readme_non_python,
    "copyright_non_python_readmes": copyright_readme_non_python,
    "proportion": proportion
}))"""

env_args = {'var_function-call-8536059397377604475': 'file_storage/function-call-8536059397377604475.json', 'var_function-call-11643165055295347855': [], 'var_function-call-3811463403129782095': [{'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/fun1_to_proc_par2.ll', 'mode': '40960', 'id': '316ad972693d0355c3504729fff14287419e004d', 'symlink_target': '../all/fun1_to_proc_par2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'tests/failure/wrong_order_par_seq_middle.t/wrong_order_par_seq_middle.ll', 'mode': '40960', 'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'symlink_target': '../../../fixtures/all/wrong_order_par_seq_middle.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/layout_case.ll', 'mode': '40960', 'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'symlink_target': '../all/layout_case.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/merger_loli_Sort.ll', 'mode': '40960', 'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'symlink_target': '../all/merger_loli_Sort.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/infer_recv.ll', 'mode': '40960', 'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'symlink_target': '../all/infer_recv.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/parallel_assoc_tensor3_flat.ll', 'mode': '40960', 'id': '248004ff4dd7722e31b548a776a3463ab8b52a78', 'symlink_target': '../all/parallel_assoc_tensor3_flat.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-failure/ten_loli_par.ll', 'mode': '40960', 'id': '23bb40fccf644811f011fb80b8f484a825d66543', 'symlink_target': '../all/ten_loli_par.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/compile/my_loli.ll', 'mode': '40960', 'id': '561e0c258b57a3dec9da2a2b6143003ede425013', 'symlink_target': '../all/my_loli.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/dead_lock_tensor2_tensor2.ll', 'mode': '40960', 'id': '053669348398e5f7a34966fb62f93cc6f694e888', 'symlink_target': '../all/dead_lock_tensor2_tensor2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/sequence/par_ten_ten_v1.ll', 'mode': '40960', 'id': '4d284e73f44321e6291601728fd1a6d15e26d2f2', 'symlink_target': '../all/par_ten_ten_v1.ll'}], 'var_function-call-6561753850001512389': [{'repo_name': 'cjdelisle/cjdns', 'ref': 'refs/heads/master', 'path': 'tunnel/README.md', 'mode': '40960', 'id': '004c395f4ef4276e2c207cc35f9bb5c6346ade8a', 'symlink_target': '../doc/tunnel.md'}, {'repo_name': 'poliastro/poliastro', 'ref': 'refs/heads/master', 'path': 'README.rst', 'mode': '40960', 'id': '100b93820ade4c16225673b4ca62bb3ade63c313', 'symlink_target': 'README'}, {'repo_name': 'jgeboski/bitlbee-steam', 'ref': 'refs/heads/master', 'path': 'README.md', 'mode': '40960', 'id': '100b93820ade4c16225673b4ca62bb3ade63c313', 'symlink_target': 'README'}, {'repo_name': 'nodesource/docker-node', 'ref': 'refs/heads/master', 'path': 'centos/7/node/0.10.44/README.md', 'mode': '40960', 'id': 'ff5c79602cf4f4964d15b6230c551f9d260ab007', 'symlink_target': '../../../../README.md'}, {'repo_name': 'nodesource/docker-node', 'ref': 'refs/heads/master', 'path': 'fedora/22/node/6.1.0/README.md', 'mode': '40960', 'id': 'ff5c79602cf4f4964d15b6230c551f9d260ab007', 'symlink_target': '../../../../README.md'}, {'repo_name': 'nodesource/docker-node', 'ref': 'refs/heads/master', 'path': 'debian/sid/node/5.8.0/README.md', 'mode': '40960', 'id': 'ff5c79602cf4f4964d15b6230c551f9d260ab007', 'symlink_target': '../../../../README.md'}, {'repo_name': 'nodesource/docker-node', 'ref': 'refs/heads/master', 'path': 'debian/sid/node/0.10.40/README.md', 'mode': '40960', 'id': 'ff5c79602cf4f4964d15b6230c551f9d260ab007', 'symlink_target': '../../../../README.md'}, {'repo_name': 'NOAA-GFDL/MOM6-examples', 'ref': 'refs/heads/dev/master', 'path': 'ocean_only/global/INPUT/README', 'mode': '40960', 'id': '180c1c4139acead0048afd20f0fb042a57b2babc', 'symlink_target': '.datasets/global/siena_201204/mosaic.unpacked/README'}, {'repo_name': 'gregbanks/python-tabulate', 'ref': 'refs/heads/master', 'path': 'README', 'mode': '40960', 'id': 'facdd59d5107a79c0867333b2a7f0c74c58ef941', 'symlink_target': './README.rst'}, {'repo_name': 'NitruxSA/breeze-icon-theme', 'ref': 'refs/heads/master', 'path': 'Breeze Dark/mimetypes/16/text-x-readme.svg', 'mode': '40960', 'id': 'bafd70e1ac5a6fa22e46b90e313ccc1f06158011', 'symlink_target': 'text-x-texinfo.svg'}], 'var_function-call-7415171602186988141': [], 'var_function-call-5025444654919960895': [{'repo_name': 'waydelyle/openfund', 'has_copyright': '1'}, {'repo_name': 'DaMSL/K3', 'has_copyright': '0'}, {'repo_name': 'rgardler/azure-quickstart-templates', 'has_copyright': '0'}, {'repo_name': 'briancavalier/todomvc-fab', 'has_copyright': '0'}], 'var_function-call-4907108704688075553': [{'content_count': '24286', 'file_count': '524077'}], 'var_function-call-58917866436604708': [{'files_readme_count': '3086', 'contents_readme_count': '204'}], 'var_function-call-12831017483983691300': [{'overlap_count': '417'}], 'var_function-call-17452844990187727134': 'file_storage/function-call-17452844990187727134.json'}

exec(code, env_args)
