#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("input", "r", stdin);

  string s;
  cin >> s;

  vector<int> t;
  int n = s.size();
  int id = 0;
  for (int i = 0; i < n; i++) {
    int len = s[i] - '0';
    if (i % 2 == 0) {
      while (len--) {
        t.push_back(id);
      }
      id++;
    } else {
      while (len--) {
        t.push_back(-1);
      }
    }
  }

  int m = t.size();

  auto find_loc = [&](int id) {
    int l = -1, r = -1;
    for (int i = 0; i < m; i++) {
      if (t[i] == id) {
        if (l == -1) l = i;
        r = i;
      }
    }
    return make_pair(l, r);
  };

  auto find_empty = [&](int len, int l) {
    for (int i = 0; i + len - 1 < l; i++) {
      if (t[i] == -1) {
        bool ok = true;
        for (int j = 0; j < len; j++) {
          if (i + j >= l || t[i + j] != -1) {
            ok = false;
            break;
          }
        }
        if (ok) return i;
      }
    }
    return -1LL;
  };

  auto ass = [&](int l, int r, int x) {
    for (int i = l; i <= r; i++) {
      t[i] = x;
    }
  };

  for (int i = id - 1; i >= 0; i--) {
    auto [l, r] = find_loc(i);
    int len = r - l + 1;
    int nl = find_empty(len, l);
    if (nl == -1) continue;
    ass(l, r, -1);
    ass(nl, nl + len - 1, i);
  }

  for (int x : t) {
    cout << x << ' ';
  }
  cout << '\n';

  int checksum = 0;
  for (int i = 0; i < m; i++) {
    if (t[i] == -1) continue;
    checksum += t[i] * i;
  }

  cout << checksum;
}