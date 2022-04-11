class bola():
    def __init__(self,cor,circunferencia,material,peso,preco,status):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = circunferencia
        self.peso = peso
        self.preco  = int(preco)
        self.status = status
    
    def trocaCor (self,cor):
        if self.cor == '':
            self.cor = cor
        else:
            print('O produto já possui uma cor cadastrada.')

    def verCor (self):
        print(self.cor)

    #Função extra 1
    def encherBola (self):
        if self.status == 'Murcha':
            print('Você precisa encher a bola.')
        else:
            print('Sua bola está ideal para uso.')
    
    #Função extra 2
    def precoBola(self,validador):
        if validador == '+':
            self.preco = self.preco + 5
        elif validador == '-':
            self.preco = self.preco - 5
        print(f'Agora o valor da bola é {self.preco}')
        
bola1 = bola('',10,'Couro','200g','10','Murcha')    


bola1.verCor()
bola1.trocaCor('Amarelo')
bola1.verCor()
bola1.encherBola()

bola1.precoBola(input(f'Sabendo que o valor atual da bola é: {bola1.preco}\nDigite "+" para aumentar o valor da bola em 5, ou "-" para diminuir seu valor em 5:'))



'''
exemplos:
#Exemplo netflix

class Cliente():
    def __init__(self,nome,email,plano):
        self.nome = nome
        self.email = email
        self.signo = ''
        self.lista_plano = ['Basic','Premium']
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception("Plano inválido, por favor selecione um dos disponíveis(Basic ou Premium)")
    
    def alterar_plano(self,novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print("Plano inválido!")



Cliente1 = Cliente("Diego","diconediego@outlook.com",'Premium')

Cliente1.signo = 'seqso'
print(Cliente1.signo)
'''
        

