"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main
    """
    pass


if __name__ == '__main__':
    """
    Doc
    """
    main()

def import_data():

    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data
