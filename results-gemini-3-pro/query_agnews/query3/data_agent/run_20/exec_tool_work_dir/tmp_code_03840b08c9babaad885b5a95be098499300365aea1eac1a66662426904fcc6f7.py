code = """import json
import pandas as pd
import re

# Paths
meta_path = locals()['var_function-call-11963313759828392180']
content_path = locals()['var_function-call-6584692014692107885']

# Load data
with open(meta_path, 'r') as f:
    meta_data = json.load(f)
    
# meta_data is a dict with "ids" list or a list of dicts?
# Previous output: {"count": 14860, "ids": [3, 9, ...]} 
# Wait, the metadata file I saved in step 2 (from var...180) was from the python script that outputted a dict.
# Actually, the ORIGINAL query result (var...833) was a list of dicts `[{"article_id": "3", ...}, ...]`.
# I should use the original query result file because it has the dates!
# The filtered IDs file `var...180` only has IDs. I need dates to group by year.

meta_path_original = locals()['var_function-call-7712258569316983833']
with open(meta_path_original, 'r') as f:
    meta_records = json.load(f)

# Load content
with open(content_path, 'r') as f:
    content_records = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(meta_records)
df_content = pd.DataFrame(content_records)

# Convert article_id to string to ensure matching (content has strings "0", meta has "3" or 3)
# In the meta preview, IDs were "3". In the content preview, IDs were "0".
# Let's clean and merge.
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_content['article_id'] = df_content['article_id'].astype(str)

# Merge
# Inner join to keep only relevant articles
df = pd.merge(df_meta, df_content, on='article_id', how='inner')

# Extract Year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Filter years 2010-2020 (just to be safe)
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Define keywords
keywords = {
    'Business': [
        "business", "economy", "economic", "market", "stock", "wall street", "bond", "finance", "financial", 
        "bank", "banking", "invest", "investment", "investor", "profit", "earnings", "revenue", "loss", 
        "trade", "trading", "share", "dividend", "dollar", "euro", "yen", "currency", "forex", "tax", 
        "debt", "deficit", "budget", "inflation", "recession", "gdp", "growth", "job", "unemployment", 
        "employment", "hire", "firing", "labor", "strike", "union", "company", "firm", "corporation", 
        "corp", "inc", "ltd", "ceo", "cfo", "executive", "manager", "management", "sale", "retail", 
        "consumer", "spending", "store", "shop", "price", "cost", "deal", "merger", "acquisition", 
        "buyout", "bid", "ipo", "regulator", "antitrust", "fed", "federal reserve", "central bank", 
        "rate", "interest", "loan", "mortgage", "credit", "audit", "fraud", "accounting", "energy", 
        "oil", "gas", "petrol", "crude", "barrel", "gold", "silver", "metal", "mining", "airline", 
        "airbus", "boeing", "auto", "car", "vehicle", "manufacturer", "factory", "production", 
        "output", "supply", "demand", "imf", "wto", "world bank", "ecb", "opec"
    ],
    'Sports': [
        "sport", "game", "match", "play", "player", "team", "coach", "manager", "club", "league", 
        "cup", "championship", "champion", "tournament", "olympic", "medal", "win", "won", "lose", 
        "lost", "score", "goal", "point", "run", "race", "driver", "athlete", "football", "soccer", 
        "basketball", "baseball", "tennis", "golf", "cricket", "rugby", "hockey", "f1", "formula 1", 
        "boxing", "wrestling", "stadium", "season", "final", "semi-final", "quarter-final", "round"
    ],
    'SciTech': [
        "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", 
        "online", "net", "digital", "data", "cyber", "virus", "hacker", "security", "phone", 
        "mobile", "cell", "wireless", "broadband", "satellite", "space", "nasa", "shuttle", 
        "rocket", "orbit", "planet", "star", "galaxy", "astronomy", "telescope", "physics", 
        "chemistry", "biology", "gene", "genetic", "dna", "stem cell", "clone", "drug", "medicine", 
        "medical", "health", "disease", "cancer", "aids", "hiv", "flu", "research", "study", 
        "experiment", "lab", "scientist", "researcher", "discover", "invention", "innovation", 
        "robot", "ai", "artificial intelligence", "engine", "motor", "google", "microsoft", 
        "apple", "intel", "ibm", "facebook", "twitter", "amazon", "ebay", "yahoo", "browser", 
        "server", "chip", "processor"
    ],
    'World': [
        "world", "international", "politic", "government", "parliament", "congress", "senate", 
        "law", "legal", "court", "judge", "trial", "prison", "police", "crime", "arrest", "kill", 
        "death", "die", "dead", "murder", "bomb", "blast", "attack", "terror", "terrorist", 
        "al qaeda", "war", "army", "military", "soldier", "troop", "weapon", "nuclear", "missile", 
        "peace", "treaty", "negotiation", "diplomat", "diplomacy", "ambassador", "embassy", 
        "president", "prime minister", "minister", "chancellor", "premier", "king", "queen", 
        "prince", "leader", "official", "election", "vote", "poll", "campaign", "candidate", 
        "party", "democrat", "republican", "conservative", "liberal", "socialist", "communist", 
        "protest", "demonstration", "riot", "crisis", "disaster", "quake", "flood", "storm", 
        "hurricane", "typhoon", "fire", "accident", "crash", "plane", "train", "bus", "ship", 
        "boat", "ferry", "refugee", "immigrant", "border", "un", "united nations", "eu", 
        "european union", "nato", "iraq", "iran", "afghanistan", "palestine", "israel", "syria", 
        "russia", "china", "korea"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            # Simple substring match? Or word boundary?
            # Substring might match "companies" for "pan".
            # Better to tokenize or check boundaries.
            # For simplicity, count occurrences of kw in text.
            scores[cat] += text.count(kw)
            
    # Return category with max score
    # If tie, prioritize Business (as we want to count it) or random?
    # Or maybe if all 0, default to something?
    # Let's say default to World if all 0.
    
    max_score = -1
    best_cat = 'World' 
    
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            # Tie breaking
            pass
            
    return best_cat

# Combine title and description
df['text'] = df['title'].fillna('') + " " + df['description'].fillna('')

# Apply classification
df['category'] = df['text'].apply(classify)

# Filter for Business
df_biz = df[df['category'] == 'Business']

# Group by year and count
counts = df_biz.groupby('year').size()

# Ensure all years 2010-2020 are present
all_years = pd.Series(0, index=range(2010, 2021))
counts = counts.add(all_years, fill_value=0)

# Calculate average
avg = counts.mean()

print("__RESULT__:")
print(json.dumps({
    "counts_per_year": counts.to_dict(),
    "average": avg,
    "total_articles": len(df),
    "biz_articles": len(df_biz)
}))"""

env_args = {'var_function-call-7712258569316983833': 'file_storage/function-call-7712258569316983833.json', 'var_function-call-11963313759828392180': 'file_storage/function-call-11963313759828392180.json', 'var_function-call-17209390838595579310': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14274068418124532630': 5, 'var_function-call-6584692014692107885': 'file_storage/function-call-6584692014692107885.json'}

exec(code, env_args)
