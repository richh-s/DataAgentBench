code = """import json, re, pandas as pd

merged_sample = json.loads(json.dumps(var_call_ma04KuuBrraOxasUTXcW8iP5))
merged_df = pd.DataFrame(merged_sample)

with open(var_call_45B38BXbw6bJjoMFnpkQ1lwU, 'r') as f:
    pkg_records = json.load(f)
with open(var_call_p7T5evAZi7IcTqOiOkPg2ElH, 'r') as f:
    projpkg_records = json.load(f)
with open(var_call_suWOovSUhvOKy7ocr9hDUyjR, 'r') as f:
    projinfo_records = json.load(f)

pkg_df = pd.DataFrame(pkg_records)
projpkg_df = pd.DataFrame(projpkg_records)
projinfo_df = pd.DataFrame(projinfo_records)

vi = pkg_df['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x, str) and x.strip() != '' else {})
vi_df = pd.json_normalize(vi)
vi_df.columns = [f'vi_{c}' for c in vi_df.columns]
full_df = pd.concat([pkg_df, vi_df], axis=1)
full_df = full_df[full_df['System']=='NPM']
full_df['vi_Ordinal'] = pd.to_numeric(full_df.get('vi_Ordinal'), errors='coerce')

is_release = full_df.get('vi_IsRelease')
full_df = full_df[(is_release.isna()) | (is_release == True)]
full_df['ts'] = pd.to_numeric(full_df.get('UpstreamPublishedAt'), errors='coerce')
full_df = full_df.sort_values(['Name','vi_Ordinal','ts','Version'], ascending=[True, False, False, False])
latest_pkg = full_df.groupby('Name', as_index=False).first()[['System','Name','Version']]

projpkg_df = projpkg_df[(projpkg_df['System']=='NPM') & (projpkg_df['ProjectType']=='GITHUB')]
merged = latest_pkg.merge(projpkg_df, on=['System','Name','Version'], how='inner')

pi = projinfo_df[['id','Project_Information']].copy()

repo_pattern = re.compile(r"project ([^\s/]+/[^\s]+)|named ([^\s/]+/[^\s]+)|under the name ([^\s/]+/[^\s]+)", re.IGNORECASE)
stars_pattern = re.compile(r"(\d[\d,]*) stars")

records = []
for _, row in pi.iterrows():
    text = row['Project_Information']
    rid = row['id']
    repo = None
    m = repo_pattern.search(text)
    if m:
        for g in m.groups():
            if g:
                repo = g
                break
    sm = stars_pattern.search(text)
    stars = None
    if sm:
        stars = int(sm.group(1).replace(',', ''))
    if repo is not None and stars is not None:
        records.append({'ProjectName': repo, 'Stars': stars})

stars_df = pd.DataFrame(records).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(stars_df, on='ProjectName', how='inner')

pkg_stars = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = pkg_stars.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_45B38BXbw6bJjoMFnpkQ1lwU': 'file_storage/call_45B38BXbw6bJjoMFnpkQ1lwU.json', 'var_call_YGWF1OGnPM78oG4azGQAkr06': ['project_info', 'project_packageversion'], 'var_call_p7T5evAZi7IcTqOiOkPg2ElH': 'file_storage/call_p7T5evAZi7IcTqOiOkPg2ElH.json', 'var_call_suWOovSUhvOKy7ocr9hDUyjR': 'file_storage/call_suWOovSUhvOKy7ocr9hDUyjR.json', 'var_call_ma04KuuBrraOxasUTXcW8iP5': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectType': 'GITHUB', 'ProjectName': 'discordx-ts/discordx', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectType': 'GITHUB', 'ProjectName': 'discordx-ts/discordx', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectType': 'GITHUB', 'ProjectName': 'discordx-ts/discordx', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectType': 'GITHUB', 'ProjectName': 'discordx-ts/discordx', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '5.2.1', 'ProjectType': 'GITHUB', 'ProjectName': 'discordx-ts/discordx', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '5.2.1', 'ProjectType': 'GITHUB', 'ProjectName': 'discordx-ts/discordx', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discoteam/vueify', 'Version': '9.4.1', 'ProjectType': 'GITHUB', 'ProjectName': 'vuejs/vueify', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discoteam/vueify', 'Version': '9.4.1', 'ProjectType': 'GITHUB', 'ProjectName': 'vuejs/vueify', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discourse/itsatrap', 'Version': '2.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'ccampbell/itsatrap', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discourse/itsatrap', 'Version': '2.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'ccampbell/itsatrap', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'discourse/moment-timezone-names-translations', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'discourse/moment-timezone-names-translations', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/commons-js', 'Version': '0.0.11', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/commons-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/commons-js', 'Version': '0.0.11', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/commons-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/commons-test-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/commons-test-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.384', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/relayrabbit-addons-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.384', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/relayrabbit-addons-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/relayrabbit-commons-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7', 'ProjectType': 'GITHUB', 'ProjectName': 'discoursegroup/relayrabbit-commons-js', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}]}

exec(code, env_args)
