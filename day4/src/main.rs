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

  let mut ans = 0;

  for i in 1..char_matrix.len()-1 {
    for j in 1..char_matrix[i].len()-1 {
      if char_matrix[i][j] == 'A' {
        if char_matrix[i-1][j-1] == 'M' && char_matrix[i-1][j+1] == 'M' && char_matrix[i+1][j-1] == 'S' && char_matrix[i+1][j+1] == 'S' {
          ans += 1;
        }
        if char_matrix[i-1][j-1] == 'S' && char_matrix[i-1][j+1] == 'S' && char_matrix[i+1][j-1] == 'M' && char_matrix[i+1][j+1] == 'M' {
          ans += 1;
        }
        if char_matrix[i-1][j-1] == 'S' && char_matrix[i-1][j+1] == 'M' && char_matrix[i+1][j-1] == 'S' && char_matrix[i+1][j+1] == 'M' {
          ans += 1;
        }
        if char_matrix[i-1][j-1] == 'M' && char_matrix[i-1][j+1] == 'S' && char_matrix[i+1][j-1] == 'M' && char_matrix[i+1][j+1] == 'S' {
          ans += 1;
        }
      }
    }
  }

  println!("{}", ans);
}