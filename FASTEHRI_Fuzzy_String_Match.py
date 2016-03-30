import csv
from fuzzywuzzy import fuzz

# This script take two csv files: 1. ehri-terms.csv and 2. fast-keywords.csv.
# creates a new csv file with fuzzy matching keywords.
# For this task the fuzzywuzzy module was used.
# tried two functions:
# The token_* functions split the string on white-spaces,
# lowercase everything and get rid of non-alpha non-numeric characters,
# which means punctuation is ignored (as well as weird unicode symbols)

__author__ = 'yael'

# open the csv file, and create a dictionary (id, term) for ehri-terms
with open("ehri-terms.csv", mode='r') as ehri_terms:
   ehri_terms_dic = dict(filter(None, csv.reader(ehri_terms)))

# open the csv file, and create a dictionary (id, term) for fast subjects
with open("fast-keywords.csv", mode='r') as fast_terms:
    fast_terms_dic = dict(filter(None, csv.reader(fast_terms)))

# open a new csv file for saving the results
with open("FAST_EHRI_term_match_results.csv", 'wb') as stringMatchResult:
    # create a writer
    testWriter = csv.writer(stringMatchResult)
    # write column headers
    testWriter.writerow(['id1', 'term1', 'id2', 'term2', 'ratio', 'method'])

    while len(fast_terms_dic) > 0:
        # pop and unpack 1 tuple
        fast_term = fast_terms_dic.popitem()
        (fast_term_key, fast_term_value) = fast_term

        # string similarity using token set ratio:
        for ehri_term_key, ehri_term_value in ehri_terms_dic.items():
            similarity_token_set_Ratio = fuzz.token_set_ratio(fast_term_value, ehri_term_value)
            if similarity_token_set_Ratio > 95:
                testWriter.writerow([ehri_term_key, ehri_term_value,
                                     fast_term_key, fast_term_value,
                                     similarity_token_set_Ratio, 'token_set_ratio'])

        # string similarity using token sort ratio:
        for ehri_term_key, ehri_term_value in ehri_terms_dic.items():
            similarity_token_sort_Ratio = fuzz.token_sort_ratio(fast_term_value, ehri_term_value)
            if similarity_token_sort_Ratio > 95:
                testWriter.writerow([ehri_term_key, ehri_term_value,
                                     fast_term_key, fast_term_value,
                                     similarity_token_set_Ratio, 'token_sort_ratio'])
