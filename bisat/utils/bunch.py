import scipy.io
import pandas as pd
import os

def csv_reader(dir):
    datalist = []
    f = open(dir, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        datalist.append(int(str(line)[2]))
    f.close()
    return datalist
        
def search(dir):
        file_list = []
        files = os.listdir(dir)
        for file in files:
                # print(file)
                file_list.append(file)
        return file_list
    
def filetype_selector(file_list,file_type):
    selected_list = []
    for i in(range(len(file_list))):
        filename = file_list[i]
        if filename[-3:] == file_type:
            selected_list.append(filename)
    return selected_list

def list_to_csv(target_list,filename):
    with open(filename+'.csv','w',newline = '') as file:
        writer = csv.writer(file)
        for i in range(len(target_list)):
            writer.writerow(target_list[i])

# Need to Update for target specific dir (set current location as default)
def mat2csv(filename,data):
    ori_data = scipy.io.loadmat(data)
    hyp=ori_data['hyp']
    xx=ori_data['xx']
    dfhyp = pd.DataFrame(hyp)
    dfxx = pd.DataFrame(xx)
    dfhyp.to_csv("./hyp/"+filename+".csv",header=False,index=False)
    dfxx.to_csv("./xx/"+filename+".csv",header=False,index=False)


# Need to Update for target specific dir (set current location as default)
def csv2npz_xx(filename,data):
    xx = np.loadtxt(data,delimiter=',',dtype=np.float32)
    np.savez("./xx_npz/"+filename+".npz",xx=xx) 

# Need to Update for target specific dir (set current location as default)

def csv2npz_hyp(filename,data):
    hyp = np.loadtxt(data,delimiter=',',dtype=np.float32)
    np.savez("./hyp_npz/"+filename+".npz",hyp=hyp) 