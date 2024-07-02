import numpy as np
import torch
import sys

def load_target_jt(device, file, offset):
    one_target_jt = np.load(f"data/{file}", allow_pickle=True).astype(np.float32)
    one_target_jt = torch.from_numpy(one_target_jt).to(device)
    # target_jt = one_target_jt.unsqueeze(0)  # 在第一个纬度上增加一个纬度
    target_jt = one_target_jt + offset

    size = torch.tensor([one_target_jt.shape[0]]).to(device)
    # print(f"size:{size},shape:{target_jt.shape}")
    # sys.exit()
    return target_jt, size



