def output_console(text):
    """
    Print text in the console

    Args:
        text (str): Text to print
    """
    print(text)


def write_file_python(filepath, text):
    """
    Write text to the file using built-in python functions

    Args:
        filepath (str): Path to the file
        text (str): Data to write to the file
    """
    with open(filepath, 'a', encoding='UTF-8') as f:
        f.write(text)
        f.write('\n')


def write_file_pandas(filepath, df):
    """
    Write text to the file using pandas functions

    Args:
        filepath (str): Path to the file
        df (DataFrame): DataFrame to write to the file
    """
    df.to_csv(filepath)

