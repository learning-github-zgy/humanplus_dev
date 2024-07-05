import numpy as np
import torch
import sys
from torch.nn.utils.rnn import pad_sequence


one_target_jt = np.load(f"data/amass_humanplus_data_10092.npy", allow_pickle=True)
target_jt_list = [torch.tensor(item) for item in one_target_jt]
# 打印每个张量的形状（长度）
one_target_jt = [torch.tensor(item).cuda() for item in one_target_jt]
padded_tensor = pad_sequence(one_target_jt, batch_first=True,padding_value=-100)
mask = padded_tensor > -99
print(f"{padded_tensor.shape}")
# 打印每个张量的形状（长度）
# padded_tensor.mask
selected_data = padded_tensor.masked_select(mask)
for idx, tensor in enumerate(selected_data):
    print(f"Tensor {idx} shape: {tensor.shape}")
sys.exit()