def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    k=0
    n=len(list1)
    i=0
    while i<n:
        if list1[i]==0:
            k=k+1
        i+=1
print(main([3,4,5,6,0,0,0,]))