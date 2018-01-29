# Swami Shreeji
# So you need to randomly assign individuals to groups ...

from random import shuffle

def chunks(shuffled, num):
    """Yield successive num-sized chunks from list."""
    for i in range(0, len(shuffled), num):
        yield shuffled[i:i + num]

answer = (list(chunks(range(0, 20), 4)))
shuffle(answer)
print answer
