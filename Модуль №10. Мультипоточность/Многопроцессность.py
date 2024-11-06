from time import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file.readline():
            if line is not None:
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_start = time()
# for file_name in filenames:
#    read_info(file_name)


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        reading_information = pool.map(read_info, filenames)

time_end = time()
time_res = time_end - time_start
print(time_res)
