code = """import json
import re

# Load metadata
path_metadata = locals()['var_function-call-9274223039112968493']
with open(path_metadata, 'r') as f:
    metadata_list = json.load(f)

# Load articles
path_articles = locals()['var_function-call-3749929263555121429']
with open(path_articles, 'r') as f:
    articles_list = json.load(f)

# Create lookup
articles_dict = {str(a['article_id']): a for a in articles_list}

# Expanded keywords
countries = [
    "afghanistan", "albania", "algeria", "andorra", "angola", "antigua", "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "bosnia", "botswana", "brazil", "brunei", "bulgaria", "burkina", "burundi", "cambodia", "cameroon", "canada", "cape verde", "central african republic", "chad", "chile", "china", "colombia", "comoros", "congo", "costa rica", "croatia", "cuba", "cyprus", "czech", "denmark", "djibouti", "dominica", "dominican", "timor", "ecuador", "egypt", "salvador", "guinea", "eritrea", "estonia", "ethiopia", "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "ivory coast", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "korea", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "macedonia", "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall", "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "zealand", "nicaragua", "niger", "nigeria", "norway", "oman", "pakistan", "palau", "panama", "papua", "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "samoa", "marino", "tome", "saudi arabia", "senegal", "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon", "somalia", "south africa", "spain", "sri lanka", "sudan", "suriname", "swaziland", "sweden", "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "togo", "tonga", "trinidad", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "uae", "united kingdom", "uk", "uruguay", "uzbekistan", "vanuatu", "vatican", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"
]

world_keywords = countries + [
    "un", "nato", "eu", "european union", "united nations", "security council",
    "military", "army", "navy", "air force", "troops", "soldiers", "war", "conflict", "battle", "fighting", "clash", "attack", "bomb", "blast", "explosion", "terror", "terrorist", "terrorism", "isis", "isil", "qaeda", "taliban", "boko haram", "hamas", "hezbollah", "insurgent", "rebel", "militia", "guerrilla",
    "government", "president", "prime minister", "minister", "chancellor", "leader", "official", "diplomat", "ambassador", "embassy", "consulate", "foreign", "international", "global", "politics", "political", "election", "vote", "poll", "campaign", "party", "parliament", "congress", "senate", "law", "legislation", "policy", "treaty", "agreement", "deal", "sanctions", "peace", "ceasefire", "truce", "negotiation", "talks", "summit", "conference", "meeting",
    "protest", "demonstration", "rally", "riot", "strike", "activist", "opposition", "dissident", "rights", "human rights", "refugee", "migrant", "immigration", "border", "security", "police", "arrest", "jail", "prison", "court", "trial", "judge", "verdict", "sentence", "execution",
    "disaster", "earthquake", "tsunami", "flood", "storm", "hurricane", "typhoon", "cyclone", "fire", "wildfire", "drought", "famine", "disease", "epidemic", "outbreak", "virus", "ebola", "zika", "flu", "health",
    "crash", "accident", "incident", "death", "kill", "injured", "wound", "victim", "hostage", "kidnap", "abduction"
]

# Reuse other categories from previous code (shortened here for brevity but assuming same logic)
# I will just define them again to be safe.
sports_keywords = ["sport", "game", "match", "cup", "league", "team", "player", "coach", "score", "win", "loss", "olympic", "championship", "tournament", "football", "soccer", "basketball", "baseball", "tennis", "golf", "cricket", "rugby", "hockey", "f1", "racing", "athlete", "medal"]
business_keywords = ["business", "company", "firm", "market", "stock", "share", "price", "profit", "loss", "revenue", "earnings", "economy", "economic", "bank", "finance", "investment", "investor", "trade", "deal", "merger", "acquisition", "dollar", "euro", "currency", "oil", "gas", "energy", "industry", "corp", "inc", "ltd"]
scitech_keywords = ["science", "technology", "tech", "computer", "software", "internet", "web", "app", "mobile", "phone", "digital", "data", "cyber", "space", "nasa", "planet", "star", "galaxy", "study", "research", "scientist", "engineer", "robot", "ai", "google", "apple", "microsoft", "facebook", "amazon", "ibm"]

keywords = {
    "World": world_keywords,
    "Sports": sports_keywords,
    "Business": business_keywords,
    "Science/Technology": scitech_keywords
}

count_world_by_region = {}
article_counts = {}

for m in metadata_list:
    aid = str(m['article_id'])
    region = m['region']
    
    if aid in articles_dict:
        article = articles_dict[aid]
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        # Scoring
        scores = {cat: 0 for cat in keywords}
        words = re.findall(r'\w+', text)
        for word in words:
            for cat, kws in keywords.items():
                if word in kws:
                    scores[cat] += 1
        
        # Tie breaking: World vs Business?
        # If "oil" appears, it scores Business=1, World=0 (unless World has "oil"?)
        # "Oil" is usually Business, but "Oil" + "Iraq" is World?
        # My simple keyword counter might misclassify overlapping terms.
        # But max score is a standard baseline.
        
        if max(scores.values()) > 0:
            category = max(scores, key=scores.get)
        else:
            category = "World" # Default to World if unknown? Or ignore?
            # Safe to ignore or put in a separate bin.
            # But the question assumes classification is possible.
            # If I force "World" for 0 matches, I might inflate it.
            # Let's verify how many 0 matches there are.
            category = None

        if category == "World":
            count_world_by_region[region] = count_world_by_region.get(region, 0) + 1

# Result
if count_world_by_region:
    max_region = max(count_world_by_region, key=count_world_by_region.get)
    max_count = count_world_by_region[max_region]
else:
    max_region = "None"
    max_count = 0

print("__RESULT__:")
print(json.dumps({"max_region": max_region, "count": max_count, "counts": count_world_by_region}))"""

env_args = {'var_function-call-9274223039112968493': 'file_storage/function-call-9274223039112968493.json', 'var_function-call-15083373018326784174': 6696, 'var_function-call-478178951130007102': [{'_id': '6945278305b34f86ed629297', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6945278305b34f86ed629298', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6945278305b34f86ed629299', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6945278305b34f86ed62929a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6945278305b34f86ed62929b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3749929263555121429': 'file_storage/function-call-3749929263555121429.json', 'var_function-call-15162736852437039042': {'max_region': 'Africa', 'count': 107, 'counts': {'South America': 94, 'Africa': 107, 'Asia': 92, 'North America': 90, 'Europe': 73}}}

exec(code, env_args)
