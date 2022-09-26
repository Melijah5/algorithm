#javascript code here!

//					 challenge 1
//****************************************************************************************************************** */

// 1. Given an array that contains exactly 1 duplicate number. find that duplicate.

//     given: -[5, 1, 4, 3, 1, 2]
//     output: -[1]

//****************************************************************************************************************** */
					//Using two pointers (nested loop)
//****************************************************************************************************************** */
function findDup(arr) {
    output = []
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] == arr[j]) {
                output.push(arr[i])
            }
        }
    }
    console.log(output)

}

// findDup([5, 1, 4, 3, 1, 2, 3])


// Time complexity - O(n2)
//Space Complexity - O(1)

//****************************************************************************************************************** */
						//sort
//****************************************************************************************************************** */

// first sort the Array
// then compare with the adjacent element

function findDup1(arr) {
    let sortArr = arr.sort()
    let dup = [];
    for (let i = 0; i < sortArr.length; i++) {
        if (arr[i] == arr[i + 1]) {
            dup.push(arr[i])
        }
    }
    console.log(dup)

}
// findDup1([5, 1, 4, 3, 1, 2, 3])

// Time complexity - O(nlogn)
//Space Complexity - O(n)

//****************************************************************************************************************** */
						//Hashmap
//****************************************************************************************************************** */

// key value
// 5   1
// 1   1   --1
// 4   1
// 3   1   --1
// 2   1

function findDup2(arr) {
    let Hashmap = new Map()
    for (let i = 0; i < arr.length; i++) {
        if (!Hashmap.has(i)) {
            Hashmap.set(i, 1)
        } else {
            Hashmap.set(i, Hashmap.get(i) + 1)
        }
    }
    for (let i = 0; i < Hashmap.has(); i++) {
        if (Hashmap.get(i > 1)) {
            console.log(i)
        }

    }


}
console.log(findDup2([5, 1, 4, 3, 1, 2, 3]))


//****************************************************************************************************************** */

// arr = [5, 1, 4, 3, 1, 2, 3]

// result= []
// i=0
// value = Abs(5) = 5
// index = 5 - 1 = 4
// arr[4] <0 ? No
// arr[4] *= -1


// function findDup3(arr) {
//     let result = [];
//     for (let i = 0; i < arr.length; i++) {
//         let value = Math.abs(arr[i]);
//         let index = value - 1
//         if (arr[index] < 0) {
//             result.push(value)
//         } else {
//             arr[index] *= -1
//         }

//     }
//     return result

// }

// console.log(findDup3([5, 1, 4, 3, 1, 2, 3]))

//****************************************************************************************************************** */
//****************************************************************************************************************** */
// 2. reverse the whole string ?
//     I / p = "I love icecream"
// O / p = "maerceci evol I"
//****************************************************************************************************************** */
//						//loop from the end
//****************************************************************************************************************** */

function reverseString(str) {
    let reverse = ""
    for (let i = str.length - 1; i >= 0; i--) {
        reverse = reverse + str[i]

    }
    console.log(reverse)

}

reverseString("I love icecream")

// Time complexity - O(n)
//Space Complexity - O(1)

//****************************************************************************************************************** */
						// recursion 
//****************************************************************************************************************** */
function reverseString(str) {
    if (str === "")
        return "";
    else
        return reverseString(str.substr(1)) + str.charAt(0);
}
console.log(reverseString("hello"))































# python code below!

# bubble sort
# sort the array in ascending orders
arr =[8,9,4,7,25,1,5,2,1,4,6]

def bubblesort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1]= arr[i+1],arr[i]
    return arr
print(bubblesort(arr))




# selection sort -  A sort algorithm that repeatedly searches remaining items to find the least one and moves it to its final location. The run time is Θ(n²),
# where n is the number of elements. The number of swaps is O(n).

arr =[9,2,3,6,7,85,4,2,5]

def selectionsort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i+1, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value],arr[i]
    return arr
print(selectionsort(arr))


# final countdown
# just like flexible countdown, add an extra parameter so that if mult is equal to para4, skip that number using a while loop
def final_countdown(mult,low, high, para4):
    while low < high:
        low = low + 1
        if low % mult == 0 and low != para4:
            print low
            
            
# first plus length
# given and array, return the sum of the first value in the array plus the arrays length.
# what happens if the array's first value is not a number but a string or boolean.
def first_plus_length(list):
    if type(list[0]) is int:
        sum = list[0] + len(list)
    elif type(list[0]) is str:
        sum = "First value of list is a String"
    elif type(list[0]) is bool:
        sum = "First value of list is a Boolean"
    else:
        sum = "idonno what it is?"
    return sum


#if 2 given number represent your birth month and day in either order, log "how did you know?", else log "Just another day..."
def log_day(num1, num2):
    if num1 == 5 and num2 == 6:
        print ("how did you know?")
    elif num1 == 6 and num2 == 5:
        print ("how did you know?")
    else:
        print("Just another day ...")
        
# Get a string made of its first three characters of a specified string
def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))


# ******************
# ---------- 'aaabbcccddbbee' => a3b2c3d2b2e2

def encode(str):
    output= '',
    count=1,
    char = str[0]
    for i in range(len(str)):
        if char ==str[i]:
            count++
        else if
            char != str[i] || i == len(str):
            output += char + count;
            count =1;
            char = str[i];
        }
    return output
}

# bubble_sort([0, 5, 2, 3, 2,6])
#     [0, 2, 2, 3, 5,6]
	
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection




