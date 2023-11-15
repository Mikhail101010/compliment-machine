import random


def generate(names = [], good_words = [], bad_words = [], only_good = False):
    someone_else = False
    if names:
        someone_else = True if random.randint(0, len(names)) > 0 else  False
    if someone_else:
        name = names[random.randint(0, len(names) - 1)].title() + " is "
    else:
        name = "You are "
    good = True
    if good_words or bad_words:
        if not only_good:
            good = random.randint(0, len(bad_words) + len(good_words) - 1) >= len(bad_words)
            if good:
                name += good_words[random.randint(0, len(good_words) - 1)] + "."
            else:
                name += bad_words[random.randint(0, len(bad_words) - 1)] + "!"
        else:
            name += good_words[random.randint(0, len(good_words) - 1)] + [".", "!"][random.randint(0, 1)]
        print(name)
    else:
        raise IndexError("No words provided.")


generate(
    names = [
        "David C",
        "David Y",
        "Dmitry",
        "Momchil"
    ],
    good_words = [
        "good",
        "smart",
        "not dumb",
        "not stupid",
        "not a fool"
    ],
    bad_words = [
        "dumb",
        "stupid",
        "a fool",
        "foolish"
    ],
    only_good = True
)