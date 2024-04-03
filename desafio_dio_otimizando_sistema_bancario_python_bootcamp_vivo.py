#========================== Sistema bancário ==========================

def menu():
    menu = """
    =================== Menu =========================
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [nc] - Nova conta
    [lc] - Listar contas
    [nu] - Novo usuário
    [q] - Sair
    ===================================================

     => """
    return input(menu)


def depositar(saldo, valor, extrato, numero_saques, /): #positional-only /
    
    if valor < 0:
      print('Valor inválido para depósito, insira um valor a partir de R$ 0.01')

    else:
      saldo += valor
      extrato += f'Depósito de: R${valor:.2f}\n'

    return saldo, extrato, numero_saques


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #keyword-only *
    
    if saldo > 0 and saldo >= valor:
        if numero_saques < limite_saques and valor <= limite:
          saldo -= valor
          extrato += f'Saque de: R${valor:.2f}\n'
          numero_saques += 1

        elif  numero_saques == limite_saques:
            print(f'Você atingiu o limite de saques diário que são 3.\nSaques feitos hoje: {numero_saques}')

        elif valor > limite:
            print('Ultrapassou o valor do limite por saque que é de R$ 500.00.')

    else:
      print(f'Você não tem saldo suficiente, seu saldo atual é de: {saldo: .2f}')

    return saldo, extrato, numero_saques,



def exibir_extrato(saldo, numero_saques, /, *, extrato, ):
    
    if extrato == "":
      print('==================== EXTRATO ====================')
      print('Você não tem movimentações')
      print('=================================================')

    else:
      print('==================== EXTRATO ====================')
      print(f'\n{extrato}\nSaldo atual: {saldo: .2f}\nNúmero de saques feitos hoje: {numero_saques}')
      print('==================================================')

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF - somente números')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe usuário com esse CPF!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, num - bairro - cidade/sigla estado: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)


    if usuario:
        print('\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\nUsuário não encontrado, foi encerrado a criação da conta!')


def listar_contas():
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuário']['nome']}
        """

        print("=" *100)
        print(linha)




def main():

    
    saldo = 0.0
    limite = 500.00
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []
    
    LIMITE_SAQUES = 3
    AGENCIA = '0001'


    while True:

      opcao = menu()

      #Depósito
      if opcao == 'd':
      
        valor = float(input('Informe o valor do depósito: \n'))

        saldo, extrato, numero_saques = depositar(saldo, valor, extrato, numero_saques)

      #Saldo
      elif opcao == 's':
      
        valor = float(input('Informe o valor do saque: \n'))

        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        
        
      #Extrato
      elif opcao == 'e':
           exibir_extrato(saldo, numero_saques, extrato=extrato, )


      #Novo Usuário
      elif opcao == 'nu':
          criar_usuario(usuarios)


      elif opcao == 'nc':
          numero_conta = len(contas) +1
          conta = criar_conta(AGENCIA, numero_conta, usuarios)

          if conta:
              conta.append(conta)

      elif opcao == 'lc':
          listar_contas(contas)

           
      #Sair
      elif opcao == 'q':
          print('Volte sempre!! \(^^)/.....')

          break

      else:
         print('Entrada inválida!')


#def cadastrar_cliente():


#def cadastrar_conta_bancaria():





main()















































