"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main
    """
    data = import_data()
    data = rename_columns(data)

    
def import_data() -> pd.DataFrame:
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data

def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Doc
    """
    data_renamed = data.rename(columns={"sepal.length": 'sepal_length',
                                "sepal.width": 'sepal_width',
                                "petal.length": 'petal_length',
                                "petal.width": 'petal_width'})
    
    return data_renamed


def sample_data(data: pd.DataFrame, n: int = 50) -> pd.DataFrame:

    return data.sample(n)
    
def multiply_data(data: pd.DataFrame) -> pd.DataFrame:

    return pd.concat([data] * 3, ignore_index=True)


if __name__ == '__main__':
    """
    Doc
    """
    main()
