import pandas
from app.io.input import read_file_python, read_file_pandas


class TestReadFilePython:
    def test_read_file_python_exists(self, tmp_path):
        temp_dir = tmp_path / "my_dir"
        temp_dir.mkdir()
        test_file = temp_dir / "file.txt"
        test_file.write_text("Test")

        filepath = test_file.__str__()
        data_py = read_file_python(filepath)

        assert isinstance(data_py, str)

    def test_read_file_python_does_not_exist(self):
        filepath = 'something.txt'
        data_py = read_file_python(filepath)

        assert data_py is None

    def test_read_file_python_correct_text(self, tmp_path):
        content = 'Hello, World!'

        temp_dir = tmp_path / "my_dir"
        temp_dir.mkdir()
        test_file = temp_dir / "file.txt"
        test_file.write_text(content)

        filepath = test_file.__str__()
        data_py = read_file_python(filepath)

        assert data_py == content


class TestReadFilePandas:
    def test_read_file_pandas_exists(self, tmp_path):
        temp_dir = tmp_path / "my_dir"
        temp_dir.mkdir()
        test_file = temp_dir / "file.csv"
        test_file.write_text("Name,Value\nmy_name,my_value")

        filepath = test_file.__str__()
        data_pd = read_file_pandas(filepath)

        assert isinstance(data_pd, pandas.DataFrame)

    def test_read_file_pandas_does_not_exist(self):
        filepath = 'something.csv'
        data_pd = read_file_pandas(filepath)

        assert data_pd is None

    def test_read_file_pandas_correct_text(self, tmp_path):
        content = pandas.DataFrame({"name": ["name1", "name2", "name3"],
                                    "value": [12, 8, 31]})
        temp_dir = tmp_path / "my_dir"
        temp_dir.mkdir()
        test_file = temp_dir / "file.csv"
        content.to_csv(test_file, index=False)

        filepath = test_file.__str__()
        data_pd = read_file_pandas(filepath)

        assert content.equals(data_pd)
