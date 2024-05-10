import pandas as pd
import os
from matplotlib import pyplot as plt


class PlotDrawer:
    def draw_plots(self, json_file):
        # Чтение данных из JSON-файла в DataFrame
        data = pd.read_json(json_file)

        # Создание папки "plots", если её нет
        if not os.path.exists("plots"):
            os.makedirs("plots")

        # Создание графиков и сохранение их в папку "plots"
        plot_paths = []
        for column in data.columns:
            if column == "name":
                continue
            plt.figure()
            plt.plot(data[column])
            plt.title(column)
            plot_path = os.path.join("plots", f"{column}.png")
            plt.savefig(plot_path)
            plot_paths.append(plot_path)
            plt.close()

        return plot_paths

# Создаем экземпляр класса PlotDrawer
plot_drawer = PlotDrawer()

# Путь к JSON-файлу с данными
json_file = "deviation.json"

# Вызываем функцию draw_plots для построения графиков
plot_paths = plot_drawer.draw_plots(json_file)

# Выводим пути к сохраненным графикам
print("Plots saved at:", plot_paths)


