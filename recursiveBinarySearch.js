function recursiveBinarySearch(list, target) {
    console.log(list.length)
    if (list.length === 0) {
        return false
    } else {
        let midpoint = Math.floor(list.length / 2)
        if (list[midpoint] == target) {
            return true
        } else {
            if (list[midpoint] < target) {
                recursiveBinarySearch(list.slice(midpoint + 1), target)
            } else {
                recursiveBinarySearch(list.slice(0, midpoint), target)
            }
        }
    }
}



function verify(index) {
    if (index == true) {
        console.log("Target Found")
    } else {
        console.log("Target Not found!")
    }
}

const list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
let index = recursiveBinarySearch(list, 6)
verify(index)




// The Code from this Article: https://medium.com/jsunderthescope/a-recursive-binary-search-in-javascript-b29efaff64d6

var binarySearch = function (array, target, min, max) {
    if (min === undefined) min = 0;
    if (max === undefined) max = array.length - 1;

    var guess = Math.floor(((max - min) / 2) + min);
    if (max <= min && array[guess] !== target) return null;
    else if (array[guess] === target) return guess;
    else if (array[guess] < target) return binarySearch(array, target, guess + 1, max);
    else return binarySearch(array, target, min, guess - 1);
};