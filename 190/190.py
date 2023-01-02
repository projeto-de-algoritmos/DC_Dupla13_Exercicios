# O problema consiste na inversão de um número de 32 bits
# Para a sua solução, serão usadas as operações de right e left shift
class Solution:
    def reverseBits(self, n: int) -> int:
        # Inicia o número invertido com o valor zero
        numInverso = 0
        
        # Executa o loop 32 vezes, uma vez que as entradas do problema possuem 32 bits.
        for _ in range(32):
            # Executa o left-shift no número inverso, adicionando um 0 a sua direita 
            numInverso = numInverso << 1
            # Adiciona ao número inverso o valor da operação AND entre o número da entrada 
            # e o número 1. A operação AND é necessária para obter-se o valor do último bit
            # do número de entrada uma vez que qualquer bit em operação AND com o 1 resulta 
            # nele mesmo. Assim, esse valor é adicionado ao número inverso, "ocupando" o bit
            # 0 que foi adicionado na etapa passada 
            numInverso += n & 1
            # Executa o right-shift no valor da entrada, removendo o seu último bit, que já 
            # foi adicionado ao número inverso na última etapa
            n = n >> 1
        
        return numInverso