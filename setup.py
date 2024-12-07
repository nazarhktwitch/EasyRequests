from cx_Freeze import setup, Executable

includes = ["queue"]
packages = ["requests", "json"]

setup(
    name="EasyRequests",
    version="0.1",
    description="Easy Python requests",
    options={
        "build_exe": {
            "packages": packages,
            "includes": includes,
            "include_files": include_files,
        }
    },
    executables=[Executable("EasyRequests.py", base=None)]
)
