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

  let parts = contents.split("\n");
  let collection = parts.collect::<Vec<&str>>();

  dbg!(&collection[0..5]);

  let lists = collection.iter().map(|x| x.split("   ").collect::<Vec<&str>>()).collect::<Vec<Vec<&str>>>();
  let mut list1 = lists.iter().map(|x| x[0]).collect::<Vec<&str>>().into_iter().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
  let mut list2 = lists.iter().map(|x| x[1]).collect::<Vec<&str>>().into_iter().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
  
  dbg!(&list1[0..5]);
  dbg!(&list2[0..5]);
  
  list1.sort();
  list2.sort();

  let mut ans1 = 0;
  for i in 0..list1.len() {
    ans1 += (list1[i] - list2[i]).abs();
  }
  println!("{}", ans1);

  let mut map2 = HashMap::new();
  for i in 0..list2.len() {
    let count = map2.entry(list2[i]).or_insert(0);
    *count += 1;
  }

  let mut ans2 = 0;
  for i in 0..list2.len() {
    ans2 += list1[i] * map2.get(&list1[i]).unwrap_or(&0);
  }
  println!("{}", ans2);
}