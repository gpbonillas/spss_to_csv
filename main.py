from spss_converter import read, write
import pandas as pd
import pyreadstat

def convert_to_csv():
    fpath = "ATPW64.sav"
    outpath = "ATPW64.csv"

    reader = pyreadstat.read_file_in_chunks(pyreadstat.read_sav, fpath, chunksize=1000, apply_value_formats=True)

    cnt = 0
    for df, meta in reader:
        # if on the first iteration write otherwise append
        if cnt > 0:
            wmode = "a"
            header = False
        else:
            wmode = "w"
            header = True
        # write
        df.to_csv(outpath, mode=wmode, header=header)
        cnt += 1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    convert_to_csv()
