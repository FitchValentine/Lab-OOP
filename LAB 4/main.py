from typing import Callable, Tuple
from time import sleep
from collections import deque
from threading import Thread

# Определение типов
Action = Callable[[], None]
Keymap = dict[str, Tuple[Action, Action]]


class Keyboard:
    def __init__(self):
        # Инициализация словаря для отображения клавиш на действия и истории действий
        self.keymap: Keymap = {}
        self.history = deque()

    def reg_key(self, key: str, action: Action, undo_action: Action = lambda: None):
        # Регистрация клавиши с соответствующими действиями и действиями отмены
        self.keymap[key] = (action, undo_action)

    def press_key(self, key: str):
        # Обработка нажатия клавиши, проверка наличия клавиши в словаре
        assert key in self.keymap, "Нажата неизвестная кнопка"
        # Добавление клавиши в историю и выполнение соответствующего действия
        self.history.append(key)
        self.keymap[key][0]()

    def undo(self):
        # Отмена последнего действия
        if self.history:
            # Получение последней клавиши из истории и выполнение соответствующего действия отмены
            self.keymap[self.history.pop()][1]()


class Workflow:
    def __init__(self, keyboard: Keyboard):
        # Инициализация объекта Workflow с переданным объектом Keyboard
        self.keyboard = keyboard
        self.actions = []

    def press(self, key: str):
        # Метод для имитации нажатия клавиши с задержкой в полсекунды
        self.keyboard.press_key(key)
        sleep(0.5)

    def undo(self):
        # Метод для имитации отмены действия с задержкой в полсекунды
        self.keyboard.undo()
        sleep(0.5)

    def start(self):
        # Метод для запуска последовательности действий Workflow
        for action in self.actions:
            action()


def main():
    # Устанавливаем локаль для корректного отображения русского текста
    # (по аналогии с setlocale(LC_ALL, "Russian") в C++)
    print("Привет!")

    # Создаем объект Keyboard
    keyboard = Keyboard()

    # Регистрируем клавиши с соответствующими действиями
    keyboard.reg_key("A", lambda: print("Нажали A"), lambda: print("Отжали A"))
    keyboard.reg_key("Alt+F4", lambda: print("Закрыли приложение"), lambda: print("Обратно открыли приложение"))

    # Создаем объект Workflow с переданным объектом Keyboard
    workflow = Workflow(keyboard)

    # Добавляем последовательность действий в Workflow
    workflow.actions.extend([
        lambda: workflow.press("A"),
        lambda: workflow.press("Alt+F4"),
        lambda: workflow.undo(),
        lambda: workflow.undo()
    ])

    # Запускаем Workflow
    workflow.start()
    print()

    # Регистрируем новые действия для клавиш
    keyboard.reg_key("A", lambda: print("Нажали B"), lambda: print("Отжали B"))
    keyboard.reg_key("Alt+F4", lambda: print("Теперь это сочетание сдаёт лабораторную"), lambda: print("Больше не сдаёт"))

    # Запускаем Workflow с новыми действиями
    workflow.start()


if __name__ == "__main__":
    main()
