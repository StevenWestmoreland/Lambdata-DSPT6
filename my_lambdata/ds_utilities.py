import pandas as pd
from sklearn.model_selection import train_test_split


class Splits:
    '''A class containing functions for splitting dataframes'''
    def train_val_test_split(X, y, train_size=0.7, val_size=0.1,
                             test_size=0.2, random_state=None, shuffle=True):
        '''Split a dataframe into train, validation, and test dataframes.

        Keyword arguments:
        X -- dataframe to be split
        y -- target feature
        train_size -- proportion of dataset included in test (default 0.7)
        val_size -- proportion of dataset included in validation (default 0.1)
        test_size -- proportion of dataset included in test (default 0.2)
        random_state -- pass int to reproduce across calls (default None)
        shuffle -- whether or not to shuffle data pre-split (default True)
        '''
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state,
            shuffle=shuffle)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val,
            test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)

        return X_train, X_val, X_test, y_train, y_val, y_test

    def datesplit(X, col):
        '''Split a time based feature into day, month, and year features.

        Keyword arguments:
        X -- dataframe containing the time feature
        col -- time based feature
        '''

        X['year'] = pd.to_datetime(X[col]).dt.year
        X['month'] = pd.to_datetime(X[col]).dt.month
        X['day'] = pd.to_datetime(X[col]).dt.day
        return X