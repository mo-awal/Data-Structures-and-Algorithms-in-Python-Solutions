all_combinations = []

def get_combinations(letters, combination, ans=all_combinations):
    if not letters:
        ans.append(''.join(combination))
    else:
        for i in range(len(letters)):
            combination.append(letters.pop(i))
            get_combinations(letters, combination)
            letters.insert(i, combination.pop())
    return ans

print(get_combinations(['a', 'b', 'c'], []))
