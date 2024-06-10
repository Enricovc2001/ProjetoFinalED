import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def auto_complete(self, prefix):
        def dfs(current_node, current_prefix):
            if current_node.is_end_of_word:
                words.append(current_prefix)
            for char, next_node in current_node.children.items():
                dfs(next_node, current_prefix + char)

        node = self.root
        words = []
        for char in prefix:
            if char not in node.children:
                return words
            node = node.children[char]
        dfs(node, prefix)
        return words

def load_dictionary(trie, filepath):
    if not os.path.isfile(filepath):
        print(f"Arquivo {filepath} não encontrado.")
        return
    with open(filepath, 'r') as file:
        for word in file:
            trie.insert(word.strip().lower())

# Caminho absoluto para o arquivo dictionary.txt
filepath = r'C:\Users\enrcosta.CISCO\OneDrive - Cisco\Documents\FACENS\Estrutura de dados\dictionary.txt'

# Cria uma instância da Trie e carrega um dicionário
trie = Trie()
load_dictionary(trie, filepath)

def main():
    while True:
        print("\nMenu:")
        print("1. Autocompletar")
        print("2. Verificação Ortográfica")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            prefix = input("Digite o prefixo: ").lower()
            suggestions = trie.auto_complete(prefix)
            print("Sugestões:", suggestions)
        elif choice == '2':
            word = input("Digite a palavra: ").lower()
            if trie.search(word):
                print(f"A palavra '{word}' está correta.")
            else:
                print(f"A palavra '{word}' está incorreta.")
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
