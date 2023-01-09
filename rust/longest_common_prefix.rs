// in an implementation with a lot of values, sort by length first

// can be made faster by implementing early breaking the loop that check for length of substring
// doesn't matter if the following words share a longer substring, so you can break early if it
// is as long as the shortest common prefix you've seen so far

use std::cmp;

fn get_prefix(s: &str, end: usize) -> String {
    s[0..end].to_string()
}

fn comm_pref_end(s1: &str, s2: &str) -> Option<usize> {
    println!("string one: {s1}, string two: {s2}");
    let ascii_arr1 = s1.as_bytes();
    let ascii_arr2 = s2.as_bytes();
    let mut pref_end:i32 = -1;
    for i in 0..cmp::min(ascii_arr1.len(), ascii_arr2.len()) {
        if ascii_arr1[i] == ascii_arr2[i] {
            println!("{:?} == {:?}", ascii_arr1[i], ascii_arr2[i]);
            pref_end += 1;
        } else {
            println!("{} != {}", ascii_arr1[i], ascii_arr2[i]);
            break;
        }
    }
    match pref_end {
        -1 => None,
        _ => Some((pref_end + 1) as usize)
    }
}

impl Solution {  
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut end_of_pref:usize = strs[0].len();
        // iterate through the vector of strings to find the end of the common prefix
        for i in 0..strs.len() - 1 {
            let pref_result = comm_pref_end(&strs[i], &strs[i+1]);
            match pref_result {
                None => {return "".to_string();},
                Some(new_end) if new_end < end_of_pref => {
                    end_of_pref = new_end;
                },
                _ => {}
            }
        }
        return get_prefix(&strs[0], end_of_pref);
    }
}