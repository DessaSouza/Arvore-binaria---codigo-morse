class Nodo:
    def __init__(self, caractere=None):
        self.caractere = caractere
        self.filho_esquerdo = None
        self.filho_direito = None


class ArvoreBinariaMorse:
    def __init__(self):
      
        #inicializa a árvore com a raiz vazia
        self.raiz = Nodo()

    def inserir(self, codigo_morse, caractere):
        no_atual = self.raiz
      
        #percorre os símbolo do código Morse (ponto ou traço)
        for simbolo in codigo_morse:
            if simbolo == '.':
              
                #se for ponto vai para a subárvore da esquerda
                if no_atual.filho_esquerdo is None:
                    no_atual.filho_esquerdo = Nodo()
                no_atual = no_atual.filho_esquerdo
            elif simbolo == '-':
              
                #se for traço vai para a subárvore da direita
                if no_atual.filho_direito is None:
                    no_atual.filho_direito = Nodo()
                no_atual = no_atual.filho_direito
              
        #coloca o caractere ao nó certo
        no_atual.caractere = caractere

    def buscar(self, codigo_morse):
        no_atual = self.raiz
      
        #percorre a árvore de acordo com o código Morse
        for simbolo in codigo_morse:
            if simbolo == '.':
                no_atual = no_atual.filho_esquerdo
            elif simbolo == '-':
                no_atual = no_atual.filho_direito
            if no_atual is None:
              
                #se o caminho não existir retorna None
                return None
              
        #retorna o caractere encontrado
        return no_atual.caractere

    def exibir(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
          
        if no.caractere:
            #exibe o caractere no nível atual
            print(' ' * nivel + no.caractere)
          
        if no.filho_esquerdo:
            #exibe a subárvore esquerda com o nível aumentado
            print(' ' * nivel + '•')
            self.exibir(no.filho_esquerdo, nivel + 1)
          
        if no.filho_direito:
            #exibe a subárvore direita com o nível aumentado
            print(' ' * nivel + '-')
            self.exibir(no.filho_direito, nivel + 1)


#tabela do código Morse
morse_table = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}


#inicializa a árvore e insere todos os caracteres alfanuméricos do código Morse
def inicializar_arvore_completa():
    arvore = ArvoreBinariaMorse()
    for caractere, morse in morse_table.items():
        arvore.inserir(morse, caractere)
    return arvore


#função para buscar e formar uma mensagem em Morse
def buscar_mensagem_morse(arvore, mensagem_morse):
    resultado = ''
    palavras = mensagem_morse.split(' ')
    for codigo_morse in palavras:
        resultado += arvore.buscar(codigo_morse) or '?'
    return resultado


#exemplo de uso completo
if __name__ == "__main__":
    arvore = inicializar_arvore_completa()

    #entrada do usuário em código Morse
    entrada_usuario = input("Digite a mensagem em código Morse separada por espaços (ex: '... --- ...'): ")
    mensagem = buscar_mensagem_morse(arvore, entrada_usuario)

    #exibe a mensagem decodificada
    print("Mensagem decodificada:", mensagem)

    #exibe a árvore inteira
    print("\nEstrutura da árvore binária Morse:")
    arvore.exibir()
