import pickle

def save_data(library, filename):
    with open(filename , 'wb') as file :
        pickle.dump(library , file)
        
        
def load_data (filename):
    try:
        with open(filename , 'rb') as file :
            return pickle.load(file)
    except FileNotFoundError:
        return None