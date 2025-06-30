import duckdb
import pandas as pd
from pymongo import MongoClient
from openai import AzureOpenAI
import json

# === Step 0: Setup Connections ===
con_duck = duckdb.connect("../query_dataset/yelp_user.db")
client_mongo = MongoClient("mongodb://localhost:27017/")
biz_collection = client_mongo["yelp_business"]["business"]

deployment_name = "gpt-4o-mini"
deployment_name_large = "gpt-4o"
client = AzureOpenAI(
    api_key="609ced4d971240b8a08f7fb0e6d846ea",
    api_version="2024-08-01-preview",
    azure_endpoint="https://promptdelta-nc.openai.azure.com"
)


# === Step 1: Load user and review data ===
df_user = con_duck.execute("SELECT * FROM user").fetchdf()
df_review = con_duck.execute("SELECT * FROM review").fetchdf()

# === Step 2: Use GPT to find users registered in 2016 ===
def is_registered_in_2016(yelping_since):
    prompt = (
        "Determine whether the following date indicates the user registered in the year 2016.\n"
        "Only respond with 'yes' or 'no'.\n\n"
        f"Registration time: {yelping_since}"
    )
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You check if the user registered in 2016."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=5
        )
        return response.choices[0].message.content.strip().lower().startswith("yes")
    except:
        return False

user_mask = []
for i, row in df_user.iterrows():
    time_str = row["yelping_since"]
    if pd.isna(time_str):
        user_mask.append(False)
        continue
    result = is_registered_in_2016(time_str)
    print({i}, {time_str}, {result})
    user_mask.append(result)

df_user_2016 = df_user[user_mask].copy()
user_ids_2016 = df_user_2016["user_id"].tolist()
user_since_map = df_user_2016.set_index("user_id")["yelping_since"].to_dict()

# === Step 3: Filter reviews by those users, then GPT judge review is after registration ===
df_review_2016_users = df_review[df_review["user_id"].isin(user_ids_2016)].copy()

def is_after_registration_gpt(reg_time, review_time):
    prompt = (
        "Determine whether the review occurred strictly *after* the user's registration.\n"
        "Only respond with 'yes' or 'no'.\n\n"
        f"User registered on: {reg_time}\n"
        f"Review timestamp: {review_time}"
    )
    try:
        response = client.chat.completions.create(
            model=deployment_name_large,
            messages=[
                {"role": "system", "content": "You compare two timestamps to see if the review came after registration."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=5
        )
        return response.choices[0].message.content.strip().lower().startswith("yes")
    except:
        return False

valid_reviews = []
for i, row in df_review_2016_users.iterrows():
    user_id = row["user_id"]
    review_time = row["date"]
    reg_time = user_since_map.get(user_id)

    if not reg_time or pd.isna(review_time):
        print(f"[{i}] ⚠️ Missing timestamp(s): reg_time = {reg_time}, review_time = {review_time} → ❌ filtered")
        continue

    result = is_after_registration_gpt(reg_time, review_time)

    if result:
        valid_reviews.append(row)
        print(f"[{i}] ✅ kept | reg_time = {reg_time}, review_time = {review_time}")
    else:
        print(f"[{i}] ❌ filtered | reg_time = {reg_time}, review_time = {review_time} → review is not after registration")
      

df_reviews_from_2016_users = pd.DataFrame(valid_reviews)

# === Step 4: Map business_ref to business_id ===
business_refs = df_reviews_from_2016_users["business_ref"].dropna().unique().tolist()
business_docs = list(biz_collection.find({}, {"business_id": 1, "description": 1}))
business_ids = [b["business_id"] for b in business_docs if "business_id" in b]

# === Step 5: GPT infer mapping rule ===
def get_mapping_rule(business_ids, business_refs):
    prompt = (
        "You are given two complete ID columns from two different datasets:\n"
        f"- The first column is `business_ref` from a review dataset: {json.dumps(business_refs, indent=2)}\n"
        f"- The second column is `business_id` from a business metadata dataset: {json.dumps(business_ids, indent=2)}\n\n"
        "Each business_ref corresponds to a business_id, but the mapping rule is not provided.\n"
        "Determine the mapping relationship between the two sets of IDs.\n"
        "Please respond with:\n"
        "1. The exact mapping rule in plain English\n"
        "2. An explanation of why you think this rule holds."
    )
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a data engineer analyzing ID columns from different datasets to infer a mapping rule."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

mapping_rule_explanation = get_mapping_rule(business_ids, business_refs)
print("\n🧠 GPT-inferred mapping rule:\n", mapping_rule_explanation)

# === Step 6: Resolve business_ref → business_id ===
def resolve_ref_to_id(business_ref):
    prompt = (
        f"The inferred mapping rule is:\n\n{mapping_rule_explanation}\n\n"
        f"Now determine the business_id for:\n"
        f"- business_ref: {business_ref}\n\n"
        "Only respond with the business_id (e.g., 'biz_001')."
    )
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a data assistant mapping business_ref to business_id."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=20
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ GPT error on {business_ref}: {e}")
        return None

ref_to_id_map = {}
predicted_business_ids = []

for i, row in df_reviews_from_2016_users.iterrows():
    business_ref = row["business_ref"]
    if pd.isna(business_ref):
        predicted_business_ids.append(None)
        continue

    if business_ref not in ref_to_id_map:
        ref_to_id_map[business_ref] = resolve_ref_to_id(business_ref)

    business_id = ref_to_id_map[business_ref]
    predicted_business_ids.append(business_id)
    print(f"[{i}] business_ref = {business_ref} → business_id = {business_id}")

df_reviews_from_2016_users = df_reviews_from_2016_users.copy()
df_reviews_from_2016_users["business_id"] = predicted_business_ids

# === Step 7: Extract name + category from description ===
def extract_categories(description):
    prompt = (
        "Given the following business description, extract **all category terms that are explicitly mentioned in the text**.\n"
        "Only include categories that appear **verbatim** (word-for-word) in the description.\n"
        "If multiple categories are present, return a **comma-separated list** (e.g., \"Nail Salon, Spa\").\n"
        "Do **not** guess or generalize; do **not** include any explanation.\n\n"
        f"Description: {description}"
    )
    try:
        res = client.chat.completions.create(
            model=deployment_name_large,
            messages=[
                {"role": "system", "content": "You extract business categories."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=30
        )
        return res.choices[0].message.content.strip()
    except:
        return "Unknown"

biz_id_to_desc = {b["business_id"]: b.get("description", "") for b in business_docs}
category_records = []


for biz_id in df_reviews_from_2016_users["business_id"].dropna().unique():
    desc = biz_id_to_desc.get(biz_id, "")
    if not desc:
        continue
    cats = extract_categories(desc)
    for cat in [c.strip() for c in cats.split(",") if c.strip()]:
        category_records.append({"business_id": biz_id, "category": cat})
    print(f"[{biz_id}] {cats} \n↳ Desc: {desc}\n")
df_category_map = pd.DataFrame(category_records)

# === Step 8: Merge category info with review counts ===
df_review_counts = df_reviews_from_2016_users.groupby("business_id").size().reset_index(name="review_count")
df_merge = df_category_map.merge(df_review_counts, on="business_id", how="inner")
df_top = df_merge.groupby("category")["review_count"].sum().reset_index()
df_top = df_top.sort_values(by="review_count", ascending=False).head(5)

# === Step 9: Output ===
print("\n Top 5 Categories (2016 users):")
print(df_top)