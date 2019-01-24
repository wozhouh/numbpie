def read_ganchooseFile(path_gan):

    choose_dic_1 = {
        1: 'sleeve_length:3/4',
        2: 'sleeve_length:long',
        3: 'sleeve_length:short',
        4: 'sleeve_length:sleeveless',
        5: 'fit:loose',
        6: 'fit:normal',
        7: 'fit:tight',
        8: 'neckline:round',
        9: 'neckline:v',
        10: 'neckline:wide',
        11: 'skip'
    }

    choose_dic_2 = {
        12: 'floral',
        13: 'stripes',
        14: 'skip',
    }

    choose_dic_3 = {
        14: 'add',
        15: 'remove'
    }

    import glob
    import os

    # path = '../../folder'
    str_gan = []

    for i in glob.glob(os.path.join(path_gan,'*.txt')):
        if i == path_gan+"/1.txt":
            f1 = open(i, 'r').readlines()[0]
            d = choose_dic_1[int(f1)]
            d_i = d.index(":")
            str_gan.append(d[d_i+1:])
            str_gan.append(d[:d_i])

        elif i == path_gan+"/2.txt":
            f2 = open(i, 'r').readlines()[0]
            d = choose_dic_2[int(f2)]
            str_gan.append(d)

        elif i == path_gan+"/3.txt":
            f3 = open(i, 'r').readlines()[0]
            d = choose_dic_3[int(f3)]
            str_gan.append(d)

    return str_gan[::-1]


if __name__ == "__main__":

    path_gan = "/Users/yangguofeng/Downloads/numbpie/11"
    a = read_ganchooseFile(path_gan)
    print(a)
