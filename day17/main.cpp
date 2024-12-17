#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("sample", "r", stdin);
  freopen("output", "w", stdout);
  freopen("error", "w", stderr);

  int a = 0;
  int b = 0;
  int c = 0;

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

  auto f = [&](int aa) {
    a = aa;
    b = 0;
    c = 0;

    vector<int> res;
    int p = 0;
    bool ok = true;
    while (p < ops.size()) {
      int ins = ops[p++];
      if (p == ops.size()) break;

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
        res.push_back(combo(op) % 8);
        // if (res.back() != ops[res.size() - 1]) {
        //   ok = false;
        //   break;
        // }
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
    return res;
  };

  // for (int aa = 0; aa < 10000; aa++) {
  //   auto x = f(aa);
  //   for (int y : x) cout << y << " ";
  //   cout << '\n';
  // }
  // return 0;

  vector<int> v = ops;

  auto rec = [&](auto self, int ans, int i) -> void {
    if (i < 0) {
      cout << ans;
      exit(0);
    }
    if (f(ans)[i] == v[i]) {
      self(self, ans, i - 1);
    }
    int len = i + 1;
    int l = 1LL << (3 * (len - 1));
    int r = 1LL << (3 * len);

    for (int ll = l; ll < r; ll += l) {
      if (f(ans + ll)[i] == v[i]) {
        self(self, ans + ll, i - 1);
      }
    }
  };

  rec(rec, 0, v.size() - 1);
}