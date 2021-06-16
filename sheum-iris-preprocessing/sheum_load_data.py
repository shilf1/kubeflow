import pandas as pd
import argparse

#import time

if __name__ == "__main__":

#    time.sleep(1800) 
    
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        '--data_path', type=str,
        help="Input data path"
    )

    args = argument_parser.parse_args()
    data = pd.read_csv(args.data_path)
    print("[sheum] print data.shape\n")
    print(data.shape)

    print("[sheum] data.to_csv m_iris.csv\n")

    data.to_csv('/m_iris.csv', index=False)

#    time.sleep(1800) 
