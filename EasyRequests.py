# -*- coding: utf-8 -*-

import os
import logging
import json
import requests
import traceback
from datetime import datetime

SETTINGS_FILE = "settings.json"
LOGS_DIR = "logs"

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

log_filename = os.path.join(LOGS_DIR, f"easyrequests_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

crash_log_filename = os.path.join(LOGS_DIR, "log.txt")
crash_logger = logging.getLogger("crashLogger")
crash_logger.setLevel(logging.ERROR)
crash_handler = logging.FileHandler(crash_log_filename)
crash_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
crash_logger.addHandler(crash_handler)

LANGUAGES = {
    "en": {
        "welcome": "Welcome to EasyRequests!",
        "enter_url": "Enter URL (e.g., https://example.com):",
        "choose_mode": "Choose mode",
        "choose_language": "Choose language: ",
        "choose_art": "Choose art: ",
        "modes": [
            "1. Send GET request",
            "2. Send POST request",
            "3. Brute force parameters",
            "4. Settings",
            "5. Exit"
        ],
        "invalid_choice": "Invalid choice. Try again.",
        "send_get": "Sending GET request...",
        "status_code": "Status code:",
        "response_body": "Response body:",
        "send_post": "Sending POST request...",
        "enter_post_data": "Enter data for POST request (JSON format):",
        "brute_force": "Starting parameter brute force...",
        "enter_param_name": "Enter parameter name to brute force:",
        "enter_wordlist": "Enter path to wordlist file:",
        "check_url": "Checking:",
        "success": "Success:",
        "try_again": "Do you want to try again? (y/n):",
        "choose_art": "Choose ASCII art:",
        "config_saved": "Settings saved successfully.",
        "load_config": "Loading settings...",
        "settings_file_not_found": "Settings file not found, using defaults.",
        "choose_language": "Choose language:",
        "exited": "Exiting... Goodbye!",
        "restart_alert": "---PLEASE, RESTART EASYREQUESTS TO APPLY LANGUAGE CHANGE---"
    },
    "ru": {
        "welcome": "Добро пожаловать в EasyRequests!",
        "enter_url": "Введите URL (например, https://example.com):",
        "choose_mode": "Выберите режим",
        "choose_art": "Выберите арт: ",
        "modes": [
            "1. Отправить GET-запрос",
            "2. Отправить POST-запрос",
            "3. Перебор параметров",
            "4. Настройки",
            "5. Выход"
        ],
        "invalid_choice": "Неверный выбор. Попробуйте снова.",
        "send_get": "Отправка GET-запроса...",
        "status_code": "Статус код:",
        "response_body": "Тело ответа:",
        "send_post": "Отправка POST-запроса...",
        "enter_post_data": "Введите данные для POST-запроса (в формате JSON):",
        "brute_force": "Начало перебора параметров...",
        "enter_param_name": "Введите имя параметра для перебора:",
        "enter_wordlist": "Введите путь к словарю (wordlist):",
        "check_url": "Проверка:",
        "success": "Успешно:",
        "try_again": "Хотите попробовать снова? (y/n):",
        "choose_art": "Выберите ASCII арт:",
        "config_saved": "Настройки успешно сохранены.",
        "load_config": "Загрузка настроек...",
        "settings_file_not_found": "Файл настроек не найден, используются значения по умолчанию.",
        "choose_language": "Выберите язык:",
        "exited": "Выход из программы... До свидания!",
        "restart_alert": "---ПОЖАЛУЙСТА, ПЕРЕЗАПУСТИТЕ EASYREQUESTS ДЛЯ ПРИМЕНЕНИЯ ИЗМЕНЕНИЙ ЯЗЫКА---"
    },
    "uk": {
        "welcome": "Ласкаво просимо до EasyRequests!",
        "enter_url": "Введіть URL (наприклад, https://example.com):",
        "choose_mode": "Оберіть режим",
        "choose_art": "Виберіть арт: ",
        "modes": [
            "1. Відправити GET-запит",
            "2. Відправити POST-запит",
            "3. Перебір параметрів",
            "4. Налаштування",
            "5. Вихід"
        ],
        "invalid_choice": "Невірний вибір. Спробуйте ще раз.",
        "send_get": "Відправка GET-запиту...",
        "status_code": "Статус код:",
        "response_body": "Тіло відповіді:",
        "send_post": "Відправка POST-запиту...",
        "enter_post_data": "Введіть дані для POST-запиту (у форматі JSON):",
        "brute_force": "Початок перебору параметрів...",
        "enter_param_name": "Введіть ім'я параметра для перебору:",
        "enter_wordlist": "Введіть шлях до файлу словника:",
        "check_url": "Перевірка:",
        "success": "Успіх:",
        "try_again": "Хочете спробувати ще раз? (y/n):",
        "choose_art": "Оберіть ASCII-арт:",
        "config_saved": "Налаштування успішно збережені.",
        "load_config": "Завантаження налаштувань...",
        "settings_file_not_found": "Файл налаштувань не знайдений, використовуються значення за замовчуванням.",
        "choose_language": "Оберіть мову:",
        "exited": "Вихід з програми... До побачення!",
        "restart_alert": "---БУДЬ ЛАСКА, ПЕРЕЗАПУСТІТЬ EASYREQUESTS ДЛЯ ЗМІН МОВИ---"
    },
    "zh": {
        "welcome": "欢迎使用 EasyRequests！",
        "enter_url": "请输入 URL（例如：https://example.com）：",
        "choose_mode": "选择模式",
        "modes": [
            "1. 发送 GET 请求",
            "2. 发送 POST 请求",
            "3. 暴力破解参数",
            "4. 设置",
            "5. 退出"
        ],
        "invalid_choice": "无效的选择，请重试。",
        "send_get": "发送 GET 请求...",
        "status_code": "状态码：",
        "response_body": "响应体：",
        "send_post": "发送 POST 请求...",
        "enter_post_data": "请输入 POST 请求的数据（JSON 格式）：",
        "brute_force": "开始参数暴力破解...",
        "enter_param_name": "请输入要暴力破解的参数名：",
        "enter_wordlist": "请输入字典文件的路径：",
        "check_url": "检查中：",
        "success": "成功：",
        "try_again": "是否重试？（y/n）：",
        "choose_art": "选择 ASCII 艺术：",
        "config_saved": "设置已成功保存。",
        "load_config": "加载设置...",
        "settings_file_not_found": "未找到设置文件，使用默认值。",
        "choose_language": "选择语言：",
        "exited": "退出...再见！",
        "restart_alert": "---请重新启动 EasyRequests 以应用语言更改---"
    },
    "ja": {
        "welcome": "EasyRequestsへようこそ！",
        "enter_url": "URLを入力してください（例：https://example.com）：",
        "choose_mode": "モードを選択してください：",
        "modes": [
            "1. GETリクエストを送信",
            "2. POSTリクエストを送信",
            "3. パラメータブルートフォース",
            "4. 設定",
            "5. 終了"
        ],
        "invalid_choice": "無効な選択です。もう一度お試しください。",
        "send_get": "GETリクエストを送信中...",
        "status_code": "ステータスコード：",
        "response_body": "レスポンスボディ：",
        "send_post": "POSTリクエストを送信中...",
        "enter_post_data": "POSTリクエストのデータを入力してください（JSON形式）：",
        "brute_force": "パラメータのブルートフォースを開始中...",
        "enter_param_name": "ブルートフォースするパラメータ名を入力してください：",
        "enter_wordlist": "ワードリストファイルのパスを入力してください：",
        "check_url": "確認中：",
        "success": "成功：",
        "try_again": "もう一度試しますか？（y/n）：",
        "choose_art": "ASCIIアートを選択してください：",
        "config_saved": "設定が正常に保存されました。",
        "load_config": "設定を読み込み中...",
        "settings_file_not_found": "設定ファイルが見つかりませんでした。デフォルト設定を使用します。",
        "choose_language": "言語を選択してください：",
        "exited": "終了します...さようなら！",
        "restart_alert": "---言語変更を適用するにはEasyRequestsを再起動してください---"
    },
    "fr": {
        "welcome": "Bienvenue dans EasyRequests !",
        "enter_url": "Entrez l'URL (par exemple, https://example.com) :",
        "choose_mode": "Choisissez le mode",
        "modes": [
            "1. Envoyer une requête GET",
            "2. Envoyer une requête POST",
            "3. Force brute des paramètres",
            "4. Paramètres",
            "5. Quitter"
        ],
        "invalid_choice": "Choix invalide. Essayez à nouveau.",
        "send_get": "Envoi de la requête GET...",
        "status_code": "Code de statut :",
        "response_body": "Corps de la réponse :",
        "send_post": "Envoi de la requête POST...",
        "enter_post_data": "Entrez les données pour la requête POST (format JSON) :",
        "brute_force": "Début de la force brute des paramètres...",
        "enter_param_name": "Entrez le nom du paramètre à brute forcer :",
        "enter_wordlist": "Entrez le chemin du fichier de mots :",
        "check_url": "Vérification :",
        "success": "Réussi :",
        "try_again": "Voulez-vous essayer à nouveau ? (y/n) :",
        "choose_art": "Choisissez un art ASCII :",
        "config_saved": "Paramètres enregistrés avec succès.",
        "load_config": "Chargement des paramètres...",
        "settings_file_not_found": "Fichier de paramètres introuvable, utilisation des valeurs par défaut.",
        "choose_language": "Choisissez la langue :",
        "exited": "Sortie... Au revoir !",
        "restart_alert": "---VEUILLEZ REDÉMARRER EASYREQUESTS POUR APPLIQUER LE CHANGEMENT DE LANGUE---"
    },
    "es": {
        "welcome": "¡Bienvenido a EasyRequests!",
        "enter_url": "Ingrese URL (por ejemplo, https://example.com):",
        "choose_mode": "Elige el modo",
        "modes": [
            "1. Enviar solicitud GET",
            "2. Enviar solicitud POST",
            "3. Fuerza bruta de parámetros",
            "4. Configuración",
            "5. Salir"
        ],
        "invalid_choice": "Opción no válida. Inténtalo de nuevo.",
        "send_get": "Enviando solicitud GET...",
        "status_code": "Código de estado:",
        "response_body": "Cuerpo de la respuesta:",
        "send_post": "Enviando solicitud POST...",
        "enter_post_data": "Ingresa los datos para la solicitud POST (formato JSON):",
        "brute_force": "Iniciando fuerza bruta de parámetros...",
        "enter_param_name": "Ingresa el nombre del parámetro para hacer fuerza bruta:",
        "enter_wordlist": "Ingresa la ruta al archivo de lista de palabras:",
        "check_url": "Comprobando:",
        "success": "Éxito:",
        "try_again": "¿Quieres intentar de nuevo? (y/n):",
        "choose_art": "Elige el arte ASCII:",
        "config_saved": "Configuración guardada con éxito.",
        "load_config": "Cargando configuración...",
        "settings_file_not_found": "Archivo de configuración no encontrado, usando valores predeterminados.",
        "choose_language": "Elige el idioma:",
        "exited": "Saliendo... ¡Adiós!",
        "restart_alert": "---POR FAVOR, REINICIE EASYREQUESTS PARA APLICAR EL CAMBIO DE IDIOMA---"
    }
}

ARTS = {
    "classic": r"""
 _____               ______                           _       
|  ___|              | ___ \                         | |      
| |__  __ _ ___ _   _| |_/ /___  __ _ _   _  ___  ___| |_ ___ 
|  __|/ _` / __| | | |    // _ \/ _` | | | |/ _ \/ __| __/ __|
| |__| (_| \__ \ |_| | |\ \  __/ (_| | |_| |  __/\__ \ |_\__ \
\____/\__,_|___/\__, \_| \_\___|\__, |\__,_|\___||___/\__|___/
                 __/ |             | |                        
                |___/              |_|                        
    """,
    "modern": r"""
___________                     __________                                     __          
\_   _____/____    _________.__.\______   \ ____  ________ __   ____   _______/  |_  ______
 |    __)_\__  \  /  ___<   |  | |       _// __ \/ ____/  |  \_/ __ \ /  ___/\   __\/  ___/
 |        \/ __ \_\___ \ \___  | |    |   \  ___< <_|  |  |  /\  ___/ \___ \  |  |  \___ \ 
/_______  (____  /____  >/ ____| |____|_  /\___  >__   |____/  \___  >____  > |__| /____  >
        \/     \/     \/ \/             \/     \/   |__|           \/     \/            \/ 
    """
}

def add_url_prefix(url):
    prefixes = ["https://", "http://", "https://www.", "http://www.", "www."]
    for prefix in prefixes:
        if url.startswith(prefix):
            return url
    return "https://" + url

def save_settings(language, art_choice):
    settings = {
        "language": language,
        "art_choice": art_choice
    }
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file)
    logging.info("Settings saved")
    print(LANGUAGES[language]["config_saved"])

def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
        logging.info("Settings loaded successfully")

        if "art_choice" not in settings:
            settings["art_choice"] = "classic"
            save_settings(settings["language"], settings["art_choice"])

        return settings
    except FileNotFoundError:
        logging.warning("Settings file not found, using defaults.")
        print(LANGUAGES["en"]["settings_file_not_found"])
        return {"language": "en", "art_choice": "classic"}

def show_ascii_art(art_choice):
    print(ARTS[art_choice])

def main():
    settings = load_settings()
    language = settings["language"]
    art_choice = settings["art_choice"]

    print(LANGUAGES[language]["welcome"])
    show_ascii_art(art_choice)

    while True:
        print(LANGUAGES[language]["choose_mode"])
        for mode in LANGUAGES[language]["modes"]:
            print(mode)

        choice = input(f"{LANGUAGES[language]['choose_mode']}: ")

        try:
            if choice == "1":
                url = input(LANGUAGES[language]["enter_url"])
                url = add_url_prefix(url)
                print(LANGUAGES[language]["send_get"])
                response = requests.get(url)
                logging.info(f"GET request sent to {url} with status code {response.status_code}")
                print(LANGUAGES[language]["status_code"], response.status_code)
                print(LANGUAGES[language]["response_body"], response.text)

            elif choice == "2":
                url = input(LANGUAGES[language]["enter_url"])
                url = add_url_prefix(url)
                post_data = input(LANGUAGES[language]["enter_post_data"])
                print(LANGUAGES[language]["send_post"])
                
                try:
                    post_data = json.loads(post_data)
                    response = requests.post(url, data=post_data)
                    logging.info(f"POST request sent to {url} with status code {response.status_code}")
                    print(LANGUAGES[language]["status_code"], response.status_code)
                    print(LANGUAGES[language]["response_body"], response.text)
                except json.JSONDecodeError:
                    print("Invalid JSON format. Please enter valid JSON data.")

            elif choice == "3":
                param_name = input(LANGUAGES[language]["enter_param_name"])
                wordlist_path = input(LANGUAGES[language]["enter_wordlist"])
                print(LANGUAGES[language]["brute_force"])

            elif choice == "4":
                print(LANGUAGES[language]["choose_language"])
                for lang in LANGUAGES.keys():
                    print(f"{lang}")
                new_language = input(LANGUAGES[language]["choose_language"])
                if new_language in LANGUAGES:
                    settings["language"] = new_language
                    print(LANGUAGES[new_language]["restart_alert"])
                else:
                    print(LANGUAGES[language]["invalid_choice"])
                print(LANGUAGES[language]["choose_art"])
                for art in ARTS.keys():
                    print(f"{art}")
                new_art = input(LANGUAGES[language]["choose_art"])
                if new_art in ARTS:
                    settings["art_choice"] = new_art
                    save_settings(new_language, art_choice)
                else:
                    print(LANGUAGES[language]["invalid_choice"])

            elif choice == "5":
                print(LANGUAGES[language]["exited"])
                break

            else:
                print(LANGUAGES[language]["invalid_choice"])

        except Exception as e:
            error_message = f"An error occurred: {e}\n{traceback.format_exc()}"
            crash_logger.error(error_message)
            logging.error(error_message)
            print(f"{LANGUAGES[language]['invalid_choice']} - Error logged.")
            break

if __name__ == "__main__":
    main()
