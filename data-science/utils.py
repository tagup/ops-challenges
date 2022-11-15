"""Module that contains utility functions  """
import numpy as np
import pandas as pd
from scipy import signal
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def denoise_data(data:pd.DataFrame, window=10)->pd.DataFrame:

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


def spectrogram_data(data:pd.DataFrame, nperseg=64)->pd.DataFrame:
    
    spectra = []

    for sensor in data.columns:
        
        f, t, Sxx = signal.spectrogram(data[sensor], nperseg=nperseg)

        index = pd.Series(t.astype(int), name="time")
        columns = pd.MultiIndex.from_tuples([(sensor, x) for x in f], names=["sensor", "frequency"])

        spectra.append(pd.DataFrame(Sxx.T, index=index, columns=columns))

    return pd.concat(spectra, axis=1)

def pca_spectrogram(spec_data:pd.DataFrame, n_components=4)->pd.DataFrame:

    pca_data = []

    index = spec_data.index

    for sensor in spec_data.columns.unique(0):

        scaler = StandardScaler()
        X = scaler.fit_transform(spec_data[sensor].values)

        pca = PCA(n_components=n_components)
        columns = pd.MultiIndex.from_tuples([(sensor, i) for i in range(n_components)], names=["sensor", "freq component"])
        pca_data.append(pd.DataFrame(pca.fit_transform(X), index=index, columns=columns))
    
    return pd.concat(pca_data, axis=1)