from torch.utils.data import Dataset
#用于打开图片
from PIL import Image
#用于获取图片列表
import os

class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        #获取label目录上的根目录路径
        self.root_dir = root_dir
        #获取label目录路径，label目录即图片的上一级目录
        self.label_dir = label_dir
        #用os库的join函数把根目录和label目录路径拼起来，好处是系统自动匹配地路径接符，不用人为处理（Linux系统与Windows系统的路径连接符不同）
        self.path = os.path.join(self.root_dir, self.label_dir)
        #用os库的listdir函数把label目录中的所有图片编成一个列表，得到每张图片的索引
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        #self其实是相当于一个全局变量的作用
        img_name = self.img_path[idx]
        #用os库的join函数把label目录路径与图片名拼起来就得到了每一张图片的路径
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        #用PIL的Image来打开、获取图片
        img = Image.open(img_item_path)
        #获取图片的label
        label = self.label_dir
        #这个函数需要返回图片和label
        return img, label

    def __len__(self):
        #返回列表长度（即图片数量）
        return len(self.img_path)

#先处理ants的dataset：输入ants的根目录路径
root_dir = "dataset/hymenoptera_data/train"
#输入ants的label目录路径（该目录即label名）
ants_label_dir = "ants"
#bees的操作也一样，不过因为根目录和ants的是一样的，所以不用额外写
bees_label_dir = "bees"
#把两个参数传入MyData函数，获取MyData的
ants_dataset= MyData(root_dir, ants_label_dir)
bees_dataset= MyData(root_dir, bees_label_dir)

#直接把两个数据集加起来就是整体的数据集
train_dataset = ants_dataset + bees_dataset