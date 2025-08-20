import pandas as pd
import os

base_path = "../ground_truth_dataset"

# Load CSV files
df_languages = pd.read_csv(os.path.join(base_path, "LANGUAGES.csv"))
df_licenses = pd.read_csv(os.path.join(base_path, "LICENSES.csv"))
df_commits = pd.read_csv(os.path.join(base_path, "SAMPLE_COMMITS.csv"))

print("Step 0: Raw counts")
print("  LANGUAGES:", len(df_languages))
print("  LICENSES:", len(df_licenses))
print("  SAMPLE_COMMITS:", len(df_commits))

# Step 1: Find repos that mention "Shell" (case-insensitive)
repos_with_shell = df_languages[
    df_languages["language"].str.contains("shell", case=False, na=False)
]["repo_name"].unique()
print("Step 1: repos_with_shell:", len(repos_with_shell))

# Step 2: Find repos with apache-2.0 license
repos_with_apache = df_licenses[
    df_licenses["license"].str.lower() == "apache-2.0"
]["repo_name"].unique()
print("Step 2: repos_with_apache:", len(repos_with_apache))

# Step 3: Intersection of repos (Shell + Apache-2.0)
valid_repos = set(repos_with_shell).intersection(set(repos_with_apache))
print("Step 3: valid_repos (Shell + Apache-2.0):", len(valid_repos))

# Step 4: Filter commit messages
df_filtered_commits = df_commits[df_commits["repo_name"].isin(valid_repos)].copy()

df_filtered_commits = df_filtered_commits[
    df_filtered_commits["message"].notna() &
    (df_filtered_commits["message"].str.len() < 1000) &
    (~df_filtered_commits["message"].str.lower().str.startswith("merge")) &
    (~df_filtered_commits["message"].str.lower().str.startswith("update")) &
    (~df_filtered_commits["message"].str.lower().str.startswith("test"))
]

print("Step 4: filtered commits:", len(df_filtered_commits))

# Step 5: Count commit messages
num_messages = len(df_filtered_commits)
print("Step 5: num_messages =", num_messages)

# Step 6: Save ground truth
result = pd.DataFrame([{"num_messages": num_messages}])
output_path = "ground_truth.csv"
result.to_csv(output_path, index=False)
print(f"✅ Saved result to {output_path}")
