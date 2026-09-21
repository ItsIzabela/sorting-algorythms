import tkinter as tk

class Sorting:
    def __init__(self, root, user_input):
        self.root = root
        tk.Label(self.root, text="Wpisz tablice do posortowania, oddzielajac liczby spacjami").pack(pady=5)
        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()
        self.array = []
        self.input_list = []
        self.result = ""

    def choose_array(self):
        input_string = self.user_input_entry.get()
        self.input_list = input_string.split(' ')
        self.array.clear()
        for item in self.input_list:
            if item:
                num = int(item)
                self.array.append(num)
        print(self.array)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n-1):
            for j in range(n-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        self.result.config(text=f"Posortowana tablica: \n {self.array}")

    def selection_sort(self):
        n = len(self.array)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = self.array[j]
            if min_index != i:
                self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        self.result.config(text=f"Posortowana tablica: \n {self.array}")

    def insertion_sort(self):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.array[j + 1] = key
        self.result.config(text=f"Posortowana tablica: \n {self.array}")

    def quick_sort(self):
        n = len(self.array)
        pivot = self.array[0]

        left = []
        right=[]

        for i in range(1, n):
            if pivot > self.array[i]:
                left.append(self.array[i])
            else:
                right.append(self.array[i])

        for j in range(0, len(left)-1):
            if left[j] > left[j+1]:
                left[j], left[j+1] = left[j+1], left[j]

        for k in range(0, len(right)-1):
            if right[k] > right[k+1]:
                right[k], right[k+1] = right[k+1], right[k]

        self.array.clear()
        self.array = left + [pivot] + right

        self.result.config(text=f"Posortowana tablica: \n {self.array}")

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.array[l] > self.array[largest]:
            largest = l
        
        if r < n and self.array[r] > self.array[largest]:
            largest = r
        
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(n, largest)

    def heap_sort(self):
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        
        for i in range(n - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heapify(i, 0)

        self.result.config(text=f"Posortowana tablica: \n {self.array}")

    def choose_sorting_method(self):
        submit_btn = tk.Button(self.root, text="Wczytaj tablice", command=self.choose_array)
        submit_btn.pack(pady=10)

        tk.Label(self.root, text="Wybierz metode sortowania:", foreground="black", font="Arial, 24").pack(pady=10)

        bubble_btn = tk.Button(self.root, text="Sortowanie bąbelkowe", command=self.bubble_sort)
        bubble_btn.pack(pady=5)

        selection_btn = tk.Button(self.root, text="Sortowanie poprzez wybieranie", command=self.selection_sort)
        selection_btn.pack(pady=5)

        insertion_btn = tk.Button(self.root, text="Sortowanie poprzez wstawianie", command=self.insertion_sort)
        insertion_btn.pack(pady=5)

        quick_btn = tk.Button(self.root, text="Sortowanie szybkie", command=self.quick_sort)
        quick_btn.pack(pady=5)

        heap_btn = tk.Button(self.root, text="Sortowanie heap", command=self.heap_sort)
        heap_btn.pack(pady=5)

        self.result = tk.Label(self.root, text=f"{self.array}", foreground="black", font="Arial 20")
        self.result.pack(pady=5)

    def run(self):
        self.choose_sorting_method()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Algorytmy Sortowania")
    app = Sorting(root, "")
    app.run()
