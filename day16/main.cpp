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
  priority_queue<state> pq;
  pq.push({pos, dir, 0});

  int ans = 1e18;
  pair<pair<int, int>, pair<int, int>> ans_state;
  while (pq.size()) {
    state cur = pq.top();
    pq.pop();

    if (cur.pos == end) {
      if (cur.cost < ans) {
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
        pq.push(next);
      }
    }
  }

  cerr << "Ans " << ans << endl;

  // dijkstra from end to start
  int cnt = 0;

  map<pair<pair<int, int>, pair<int, int>>, int> dist2;
  assert(pq.empty());
  for (auto dir : vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
    pq.push({end, dir, 0});
    dist2[{end, dir}] = 0;
  }

  while (pq.size()) {
    state cur = pq.top();
    pq.pop();

    auto [pos, dir, cost] = cur;
    if (dist2.count({pos, dir}) && cost > dist2[{pos, dir}]) {
      continue;
    }

    // rotate
    {
      state next = cur;
      next.dir = {-dir.second, dir.first};
      next.cost = cost + 1000;
      if (!dist2.count({next.pos, next.dir}) || next.cost < dist2[{next.pos, next.dir}]) {
        dist2[{next.pos, next.dir}] = next.cost;
        pq.push(next);
      }
    }

    // rotate other dir
    {
      state next = cur;
      next.dir = {dir.second, -dir.first};
      next.cost = cost + 1000;
      if (!dist2.count({next.pos, next.dir}) || next.cost < dist2[{next.pos, next.dir}]) {
        dist2[{next.pos, next.dir}] = next.cost;
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
      && (!dist2.count({next.pos, next.dir}) || next.cost < dist2[{next.pos, next.dir}])) {
        dist2[{next.pos, next.dir}] = next.cost;
        pq.push(next);
      }
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (a[i][j] != '#') {
        for (auto dir : vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
          pair<int, int> pos = {i, j};
          pair<int, int> nxt = {i + dir.first, j + dir.second};
          if (a[nxt.first][nxt.second] == '#') {
            continue;
          }
          pair<int, int> opp_dir = {-dir.first, -dir.second};
          if (dist.count({pos, dir}) && dist2.count({nxt, opp_dir})) {
            if (dist[{pos, dir}] + dist2[{nxt, opp_dir}] + 1 == ans) {
              cnt++;
              cerr << "CAC\n";
              cerr << pos.first << " " << pos.second << " " << dir.first << " " << dir.second << " " << dist[{pos, dir}] << endl;
              cerr << nxt.first << " " << nxt.second << " " << opp_dir.first << " " << opp_dir.second << " " << dist2[{nxt, opp_dir}] << endl;
              cerr << "\n";
              break;
            }
          }
        }
      }
    }
  }

  // add one for E
  cout << cnt + 1;
}