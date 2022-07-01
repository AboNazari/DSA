function binarySearch(list, target) {
    let midpoint;
    first = 0
    last = list.length - 1
    while (first <= last) {
        midpoint = Math.floor((first + last) / 2)
        if (list[midpoint] == target) {
            return midpoint
        } else if (list[midpoint] < target) {
            first = midpoint + 1
        } else if (list[midpoint] > target) {
            last = midpoint - 1
        }
    }
    return null
}

function verify(index) {
    if (index != null) {
        return console.log(`Target found in index:`, index)
    } else {
        return console.log("Target not found!")
    }
}


const list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
let index = binarySearch(list, 1)
verify(index)