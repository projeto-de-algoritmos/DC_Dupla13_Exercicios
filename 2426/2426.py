# O problema define que i e j devem safisfazer a inequação 
# nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
# Para tornar a resolução do problema mais simples, a inequação é manipulada
# para que seja possível analisar somente um indice por vez, respeitando
# o seu valor matemáticamente. Esaa manipulação resulta em:
# nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff


from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # Guarda o tamanho do vetor num1 que é o mesmo do num2
        N = len(nums1)
        # Utiliza uma sorted list, estrutura contida na biblioteca sortedcontainers 
        # do python. Nesta estrutura, os valores sempre são adicionados de forma ordenada,
        # o que permite a operação "bisect". Como em uma árvore binária de busca, essa operação
        # retorna a posição em que um número deve ser alocado no vetor ordenado. 
        diferencas = SortedList()
        # Contador para o número de pares que satisfazem a inequação
        n_pares = 0

        # Loop que opera no tamanho dos vetores
        for i in range(N):
            # Diferença entre os valores dos dois vetores no índice i. 
            delta = nums1[i] - nums2[i]
            # Ao utilizar a operação "bisect_right" do delta + o valor diff na lista ordenada
            # com os deltas já adicionados, verificamos de quantos deltas o delta atual é maior.
            # Desta forma, podemos considerar que os pares que resultaram nos deltas anteriores 
            # (nums1[i] - nums2[i]) são menores ou iguais ao delta atual mais o valor da diff
            # (nums1[j] - nums2[j] + diff), satisfazendo assim a inequação.
            maior_que = diferencas.bisect_right(delta + diff)
            # Soma ao número de pares que satisfazem a equação o valor encontrado na etapa anterior
            n_pares += maior_que

            # Adiciona à lista ordenada o delta analisado no loop
            diferencas.add(delta)

        return n_pares