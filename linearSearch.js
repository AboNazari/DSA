function linearSearch(list, target) {
  for (i in list) {
    if (list[i] == target) {
      return i;
    }
  }
  return -1;
}

function verify(index) {
  if (index != -1) {
    console.log("Target Found at: " + index);
  } else {
    console.log("Target Not Found");
  }
}

const list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let index = linearSearch(list, 5);
verify(index);

index = linearSearch(list, 4);
verify(index);
