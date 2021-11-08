import time
from collections import Counter
from time import sleep

a = 'Ala ma kota'
b = 'aLA am atok'


def rev_str(text: str):
    return ' '.join(x[::-1] for x in text.split())


print(rev_str(a))

x = [1, 2, 3, 4, 4, 4, 4, 5, 326, 26, 6, 4, 6, 4]


def duplicates(x):
    c = Counter(x)
    result = []
    for k, v in c.items():
        if v > 1:
            result.append(k)
    return result


print(duplicates(x))


def duplicates2(x):
    return set([k for k in x if x.count(k) > 1])


print(duplicates(x))


def duplicates3(x):
    return set([k for k, v in Counter(x).items() if v > 1])


print(duplicates(x))

i = [('Tom', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]
j = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


def sorted_list(list_):
    return sorted(list_, key=lambda x: (x[0], x[2], x[1]))


print(sorted_list(i))


def time_it(fun):
    def inner(*args, **kwargs):
        start = time.time()
        result = fun(*args, *kwargs)
        end = time.time()
        print(f'Time taken {end - start}')
        return result

    return inner

@time_it
def sleeper():
    sleep(2)
