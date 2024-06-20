from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Автоматическая установка edge driver'a
driver_path = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=driver_path)

# Открытие Telegram Web
driver.get("https://web.telegram.org/")
print('у вас есть 40 секунд войти в аккаунт')
time.sleep(40)  # Время для входа в аккаунт вручную

# Список пользователей для отслеживания
users = ["ps852","ku6fu","Dartfart","Te_sel","nikitadacuk","dsamedovv"
,"UsnSL","pes0chik","insearchofparadise","fuccb0i","ogserpico","zhas_ab","stylizedname","trnqdelniy","biyacuya"
,"playmix_x","milionerkrutoi","Login0310","empty_insid","dsamedovv","nekitos16","RikaN06","GodSystem_1337","Ksmiha"]  # Замените на ники пользователей

def check_status(user):
    # Поиск пользователя по нику
    search_box = driver.find_element(By.XPATH, "//input[@type='text']")
    search_box.clear()
    search_box.send_keys(user)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # Проверка онлайн-статуса
    try:
        status = driver.find_element(By.XPATH, "//span[@class='user-status']")
        print(f"{user} - {status.text}")
    except:
        print(f"Не удалось определить статус пользователя {user}")

try:
    while True:
        for user in users:
            check_status(user)
            time.sleep(2)  # Небольшая пауза между проверками
        time.sleep(15)  # Интервал между полными циклами проверки
except KeyboardInterrupt:
    print("Программа завершена пользователем")

# Закрытие браузера
driver.quit()
