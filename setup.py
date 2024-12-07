from cx_Freeze import setup, Executable

includes = ["queue"]

setup(
    name="EasyRequests",
    version="0.1",
    description="Easy python requests",
    options={
        "build_exe": {
            "packages": ["requests", "json"],
            "includes": includes,
        }
    },
    executables=[Executable("EasyRequests.py")]
)
