# https://leetcode.com/problems/sorting-the-sentence/

def sort_sentence(s):
    sorted_arr = sorted(s.split(" "), key=lambda word: int(word[-1]))
    sorted_arr = [word[:-1] for word in sorted_arr]

    return " ".join(sorted_arr)

print(sort_sentence("is2 sentence4 This1 a3"))
print(sort_sentence("Myself2 Me1 I4 and3"))

# ---------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_arr = sorted(s.split(" "), key=lambda word: int(word[-1]))
        sorted_arr = [word[:-1] for word in sorted_arr]

        return " ".join(sorted_arr)
