#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import subprocess

def selecionar_arquivo():
    arquivo_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    entry_caminho.delete(0, tk.END)
    entry_caminho.insert(0, arquivo_path)

def comprimir_pdf():
    arquivo_path = entry_caminho.get()

    if not arquivo_path.endswith('.pdf'):
        resultado_label.config(text="Por favor, selecione um arquivo PDF.")
        return

    arquivo_saida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivos PDF", "*.pdf")])

    if arquivo_saida:
        # Comprimir usando Ghostscript
        comando = ["gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", "-dPDFSETTINGS=/ebook", "-dNOPAUSE", "-dQUIET", "-dBATCH", f"-sOutputFile={arquivo_saida}", arquivo_path]

        try:
            subprocess.run(comando, check=True)
            resultado_label.config(text="Compressão concluída com sucesso.")
        except subprocess.CalledProcessError as e:
            resultado_label.config(text=f"Erro ao comprimir o PDF: {e}")
    else:
        resultado_label.config(text="Compressão cancelada.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Comprimir PDF com Ghostscript")

# Criar os widgets
label_selecionar = tk.Label(janela, text="Selecione um arquivo PDF:")
entry_caminho = tk.Entry(janela, width=50)
botao_selecionar = tk.Button(janela, text="Selecionar", command=selecionar_arquivo)

botao_comprimir = tk.Button(janela, text="Comprimir PDF", command=comprimir_pdf)
resultado_label = tk.Label(janela, text="")

# Posicionar os widgets na janela
label_selecionar.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_caminho.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
botao_selecionar.grid(row=0, column=3, padx=10, pady=5)

botao_comprimir.grid(row=1, column=0, columnspan=2, pady=10)
resultado_label.grid(row=1, column=2, columnspan=2, pady=10)

# Iniciar a execução da interface gráfica
janela.mainloop()
