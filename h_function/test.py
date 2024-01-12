def count_of_a(*strs):
    count = 0
    counts = []

    for str in strs:

        for s in str:

            if s == 'A':
                count += 1

        counts.append(count)
        count = 0

    return counts

print(count_of_a('AAAAAAC', 'AAB', 'AAA'))