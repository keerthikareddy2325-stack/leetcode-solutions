class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, ch in enumerate(s):
            res[indices[i]] = ch
        return ''.join(res)
     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna