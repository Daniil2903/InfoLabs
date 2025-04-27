import nbformat
from nbconvert import PythonExporter

# Загрузка .ipynb файла
with open('bigLab2.ipynb', 'r', encoding='utf-8') as f:
    notebook_content = nbformat.read(f, as_version=4)

# Инициализация конвертера
python_exporter = PythonExporter()

# Конвертация в Python-скрипт
script, _ = python_exporter.from_notebook_node(notebook_content)

# Сохранение результата в .py файл
with open('your_script.py', 'w', encoding='utf-8') as f:
    f.write(script)

print("Конвертация завершена!")

