use std::env;
use std::fs;

fn main() {
  let args: Vec<String> = env::args().collect();

  let file_path = &args[1];

  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  println!("With text:\n{contents}");

  let char_matrix: Vec<Vec<char>> = contents
    .lines()
    .map(|line| line.chars().collect())
    .collect();

  let diri = [-1, 0, 1, 0, -1, 1, -1, 1] as [i32; 8];
  let dirj = [0, 1, 0, -1, -1, 1, 1, -1] as [i32; 8];
  let need = ['X', 'M', 'A', 'S'];
  let mut ans = 0;

  for i in 0..char_matrix.len() {
    for j in 0..char_matrix[i].len() {
      if char_matrix[i][j] == 'X' {
        for dir in 0..8 {
          let mut flag = true;
          for step in 0..4 {
            let ni = (i as i32) + diri[dir] * step;
            let nj = (j as i32) + dirj[dir] * step;
            if !((ni >= 0 && ni < char_matrix.len() as i32 && nj >= 0 && nj < char_matrix[ni as usize].len() as i32)) || char_matrix[ni as usize][nj as usize] != need[step as usize] {
              flag = false;
              break;
            }
          }
          if flag {
            println!("Found at ({}, {}, {})", i, j, dir);
          }
          ans += flag as i32;
        } 
      }
    }
  }

  println!("{}", ans);
}