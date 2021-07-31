def letterCombinations(digits):
    stack = []
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(i, current_string):
        if len(digits) == len(current_string):
            stack.append(current_string)
            return

        for char in dic[digits[i]]:
            backtrack(i + 1, char + current_string)

    if digits:
        backtrack(0, "")
    print(stack)


digits = "23 "
letterCombinations(digits)

# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
