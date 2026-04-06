from setuptools import setup
setup(
    name="ja",
    version="0.7",
    py_modules=["main", "journal", "idle", "log_utils", "config"],
    entry_points={
        "console_scripts": [
            "_ja=main:main"
        ]
    }
)