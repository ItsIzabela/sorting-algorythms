from colorama import Fore, Back, Style

class Sorting:
    def __init__(self, user_input, array):
        self.user_input = user_input
        self.array = array
        self.input_list = []
        self.min = 0 # selection sort
        self.pivot = 0 # quick sort
        self.largest = 0 # heap sort
        self.l = 0
        self.r = 0

    def choose_array(self):
        print(Fore.GREEN + "---")
        self.user_input = input("Wprowadz tablice do posortowania oddzielajac liczby spacjami: ")
        self.input_list = self.user_input.split(' ')
        self.array.clear()
        for item in self.input_list:
            num = int(item)
            self.array.append(num)
        

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

    def selection_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            if min_index != i:
                self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        return self.array

    def insertion_sort(self):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        return self.array

    def quick_sort(self):
        n = len(self.array)
        self.pivot = self.array[0]  

        left = []
        right = []

        for i in range(1, n):  
            if self.pivot > self.array[i]:
                left.append(self.array[i])
            else:
                right.append(self.array[i])

        for j in range(0, len(left) - 1):  
            if left[j] > left[j+1]:
                left[j], left[j+1] = left[j+1], left[j]

        for k in range(0, len(right) - 1):
            if right[k] > right[k+1]:
                right[k], right[k+1] = right[k+1], right[k]

        self.array.clear()
        self.array = left + [self.pivot] + right
        return self.array

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

        return self.array

    def choose_sorting_method(self):
        print(Fore.GREEN + "---")
        print("Wybierz metode sortowania:")
        print("1. Sortowanie bąbelkowe")
        print("2. Sortowanie poprzez wybieranie")
        print("3. Sortowanie przez wstawianie")
        print("4. Sortowanie szybkie")
        print("5. Sortowanie Heap")
        print(Fore.GREEN + "---")


if __name__ == '__main__':
    app = Sorting("", [])
    app.choose_array()
    app.choose_sorting_method()
    choice = int(input("Wybierz metode sortowania (1 do 5):"))
    if choice == 1:
        sorted_array = app.bubble_sort()
    elif choice == 2:
        sorted_array = app.selection_sort()
    elif choice == 3:
        sorted_array = app.insertion_sort()
    elif choice == 4:
        sorted_array = app.quick_sort()
    elif choice == 5:
        sorted_array = app.heap_sort()
    print("Posortowana tablica:", sorted_array)
