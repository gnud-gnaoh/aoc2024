use std::env;
use std::fs;
use regex::Regex;

fn main() {
  let args: Vec<String> = env::args().collect();

  let file_path = &args[1];

  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  println!("With text:\n{contents}");

  let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();

  let mut ans = 0;
  for cap in re.captures_iter(&contents) {
    let start = cap.get(0).unwrap().start();
    let end = cap.get(0).unwrap().end();
    println!("Match found at position: {} to {}", start, end);

    let founddont = contents[..start].rfind("don't()").unwrap_or(0);
    let founddo = contents[..start].rfind("do()").unwrap_or(0);

    println!("Matched: X = {}, Y = {}", &cap[1], &cap[2]);
    if founddo >= founddont {
      ans += cap[1].parse::<i32>().unwrap() * cap[2].parse::<i32>().unwrap();
    }
  }
  println!("{}", ans);
}