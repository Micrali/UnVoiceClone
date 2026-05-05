from concurrent.futures import ThreadPoolExecutor


def run_parallel(items, worker, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(worker, items))
