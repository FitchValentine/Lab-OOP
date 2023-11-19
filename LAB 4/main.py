# Импорт необходимых модулей
import subprocess
import keyboard
import time

# Класс VirtualKeyboard, представляющий виртуальную клавиатуру
class VirtualKeyboard:
    def __init__(self):
        # Словарь для отображения клавиш на действия
        self.key_mappings = {}
        # История выполненных действий
        self.history = []
        # Процесс браузера (для открытия и закрытия)
        self.browser_process = None

    # Метод для переназначения клавиши на определенное действие
    def remap_key(self, key, action):
        self.key_mappings[key] = action

    # Метод для обработки нажатия клавиши
    def press_key(self, key):
        # Проверка, есть ли клавиша в отображении
        if key in self.key_mappings:
            action = self.key_mappings[key]
            print(f'Выполнено действие: {action}')
            self.history.append(action)
            # Если действие - открыть браузер, вызываем соответствующий метод
            if action == 'Открыть браузер':
                self.open_browser()
                time.sleep(1)  # Задержка в 1 секунду после открытия браузера
        else:
            print(f'Нажата клавиша: {key}')

    # Метод для открытия браузера
    def open_browser(self):
        path_to_browser = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.browser_process = subprocess.Popen([path_to_browser])

    # Метод для закрытия браузера
    def close_browser(self):
        if self.browser_process and self.browser_process.poll() is None:
            self.browser_process.terminate()
            self.browser_process = None
            print('Браузер закрыт')

    # Метод для отмены последнего выполненного действия
    def undo_last_action(self):
        if self.history:
            undone_action = self.history.pop()
            print(f'Отменено действие: {undone_action}')
            # Если отмененное действие - открыть браузер, выводим сообщение и закрываем браузер
            if undone_action == 'Открыть браузер':
                print('Действие отменено')
                self.close_browser()
        else:
            print('История пуста, отмена невозможна')

# Функция-обработчик событий нажатия клавиш
def on_key_press(event):
    # Проверка, что событие - нажатие клавиши
    if event.event_type == keyboard.KEY_DOWN:
        # Проверка, что нажаты клавиши ctrl или z
        if event.name == 'ctrl' or event.name == 'z':
            vk.undo_last_action()
    else:
        # Если это не нажатие клавиши, вызываем метод press_key с именем клавиши
        vk.press_key(event.name)

# Функция для демонстрации работы виртуальной клавиатуры
def demo_workflow(virtual_keyboard):
    virtual_keyboard.remap_key('A', 'Открыть браузер')

    print("Нажмите клавишу 'A' для открытия браузера, 'Ctrl+Z' для отмены и 'Esc' для завершения")

    # Устанавливаем хук для обработки событий клавиш
    keyboard.hook(on_key_press)
    # Ожидаем нажатия клавиши 'Esc' для завершения программы
    keyboard.wait('esc')

# Точка входа в программу
if __name__ == "__main__":
    # Создаем объект виртуальной клавиатуры
    vk = VirtualKeyboard()
    # Запускаем демонстрацию работы виртуальной клавиатуры
    demo_workflow(vk)
