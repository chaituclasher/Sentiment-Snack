# Sentiment Analysis 




[![Explore Sentiment Snack](https://img.shields.io/badge/Explore%20Sentiment%20Snack-Try%20Now-9cf?style=for-the-badge&logo=streamlit&logoColor=white)](https://sentiment-snack.streamlit.app/)





<img src=".devcontainer/sentiments.png" alt="Sentiment Analysis" length="2000" width="2000"/>

## Overview

This Streamlit application, titled "Sentiment Snack: Bite-Sized Insights into Textual Emotions," allows users to analyze the sentiment and subjectivity of text inputs.

## Features

- **Clean Text Expander**: Users can clean their text inputs before analysis by removing extra spaces and stopwords.
- **Feed Your Text to Analyze Expander**: Users can input text to analyze its sentiment and subjectivity.
  - Displays sentiment emoji (😃 for very positive, 🙂 for positive, 😐 for neutral, and 😠 for negative).
  - Provides polarity and subjectivity scores.
  - Visualizes subjectivity level with a progress bar.
  - Labels subjectivity level as "Factual," "Somewhat Opinionated," or "Highly Opinionated."
  - Provides color-coded feedback based on sentiment (green for positive, red for negative).
  
## Instructions

1. **Clean Text Expander**: 
   - Enter text in the input box and click the button to clean the text.
   - Cleaned text will be displayed below the input box.

2. **Feed Your Text to Analyze Expander**:
   - Enter text in the input box and click enter to analyze the sentiment.
   - Sentiment emoji, polarity, subjectivity, and subjectivity level will be displayed.
   - Progress bar indicates the subjectivity level visually.
   - Feedback on sentiment is provided in color-coded text.

## Dependencies

- Streamlit
- TextBlob
- cleantext

## Usage

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app with `streamlit run app.py`.
4. Open the URL provided in the terminal to access the application.
5. Use the provided expanders to clean text and analyze sentiment.

## Try it Out!

Give it a try by visiting the [Sentiment Snack](https://sentiment-snack.streamlit.app/)!
