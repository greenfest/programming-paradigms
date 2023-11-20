function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);

    if (arr[mid] === target) {
      return mid; // Найден искомый элемент, возвращаем индекс
    } else if (arr[mid] < target) {
      low = mid + 1; // Искомый элемент находится в правой половине
    } else {
      high = mid - 1; // Искомый элемент находится в левой половине
    }
  }

  return -1; // Элемент не найден
}

// Пример использования
const sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const targetElement = 6;

const result = binarySearch(sortedArray, targetElement);

if (result !== -1) {
  console.log(`Элемент ${targetElement} найден по индексу ${result}.`);
} else {
  console.log(`Элемент ${targetElement} не найден в массиве.`);
}
