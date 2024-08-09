import os
import glob

def excluir_arquivos(pastas):
    for pasta in pastas:
        # Lista todos os arquivos na pasta especificada
        arquivos = glob.glob(os.path.join(pasta, '*'))
        
        for arquivo in arquivos:
            try:
                os.remove(arquivo)  # Remove o arquivo
                print(f"{arquivo} foi excluído com sucesso.")
            except Exception as e:
                print(f"Erro ao excluir {arquivo}: {e}")

# Lista de caminhos das pastas que você deseja excluir os arquivos
pastas = [
    'C:SUA PASTA AQUI', 
    'C:SUA PASTA AQUI', 
    'C:SUA PASTA AQUI', 
    'C:\\Windows\\Temp' #EXEMPLO
]

excluir_arquivos(pastas)
