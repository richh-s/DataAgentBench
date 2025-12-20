code = """import json
import collections
import re
import os

# Load metadata
meta_var = locals()['var_function-call-2966547176505599547']
if isinstance(meta_var, str) and os.path.exists(meta_var):
    with open(meta_var, 'r') as f:
        metadata_list = json.load(f)
else:
    metadata_list = meta_var

id_to_region = {str(item['article_id']): item['region'] for item in metadata_list}

# Load articles batch 2
articles_var = locals()['var_function-call-7887833992064613079']
if isinstance(articles_var, str) and os.path.exists(articles_var):
    with open(articles_var, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = articles_var

# Keywords
keywords = {
    'Business': [
        "oil", "prices", "price", "stocks", "stock", "market", "economy", "investors", "investor", "profit", "earnings", "sales", "deal", "merger", "acquisition", "shares", "share", "bank", "corp", "company", "airline", "boeing", "airbus", "dollar", "euro", "yen", "gold", "bid", "costs", "cost", "growth", "rate", "fed", "greenspan", "inflation", "trade", "budget", "deficit", "imf", "wto", "ipo", "ceo", "cfo", "executive", "employment", "job", "jobs", "wall street", "nasdaq", "dow", "s&p", "business", "financial", "finance"
    ],
    'Sci/Tech': [
        "technology", "tech", "computer", "internet", "software", "web", "online", "search", "google", "yahoo", "microsoft", "intel", "linux", "virus", "worm", "hacker", "security", "patch", "browser", "phone", "mobile", "wireless", "cell", "camera", "digital", "space", "nasa", "orbit", "moon", "mars", "satellite", "launch", "stem cell", "research", "study", "scientist", "drug", "cancer", "medical", "health", "aids", "hiv", "gene", "dna", "cloning", "physics", "science", "ipod", "apple", "ibm", "server", "network", "broadband"
    ],
    'Sports': [
        "game", "match", "win", "loss", "score", "team", "season", "league", "cup", "championship", "champion", "tournament", "olympics", "olympic", "medal", "gold", "silver", "bronze", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "rugby", "cricket", "f1", "racing", "driver", "athlete", "player", "coach", "manager", "club", "united", "real madrid", "arsenal", "chelsea", "liverpool", "manchester", "milan", "juventus", "barcelona", "bayern", "nfl", "nba", "mlb", "nhl", "red sox", "yankees", "lakers", "pistons", "patriots", "eagles", "fifa", "uefa", "wta", "atp", "tour", "sport", "sports"
    ],
    'World': [
        "president", "minister", "prime minister", "premier", "secretary", "official", "government", "parliament", "congress", "senate", "democrat", "republican", "election", "vote", "poll", "campaign", "party", "leader", "chief", "king", "prince", "queen", "pope", "un", "united nations", "eu", "european union", "nato", "war", "peace", "truce", "ceasefire", "treaty", "talks", "negotiation", "summit", "meeting", "visit", "relations", "diplomat", "ambassador", "embassy", "border", "military", "troops", "army", "navy", "air force", "soldiers", "police", "security", "forces", "rebel", "insurgent", "guerrilla", "militant", "terrorist", "al qaeda", "bin laden", "attack", "bomb", "blast", "explosion", "suicide", "kill", "dead", "die", "injure", "wound", "hostage", "kidnap", "arrest", "jail", "prison", "court", "trial", "judge", "law", "ruling", "ban", "protest", "demonstration", "riot", "strike", "disaster", "storm", "hurricane", "typhoon", "cyclone", "flood", "earthquake", "quake", "tsunami", "fire", "crash", "accident", "plane", "train", "ship", "ferry", "iraq", "baghdad", "afghanistan", "kabul", "pakistan", "india", "kashmir", "sri lanka", "nepal", "china", "beijing", "japan", "tokyo", "korea", "seoul", "pyongyang", "indonesia", "jakarta", "philippines", "manila", "thailand", "bangkok", "vietnam", "burma", "myanmar", "malaysia", "singapore", "australia", "new zealand", "iran", "tehran", "syria", "damascus", "lebanon", "beirut", "israel", "jerusalem", "palestinian", "gaza", "west bank", "hamas", "hezbollah", "arafat", "sharon", "abbas", "egypt", "cairo", "libya", "sudan", "darfur", "africa", "nigeria", "congo", "zimbabwe", "south africa", "russia", "moscow", "chechnya", "putin", "ukraine", "kiev", "georgia", "turkey", "ankara", "cyprus", "greece", "athens", "italy", "rome", "vatican", "spain", "madrid", "france", "paris", "germany", "berlin", "uk", "britain", "london", "blair", "ireland", "canada", "toronto", "ottawa", "mexico", "venezuela", "chavez", "brazil", "argentina", "colombia", "peru", "chile", "haiti", "cuba", "castro", "world", "international"
    ]
}

def classify(text):
    text = text.lower()
    counts = {cat: 0 for cat in keywords}
    tokens = re.findall(r'\w+', text)
    for cat, keys in keywords.items():
        for k in keys:
            if ' ' in k:
                if k in text:
                    counts[cat] += text.count(k)
            else:
                counts[cat] += tokens.count(k)
    best_cat = max(counts, key=counts.get)
    if counts[best_cat] == 0: return None
    return best_cat

# Initialize with previous counts
world_counts = collections.defaultdict(int, {
    "Africa": 78, "Asia": 58, "North America": 68, "Europe": 54, "South America": 72
})
last_id = 19999

for article in articles_list:
    aid = str(article['article_id'])
    try:
        aid_int = int(aid)
        if aid_int > last_id:
            last_id = aid_int
    except:
        pass

    if aid in id_to_region:
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = title + " " + desc
        if classify(full_text) == 'World':
            region = id_to_region[aid]
            world_counts[region] += 1

print("__RESULT__:")
print(json.dumps({
    "counts": world_counts,
    "last_id": last_id
}))"""

env_args = {'var_function-call-2966547176505599547': 'file_storage/function-call-2966547176505599547.json', 'var_function-call-17218163166465404922': {'count': 6696, 'sample_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_function-call-1597702634935355858': [{'_id': '694503fa506371ba165c4cdf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694503fa506371ba165c4ce0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694503fa506371ba165c4ce1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694503fa506371ba165c4ce2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694503fa506371ba165c4ce3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-327116729614798104': {'world_counts': {}, 'total_articles_fetched': 5, 'articles_matched_2015': 0, 'unclassified': 0}, 'var_function-call-1315168482124239170': 'file_storage/function-call-1315168482124239170.json', 'var_function-call-11095760226154555113': {'total_meta_ids': 6696, 'max_meta_id': 127570, 'fetched_count': 20000, 'missing_count': 5698, 'sample_missing': ['101726', '60498', '61408', '38579', '114118', '86186', '24727', '108338', '103830', '48457']}, 'var_function-call-5070811610805299418': [{'_id': '694503fa506371ba165c4cec', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-2238988167583568944': 'file_storage/function-call-2238988167583568944.json', 'var_function-call-4853828059629029643': 'file_storage/function-call-4853828059629029643.json', 'var_function-call-14971409533336851086': {'counts': {'Africa': 78, 'Asia': 58, 'North America': 68, 'Europe': 54, 'South America': 72}, 'last_id': 19999}, 'var_function-call-7887833992064613079': 'file_storage/function-call-7887833992064613079.json'}

exec(code, env_args)
