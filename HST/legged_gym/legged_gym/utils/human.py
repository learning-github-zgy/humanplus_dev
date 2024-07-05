import numpy as np
import torch
import sys
from torch.nn.utils.rnn import pad_sequence

def load_target_jt(device, file, offset):
    one_target_jt = np.load(f"data/{file}", allow_pickle=True)
    #  gpu上的 tensor 不能直接转为 numpy； 须要先在 cpu 上完成操做，再回到 gpu 上
    one_target_jt = [torch.tensor(item).to(device) for item in one_target_jt]
    # size = torch.tensor([one_target_jt.shape[0]]).to(device)
    size = torch.zeros(len(one_target_jt)).to(device) # size存储每个动作序列的真实长度
    for i in range (len(one_target_jt)):
        size[i] = one_target_jt[i].shape[0]
        # print(size[i])
    padded_tensor = pad_sequence(one_target_jt, batch_first=True) # 将不同长度的动作序列填充到相同长度
    padded_tensor += offset
    return padded_tensor, size



