code = """import json
from collections import Counter

# Load metadata
with open(locals()['var_function-call-6478820518397450019'], 'r') as f:
    metadata_list = json.load(f)

article_region = {str(item['article_id']): item['region'] for item in metadata_list}

# Load articles
with open(locals()['var_function-call-8772719174433401329'], 'r') as f:
    articles_list = json.load(f)

# Define keywords (expanded/adjusted for substring match)
categories = {
    "World": [
        "president", "minister", "prime", "official", "police", "military", "security", "war", "iraq", "israel", 
        "palestin", "iran", "nuclear", "government", "elect", "party", "vote", "leader", "talk", "peace", 
        "treaty", "un", "united nations", "bomb", "attack", "kill", "blast", "troop", "force", "rebel", "strike", 
        "crash", "disaster", "storm", "hurricane", "china", "russia", "north korea", "syria", "afghan", 
        "pakistan", "baghdad", "gaza", "cairo", "moscow", "beijing", "parliament", "senate", "law", "court", "trial",
        "judge", "protest", "demonstrat", "riot", "crisis", "conflict", "diploma", "embassy", "foreign", "internation"
    ],
    "Sports": [
        "sport", "game", "match", "team", "win", "lose", "victory", "defeat", "score", "cup", "league", "season", 
        "champion", "title", "medal", "olympic", "football", "soccer", "basketball", "baseball", "tennis", "golf", 
        "hockey", "coach", "player", "athlete", "club", "stadium", "point", "record", "final", "round", "tournament", 
        "racing", "driver", "f1", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", "open", "series"
    ],
    "Business": [
        "business", "company", "market", "stock", "share", "price", "profit", "loss", "earn", "bank", "economy", 
        "trade", "dollar", "euro", "yen", "oil", "gas", "energy", "corp", "inc", "ltd", "merger", "acquisition", 
        "deal", "sale", "buy", "sell", "invest", "fund", "rate", "inflation", "fed", "federal reserve", "wall st", 
        "nasdaq", "dow", "ceo", "cfo", "budget", "finance", "revenue", "analyst", "forecast", "growth", "sector"
    ],
    "Sci/Tech": [
        "technology", "science", "computer", "software", "hardware", "internet", "web", "online", "net", "google", 
        "microsoft", "apple", "intel", "ibm", "virus", "worm", "hacker", "security", "space", "nasa", "orbit", 
        "mars", "moon", "launch", "satellite", "phone", "mobile", "wireless", "network", "chip", "processor", 
        "server", "game", "video", "digital", "research", "study", "cancer", "disease", "drug", "health", "hospital", 
        "doctor", "patient", "treatment", "biotech", "genetic", "physic", "astronom", "lab", "experiment"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # Handle ties or zero
    if sum(scores.values()) == 0:
        return "Unknown"
    
    # Prioritize if multiple max? For now just take one.
    # Note: "security" is in World and Tech. "game" in Sports and Tech.
    # Maybe adjust weights later if needed.
    return max(scores, key=scores.get)

world_counts = Counter()
debug_samples = []

count_processed = 0
for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_region:
        count_processed += 1
        content = (article.get('title', '') + " " + article.get('description', ''))
        cat = classify(content)
        
        if cat == "World":
            region = article_region[aid]
            world_counts[region] += 1
            if len(debug_samples) < 3:
                debug_samples.append({"title": article.get('title'), "cat": cat})
        elif len(debug_samples) < 6:
             # Add non-world samples too for verification
             debug_samples.append({"title": article.get('title'), "cat": cat})

print("__RESULT__:")
print(json.dumps({"counts": world_counts, "processed": count_processed, "samples": debug_samples}))"""

env_args = {'var_function-call-9850316120653619328': ['authors', 'article_metadata'], 'var_function-call-9850316120653621663': ['articles'], 'var_function-call-6478820518397450019': 'file_storage/function-call-6478820518397450019.json', 'var_function-call-83190611252947939': 6696, 'var_function-call-1618363836141742396': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8772719174433401329': 'file_storage/function-call-8772719174433401329.json', 'var_function-call-17003818754982913757': {}, 'var_function-call-1547361439319782937': {'metadata_count': 6696, 'articles_count': 20000, 'intersection_count': 998, 'sample_intersection': ['4438', '4665', '5171', '19580', '4568']}, 'var_function-call-17350298307668685415': [{'id': '987', 'title': 'Sprint Broadens Its Vision (NewsFactor)', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '10539', 'title': 'Ahold Reports Weaker Second Quarter Profit (AP)', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '6691', 'title': 'Newbery Wins Platform Diving Gold for Australia', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '1996', 'title': 'Williamson Gets Third Opinion on Elbow (AP)', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '8473', 'title': 'RCN looks to exit Chapter 11', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '12601', 'title': 'California sues Microsoft for antitrust--again', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '2707', 'title': 'Google, Set for Offering, Cuts Share Price by About a Quarter', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '18078', 'title': 'Cowboys Name Romo No. 2 QB, Woodson Out (AP)', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '17097', 'title': 'Woodgate backing for Robson', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}, {'id': '18690', 'title': 'Iraq Injury Count Rose', 'scores': {'World': 0, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}}]}

exec(code, env_args)
