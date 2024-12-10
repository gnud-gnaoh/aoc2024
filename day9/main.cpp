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

  for (int x : t) {
    cout << x << ' ';
  }
  cout << '\n';

  int m = t.size();
  int pos = find(t.begin(), t.end(), -1) - t.begin();
  for (int i = m - 1; i >= 0 && pos < i; i--) {
    if (t[i] != -1) {
      t[pos] = t[i];
      t[i] = -1;
      pos = find(t.begin() + pos + 1, t.end(), -1) - t.begin();
    }
  }

  for (int x : t) {
    cout << x << ' ';
  }
  cout << '\n';

  int checksum = 0;
  for (int i = 0; i < m; i++) {
    if (t[i] == -1) break;
    checksum += t[i] * i;
  }

  cout << checksum;
}