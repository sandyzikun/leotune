import zhconv
with open("./i.txt", "r") as fl:
    txt_raw = fl.readlines()
    fl.close()
txt_new = []
for k in range(len(txt_raw)):
    if k % 2:
        txt_new.append(zhconv.convert(txt_raw[k], "zh-hk"))
    else:
        txt_new.append(txt_raw[k])
with open("./o.txt", "w+") as fl:
    fl.writelines(txt_new[ :: 2 ])
    fl.write("\n-***-\n\n")
    fl.writelines(txt_new[ 1 :: 2 ])
    fl.close()