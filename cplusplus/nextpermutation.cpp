// A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

// For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
// The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

// For example, the next permutation of arr = [1,2,3] is [1,3,2].
// Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
// While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
// Given an array of integers nums, find the next permutation of nums.

// Example 1:

// Input: nums = [1,2,3]
// Output: [1,3,2]
// Example 2:

// Input: nums = [3,2,1]
// Output: [1,2,3]
// Example 3:

// Input: nums = [1,1,5]
// Output: [1,5,1]
 

// Constraints:

// 1 <= nums.length <= 100
// 0 <= nums[i] <= 100

// largest permutation is ints sorted greatest to least
// smallest permutation is ints sorted least to greatest
// progress upward is made by progressively moving small ints down the list
// solve base cases, then call on subarrays
// if the subarray you are looking at is already ordered greatest to least, look to the digit on the left of subarray

#include <vector>
#include <algorithm>
#include <assert.h>
#include <iostream>
using namespace std;

#define PRINT_DEBUG true

class Solution {
    public:       
        // returns index of next highest value in the subarray if it exists, else returns -1
        int find_index_of_next_greater_val(vector<int>& nums, const int target_value, const int search_start_index, const int search_end_index) {
            int return_index = -1;
            int curr_search_value = INT_MAX;
            for(int index=search_start_index; index <= search_end_index; index++){
                if(nums.at(index) > target_value && nums.at(index) < curr_search_value) {
                    return_index = index;
                    curr_search_value = nums.at(index);
                } else if (nums.at(index) <= target_value) {
                    // if we have gotten to this point in the process, we know this subarray is sorted
                    // from greatest to least, so we know we won't find a new viable value.
                    break;
                }
            }
            return return_index;
        }
        void swap_vec_elems(vector<int>& nums, int index_a, int index_b){
            const int temp_a = nums.at(index_a);
            nums.at(index_a) = nums.at(index_b);
            nums.at(index_b) = temp_a;
        }
        // SLOW AND REPLACED - simple bubble sort least to greatest
        void bubble_sort_subarray(vector<int>& nums, int start, int end){
            bool sorted = false;
            while(sorted == false){
                sorted = true;
                for(int index = start; index < end; index++){
                    if(nums.at(index) > nums.at(index + 1)) {
                        sorted = false;
                        swap_vec_elems(nums, index, index + 1);
                    }
                }
            }
        }
        // Sort subarray with (quicksort?). Ideally it is an in-place algo whatever it is.
        void sort_subarray(vector<int>& nums, int start, int end) {
            sort(nums.begin() + start, nums.begin() + end + 1);
        }
        // returns "true" if next permutation was found in this subarray, level of recursion
        bool nextPermRecursive(vector<int>& nums, int start, int end){
            switch ((end+1) - start) {
                case 0:
                    return false;
                case 1:
                    return false;
                case 2:
                    if ( nums.at(start) < nums.at(end) ) {
                        swap_vec_elems(nums, start, end);
                        return true;
                    }
                    return false;
                default:
                    // shrink the subarray in search of next permutation
                    const bool next_perm_found = nextPermRecursive(nums, start + 1, end);
                    if(next_perm_found){return true;}

                    // search for next higher number in right subarray if it exists
                    const int next_higher_value_index = find_index_of_next_greater_val(nums, nums.at(start), start + 1, end);
                    
                    if ( next_higher_value_index != -1 ){
                        // swap with next highest number in subarray
                        swap_vec_elems(nums, next_higher_value_index, start);
                        // sort the new subarray from smallest to largest
                        sort_subarray(nums, start + 1, end);
                        return true;
                    } else if (start == 0) {
                        // this is the highest possible permutation, start back at the beginning by sorting the array
                        sort_subarray(nums, 0, nums.size() - 1);
                        return true;
                    }
                    // a next perm was not found at this level, but higher levels can still be checked
                    return false;
            }
            
            // this is the highest permutation possible, generate lowest permutation from entire vector
            sort_subarray(nums, 0, nums.size() - 1);
            return true;
        }
        void nextPermutation(vector<int>& nums) {
            nextPermRecursive(nums, 0, nums.size() - 1);
        }
};

void test_solution(vector<int>& test_vec, vector<int> answer_vec){
    Solution sol; // OOP is fun
    vector<int>::iterator ptr;
    
    if(PRINT_DEBUG){ cout << "\nINPUT VECTOR: "; }
    if(PRINT_DEBUG){ for(ptr = test_vec.begin(); ptr < test_vec.end(); ptr++){cout << *ptr;} }
    
    sol.nextPermutation(test_vec); // OOP is really fun
    
    if(PRINT_DEBUG){ cout << "\nOUTPUT VECTOR: "; }
    if(PRINT_DEBUG){ for(ptr = test_vec.begin(); ptr < test_vec.end(); ptr++){cout << *ptr;} }
    if(PRINT_DEBUG){ cout << endl; }

    assert(test_vec == answer_vec);
}

void test_suite(){
    vector<int> test_one{ 1, 2, 3 };
    vector<int> test_one_ans{ 1, 3, 2 };
    test_solution(test_one, test_one_ans);

    vector<int> test_two{ 3, 2, 1 };
    vector<int> test_two_ans{ 1, 2, 3 };
    test_solution(test_two, test_two_ans);

    vector<int> test_three{ 3, 1, 2 };
    vector<int> test_three_ans{ 3, 2, 1 };
    test_solution(test_three, test_three_ans);

    vector<int> test_four{ 1, 3, 2 };
    vector<int> test_four_ans{ 2, 1, 3 };
    test_solution(test_four, test_four_ans);

    vector<int> test_five{ 2, 1, 3 };
    vector<int> test_five_ans{ 2, 3, 1 };
    test_solution(test_five, test_five_ans);

    vector<int> test_six{ 2, 3, 1 };
    vector<int> test_six_ans{ 3, 1, 2 };
    test_solution(test_six, test_six_ans);

    vector<int> test_eight{ 5, 4, 3, 2, 1 };
    vector<int> test_eight_ans{ 1, 2, 3, 4, 5 };
    test_solution(test_eight, test_eight_ans);

    vector<int> test_seven{ 5, 4, 7, 5, 3, 2 };
    vector<int> test_seven_ans{ 5, 5, 2, 3, 4, 7 };
    test_solution(test_seven, test_seven_ans);
}

int main(){
    test_suite();
    return 1;
}