use std::env;
use std::fs;
use std::collections::HashMap;

fn main() {
  let args: Vec<String> = env::args().collect();

  let file_path = &args[1];

  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  println!("With text:\n{contents}");

  let mut board: Vec<Vec<char>> = contents
    .lines()
    .map(|line| line.chars().collect())
    .collect();

  let mut char_map: HashMap<char, Vec<(usize, usize)>> = HashMap::new();

  for (i, row) in board.iter().enumerate() {
    for (j, &ch) in row.iter().enumerate() {
      if (ch == '.') { continue };
      char_map.entry(ch).or_insert_with(Vec::new).push((i, j));
    }
  }

  println!("{:?}", char_map);
  let mut bool_board: Vec<Vec<bool>> = vec![vec![false; board[0].len()]; board.len()];
  for (ch, vpos) in char_map.iter() {
    for (i, &pos1) in vpos.iter().enumerate() {
      for &pos2 in vpos.iter().skip(i + 1) {
        println!("Character: {}, Pos1: {:?}, Pos2: {:?}", ch, pos1, pos2);
        bool_board[pos1.0][pos1.1] = true;
        bool_board[pos2.0][pos2.1] = true;
        let dir = ((pos2.0 as i32 - pos1.0 as i32), (pos2.1 as i32 - pos1.1 as i32));
        for scale in 1..(board.len() as i32 + board[0].len() as i32) {
          let pos22 = (pos2.0 as i32 + dir.0 * scale, pos2.1 as i32 + dir.1 * scale);
          let pos11 = (pos1.0 as i32 - dir.0 * scale, pos1.1 as i32 - dir.1 * scale);
          if pos22.0 >= 0 && pos22.0 < board.len() as i32 && pos22.1 >= 0 && pos22.1 < board[0].len() as i32 {
            bool_board[pos22.0 as usize][pos22.1 as usize] = true;
          }
          if pos11.0 >= 0 && pos11.0 < board.len() as i32 && pos11.1 >= 0 && pos11.1 < board[0].len() as i32 {
            bool_board[pos11.0 as usize][pos11.1 as usize] = true;
          }
        }
      }
    }
  }

  let ans = bool_board.iter().flatten().filter(|&&b| b).count();
  println!("Number of true in bool_board: {}", ans);
}