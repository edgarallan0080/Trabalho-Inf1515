import nbformat
import os

# Lista dos notebooks a serem unidos (na ordem que desejar)
notebooks = [
    "exemplo_coletadadosb3.ipynb",
    "Exemplo_Cookie_Clickers.ipynb",
    "Exemplo_Previsao_Tempo.ipynb",
    "exemplo_triagem_curriculos.ipynb"
]

# Novo notebook final
notebook_final = nbformat.v4.new_notebook()
final_cells = []

# Carrega todos e junta os blocos
for nb_file in notebooks:
    if os.path.exists(nb_file):
        with open(nb_file, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            # Título de separação entre notebooks
            final_cells.append(nbformat.v4.new_markdown_cell(f"# 🔹 Conteúdo de: {nb_file}\n"))
            final_cells.extend(nb.cells)

notebook_final.cells = final_cells

# Salva o resultado
output_file = "projeto_final.ipynb"
with open(output_file, "w", encoding="utf-8") as f:
    nbformat.write(notebook_final, f)

print("✅ Notebook unido criado com sucesso:", output_file)
