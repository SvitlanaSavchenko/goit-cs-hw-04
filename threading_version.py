import threading
import time

# Функція для пошуку ключових слів у файлі
def search_in_file(file_path, keywords, results):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in results:
                        results[keyword] = []
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Основна функція для запуску потоків
def search_in_files_threading(files, keywords):
    threads = []
    results = {}
    for file_path in files:
        thread = threading.Thread(target=search_in_file, args=(file_path, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

# Приклад використання
if __name__ == "__main__":
    keywords = ['python', 'java']
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    
    # Вимірювання часу виконання
    start_time = time.time()
    result_threading = search_in_files_threading(files, keywords)
    print("Threading Result:", result_threading)
    print("Threading Time:", time.time() - start_time)
