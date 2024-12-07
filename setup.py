from cx_Freeze import setup, Executable

setup(
    name="EasyRequests",
    version="0.1",
    description="Easy python requests",
    executables=[Executable("EasyRequests.py")]
)