This is a Python application that supports multiple languages and includes various modes such as sending GET and POST requests, brute force attacks, and more. The application also allows users to choose between different ASCII art styles and languages.

## Features

- Multi-language support: English, Russian, Ukrainian, Chinese, Japanese, French, and Spanish (Request for more).
- ASCII Art: Classic, Modern, and Retro styles.
- Modes for sending GET/POST requests and brute-force operations.
- Simple and interactive menu system.

## Installation

You can download latest release or compile itself (Reccomended).

Compiling into exe:

Using setup.py:

    1. Run (If you don't have cx_freeze):
    
    pip install cx_freeze

    2. Run in a project folder:
    
    python setup.py build

    3. After done go to build/[folder-name, example: exe.win-amd64-3.12] and you can start program

Using PyInstaller:

    1. Run (If you don't have PyInstaller):

    pip install pyinstaller

    2. Run in a project folder:

    pyinstaller --onefile --clean --strip --exclude-module test --exclude-module unused_module --name "EasyRequests" EasyRequests.py

    Or use your custom command

    3. Go to dist folder and run EasyRequests.exe

Using Py2Exe:

    Not avaible rn because of my python version incompatibility (>3.10)

Nuitka:

    I can't compile it with nuitka (Infinite loading)

    
1. Clone the repository (Or download source code):
    
   git clone https://github.com/nazarhktwitch/EasyRequests

   cd EasyRequests

3. Install the required Python packages:

   pip install -r requirements.txt

## Usage

To run the application, simply execute the Python script:

python EasyRequests.py

### Choosing Your Preferences

- **Language**: Select your preferred language when prompted (English, Russian, Ukrainian, etc.).
- **ASCII Art**: Choose the style of ASCII art you prefer (Classic, Modern, Retro).
- **Modes**: Choose between different modes, including GET/POST request sending or brute force operations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to fork the repository, make improvements, and create a pull request. Contributions are welcome!

## Contact

For more information or inquiries, feel free to contact me at nazarburlan3@outlook.com.
