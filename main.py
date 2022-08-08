# Aluno: Bruno Teider

# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
# linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de
# operações que serão realizadas entre dois conjuntos de dados.


# Funções
def uniao(A, B):
    result = []
    for i in A:
        result.append(i)
    for i in B:
        if i not in A:
            result.append(i)
    return result


def inter(A, B):
    result = []
    for i in A:
        if i in B:
            result.append(i)
    return result


def dif(A, B):
    result = []
    for i in A:
        if i not in B:
            result.append(i)
    return result


def produto(A, B):
    result = []
    for i in A:
        for c in B:
            temp = []
            temp.append(i)
            temp.append(c)
            result.append(temp)
    return result


def printer(op, A, B, result):
    A = (' '.join(A)).replace(" ", ",")
    B = (' '.join(B)).replace(" ", ",")

    if op != "Produto Cartesiano":
        result = (' '.join(result).replace(" ", ","))
        print(
            f"{op}: conjunto 1 {{{A}}}, conjunto 2 {{{B}}}. Resultado: {{{result}}} "
        )
    else:
        temp = ' '
        counter = 0
        for i in result:
            temp += '('
            for c in i:
                temp += ' '.join(c)
                counter += 1
                if counter % 2 != 0:
                    temp += ','
            temp += '),'
        temp = temp[1:-1]
        print(
            f"{op}: conjunto 1 {{{A}}}, conjunto 2 {{{B}}}. Resultado: {{{temp}}}"
        )


# Código Principal
read_txt = open('entrada1.txt')
num_repet = int(read_txt.readline())

for c in range(num_repet):
    conjunto_1 = []
    conjunto_2 = []
    for i in range(3):
        value = ((read_txt.readline()).rstrip('\n')).replace(" ", "")
        if i == 0:
            operation_code = value
        elif i == 1:
            conjunto_1 = value.split(',')
        elif i == 2:
            conjunto_2 = value.split(',')

    if operation_code == "U":
        operation_code = "União"
        printer(operation_code, conjunto_1, conjunto_2,
                uniao(conjunto_1, conjunto_2))
    elif operation_code == "I":
        operation_code = "Interseção"
        printer(operation_code, conjunto_1, conjunto_2,
                inter(conjunto_1, conjunto_2))
    elif operation_code == "D":
        operation_code = "Diferença"
        printer(operation_code, conjunto_1, conjunto_2,
                dif(conjunto_1, conjunto_2))
    elif operation_code == "C":
        operation_code = "Produto Cartesiano"
        printer(operation_code, conjunto_1, conjunto_2,
                produto(conjunto_1, conjunto_2))

read_txt.close()
