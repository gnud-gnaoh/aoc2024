#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  freopen("error", "w", stderr);

  map<char, pair<int, int>> dir;
  dir['^'] = {-1, 0};
  dir['v'] = {1, 0};
  dir['<'] = {0, -1};
  dir['>'] = {0, 1};

  int n = 50;
  vector<string> tgrid(n), grid(n);
  pair<int, int> pos;
  for (int i = 0; i < n; i++) {
    cin >> tgrid[i];
    for (char c : tgrid[i]) {
      if (c == '#') grid[i] += "##";
      else if (c == 'O') grid[i] += "[]";
      else if (c == '.') grid[i] += "..";
      else grid[i] += "@.";
    }
    
    for (int j = 0; j < 2*n; j++) {
      if (grid[i][j] == '@') {
        pos = {i, j};
      }
    }
  }

  string moves;
  string tmp;
  while (cin >> tmp) {
    moves += tmp;
  }

  for (char c : moves) {

    for (auto x : grid) {
      cerr << x << '\n';
    }
    cerr << "Move " << c << '\n';

    pair<int, int> d = dir[c];
    pair<int, int> npos = {pos.first + d.first, pos.second + d.second};

    if (grid[npos.first][npos.second] == '#') {
      continue;
    }

    if (grid[npos.first][npos.second] == '.') {
      swap(grid[pos.first][pos.second], grid[npos.first][npos.second]);
      pos = npos;
      continue;
    }

    if (c == '>' || c == '<') {
      pair<int, int> nxt = npos;
      while (grid[nxt.first][nxt.second] == '[' || grid[nxt.first][nxt.second] == ']') {
        nxt.first += d.first;
        nxt.second += d.second;
      }
      if (grid[nxt.first][nxt.second] == '#') {
        continue;
      }

      while (nxt != npos) {
        pair<int, int> nnxt = {nxt.first - d.first, nxt.second - d.second};
        swap(grid[nxt.first][nxt.second], grid[nnxt.first][nnxt.second]);
        nxt = nnxt;
      }

      swap(grid[pos.first][pos.second], grid[npos.first][npos.second]);
      pos = npos;
      continue;
    }


    queue<pair<int, int>> q;
    q.push(npos);
    vector<pair<int, int>> all;
    bool stop = false;
    set<pair<int, int>> vis;

    while (q.size()) {
      pair<int, int> cur = q.front();
      q.pop();
      
      pair<int, int> oth = (grid[cur.first][cur.second] == '[') ?
        pair<int, int>{cur.first, cur.second + 1} : 
        pair<int, int>{cur.first, cur.second - 1};

      if (grid[cur.first][cur.second] == ']') swap(cur, oth);

      assert(grid[cur.first][cur.second] == '[');
      assert(grid[oth.first][oth.second] == ']');

      if (vis.count(cur)) continue;
      vis.insert(cur);

      all.push_back(cur);

      pair<int, int> ncur = {cur.first + d.first, cur.second + d.second};
      pair<int, int> noth = {oth.first + d.first, oth.second + d.second};
      if (grid[ncur.first][ncur.second] == '[') {
        assert(grid[noth.first][noth.second] == ']');
        q.push(ncur);
      } 
      
      if (grid[ncur.first][ncur.second] == ']') {
        q.push(ncur);
      } 
      if (grid[noth.first][noth.second] == '[') {
        q.push(noth);
      }

      if (grid[ncur.first][ncur.second] == '#' || grid[noth.first][noth.second] == '#') {
        stop = true;
        break;
      }
    }

    if (stop) {
      cerr << "Stopped\n";
      continue;
    }

    vector<string> ngrid = grid;
    for (pair<int, int> x : all) { 
      ngrid[x.first][x.second] = '.';
      ngrid[x.first][x.second + 1] = '.';
    }
    for (pair<int, int> x : all) {
      ngrid[x.first + d.first][x.second + d.second] = '[';
      ngrid[x.first + d.first][x.second + d.second + 1] = ']';
    }
    grid = ngrid;

    assert(grid[pos.first][pos.second] == '@');
    assert(grid[npos.first][npos.second] == '.');
    swap(grid[pos.first][pos.second], grid[npos.first][npos.second]);
    pos = npos;
  }

  int ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 2*n; j++) {
      if (grid[i][j] == '[') {
        ans += i * 100 + j;
      }
    }
  }

  cout << ans << '\n';
}