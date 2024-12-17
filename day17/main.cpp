#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("sample", "r", stdin);
  freopen("output", "w", stdout);
  freopen("error", "w", stderr);

  int a, b, c;
  cin >> a >> b >> c;

  vector<int> ops;
  int tmp;
  while (cin >> tmp) ops.push_back(tmp);

  auto combo = [&](int x) {
    if (x <= 3) return x;
    if (x == 4) return a;
    if (x == 5) return b;
    if (x == 6) return c;
    assert(x != 7);
    return x;
  };

  int p = 0;
  while (p < ops.size()) {
    int ins = ops[p++];
    if (p == ops.size()) break;
    if (ins == 3 && a == 0) continue;

    int op = ops[p++];

    if (ins == 0) {
      op = combo(op);
      a = a >> op;
    } else if (ins == 1) {
      b = b ^ op;
    } else if (ins == 2) {
      op = combo(op);
      b = op % 8;
    } else if (ins == 3) {
      if (a == 0) continue;
      p = op;
    } else if (ins == 4) {
      b = b ^ c;
    } else if (ins == 5) {
      cout << (combo(op) % 8) << ',';
    } else if (ins == 6) {
      op = combo(op);
      b = a >> op;
    } else if (ins == 7) {
      op = combo(op);
      c = a >> op;
    } else {
      assert(false);
    }
  }

  cerr << a << " " << b << " " << c << '\n';
}