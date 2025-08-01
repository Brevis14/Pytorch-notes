import os

root_dir = "dataset/hymenoptera_data/train"
target_dir = "ants_image" #If you need to process the bees dataset, change "ants" to "bees".
img_path = os.listdir(os.path.join(root_dir, target_dir))
label = target_dir.split("_")[0]
out_dir = "ants_label" #If you need to process the bees dataset, change "ants" to "bees".
for i in img_path:
    file_name = i.split(".")[0]
    with open(os.path.join(root_dir, out_dir, "{}.txt".format(file_name)), 'w') as f:
        f.write(label)