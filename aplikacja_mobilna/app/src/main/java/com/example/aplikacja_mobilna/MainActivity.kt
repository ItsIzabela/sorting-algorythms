package com.example.aplikacja_mobilna

import android.content.Context
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.Divider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.example.aplikacja_mobilna.ui.theme.Aplikacja_mobilnaTheme
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import androidx.compose.foundation.layout.Row

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Aplikacja_mobilnaTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    AppContent(modifier = Modifier.padding(innerPadding))
                }
            }
        }
    }
}

@Composable
fun AppContent(modifier: Modifier = Modifier) {
    var arrayInput by remember { mutableStateOf("") }
    var arrayList by remember { mutableStateOf(mutableListOf<Double>()) }
    var arrayError by remember { mutableStateOf<String?>(null) }

    fun parseInputToMutableList(input: String): MutableList<Double> {
        return input.split(",")
            .mapNotNull { it.trim().toDoubleOrNull() }
            .toMutableList()
    }

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = "Algorytmy Sortowania",
            style = MaterialTheme.typography.headlineMedium,
            fontWeight = FontWeight.Bold
        )

        OutlinedTextField(
            value = arrayInput,
            onValueChange = { input ->
                val sanitized = input.replace(" ", "")
                val regex = Regex("""^(-?\d*\.?\d+,)*(-?\d*\.?\d+)?$""")
                arrayInput = input
                arrayError = if (sanitized.isEmpty() || regex.matches(sanitized)) null
                else "Liczby powinny być oddzielone przecinkami i mogą być ujemne!"
            },
            label = { Text("Wpisz liczby oddzielajac je przecinkami") },
            isError = arrayError != null,
            supportingText = { arrayError?.let { Text(it) } },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(16.dp))

        Button(
            onClick = {
                arrayList = parseInputToMutableList(arrayInput)
            }
        ) {
            Text("Konwertuj na listę")
        }

        Spacer(modifier = Modifier.height(16.dp))

        LazyRow(modifier = Modifier.fillMaxWidth()) {
            items(arrayList) { number ->
                Text(text = number.toString(), modifier = Modifier.padding(8.dp))
            }
        }

        Spacer(modifier = Modifier.height(16.dp))

        Button(
            onClick = {
                arrayList = parseInputToMutableList(arrayInput)
                val n = arrayList.size
                for (i in 0 until n) {
                    for (j in 0 until n - i - 1) {
                        if (arrayList[j] > arrayList[j + 1]) {
                            val temp = arrayList[j]
                            arrayList[j] = arrayList[j + 1]
                            arrayList[j + 1] = temp
                        }
                    }
                }
            }
        ) {
            Text("Sortowanie bąbelkowe")
        }

        Button(
            onClick = {
                arrayList = parseInputToMutableList(arrayInput)
                val n = arrayList.size
                for (i in 0 until n - 1) {
                    var min_index = i
                    for (j in i + 1 until n) {
                        if (arrayList[j] < arrayList[min_index]) {
                            min_index = j
                        }
                    }
                    if (min_index != i) {
                        val temp = arrayList[i]
                        arrayList[i] = arrayList[min_index]
                        arrayList[min_index] = temp
                    }
                }
            }
        ) {
            Text("Sortowanie poprzez wybieranie") // Selection Sort
        }


        Button(
            onClick = {
                arrayList = parseInputToMutableList(arrayInput)
                for (i in 0 until arrayList.size) {
                    val key = arrayList[i]
                    var j = i - 1
                    while (j >= 0 && arrayList[j] > key) {
                        arrayList[j + 1] = arrayList[j]
                        j--
                    }
                    arrayList[j + 1] = key
                }
            }
        ) {
            Text("Sortowanie poprzez wstawianie")
        }

        Button(
            onClick = {
                arrayList = parseInputToMutableList(arrayInput)

                val pivot = arrayList[0]
                val left = mutableListOf<Double>()
                val right = mutableListOf<Double>()

                for (i in 1 until arrayList.size) {
                    if (arrayList[i] < pivot) {
                        left.add(arrayList[i])
                    } else {
                        right.add(arrayList[i])
                    }
                }

                for (j in 0 until left.size - 1) {
                    for (k in 0 until left.size - j - 1) {
                        if (left[k] > left[k + 1]) {
                            val temp = left[k]
                            left[k] = left[k + 1]
                            left[k + 1] = temp
                        }
                    }
                }

                for (j in 0 until right.size - 1) {
                    for (k in 0 until right.size - j - 1) {
                        if (right[k] > right[k + 1]) {
                            val temp = right[k]
                            right[k] = right[k + 1]
                            right[k + 1] = temp
                        }
                    }
                }

                arrayList = (left + pivot + right).toMutableList()
            }
        ) {
            Text("Sortowanie szybkie")
        }

        Button(
            onClick = {
                arrayList = parseInputToMutableList(arrayInput)

                fun heapify(array: MutableList<Double>, n: Int, i: Int) {
                    var largest = i
                    val l = 2 * i + 1
                    val r = 2 * i + 2

                    if (l < n && array[l] > array[largest]) {
                        largest = l
                    }
                    if (r < n && array[r] > array[largest]) {
                        largest = r
                    }
                    if (largest != i) {
                        val temp = array[i]
                        array[i] = array[largest]
                        array[largest] = temp
                        heapify(array, n, largest)
                    }
                }

                fun heapSort(array: MutableList<Double>) {
                    val n = array.size
                    for (i in n / 2 - 1 downTo 0) {
                        heapify(array, n, i)
                    }
                    for (i in n - 1 downTo 1) {
                        val temp = array[0]
                        array[0] = array[i]
                        array[i] = temp
                        heapify(array, i, 0)
                    }
                }

                heapSort(arrayList)
            }
        ) {
            Text("Sortowanie heap")
        }

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = "Wynik sortowania:",
            style = MaterialTheme.typography.headlineMedium,
            fontWeight = FontWeight.Bold
        )

        Spacer(modifier = Modifier.height(16.dp))

        LazyColumn(modifier = Modifier.fillMaxWidth()) {
            items(arrayList) { number ->
                Text(text = number.toString(), modifier = Modifier.padding(8.dp))
            }
        }
    }
}


