use std::env;
use std::fs;

fn main() {
  let args: Vec<String> = env::args().collect();

  let file_path = &args[1];

  println!("In file {file_path}");

  let contents = fs::read_to_string(file_path)
      .expect("Should have been able to read the file");

  println!("With text:\n{contents}");

  let equations: Vec<&str> = contents
    .lines()
    .collect();

  println!("{:?}", equations);

  let parsed_equations: Vec<(usize, Vec<usize>)> = equations
    .iter()
    .map(|&equation| {
      let parts: Vec<&str> = equation.split(": ").collect();
      let sum: usize = parts[0].trim().parse().expect("Invalid sum");
      let numbers: Vec<usize> = parts[1]
        .split(' ')
        .map(|num| num.trim().parse().expect("Invalid number"))
        .collect();
      (sum, numbers)
    })
    .collect();

  println!("{:?}", parsed_equations);
  
  assert_eq!(usize::MAX, 18446744073709551615);

  let mut ans = 0;
  for equation in parsed_equations {
    println!("{:?}", equation);
    
    let len = equation.1.len() - 1;
    let mut found = false;
    for msk in 0..(1 << len) {
      if found {
        break;
      }
      let mut submsk = msk;
      loop {
        // println!("{:?}", submsk);
        let mut cur = equation.1[0];
        for i in 0..len {
          if (msk >> i) & 1 == 0 && (submsk >> i) & 1 == 0 {
            cur += equation.1[i+1];
          } else if (msk >> i) & 1 == 1 && (submsk >> i) & 1 == 1 {
            cur *= equation.1[i+1];
          } else {
            cur = cur * 10_usize.pow(equation.1[i+1].to_string().len() as u32) + equation.1[i+1];
          }
        }
        
        if cur == equation.0 {
          println!("can create {:?}", cur);
          ans += cur;
          found = true;
          break;
        }

        if submsk == 0 {
          break;
        }
        submsk = (submsk - 1) & msk;
      }
    }
  }

  println!("{:?}", ans);
}