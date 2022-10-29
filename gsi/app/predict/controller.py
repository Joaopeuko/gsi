from gsi.app.predict.model import InputPredict
from log_manager import log
from parameters import parameters
import pandas as pd
import requests
from nltk.sentiment import SentimentIntensityAnalyzer

import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

headers = {'Authorization': 'token ' + parameters['GITHUB_TOKEN']}


def predictor(input_data: InputPredict) -> dict:
    """
    This function call the prediction
    Args:
        input_data:
            It is the values that needs to ebe predicted

    Returns:
        It returns the prediction

    """
    log.logger.info(f'calling the predictor with variables {input_data}')

    issues_numbers = get_issues_numbers(input_data=input_data)
    issues_comments = get_comments(input_data=input_data, issues_numbers=issues_numbers)

    issues_comments_df = pd.DataFrame(issues_comments)
    predictions = []
    for comment in issues_comments_df['comment'].values:
        prediction = sia.polarity_scores(comment)
        predictions.append(prediction)
        log.logger.info(f'the predictor predict {prediction} for {comment}')

    issues_comments_df['predictions'] = predictions

    return issues_comments_df.to_dict()


def get_issues_numbers(input_data: InputPredict) -> list:
    issues_numbers = []
    for page in range(input_data.pages_amount):
        url = parameters['GITHUB_BASE_API_URL'] + f'repos/{input_data.owner}/{input_data.repo}/issues?page={page}'
        result = requests.get(url, headers=headers)
        issues_numbers += list(pd.DataFrame(result.json())['number'].values)

    return issues_numbers


def get_comments(input_data: InputPredict, issues_numbers: list) -> list:
    issues_comments = []
    for number in issues_numbers:
        url = parameters['GITHUB_BASE_API_URL'] + f'repos/{input_data.owner}/{input_data.repo}/issues/{number}/comments'
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            result_df = pd.DataFrame(result.json())
            if len(result_df) != 0:
                comments = result_df['body'].values
                [issues_comments.append({'issue_number': number, 'comment': comment}) for comment in comments]

    return issues_comments
