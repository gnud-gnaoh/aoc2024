#include <bits/stdc++.h>
using namespace std;
#define int long long

struct state {
  pair<int, int> pos, dir;
  int cost;

  bool operator<(const state &other) const {
    return cost > other.cost;
  }
};

signed main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  freopen("error", "w", stderr);

  int n = 141;
  vector<string> a(n);
  pair<int, int> pos, dir;
  pair<int, int> end;
  dir = {0, 1};
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    for (int j = 0; j < n; j++) {
      if (a[i][j] == 'S') {
        pos = {i, j};
      } else if (a[i][j] == 'E') {
        end = {i, j};
      }
    }
  }

  auto start = make_pair(pos, dir);

  map<pair<pair<int, int>, pair<int, int>>, int> dist;
  map<pair<pair<int, int>, pair<int, int>>, pair<pair<int, int>, pair<int, int>>> par;
  priority_queue<state> pq;
  pq.push({pos, dir, 0});

  int ans = 1e18;
  pair<pair<int, int>, pair<int, int>> ans_state;
  while (pq.size()) {
    state cur = pq.top();
    pq.pop();

    cerr << cur.pos.first << " " << cur.pos.second << " " << cur.dir.first << " " << cur.dir.second << " " << cur.cost << endl;

    if (cur.pos == end) {
      if (cur.cost < ans) {
        cout << "found " << cur.pos.first << " " << cur.pos.second << " " << cur.dir.first << " " << cur.dir.second << " " << cur.cost << endl;
        ans = cur.cost;
        ans_state = {cur.pos, cur.dir};
      }
    }

    auto [pos, dir, cost] = cur;
    if (dist.count({pos, dir}) && cost > dist[{pos, dir}]) {
      continue;
    }

    // rotate
    {
      state next = cur;
      next.dir = {-dir.second, dir.first};
      next.cost = cost + 1000;
      if (!dist.count({next.pos, next.dir}) || next.cost < dist[{next.pos, next.dir}]) {
        dist[{next.pos, next.dir}] = next.cost;
        par[{next.pos, next.dir}] = {pos, dir};
        pq.push(next);
      }
    }

    // rotate other dir
    {
      state next = cur;
      next.dir = {dir.second, -dir.first};
      next.cost = cost + 1000;
      if (!dist.count({next.pos, next.dir}) || next.cost < dist[{next.pos, next.dir}]) {
        dist[{next.pos, next.dir}] = next.cost;
        par[{next.pos, next.dir}] = {pos, dir};
        pq.push(next);
      }
    }

    // move
    {
      state next = cur;
      next.pos = {pos.first + dir.first, pos.second + dir.second};
      next.cost = cost + 1;
      if (next.pos.first >= 0 && next.pos.first < n && next.pos.second >= 0 && next.pos.second < n 
      && a[next.pos.first][next.pos.second] != '#' 
      && (!dist.count({next.pos, next.dir}) || next.cost < dist[{next.pos, next.dir}])) {
        dist[{next.pos, next.dir}] = next.cost;
        par[{next.pos, next.dir}] = {pos, dir};
        pq.push(next);
      }
    }
  }

  // cout << "fin " << ans_state.first.first << " " << ans_state.first.second << " " << ans_state.second.first << " " << ans_state.second.second << endl;
  assert(par.count(ans_state));

  vector<pair<pair<int, int>, pair<int, int>>> path;
  for (auto cur = ans_state; ; cur = par[cur]) {
    path.push_back(cur);
    if (cur == start) {
      break;
    }
  }
  reverse(path.begin(), path.end());

  // for (auto [pos, dir] : path) {
  //   cout << pos.first << " " << pos.second << " " << dir.first << " " << dir.second << endl;
  // }
  cout << ans;
}