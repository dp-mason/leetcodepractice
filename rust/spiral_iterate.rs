// track the min/max column/row, when a row/col is completed increment/decrement the min/max row/col
// track current direction that is being iterated over

#[derive(Debug)]
enum IterDir{
    Right,
    Down,
    Left,
    Up
}

#[derive(Debug)]
struct MIndex {
    row:usize,
    col:usize
}

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result:Vec<i32> = vec![i32::MIN; matrix.len() * matrix[0].len()];
        let mut min_row:usize = 0;
        let mut max_row:usize = matrix.len() - 1;
        let mut min_col:usize = 0;
        let mut max_col:usize = matrix[0].len() - 1;
        let mut direction = IterDir::Right;
        let mut curr_m_index = MIndex{row:0, col:0};
        let mut index_into_result:usize = 0;
        
        println!("\n\nMatrix: {:?}", matrix);
        println!("Min Row: {min_row} Max Row: {max_row} Min Col: {min_col} Max Col: {max_col}");

        for index_into_result in 0..result.len() {
            println!("Curr index into Matrix is {:?} direction: {:?}", curr_m_index, direction);
            result[index_into_result] = matrix[curr_m_index.row][curr_m_index.col];
            
            match direction {
                IterDir::Right => {
                    // base cases
                    // curr col less than max col
                    if curr_m_index.col < max_col {
                        curr_m_index.col += 1;
                    } else if curr_m_index.col == max_col {
                        min_row += 1;
                        curr_m_index.row = min_row;
                        direction = IterDir::Down;
                    } else {
                        println!("UNCAUGHT RIGHT CONDITION");
                        break;
                    }
                },
                IterDir::Down => {
                    // base cases
                    // curr row is less than max row
                    if curr_m_index.row < max_row {
                        curr_m_index.row += 1;
                    } else if curr_m_index.row == max_row {
                        max_col -= 1;
                        curr_m_index.col = max_col;
                        direction = IterDir::Left;
                    } else {
                        println!("UNCAUGHT DOWN CONDITION");
                        break;
                    }
                },
                IterDir::Left => {
                    // base cases
                    // curr row is less than max row
                    if curr_m_index.col > min_col {
                        curr_m_index.col -= 1;
                    } else if curr_m_index.col == min_col {
                        max_row -= 1;
                        curr_m_index.row = max_row;
                        direction = IterDir::Up;
                    } else {
                        println!("UNCAUGHT LEFT CONDITION");
                        break;
                    }
                },
                IterDir::Up => {
                    // base cases
                    // curr row is more than min row
                    if curr_m_index.row > min_row {
                        curr_m_index.row -= 1;
                    } else if curr_m_index.row == min_row {
                        min_col += 1;
                        curr_m_index.col = min_col;
                        direction = IterDir::Right;
                    } else {
                        println!("UNCAUGHT UP CONDITION");
                        break;
                    }
                },
                _ => {break;}
            }
        }

        result
    }
}