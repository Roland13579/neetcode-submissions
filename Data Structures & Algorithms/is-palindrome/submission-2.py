class Solution:
    def isPalindrome(self, s: str) -> bool:
        #No need to use strip function. Just create a new string and add in only     alphanumeric   
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        print(cleaned)
        left = 0
        right = len(cleaned) - 1

        while(left < right):
            if(cleaned[left] == cleaned[right]):
                left +=1
                right-=1
            else:
                print("False reason: ", s[left], "is not equal to", s[right])
                return False
        return True
