import pandas as pd
def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    data_dic = {'Feature Name': df.columns,'Data Type': list(df.dtypes) ,'Has Missing Values?': df.isnull().any(), 'Number of Unique Values': [df[col].nunique() for col in df.columns]}
    df_data  = pd.DataFrame(data = data_dic) 
    return df_data
