code = """import json, pandas as pd, re

# load non-python repos list
path_nonpy = var_call_XgokpvBWT5lp2j0W7qe6Khep
with open(path_nonpy, 'r', encoding='utf-8') as f:
    nonpy = json.load(f)
nonpy_set = set(r['repo_name'] for r in nonpy)

df_readme = pd.DataFrame(var_call_IrUdzOPIuBtyPBMWv4Vpw5R2)
mask = df_readme['repo_name'].isin(nonpy_set)
df_np_readme = df_readme.loc[mask].copy()

def has_copyright(text):
    if text is None:
        return False
    t = str(text)
    tl = t.lower()
    # Copyright indicators
    if 'copyright' in tl or 'all rights reserved' in tl:
        return True
    if '©' in t:
        return True
    if re.search(r'\(c\)', tl):
        return True
    return False

repo_any = df_np_readme.groupby('repo_name')['content'].apply(lambda s: any(has_copyright(x) for x in s))
with_readme = int(repo_any.shape[0])
with_c = int(repo_any.sum())
prop = (with_c / with_readme) if with_readme else None

res = {
    "non_python_repos": int(var_call_DcpvPnLulzSGq2TIvmBgTQay[0]['non_python_repos']),
    "non_python_repos_with_readme_md": with_readme,
    "non_python_repos_with_readme_md_and_copyright": with_c,
    "proportion": prop
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_XgokpvBWT5lp2j0W7qe6Khep': 'file_storage/call_XgokpvBWT5lp2j0W7qe6Khep.json', 'var_call_jGbqH7RQR3mBNaTe2GV7D2hw': [], 'var_call_DcpvPnLulzSGq2TIvmBgTQay': [{'non_python_repos': '2774729'}], 'var_call_FWE0kQVJj1n1rBITKF2qi986': {'non_python_repos': 2774729, 'non_python_repos_with_readme_md': 0, 'non_python_repos_with_readme_md_and_copyright': 0, 'proportion': None}, 'var_call_IrUdzOPIuBtyPBMWv4Vpw5R2': [{'repo_name': 'waydelyle/openfund', 'content': "CKEditor 4\n==========\n\nCopyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.\nhttp://ckeditor.com - See LICENSE.md for license information.\n\nCKEditor is a text editor to be used inside web pages. It's not a replacement\nfor desktop text editors like Word or OpenOffice, but a component to be used as\npart of web applications and websites.\n\n## Documentation\n\nThe full editor documentation is available online at the following address:\nhttp://docs.ckeditor.com\n\n## Installation\n\nInstalling CKEditor is an easy task. Just follow these simple steps:\n\n 1. **Download** the latest version from the CKEditor website:\n    http://ckeditor.com. You should have already completed this step, but be\n    sure you have the very latest version.\n 2. **Extract** (decompress) the downloaded file into the root of your website.\n\n**Note:** CKEditor is by default installed in the `ckeditor` folder. You can\nplace the files in whichever you want though.\n\n## Checking Your Installation\n\nThe editor comes with a few sample pages that can be used to verify that\ninstallation proceeded properly. Take a look at the `samples` directory.\n\nTo test your installation, just call the following page at your website:\n\n\thttp://<your site>/<CKEditor installation path>/samples/index.html\n\nFor example:\n\n\thttp://www.example.com/ckeditor/samples/index.html\n"}, {'repo_name': 'DaMSL/K3', 'content': 'K3 Dockerfiles\n==========\n\nDockerfiles are updated for three images:\n\n1. **k3-app** -- (~250MB) light-weight image to run a K3 program. Based on debian:jessie. It contains only the necessary dependency libraries.\n2. **k3-compiler** -- (~2 GB) Image containing the GHC and GCC tool chains to compile a K3 program to binary. Based on debian:jessie\n3. **k3-dev** (~2.5 GB)  -- Larger container with additional library and application support (e.g. clang, ruby, vim, and others). It is based on debian:sid\n\nTo build an image use the following command:\n\n```\ndocker build -f k3-dev -t damsl/k3-dev:<your_tag> .\n```\n\n(Note: Docker build now has the -f option, so you don\'t have to call all docker files, "Dockerfile")\n\nThe image ```damsl/k3-dev:vanilla``` which is pushed to the repo contains the K3 source built with no options. Feel free to pull, use, & re-build K3 with whatever options necessary (and re-push with a new tag if needed).\n\nThe other scripts in here are left for legacy purposes.\n\nBuild Dependency Versions:\n<pre>\n  - GHC: 7.10.1\n  - GCC: 4.9.2\n  - Boost: 1.57\n  - Mesos: 0.22.1</pre>\n'}, {'repo_name': 'briancavalier/todomvc-fab', 'content': "curl.js loader plugins\n===\n\nPlease see the wiki for information about using plugins.  If you're interested\nin creating your own plugins, please check out the Plugin Author's Guide\non the wiki (TBD).\n\nAll of these plugins conform to the AMD specification.  However, that\ndoesn't necessarily mean that they'll work with other AMD loaders or\nbuilders.  Until the build-time API of AMD is finalized, there will be\nincompatibilities.\n\nModules that should work with any loader/builder:\n\nasync!\ndomReady!\njs!\nlink!\n\nTODO:\n\njson! (auto-detects xdomain and uses JSON-P)\n"}, {'repo_name': 'rgardler/azure-quickstart-templates', 'content': '# Emercoin Instance\n\nThis Microsoft Azure template deploys a single Emercoin client which will connect to the public Emercoin network.\n\n[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Femercoin-ubuntu%2Fazuredeploy.json)\n<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Femercoin-ubuntu%2Fazuredeploy.json" target="_blank">\n    <img src="http://armviz.io/visualizebutton.png"/>\n</a>\n\nOnce your deployment is complete you will be able to connect to the Emercoin public network.\n\n![Emercoin-Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/emercoin-ubuntu/images/emercoin.png)\n\n# Template Parameters\nWhen you launch the installation of the VM, you need to specify the following parameters:\n* `vmDnsPrefix`: this is the public DNS name for the VM that you will use interact with your console. You just need to specify an unique name.\n* `adminUsername`: self-explanatory. This is the account you will use for connecting to the node\n* `adminPassword`: self-explanatory. Be aware that Azure requires passwords to have One upper case, one lower case, a special character, and a number\n* `vmSize`: The type of VM that you want to use for the node. The default size is D1_v2 but you can change that if you expect to run workloads that require more RAM or CPU resources.\n\n# Emercoin Deployment Walkthrough\n1. Get your node\'s IP\n 1. browse to https://portal.azure.com\n\n 2. then click browse all, followed by "resource groups", and choose your resource group\n\n 3. then expand your resources, and public ip address of your node.\n\n2. Connect to your node\n 1. SSH to the public ip of your node as the user you specified for `adminUsername`, enter your `adminPassword`\n 2. Try to use the cli-client by `emc help` or `emc getinfo`\n 3. Point your browser to the public ip of your node, sign in with `adminUsername` and `adminPassword` specified before (note that browser may show you a warning of bad certificate - it\'s OK, you may replace the self-signed certificates by yours at /etc/ssl/emc/emcweb*)\n'}]}

exec(code, env_args)
