def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    uniqe_values = {}
    col_indexes = df.columns
    for i in col_indexes:
        uniqe_values[i] = df[i].unique()
    return uniqe_values
    
