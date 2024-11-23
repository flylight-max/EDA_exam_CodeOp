
try:
    import pandas as pd
except ImportError as e:
    print(f"Error importing pandas: {e}")
    raise
def orig_train_test_df(orig_df,train_df,test_df,col_name):
    """Returns a pandas DataFrame with a column 'Dataset' containing the name of the dataset 
    and a column 'col_name' containing the corresponding values of each dataset of the col_name.
    Args:
        orig_df, train_df, test_df (pandas DataFrame): the DataFrames you want to combine.
        col_name (string): The name of the column you want to combine.
    """
    my_dict = {"Dataset":[], col_name:[]}
    for value in orig_df[col_name]:
        my_dict["Dataset"].append(orig_df.name)
        my_dict[col_name].append(value)
    for value2 in train_df[col_name]:
        my_dict["Dataset"].append(train_df.name)
        my_dict[col_name].append(value2)
    for value3 in test_df[col_name]:
        my_dict["Dataset"].append(test_df.name)
        my_dict[col_name].append(value3)
    col_name_df = pd.DataFrame(my_dict)
    return col_name_df

