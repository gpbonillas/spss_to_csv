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

if __name__ == '__main__':
    convert_to_csv()
