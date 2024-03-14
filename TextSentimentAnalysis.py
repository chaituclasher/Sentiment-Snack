# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import streamlit as st
from textblob import TextBlob
import cleantext

st.set_page_config(page_title="Sentiment Analysis", page_icon=":fish_cake:")
st.header('Sentiment Snack: Bite-Sized Insights into Textual Emotions')

# Clean Text Expander
with st.expander('Clean Text', expanded=False):
    pre = st.text_input('You can clean your text here before feeding: ')
    if pre:
        cleaned_text = cleantext.clean(pre, clean_all=False, extra_spaces=True, stopwords=True)
        st.write(cleaned_text)

# analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# get sentiment emoji
def get_sentiment_emoji(polarity):
    if polarity > 0.5:
        return "😃"
    elif polarity > 0:
        return "🙂"
    elif polarity < -0.5:
        return "😠"
    elif polarity < 0:
        return "😐"
    else:
        return "😐"
def get_subjectivity_label(subjectivity):
    if subjectivity <= 0.3:
        return "Factual"
    elif subjectivity <= 0.6:
        return "Somewhat Opinionated"
    else:
        return "Highly Opinionated"
# Feed Your Text to Analyze Expander
with st.expander('Feed Your Text to Analyze', expanded=False):
    text = st.text_input('Feed here: ')
    if text:
        polarity, subjectivity = analyze_sentiment(text)
        sentiment_emoji = get_sentiment_emoji(polarity)
        st.write(f'Sentiment: {sentiment_emoji}')
        st.write('Polarity: ', round(polarity, 2))
        st.write('Subjectivity: ', round(subjectivity, 2))

        # Progress bar for subjectivity
        st.write('Subjectivity Level:')
        st.progress(subjectivity)
        # Display subjectivity label
        subjectivity_label = get_subjectivity_label(subjectivity)
        st.write(f'{subjectivity_label}')
        # Styling based on polarity
        if polarity > 0:
            st.markdown(f'<p style="color:green;font-size:20px">Positive sentiment detected!</p>', unsafe_allow_html=True)
        elif polarity < 0:
            st.markdown(f'<p style="color:red;font-size:20px">Negative sentiment detected!</p>', unsafe_allow_html=True)

    

