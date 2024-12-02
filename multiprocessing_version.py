import multiprocessing
import time

# Функція для пошуку ключових слів у файлі
def search_in_file(file_path, keywords, queue):
    result = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in result:
                        result[keyword] = []
                    result[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    queue.put(result)

# Основна функція для запуску процесів
def search_in_files_multiprocessing(files, keywords):
    queue = multiprocessing.Queue()
    processes = []
    for file_path in files:
        process = multiprocessing.Process(target=search_in_file, args=(file_path, keywords, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = {}
    while not queue.empty():
        result = queue.get()
        for keyword, paths in result.items():
            if keyword not in results:
                results[keyword] = []
            results[keyword].extend(paths)

    return results

# Приклад використання
if __name__ == "__main__":
    keywords = ['python', 'java']
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    
    # Вимірювання часу виконання
    start_time = time.time()
    result_multiprocessing = search_in_files_multiprocessing(files, keywords)
    print("Multiprocessing Result:", result_multiprocessing)
    print("Multiprocessing Time:", time.time() - start_time)
