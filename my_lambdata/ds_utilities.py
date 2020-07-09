import pandas as pd
from sklearn.model_selection import train_test_split

def enlarge(n): 
    ''' This function will multiply the input by 100 '''
    return n * 100

if __name__ == '__main__':
    y = int(input("Choose a number: "))
    print(y, enlarge(y))
    
def split(X, splitn, valn):
    ''' This function will take dataframe X and perform a train/test split by the
    value of splitn. It will then split the train into train and validation by the 
    value of valn. Both splitn and valn must be between 0 and 1. '''
    
    train_no_val, test = train_test_split(X, train_size=splitn, test_size=1-splitn, random_state=42)
    train, val = train_test_split(train_no_val, train_size=valn, test_size=1-valn, random_state=42)

    return train.shape, val.shape, test.shape

def datesplit(X, col, drop):
    ''' For dataframe X, input a date feature col to create three new features for
    the dataframe: day, month, and year. Also allows for dropping of original feature '''

    X['year'] = pd.to_datetime(X[col]).dt.year
    X['month'] = pd.to_datetime(X[col]).dt.month
    X['day'] = pd.to_datetime(X[col]).dt.day

    return X