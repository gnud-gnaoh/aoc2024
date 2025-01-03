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

  let mut pos: (i32, i32) = (0, 0);
  let mut dir: (i32, i32) = (-1, 0);

  for (i, row) in board.iter().enumerate() {
    if let Some(j) = row.iter().position(|&c| c == '^') {
      pos = ((i as i32), (j as i32));
      break;
    }
  }

  let ipos = pos;
  let idir = dir;
  println!("init {:?}", pos);

  // let mut vis: Vec<Vec<bool>> = vec![vec![false; board[0].len()]; board.len()];
  let mut ans = 0;

  for i in 0..board.len() {
    for j in 0..board[i].len() {
      if board[i][j] == '#' || board[i][j] == '^' {
        continue;
      }

      let ori = board[i][j];
      board[i][j] = '#';

      pos = ipos;
      dir = idir;
      let mut cycle = false;
      let mut vis: HashMap<((i32, i32), (i32, i32)), bool> = HashMap::new();

      loop {
        vis.insert((pos, dir), true);

        // println!("{}, {}, {:?}", i, j, pos);
        // vis[pos.0 as usize][pos.1 as usize] = true;
        let nxt = (pos.0 + dir.0, pos.1 + dir.1);
        
        // println!("nxt {:?}", nxt);
        if nxt.0 < 0 || nxt.0 >= board.len() as i32 || nxt.1 < 0 || nxt.1 >= board[0].len() as i32 {
          break;  
        }
    
        if board[nxt.0 as usize][nxt.1 as usize] == '#' {
          dir = (dir.1, -dir.0);
          if vis.contains_key(&(pos, dir)) {
            // println!("{}, {}, {:?}, {:?}", i, j, pos, nxt);  
            cycle = true;
            break;
          }
          // pos = nxt;
        } else {
          pos = nxt;
        }
      }

      if cycle {
        println!("cycle {}, {}", i, j);
        ans += 1;
      }
      board[i][j] = ori;
    }
  }

  // for row in &vis {
  //   for &cell in row {
  //     print!("{}", if cell { 'X' } else { '.' });
  //   }
  //   println!();
  // }
  // let ans = vis.iter().flatten().filter(|&&v| v).count();
  println!("{}", ans);
}