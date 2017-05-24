import pickle


def read_counts():
    with open('data.pickle', 'rb') as f:
        return pickle.load(f)


def save_counts(last_count):
    with open('data.pickle', 'wb') as f:
        pickle.dump(last_count, f)

# LAST_COUNTS = {30666517: 18823, 142410745: 49, 54530371: 5505}
# save_counts(LAST_COUNTS)
# print(read_counts())
