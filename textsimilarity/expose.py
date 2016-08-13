from textsimilarity.core import TextSimilarity

def textsimilarity_compare(text1, text2):
    return TextSimilarity().compare(text1, text2)

def compare():
    return [textsimilarity_compare, str, str, float] 
