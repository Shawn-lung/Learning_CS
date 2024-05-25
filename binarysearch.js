function binarySearch(arr,target){
    let left = 0
    let right = arr.length - 1;
    while (left <= right){
        let mid = Math.floor ((left + right)/2);
        if (arr[mid] === target){
            return mid;
        }
        else if (arr[mid] < target){
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }   
    }
    return -1;
}
let arr = [2, 3, 4, 10, 40];
let target = 10;
let result = binarySearch(arr,target);

if (result != -1)
    console.log("Element is present at index " + result);
else
    console.log("Element is not present in array");