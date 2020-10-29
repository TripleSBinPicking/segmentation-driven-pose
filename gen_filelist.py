import os
from os.path import join as opj

def collect_occluded_linemod_testlist(rootpath, outname):
    path = rootpath + 'RGB-D/rgb_noseg/'
    imgs = [f for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    imgs.sort()
    # write sets
    allf = open(outname, 'w')
    for i in imgs:
        allf.write(path + i +'\n')

def collect_ycb_testlist(testListFile, rootpath, outfile):

    print("root path is ", rootpath)
    with open(testListFile, 'r') as file:
        testlines = file.readlines()
    print("total file number", len(testlines))
    with open(outfile, 'w') as file:
        for l in testlines:
            file.write(opj(rootpath,l.rstrip()+'-color.png')+'\n')

if __name__ == '__main__':
    # modify the path according to your real path of the Occluded-LINEMOD and YCB-Video dataset
    occluded_linemod_path = './data/OcclusionChallengeICCV2015/'
    collect_occluded_linemod_testlist(occluded_linemod_path, './occluded-linemod-testlist.txt')