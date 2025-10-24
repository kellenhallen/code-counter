# code_counter.py

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total = len(lines)
    empty = len([l for l in lines if l.strip() == ''])
    comments = len([l for l in lines if l.strip().startswith('#')])

    print(f"Total lines: {total}")
    print(f"Empty lines: {empty}")
    print(f"Comment lines: {comments}")

if __name__ == "__main__":
    path = input("Enter file path: ")
    count_lines(path)
