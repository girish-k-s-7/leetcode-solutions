# Reverse word in string
class Solution():
    def reverseWords(self, s):
        result = ""
        # pointer starting from the end
        i = len(s) - 1

        while i >= 0:

            # to skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            # if pointer out of bound
            if i < 0:
                break

            # mark end of the word
            end = i

            while i >= 0 and s[i] != " ":
                i -= 1
            word = s[i + 1:end + 1]

            # add spaces if result is not empty
            if result != "":
                result += " "
            result += word
        return result
