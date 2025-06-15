def duplicated(df):
    dup_records = df.duplicated().sum()
    return "Number of duplicated records: {}".format(dup_records)