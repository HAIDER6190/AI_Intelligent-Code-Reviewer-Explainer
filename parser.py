from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py": "Python",
    ".js": "JavaScript",
    ".java": "Java",
}


def validate_file(file_name: str) -> bool:
    """check whether the file extension is supported or not"""
    extension= Path(file_name).suffix.lower()
    return extension in SUPPORTED_EXTENSIONS


def get_language(file_name: str) -> str:
    """get the programming language of the file"""
    extension= Path(file_name).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file type. please upload a .py, .js, or .java file.")
    return SUPPORTED_EXTENSIONS[extension]


def read_code(file) -> str:
    """read and validate uploaded source code file"""
    if not validate_file(file.name):
        raise ValueError("Unsupported file type. please upload a .py, .js, or .java file.")
    code = file.read().decode("utf-8")

    if not code.strip():
        raise ValueError("the uploaded file is empty. please upload a valid source code file.")

    return code