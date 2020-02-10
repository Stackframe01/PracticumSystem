import sys
import requests
from tqdm import tqdm
import pdfminer.high_level

def get_standarts():
    standarts = sys.stdout
    with open('professional_standarts/data/raw_data/06.003.pdf', 'rb') as file:
        pdfminer.high_level.extract_text_to_fp(file, standarts)

    return standarts

def to_csv(file_name, data):
    with open('data/{}.csv'.format(file_name), 'w') as f_out:
        f_out.write(';Required skill\n')
        for i in range(len(data)):
            f_out.write('{};{}\n'.format(i, data[i]))
        f_out.close()

if __name__ == "__main__":
    pass