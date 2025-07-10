from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

def perform_apriori(transactions):
    all_items = sorted(set(item for t in transactions for item in t))
    df = pd.DataFrame([{item: (item in t) for item in all_items} for t in transactions])
    frequent = apriori(df, min_support=0.2, use_colnames=True)
    rules = association_rules(frequent, metric="lift", min_threshold=1.0)
    return rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].to_dict('records')