input_list = [64, 34, 12, 25, 22, 11, 90]


def bubbleSort(list):
    """
    Le tri à bulles est un algorithme de tri qui parcourt répétitivement une liste qui doit être triée,
    qui compare chaque paire d'éléments adjacents et les échange si ils sont dans le mauvais ordre.
    Ce passage à travers la liste est répété jusqu'à ce qu'il n'y ait plus d'échange.
    Ce tri est nommé suite à la façon dont les nombres se déplacent à travers la liste qui ressemble à des bulles qui remontent à la surface de l'eau.
    """
    for i in list:
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            # print(list)
            return list

def insertionSort(list):
    """
    Le tri par insertion est un algorithme de tri qui place chaque élément de la liste à sa place appropriée dans la liste triée.
    C'est le tri le plus utilisé dans la vie réelle, car il est très efficace pour les petites tailles (exemple : tri des cartes à jouer)
    """
    for i in range(len(list)-1):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x
        # print(list)
        return list

def fusionSort(list):
    """
    Le tri fusion est un algorithme de tri récursif qui divise chaque liste en deux moitiés (jusqu'à n'obtenir que des éléments solitaire),
    trie chacun des éléments , puis fusionne les deux moitiés triées.
    """
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        fusionSort(left)
        fusionSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list[k] = right[j]
                j += 1
            else:
                list[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        # print(list)
        return list




def partList(list, low, high, pivot):
    """
    low = valeur basse
    high = valeur haute
    pivot = valeur de référence

    Fractionne la liste en deux parties, une partie avec des valeurs plus petites que le pivot et l'autre avec des valeurs plus grandes que le pivot
    """
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    return i+1

def quickSort(list, first, last):
    """
    first = première valeur
    last = dernière valeur
    """
    if first < last:
        pivot = list[last]
        part = partList(list, first, last, pivot)
        quickSort(list, first, part-1)
        quickSort(list, part+1, last)
        # print(list)
        return list


# bubbleSort(input_list)

# insertionSort(input_list)

# fusionSort(input_list)

# quickSort(input_list, 0, len(input_list)-1)