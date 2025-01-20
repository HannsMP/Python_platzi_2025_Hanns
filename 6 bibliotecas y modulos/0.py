import os

cwd = os.getcwd()
print(cwd)

txt_files = [f for f in os.listdir('./txt') if f.endswith('.txt')]
print(txt_files)

os.rename('./txt/caperucita.txt', './txt/cuento.txt')