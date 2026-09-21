import React, { useState } from 'react'
import { BubbleSort } from './assets/components/bubble_sort.js'
import { HeapSort } from './assets/components/heap_sort.js'
import { InsertionSort } from './assets/components/insertion_sort.js'
import { QuickSort } from './assets/components/quick_sort.js'
import { SelectionSort } from './assets/components/selection_sort.js'

export default function App() {
  const [array, setArray] = useState([5, 3, 8, 4, 2])
  const [sortedArray, setSortedArray] = useState([])

  const [inputValue, setInputValue] = useState(array.join(' '))

  const handleInputChange = (e) => {
    const value = e.target.value
    setInputValue(value)

    const parsedArray = value
      .trim()
      .split(/\s+/)
      .map(numStr => Number(numStr))
      .filter(num => !isNaN(num))

    setArray(parsedArray)
    setSortedArray([])
  }

  const handleBubbleSort = () => {
    const result = BubbleSort(array)
    setSortedArray(result)
  }

  const handleHeapSort = () => {
    const result = HeapSort(array)
    setSortedArray(result)
  }

  const handleInsertionSort = () => {
    const result = InsertionSort(array)
    setSortedArray(result)
  }

  const handleQuicksort = () => {
    const result = QuickSort(array)
    setSortedArray(result)
  }

  const handleSelectionSort = () => {
    const result = SelectionSort(array)
    setSortedArray(result)
  }

  return (
    <>
      <h1>Algorytmy Sortowania</h1>
      <input
        type="text"
        name="array"
        id="array"
        value={inputValue}
        onChange={handleInputChange}
        placeholder="Wpisz liczby oddzielone spacją"
      />  
      <div id='buttons'>
        <button onClick={handleBubbleSort}>Sortowanie bąbelkowe</button>
        <button onClick={handleHeapSort}>Sortowanie heap</button>
        <button onClick={handleInsertionSort}>Sortowanie poprzez wstawianie</button>
        <button onClick={handleQuicksort}>Sortowanie szybkie</button>
        <button onClick={handleSelectionSort}>Sortowanie poprzez wybieranie</button>
      </div>
      <div id='results'>
        <p>Oryginalna tablica: {array.join(', ')}</p>
        <p>Posortowana tablica: {sortedArray.join(', ')}</p>
      </div>
    </>
  )
}
