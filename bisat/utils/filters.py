import os
from os import listdir
from os.path import isfile, join, splitext, isdir
from scipy.signal import butter, lfilter, filtfilt
import numpy as np
from sklearn import preprocessing

def butter_bandpass_filter(data, lowcut, highcut, fs, order=9):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    b, a = butter(order, [low, high], btype='bandpass',analog=False)
    y = lfilter(b, a, data)
    return y

def Normalization(X):
    X_max, X_min = X.max(), X.min()
    X = (X-X_min)/(X_max-X_min)
    return X