from collections import Counter
import re

# Função para limpar e preparar o texto
def clean_text(text):
    # Remove caracteres especiais, números e deixa tudo em minúsculo
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

# Função principal
def count_words(text):
    # Limpa o texto
    cleaned_text = clean_text(text)
    
    # Divide o texto em palavras
    words = cleaned_text.split()

    # Conta a frequência das palavras
    word_count = Counter(words)
    
    # Exibe o ranking das palavras mais comuns
    print("\nRanking das palavras mais frequentes:")
    for word, count in word_count.most_common():
        print(f"{word}: {count}")

# Execução do programa
if __name__ == "__main__":
    # Solicita o texto ao usuário
    user_text = input("Digite o texto: ")
    count_words(user_text)
