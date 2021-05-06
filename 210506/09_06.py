import multiprocessing as multiprocessing
if __name__ == "__main__":
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)