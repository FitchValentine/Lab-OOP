class Array3d:
    def __init__(self, dim0, dim1, dim2):
        # Инициализация экземпляра класса с заданными размерами
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        # Изменение создания массива без использования NumPy
        self.array = [[[0.0 for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]

    def __getitem__(self, indices):
        # Индексатор для доступа к элементам массива по трехмерным координатам
        i, j, k = indices
        return self.array[i][j][k]

    def GetValues0(self, i):
        # Возвращает срез массива по первой координате (i, .., ..)
        return [self.array[i][j][:] for j in range(self.dim1)]

    def GetValues1(self, j):
        # Возвращает срез массива по второй координате (.., j, ..)
        return [self.array[i][j][:] for i in range(self.dim0)]

    def GetValues2(self, k):
        # Возвращает срез массива по третьей координате (.., .., k)
        return [[self.array[i][j][k] for j in range(self.dim1)] for i in range(self.dim0)]

    def GetValues01(self, i, j):
        # Возвращает срез массива по первой и второй координатам (i, j, ..)
        return self.array[i][j][:]

    def GetValues02(self, i, k):
        # Возвращает срез массива по первой и третьей координатам (i, .., k)
        return [self.array[i][j][k] for j in range(self.dim1)]

    def GetValues12(self, j, k):
        # Возвращает срез массива по второй и третьей координатам (.., j, k)
        return [self.array[i][j][k] for i in range(self.dim0)]

    def SetValues0(self, i, values):
        # Устанавливает значения в массиве для заданной первой координаты
        for j in range(self.dim1):
            for k in range(self.dim2):
                self.array[i][j][k] = values[j][k]

    def SetValues1(self, j, values):
        # Устанавливает значения в массиве для заданной второй координаты
        for i in range(self.dim0):
            for k in range(self.dim2):
                self.array[i][j][k] = values[i][k]

    def SetValues2(self, k, values):
        # Устанавливает значения в массиве для заданной третьей координаты
        for i in range(self.dim0):
            for j in range(self.dim1):
                self.array[i][j][k] = values[i][j]

    def SetValues01(self, i, j, values):
        # Устанавливает значения в массиве для заданных первой и второй координат
        for k in range(self.dim2):
            self.array[i][j][k] = values[k]

    def SetValues02(self, i, k, values):
        # Устанавливает значения в массиве для заданных первой и третьей координат
        for j in range(self.dim1):
            self.array[i][j][k] = values[j]

    def SetValues12(self, j, k, values):
        # Устанавливает значения в массиве для заданных второй и третьей координат
        for i in range(self.dim0):
            self.array[i][j][k] = values[i]

    @classmethod
    def ones(cls, dim0, dim1, dim2):
        # Метод для создания массива с одинаковыми элементами, заполненными единицами
        instance = cls(dim0, dim1, dim2)
        # Изменение создания массива без использования NumPy
        instance.array = [[[1.0 for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]
        return instance

    @classmethod
    def zeros(cls, dim0, dim1, dim2):
        # Метод для создания массива с одинаковыми элементами, заполненными нулями
        return cls(dim0, dim1, dim2)

    @classmethod
    def fill(cls, dim0, dim1, dim2, value):
        # Метод для создания массива с одинаковыми элементами, заполненными заданным значением
        instance = cls(dim0, dim1, dim2)
        # Изменение создания массива без использования NumPy
        instance.array = [[[value for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]
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
my_array.SetValues0(1, [[1.0, 1.0, 1.0, 1.0, 1.0] for _ in range(4)])
my_array.SetValues1(2, [[1.0 for _ in range(5)] for _ in range(3)])
my_array.SetValues2(3, [[1.0, 1.0, 1.0, 1.0] for _ in range(3)])
my_array.SetValues01(1, 2, [1.0, 1.0, 1.0, 1.0, 1.0])
my_array.SetValues02(1, 3, [1.0, 1.0, 1.0, 1.0])
my_array.SetValues12(2, 3, [1.0, 1.0, 1.0])

# Используем методы для создания массива с одинаковыми элементами
ones_array = Array3d.ones(2, 2, 2)
zeros_array = Array3d.zeros(2, 2, 2)
fill_array = Array3d.fill(2, 2, 2, 7.0)

# Выводим полученные массивы
for i in range(2):
    for j in range(2):
        print(ones_array[i, j, :])
        print(zeros_array[i, j, :])
        print(fill_array[i, j, :])
