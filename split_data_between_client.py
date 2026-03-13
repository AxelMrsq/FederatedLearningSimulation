import splitfolders
import os

splitfolders.ratio("./working_dataset/all/", output="./working_dataset/FL_split/", seed=1337, ratio=(.5, .5, .0), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

os.rename("./working_dataset/FL_split/train", "./working_dataset/FL_split/client_1_all")

os.rename("./working_dataset/FL_split/val", "./working_dataset/FL_split/client_2_all")

splitfolders.ratio("./working_dataset/FL_split/client_1_all/", output="./working_dataset/FL_split/client_1_split_sets/", seed=1337, ratio=(.3, .3, .4), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

splitfolders.ratio("./working_dataset/FL_split/client_2_all/", output="./working_dataset/FL_split/client_2_split_sets/", seed=1337, ratio=(.2, .5, .3), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

os.rename("./working_dataset/FL_split/client_1_split_sets/train", "./working_dataset/FL_split/client_1_split_sets/set_1")

os.rename("./working_dataset/FL_split/client_1_split_sets/val", "./working_dataset/FL_split/client_1_split_sets/set_2")

os.rename("./working_dataset/FL_split/client_1_split_sets/test", "./working_dataset/FL_split/client_1_split_sets/set_3")

os.rename("./working_dataset/FL_split/client_2_split_sets/train", "./working_dataset/FL_split/client_2_split_sets/set_1")

os.rename("./working_dataset/FL_split/client_2_split_sets/val", "./working_dataset/FL_split/client_2_split_sets/set_2")

os.rename("./working_dataset/FL_split/client_2_split_sets/test", "./working_dataset/FL_split/client_2_split_sets/set_3")

splitfolders.ratio("./working_dataset/FL_split/client_1_split_sets/set_1", output="./working_dataset/FL_split/client_1_split_sets/set_1_split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

splitfolders.ratio("./working_dataset/FL_split/client_1_split_sets/set_2", output="./working_dataset/FL_split/client_1_split_sets/set_2_split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

splitfolders.ratio("./working_dataset/FL_split/client_1_split_sets/set_3", output="./working_dataset/FL_split/client_1_split_sets/set_3_split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

splitfolders.ratio("./working_dataset/FL_split/client_2_split_sets/set_1", output="./working_dataset/FL_split/client_2_split_sets/set_1_split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

splitfolders.ratio("./working_dataset/FL_split/client_2_split_sets/set_2", output="./working_dataset/FL_split/client_2_split_sets/set_2_split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)

splitfolders.ratio("./working_dataset/FL_split/client_2_split_sets/set_3", output="./working_dataset/FL_split/client_2_split_sets/set_3_split/", seed=1337, ratio=(.8, .1, .1), group_prefix=None, group=None, formats=None, move=False, shuffle=True)
