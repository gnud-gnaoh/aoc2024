#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("input", "r", stdin);

  int n = 1024;

  int m = 71;
  vector<vector<char>> a(m, vector<char>(m, '.'));
  
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    
    // cerr << i << '|' << x << ' ' << y << '\n';
    assert(x >= 0 && x < m && y >= 0 && y < m);
    a[x][y] = '#';
  }

  cerr << "cac\n";

  map<pair<int, int>, int> d;
  queue<pair<int, int>> q;
  d[{0, 0}] = 0;
  q.push({0, 0});

  while (q.size()) {
    pair<int, int> cur = q.front();
    q.pop();

    int i = cur.first, j = cur.second;
    for (int x = -1; x <= 1; x++) {
      for (int y = -1; y <= 1; y++) {
        if (abs(x) + abs(y) == 1) {
          int ni = i + x, nj = j + y;
          if (ni >= 0 && ni < m && nj >= 0 && nj < m && a[ni][nj] == '.' && !d.count({ni, nj})) {
            d[{ni, nj}] = d[cur] + 1;
            q.push({ni, nj});
          }
        }
      }
    }
  }

  cout << d[{m - 1, m - 1}];
}