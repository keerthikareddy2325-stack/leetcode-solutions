class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        len_s = len(s)
        first_half = s[:len_s // 2]
        second_half = s[len_s // 2:]
        count_vowels_first_half = 0
        count_vowels_second_half = 0

        for char in first_half:
            if char in 'aeiouAEIOU':
                count_vowels_first_half = count_vowels_first_half + 1


        for char in second_half:
            if char in 'aeiouAEIOU':
                count_vowels_second_half = count_vowels_second_half + 1

        if count_vowels_first_half == count_vowels_second_half:
            return True
        else:
            return False 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna