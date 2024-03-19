import copy


class PythonCodeFile:
    def __init__(self, license_content, file_extension, code='', file_name=''):
        self._license_content = license_content
        self._file_extension = file_extension
        self._code = code
        self._file_name = file_name

    @property
    def licence_content(self):
        return self._license_content

    @licence_content.setter
    def licence_content(self, value):
        self._license_content = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def file_extension(self):
        return self._file_extension

    @file_extension.setter
    def file_extension(self, value):
        self._file_extension = value

    def create_clone(self):
        return copy.copy(self)

    def __str__(self):
        return (f"File: {self._file_name}.{self._file_extension}, "
                f"license='{self._license_content}', code='{self._code}'")


class PythonCodeFilesManager:
    _base_file = PythonCodeFile("SDA", "py")

    @staticmethod
    def create_file_with_content(file_name, code):
        base_file_clone = PythonCodeFilesManager._base_file.create_clone()
        base_file_clone.file_name = file_name
        base_file_clone.code = code
        return base_file_clone


def main():
    file_1 = PythonCodeFilesManager.create_file_with_content("project_one", "import sys")
    file_2 = PythonCodeFilesManager.create_file_with_content("project_two", "print('Hello World')")

    print(file_1)
    print(file_2)


if __name__ == "__main__":
    main()
