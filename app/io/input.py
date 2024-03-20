import os
import pandas as pd


def input_console():
    """
    This function gets the user input from the console

    Returns:
        str: User input from the console
    """
    return input("Your input data: ")


def read_file_python(filepath):
    """
    This function reads data from a file using built-in python functions

    Args:
        filepath (str): Path to the file

    Returns:
        str: Data from the file. Returns None if the file does not exist.
    """
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='UTF-8') as f:
            return f.read()
    return None


def read_file_pandas(filepath):
    """
    This function reads data from a file using pandas functions

    Args:
        filepath (str): Path to the file

    Returns:
        DataFrame: Data from the file. Returns None if the file does not exist.
    """
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    return None
