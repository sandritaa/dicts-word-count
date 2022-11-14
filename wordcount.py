"""Count words in file."""


# put your code here.


def space_count(filename):

    import_file = open(filename)
    word_counter = {}

    for line in import_file:

        words = line.split(' ')

        for word in words:

            word_counter[word] = word_counter.get(word, 0) + 1

    return word_counter


var = space_count('test.txt')
print(var)
