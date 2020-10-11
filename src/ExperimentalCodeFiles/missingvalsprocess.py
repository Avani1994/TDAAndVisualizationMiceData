# this is awesome :) :*
filepath = "../Mice_Dataset/S1_Dataset.xlsx"
    #mycolumns = "BU" # choose your columns (comma separated)

df = pd.read_excel(filepath, sheetname = 'successful, temp', skiprows=0)
thresh = 10000

a = df.index.values
b = df.m2.values

idx0 = np.flatnonzero(np.r_[True, np.diff(np.isnan(b))!=0,True])
count = np.diff(idx0)
idx = idx0[:-1]
valid_mask = (count>=thresh) & np.isnan(b[idx])
out_idx = idx[valid_mask]
out_num = a[out_idx]
out_count = count[valid_mask]
out = zip(out_num, out_count)