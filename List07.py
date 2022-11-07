def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    k=0
    n=len(list1)
    while i<n:
        if list1[i]==0:
            k+=1
            k=False
        i+=1
    return k
print(main([2,3,40,0,0,6]))