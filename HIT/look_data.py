import h5py

def print_attrs(name, obj):
    """打印对象的属性"""
    print(f"\n #####{name}:")
    for key, value in obj.attrs.items():
        print(f"属性: {key} -> {value}")
def print_first_element(name, obj):
    """
    打印 HDF5 文件中的数据集的第一个数据
    """
    if isinstance(obj, h5py.Dataset):  # 检查对象是否为数据集
        print(f"Dataset: {name}")
        print(f"    First element: {obj[0]}")
# 打开 HDF5 文件（假设文件名为 'example.h5'）
file_name = 'HIT/public_datasets/data_fold_clothes/episode_00002.hdf5'

with h5py.File(file_name, 'r') as f:
    # 使用 visititems 方法遍历文件中的所有对象并打印属性
    f.visititems(print_first_element)
