def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    first = {}
    second = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        first[s[i]] = first.get(s[i], 0) + 1
        second[t[i]] = second.get(t[i], 0) + 1
        
    return first == second