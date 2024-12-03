use std::env;
use std::fs;

fn main() {
  let args: Vec<String> = env::args().collect();

  let file_path = &args[1];

  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  println!("With text:\n{contents}");

  let parts = contents.split("\n");
  let collection = parts.collect::<Vec<&str>>();

  dbg!(&collection[0..5]);

  let ans = collection.iter().filter(|x| {
    let list = x.split(" ").collect::<Vec<&str>>();
    let v = list.into_iter().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();

    for i in 0..v.len() {
      let mut temp = v.clone();
      temp.remove(i);

      let valid = temp.windows(2).all(|window| {
        (window[0] - window[1]).abs() >= 1 && (window[0] - window[1]).abs() <= 3
      });
      let safe = (temp.is_sorted() || temp.is_sorted_by(|a, b| a > b)) && valid;

      if safe {
        return true;
      }
    }
    
    return false;
  }).count();

  println!("{}", ans);
}
