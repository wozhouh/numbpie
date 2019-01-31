import os

def read_ganchooseFile(path_gan):

    c_d = os.path.join(path_gan, "checked.txt")
    lines = open(c_d, 'r').readlines()
    if len(lines)==0:
        return None
    if lines[0] == 'true':
        # path = '../../folder'
        str_gan = []
        f_d = os.path.join(path_gan,"feature.txt")
        t_d = os.path.join(path_gan,"texture.txt")
        a_d = os.path.join(path_gan,"action.txt")
        f1 = open(f_d, 'r').readlines()

        if len(f1) == 0 or "skip" in f1[0]:
            str_gan.append("")
            str_gan.append("")
        else:
            f1_split = f1[0].strip().split(':')
            str_gan.append(f1_split[0].strip().lower())
            str_gan.append(f1_split[1].strip().lower())
        f2 = open(t_d, 'r').readlines()
        if len(f2) == 0 or "skip" in f2[0]:
            str_gan.append("")
        else:
            str_gan.append(f2[0].strip().lower())
        f3 = open(a_d, 'r').readlines()
        if len(f3) == 0:
            str_gan[2] = ""
            str_gan.append("")
        else:
            str_gan.append(f3[0].strip().lower())
        return str_gan


if __name__ == "__main__":
    path_gan = "/Users/yangguofeng/Downloads/numbpie/static/gan"
    a = read_ganchooseFile(path_gan)
    print(a)