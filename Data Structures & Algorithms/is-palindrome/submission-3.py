class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated = re.sub(r"[^A-Za-z0-9]", '',s).lower()
        left, right = 0, len(formated) - 1
        print(formated)
        while left < right:
            if formated[left] != formated[right]:
                return False
            
            left+=1
            right-=1


        return True