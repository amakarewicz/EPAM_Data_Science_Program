
def main():
    import pandas as pd
    import numpy as np

    a = np.zeros((3,3))
    a = pd.DataFrame(a)
    print("Everything is OK!")


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Pandas or Numpy are not installed. Check your current environment.")