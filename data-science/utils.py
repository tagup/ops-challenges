"""Module that contains utility functions  """
import pandas as pd
import numpy as np

def denoise_data(data:pd.DataFrame, window=10)->pd.DataFrame:
    """_summary_

    Args:
        data (pd.DataFrame): Input timeseries for a single machine
        window (int): Moving average window

    Returns:
        pd.DataFrame: Data with noise removed
    """

    data = data.copy()

    for sensor in data.columns:
        # get histogram, cdf, and "derivative"
        y = data[sensor]
        counts, bins = np.histogram(abs(y), bins=50)
        cdf = np.cumsum(counts)/len(data)
        diff = cdf[1:]-cdf[:-1]
        ind = np.argmax(diff)
        cutoff = ((bins[:-1]+bins[1:])/2)[ind-1]

        # replace outlier values with nan
        cond = (abs(y) > cutoff)
        y[cond] = np.nan

        #interpolate missing values and take rolling average
        data[sensor] = y.interpolate().rolling(window=window, min_periods=1).mean()

    return data
    