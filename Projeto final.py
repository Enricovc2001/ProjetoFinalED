import os

class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_fim_de_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = NoTrie()
            no = no.filhos[char]
        no.eh_fim_de_palavra = True

    def buscar(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.eh_fim_de_palavra

    def comeca_com(self, prefixo):
        no = self.raiz
        for char in prefixo:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return True

    def auto_completar(self, prefixo):
        def dfs(no_atual, prefixo_atual):
            if no_atual.eh_fim_de_palavra:
                palavras.append(prefixo_atual)
            for char, proximo_no in no_atual.filhos.items():
                dfs(proximo_no, prefixo_atual + char)

        no = self.raiz
        palavras = []
        for char in prefixo:
            if char not in no.filhos:
                return palavras
            no = no.filhos[char]
        dfs(no, prefixo)
        return palavras

def carregar_dicionario(trie, caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        print(f"Arquivo {caminho_arquivo} não encontrado.")
        return
    with open(caminho_arquivo, 'r') as arquivo:
        for palavra in arquivo:
            trie.inserir(palavra.strip().lower())

# Caminho absoluto para o arquivo dictionary.txt
caminho_arquivo = r'C:\Users\enrcosta.CISCO\OneDrive - Cisco\Documents\FACENS\Estrutura de dados\dictionary.txt'

# Cria uma instância da Trie e carrega um dicionário
trie = Trie()
carregar_dicionario(trie, caminho_arquivo)

def main():
    while True:
        print("\nMenu:")
        print("1. Autocompletar")
        print("2. Verificação Ortográfica")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            prefixo = input("Digite o prefixo: ").lower()
            sugestoes = trie.auto_completar(prefixo)
            print("Sugestões:", sugestoes)
        elif escolha == '2':
            palavra = input("Digite a palavra: ").lower()
            if trie.buscar(palavra):
                print(f"A palavra '{palavra}' está correta.")
            else:
                print(f"A palavra '{palavra}' está incorreta.")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
