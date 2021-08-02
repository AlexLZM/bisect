def bisect_right(arr, x, lo=0, hi=None):
    if hi is None:
        hi = len(arr)
        
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
            
    return lo



def bisect_left(arr, x, lo=0, hi=None):
    if hi is None:
        hi = len(arr)
        
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
            
    return lo
