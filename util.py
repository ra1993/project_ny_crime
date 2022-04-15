#utility functions
outpath = ""

def write_2_csv(df, out_path):
    return df.write.save(out_path, format = "csv", header = True)

