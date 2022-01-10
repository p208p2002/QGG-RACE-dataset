import gdown
import os
import wget
def download_from_gd(gid,save_name,save_dir = 'datasets'):
    os.makedirs(save_dir,exist_ok=True)
    gdown.download('https://drive.google.com/uc?id=%s'%(gid), os.path.join(save_dir,save_name), quiet=False)

if __name__ == "__main__":
    os.system('rm -rf datasets/')

    # RACE
    download_from_gd('1Lwhx5jhPGC-ekCn0E1wrOKJmX-AwTXuD','RACE.tar.gz')
    os.system('tar zxvf datasets/RACE.tar.gz')
    os.system('mv RACE datasets/')

    # EQG-RACE
    wget.download('https://github.com/jemmryx/EQG-RACE/raw/main/EQG-RACE.tar.gz','datasets/')
    os.system('tar zxvf datasets/EQG-RACE.tar.gz')
    os.system('mv key-race datasets/EQG-RACE')

    