#tratar byte por byte (0-255)

# xxxxxxxyyyyzzzz
# 7x4y4z

def rlecompressor (data):
    
    comprimido = bytearray ()   #bytearray - matriz de bytes que vai de 0 até < 256

    contador = 1
    byte_atual = data[0]        # primeiro byte do arquivo
    
    for i in data[1:]:          #conta da posição 1 pra frente
        if i == byte_atual:     #Enquanto forem iguais eu vou avançando no vetor
            contador += 1

            #.append Adiciona um item ao fim da lista
            if contador >= 256: # caso meu bytearray tenha estourado eu gravo a interação e coloco o restando em outro de 255.
                comprimido.append(contador - 1)
                comprimido.append(byte_atual)
                contador = 1
                #colocando o progesso no arquivo comprimido
        
        else: #ao encontrar um elemento diferente
          comprimido.append(contador)
          comprimido.append(byte_atual)
          byte_atual = i
          contador = 1
          # colocando o progresso no arquivo comprimido
    
    # colocando o progresso no atquivo comprimido após o for.
    comprimido.append(contador)
    comprimido.append(byte_atual)

    return comprimido

arquivo = open('a.txt', 'rb')   #arquivo lido em binário
data = arquivo.read()               #le o arquivo e armazena em data
#print(data)

comprimido = rlecompressor(data)

print("Tamanho do arquivo original(bytes): ")
print(len(data))
print("Tamanho do arquivo comprimido(bytes):")
print(len(comprimido))

arquivo_comprimido = open('arq_comprimido.bin', 'wb')   # abrindo um arquivo binário de escrita
arquivo_comprimido.write(comprimido)                    #gravando compressão no arquivo