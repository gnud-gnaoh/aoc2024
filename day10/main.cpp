#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("input", "r", stdin);

  int n = 53;
  vector<string> a(n);
  for (int i=0; i<n; i++) {
    cin>>a[i];
  }

  vector<int> di = {0, 0, 1, -1};
  vector<int> dj = {1, -1, 0, 0};
  
  int cur=0;
  set<pair<int,int>> vis;
  function<void(int, int, int)> dfs = [&](int i, int j, int need) {
    if (need == 10) {
      // cerr<<i<<" "<<j<<" "<<need<<endl;
      // if (vis.count({i,j})) return;
      // vis.insert({i,j});
      cur++;
      return;
    }
    for (int dir=0; dir<4; dir++){
      int ni=i+di[dir];
      int nj=j+dj[dir];
      if (ni>=0 && ni<n && nj>=0 && nj<n && a[ni][nj]==need+'0'){
        dfs(ni,nj,need+1);
      }
    }
  };

  int ans=0;
  for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
      if (a[i][j]=='0'){
        cur=0;
        // vis.clear();
        dfs(i,j,1);
        // cerr<<i<<" "<<j<<" "<<cur<<endl;
        ans+=cur;
        // return 0;
      }
    }
  }

  cout<<ans;
}