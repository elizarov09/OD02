from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

# Пример: управление задачами печати
class PrinterQueue:
    def __init__(self):
        self.print_queue = Queue()

    def add_job(self, job):
        self.print_queue.enqueue(job)
        print(f"Добавлена задача на печать: {job}")

    def process_jobs(self):
        while not self.print_queue.is_empty():
            job = self.print_queue.dequeue()
            print(f"Печать задачи: {job}")

# Использование очереди принтера
printer = PrinterQueue()
printer.add_job("Документ1.pdf")
printer.add_job("Документ2.docx")
printer.add_job("Документ3.jpg")

printer.process_jobs()
# Вывод:
# Добавлена задача на печать: Документ1.pdf
# Добавлена задача на печать: Документ2.docx
# Добавлена задача на печать: Документ3.jpg
# Печать задачи: Документ1.pdf
# Печать задачи: Документ2.docx
# Печать задачи: Документ3.jpg
