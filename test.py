import numpy as np
import matplotlib.pyplot as plt


def makeData():
    # Строим сетку в интервале от -3.5 до 3.5, имеющую 100 отсчетов по обоим координатам
    x = np.linspace(-3.5, 3.5, 100)
    y = np.linspace(-3.5, 3.5, 100)

    # Создаем двумерную матрицу-сетку
    xgrid, ygrid = np.meshgrid(x, y)

    # В узлах рассчитываем значение функции
    z = xgrid * xgrid
    return xgrid, ygrid, z



x, y, z = makeData()

fig = plt.figure()
axes = fig.add_subplot(projection='3d')
axes.plot_surface(x, y, z, rstride=5, cstride=5, cmap='plasma')
plt.show()
