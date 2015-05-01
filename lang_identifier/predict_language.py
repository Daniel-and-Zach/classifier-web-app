from .bernoulli_feature_maker import b_add_to_df
from textblob import TextBlob
from collections import Counter, namedtuple
import pandas as pd
import sys
import pickle


languages =["Clojure", "Haskell", "Java", "JavaScript", "Ocaml", "Perl",
        "Php", "Python", "Ruby", "Scala", "Scheme"]

def make_temp_df(text):
    """Creates a basic temporary Dataframe."""
    temp_df = pd.DataFrame({"Text": text})
    temp_df["Textblob"] = temp_df.Text.apply((lambda x: TextBlob(x).words))
    temp_df["Textblob letters"] = temp_df.Text.apply((lambda x: TextBlob(x)))
    b_add_to_df(temp_df)
    return temp_df


def clean_probabilities(probabilities):
    whole_number_probabilities = map(lambda x: x * 100, probabilities.tolist()[0])
    rounded_probabilities = [round(x, 2) for x in whole_number_probabilities]
    return rounded_probabilities


def present_percent(probabilities):
    tuples = list(zip(languages, clean_probabilities(probabilities)))
    sorted_list = sorted(tuples, key=lambda x: x[1], reverse=True)

    return [sorted_list[0:3]]


def make_prediction(test_file):
    text_list = []
    with open(test_file) as test_file:
        text = test_file.read()
        text_list.append(text)
    temp_df = make_temp_df(text_list)
    file = open("language_detector.pkl",'rb')
    classifier = pickle.load(file)
    prediction = classifier.predict(temp_df.loc[0::,'Object':"php"])
    probability = classifier.predict_proba(temp_df.loc[0::,'Object':"php"])
    print("I predict the language is: {}".format(prediction[0]))
    present_percent(probability)


def make_prediction_from_text(text):
    text_list = [text]
    temp_df = make_temp_df(text_list)
    file = open("language_detector.pkl",'rb')
    classifier = pickle.load(file)
    prediction = classifier.predict(temp_df.loc[0::,'Object':"php"])
    probability = classifier.predict_proba(temp_df.loc[0::,'Object':"php"])
    top_three = present_percent(probability)
    return top_three

if __name__ == '__main__':
    text = sys.argv[1]
    make_prediction(text)
