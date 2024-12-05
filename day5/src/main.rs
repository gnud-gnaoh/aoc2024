use std::env;
use std::f32::INFINITY;
use std::fs;
use std::collections::{HashMap, HashSet, VecDeque};

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

  let conds: Vec<(i32, i32)> = {
    let mut set = HashSet::new();
    conds.into_iter().filter(|&cond| set.insert(cond)).collect()
  };

  let updates: Vec<Vec<i32>> = updates.iter()
    .map(|&update| {
      update.split(',').map(|num| num.parse().unwrap()).collect()
    })
    .collect();

  fn topological_sort(conds: &[(i32, i32)]) -> Option<Vec<i32>> {
    let mut in_degree = HashMap::new();
    let mut graph = HashMap::new();

    for &(u, v) in conds {
      graph.entry(u).or_insert_with(Vec::new).push(v);
      *in_degree.entry(v).or_insert(0) += 1;
      in_degree.entry(u).or_insert(0);
    }

    let mut queue = VecDeque::new();
    for (&node, &degree) in &in_degree {
      if degree == 0 {
        queue.push_back(node);
      }
    }

    let mut topo_order = Vec::new();
    while let Some(node) = queue.pop_front() {
      topo_order.push(node);
      if let Some(neighbors) = graph.get(&node) {
        for &neighbor in neighbors {
          let degree = in_degree.get_mut(&neighbor).unwrap();
          *degree -= 1;
          if *degree == 0 {
            queue.push_back(neighbor);
          }
        }
      }
    }

    assert!(topo_order.len() == in_degree.len());
    Some(topo_order)
  }

  // let topo_order = topological_sort(&conds).expect("Graph has a cycle");
  // println!("Topological order: {:?}", topo_order);

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
      // ans += update[update.len() / 2];
    } else {
      let cond: Vec<(i32, i32)> = conds.iter().filter(|&&(a, b)| update.contains(&a) && update.contains(&b)).cloned().collect();
      let topo_order = topological_sort(&cond).unwrap();

      println!("bad {:?}", update);
      let mut sorted_update = update.clone();
      sorted_update.sort_by_key(|&x| topo_order.iter().position(|&y| y == x).unwrap_or(1e9 as usize));
      println!("sorted bad {:?}", sorted_update);
      ans += sorted_update[sorted_update.len() / 2];  
    }
  }

  println!("{}", ans);
}