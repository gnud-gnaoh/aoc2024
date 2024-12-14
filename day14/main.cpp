#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("input", "r", stdin);

  int n=500;
  vector<pair<int,int>> pos(n), vel(n);
  
  for (int i=0; i<n; i++) {
    cin>>pos[i].first>>pos[i].second;
    cin>>vel[i].first>>vel[i].second;
  }

  int wide=101, tall=103;
  
  int t=100;
  int one=0, two=0, three=0, four=0;
  for (int i=0; i<n; i++) {
    pos[i].first += vel[i].first*t;
    pos[i].second += vel[i].second*t;

    pos[i].first %= wide;
    if (pos[i].first<0) pos[i].first += wide;
    pos[i].second %= tall;
    if (pos[i].second<0) pos[i].second += tall;

    if (pos[i].first<wide/2 && pos[i].second<tall/2) one++;
    if (pos[i].first>wide/2 && pos[i].second<tall/2) two++;
    if (pos[i].first<wide/2 && pos[i].second>tall/2) three++;
    if (pos[i].first>wide/2 && pos[i].second>tall/2) four++;
  }

  cout << one << " " << two << " " << three << " " << four << endl;
  int ans=one*two*three*four;
  cout<<ans;
}