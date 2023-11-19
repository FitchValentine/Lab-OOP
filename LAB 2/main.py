import math

# Класс для представления точки в трехмерном пространстве
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Метод для вычисления расстояния между двумя точками
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

# Класс для представления вектора в трехмерном пространстве
class Vector:
    def __init__(self, *args):
        # Вектор может быть задан либо координатами (x, y, z), либо двумя точками
        if len(args) == 3:
            self.x, self.y, self.z = args
        elif len(args) == 2:
            # Если переданы две точки, вычисляем координаты вектора
            self.x = args[1].x - args[0].x
            self.y = args[1].y - args[0].y
            self.z = args[1].z - args[0].z
        else:
            raise ValueError("Неправильное количество аргументов")

    # Операции сложения и вычитания векторов
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Получение обратного вектора
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    # Построение единичного вектора
    def normalize(self):
        length = self.length()
        return Vector(self.x / length, self.y / length, self.z / length)

    # Скалярное произведение векторов
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Векторное произведение векторов
    def cross_product(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    # Смешанное произведение векторов
    def mixed_product(self, other1, other2):
        return self.dot_product(other1.cross_product(other2))

    # Длина вектора
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Проверка коллинеарности двух векторов
    def are_collinear(self, other):
        # Векторы коллинеарны, если их векторное произведение равно нулю
        return self.cross_product(other).length() == 0

    # Проверка компланарности трех векторов
    def are_coplanar(self, other1, other2):
        # Векторы компланарны, если их смешанное произведение равно нулю
        return self.mixed_product(other1, other2) == 0

    # Расстояние между двумя точками
    def distance(self, other):
        # Теперь метод расстояния также доступен для векторов
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # Угол между двумя векторами в радианах
    def angle(self, other):
        dot_product = self.dot_product(other)
        magnitude_product = self.length() * other.length()
        if magnitude_product == 0:
            raise ValueError("Невозможно вычислить угол для нулевого вектора")
        return math.acos(dot_product / magnitude_product)

# Пример использования
if __name__ == "__main__":
    point1 = Point(1, 2, 3)
    point2 = Point(4, 5, 6)

    vector1 = Vector(1, 2, 3)
    vector2 = Vector(point1, point2)

    print(f"Вектор1: ({vector1.x}, {vector1.y}, {vector1.z})")
    print(f"Вектор2: ({vector2.x}, {vector2.y}, {vector2.z})")

    result_add = vector1 + vector2
    result_sub = vector1 - vector2
    result_neg = -vector1
    result_normalize = vector1.normalize()
    result_dot_product = vector1.dot_product(vector2)
    result_cross_product = vector1.cross_product(vector2)
    result_mixed_product = vector1.mixed_product(vector2, Vector(1, 1, 1))
    result_length = vector1.length()
    result_collinear = vector1.are_collinear(vector2)
    result_coplanar = vector1.are_coplanar(vector2, Vector(2, 2, 2))
    result_distance = point1.distance(point2)
    result_angle = vector1.angle(vector2)

    # Вывод результатов
    print(f"Сложение: ({result_add.x}, {result_add.y}, {result_add.z})")
    print(f"Вычитание: ({result_sub.x}, {result_sub.y}, {result_sub.z})")
    print(f"Обратный вектор: ({result_neg.x}, {result_neg.y}, {result_neg.z})")
    print(f"Единичный вектор: ({result_normalize.x}, {result_normalize.y}, {result_normalize.z})")
    print(f"Скалярное произведение: {result_dot_product}")
    print(f"Векторное произведение: ({result_cross_product.x}, {result_cross_product.y}, {result_cross_product.z})")
    print(f"Смешанное произведение: {result_mixed_product}")
    print(f"Длина вектора: {result_length}")
    print(f"Коллинеарность: {result_collinear}")
    print(f"Компланарность: {result_coplanar}")
    print(f"Расстояние между точками: {result_distance}")
    print(f"Угол между векторами (в радианах): {result_angle}")
