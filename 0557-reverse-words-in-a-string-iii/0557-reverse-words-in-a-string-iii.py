class Solution:
    def reverseWords(self, s):
        result = ""
        i = 0
        n = len(s)

        while i < n:
            # Mark the beginning of the word
            start = i

            # Move until the end of the word
            while i < n and s[i] != " ":
                i += 1

            # Add the word in reverse order
            result += s[start:i][::-1]

            # Add the space (if it exists)
            if i < n:
                result += " "
                i += 1

        return result