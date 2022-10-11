from TikTokApi import TikTokApi
from helpers import process_results
import pandas as pd
import sys

def get_data(hashtag):
    trending = []
    with TikTokApi() as api:
        tag = api.hashtag(name=hashtag)
        for video in tag.videos():
            trending.append(video.as_dict)

    flattened_data = process_results(trending)

    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

if __name__ == '__main__':
    # get_data('playfest2022')
    get_data(sys.argv[1])

