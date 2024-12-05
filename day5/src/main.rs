use std::env;
use std::fs;

fn main() {
  let args: Vec<String> = env::args().collect();

  let file_path = &args[1];

  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  println!("With text:\n{contents}");

  let parts: Vec<&str> = contents.splitn(2, "\n\n").collect();
  let conds = parts[0].split("\n").collect::<Vec<&str>>();
  let updates = parts[1].split("\n").collect::<Vec<&str>>();

  let conds: Vec<(i32, i32)> = conds.iter()
    .map(|&cond| {
      let parts: Vec<&str> = cond.split('|').collect();
      (parts[0].parse().unwrap(), parts[1].parse().unwrap())
    })
    .collect();

  let updates: Vec<Vec<i32>> = updates.iter()
    .map(|&update| {
      update.split(',').map(|num| num.parse().unwrap()).collect()
    })
    .collect();

  // for cond in conds {
  //   println!("{}, {}", cond.0, cond.1);
  // }

  // for update in updates {
  //   for num in update {
  //     print!("{}, ", num);
  //   }
  //   println!();
  // }

  let mut ans = 0;
  for update in updates {
    let mut ok = true;
    for cond in &conds {
      if update.iter().position(|&x| x == cond.0).is_none() || update.iter().position(|&x| x == cond.1).is_none() {
        continue;
      } else {
        let pos0 = update.iter().position(|&x| x == cond.0).unwrap();
        let pos1 = update.iter().position(|&x| x == cond.1).unwrap();
        if pos0 > pos1 {
          ok = false;
          break;
        }
      }
    }
    if ok {
      println!("good {:?}", update);
      ans += update[update.len() / 2];
    }
  }

  println!("{}", ans);
}