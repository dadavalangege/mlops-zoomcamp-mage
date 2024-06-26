from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
import pandas as pd

from mlops.homework.utils.data_preparation.cleaning import clean

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(
    df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    This function recieves the dataframe of nyc green taxi rides then splits it into three dataframes.

    Args:
        df: The initial pandas data frame to load
        kwargs: 'split_on_feature' = The feature to split on
                'split_on_feature_value' = The feature value to split on
                'target' = The feature to use as the model target

    Returns:
        Tuple of Three dataframes
        df1 = a cleaned full dataframe
        df2 = a dataframe for training
        df3 = a dataframe for validation
    """

    df = clean(df)
    df = combine_features(df)
    df = select_features(df,features=[split_on_feature, target])

    df_train, df_val = split_on_value(df,
        split_on_feature,
        split_on_feature_value,
        )

    return df, df_train, df_val