# Класс Command, представляющий команду
class Command:
    def execute(self):
        pass

    def display(self):
        pass

# Класс для команды "Открыть браузер"
class OpenBrowserCommand(Command):
    def execute(self):
        path_to_browser = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([path_to_browser])

    def display(self):
        return 'Открыть браузер'

# Класс виртуальной клавиатуры
class VirtualKeyboard:
    def __init__(self):
        self.key_mappings = {}
        self.history = []
        self.browser_process = None

    def remap_key(self, key, command):
        self.key_mappings[key] = command

    def press_key(self, key):
        if key in self.key_mappings:
            command = self.key_mappings[key]
            print(f'Выполнено действие: {command.display()}')
            self.history.append(command)
            command.execute()
        else:
            print(f'Нажата клавиша: {key}')

    def undo_last_action(self):
        if self.history:
            undone_command = self.history.pop()
            print(f'Отменено действие: {undone_command.display()}')
            undone_command.execute()
        else:
            print('История пуста, отмена невозможна')

# Функция-обработчик событий нажатия клавиш
def on_key_press(event):
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'ctrl' or event.name == 'z':
            vk.undo_last_action()
    else:
        vk.press_key(event.name)

# Функция для демонстрации работы виртуальной клавиатуры
def demo_workflow(virtual_keyboard):
    open_browser_command = OpenBrowserCommand()
    virtual_keyboard.remap_key('A', open_browser_command)

    print("Нажмите клавишу 'A' для открытия браузера, 'Ctrl+Z' для отмены и 'Esc' для завершения")

    keyboard.hook(on_key_press)
    keyboard.wait('esc')

# Точка входа в программу
if __name__ == "__main__":
    vk = VirtualKeyboard()
    demo_workflow(vk)
