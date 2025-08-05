import os
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")
print("Current working directory:", os.getcwd())
# writer.add_image()
# y = x
for i in range(100):
    writer.add_scalar("y = 2x", 2*i, i)

writer.close()
