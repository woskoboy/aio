from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prev_lines in search(f, 'python', 5):
            for p_line in prev_lines:
                print(p_line, end='')
            print(line, end='')
            print('-'*20)
