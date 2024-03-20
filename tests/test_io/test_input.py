from app.io.input import read_file_python


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
