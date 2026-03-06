class Solution:
    def isPalindrome(self, x: int) -> bool:
      s  = str(x)
      length = len(s)
      j = -1
      count = 0
      g = ""
      while count < length:
        g += s[j]
        j -= 1
        count += 1
      if g == s:
        return True
      else:
        return False
