import numpy as np

class Array3d:
    def __init__(self, dim0, dim1, dim2):
        # Инициализация экземпляра класса с заданными размерами
        self.array = np.zeros((dim0, dim1, dim2), dtype=np.float64)

    def __getitem__(self, indices):
        # Индексатор для доступа к элементам массива по трехмерным координатам
        return self.array[indices]

    def GetValues0(self, i):
        # Возвращает срез массива по первой координате (i, .., ..)
        return self.array[i, :, :]

    def GetValues1(self, j):
        # Возвращает срез массива по второй координате (.., j, ..)
        return self.array[:, j, :]

    def GetValues2(self, k):
        # Возвращает срез массива по третьей координате (.., .., k)
        return self.array[:, :, k]

    def GetValues01(self, i, j):
        # Возвращает срез массива по первой и второй координатам (i, j, ..)
        return self.array[i, j, :]

    def GetValues02(self, i, k):
        # Возвращает срез массива по первой и третьей координатам (i, .., k)
        return self.array[i, :, k]

    def GetValues12(self, j, k):
        # Возвращает срез массива по второй и третьей координатам (.., j, k)
        return self.array[:, j, k]

    def SetValues0(self, i, values):
        # Устанавливает значения в массиве для заданной первой координаты
        self.array[i, :, :] = values

    def SetValues1(self, j, values):
        # Устанавливает значения в массиве для заданной второй координаты
        self.array[:, j, :] = values

    def SetValues2(self, k, values):
        # Устанавливает значения в массиве для заданной третьей координаты
        self.array[:, :, k] = values

    def SetValues01(self, i, j, values):
        # Устанавливает значения в массиве для заданных первой и второй координат
        self.array[i, j, :] = values

    def SetValues02(self, i, k, values):
        # Устанавливает значения в массиве для заданных первой и третьей координат
        self.array[i, :, k] = values

    def SetValues12(self, j, k, values):
        # Устанавливает значения в массиве для заданных второй и третьей координат
        self.array[:, j, k] = values

    @classmethod
    def ones(cls, dim0, dim1, dim2):
        # Метод для создания массива с одинаковыми элементами, заполненными единицами
        instance = cls(dim0, dim1, dim2)
        instance.array = np.ones((dim0, dim1, dim2), dtype=np.float64)
        return instance

    @classmethod
    def zeros(cls, dim0, dim1, dim2):
        # Метод для создания массива с одинаковыми элементами, заполненными нулями
        instance = cls(dim0, dim1, dim2)
        return instance

    @classmethod
    def fill(cls, dim0, dim1, dim2, value):
        # Метод для создания массива с одинаковыми элементами, заполненными заданным значением
        instance = cls(dim0, dim1, dim2)
        instance.array.fill(value)
        return instance

# Пример использования
# Создаем экземпляр класса Array3d
my_array = Array3d(3, 4, 5)

# Используем индексатор для доступа к элементам массива
print(my_array[1, 2, 3])  # Вывод: 0.0

# Используем методы для получения срезов массива
print(my_array.GetValues0(1))
print(my_array.GetValues1(2))
print(my_array.GetValues2(3))
print(my_array.GetValues01(1, 2))
print(my_array.GetValues02(1, 3))
print(my_array.GetValues12(2, 3))

# Используем методы для установки значений в массиве
my_array.SetValues0(1, np.ones((4, 5)))
my_array.SetValues1(2, np.ones((3, 5)))
my_array.SetValues2(3, np.ones((3, 4)))
my_array.SetValues01(1, 2, np.ones(5))
my_array.SetValues02(1, 3, np.ones(4))
my_array.SetValues12(2, 3, np.ones(3))

# Используем методы для создания массива с одинаковыми элементами
ones_array = Array3d.ones(2, 2, 2)
zeros_array = Array3d.zeros(2, 2, 2)
fill_array = Array3d.fill(2, 2, 2, 7.0)

# Выводим полученные массивы
print(ones_array.array)
print(zeros_array.array)
print(fill_array.array)
