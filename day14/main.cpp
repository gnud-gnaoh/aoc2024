#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);

  int n=500;
  vector<pair<int,int>> opos(n), ovel(n);
  
  for (int i=0; i<n; i++) {
    cin>>opos[i].first>>opos[i].second;
    cin>>ovel[i].first>>ovel[i].second;
  }

  int wide=101, tall=103;
  
  // int t=100;
  vector<pair<int,int>> states;
  for (int t=1;t<=101*103;t++) {
    vector<pair<int,int>> pos = opos, vel = ovel;
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
    states.push_back({one*two*three*four, t});
    // if (one + three != two + four) continue;

    // bool check = true;
    // cout << "ANS = " << t << endl;
    // vector<vector<char>> grid(tall, vector<char>(wide, '.'));
    // for (int i=0; i<n; i++) {
    //   grid[pos[i].second][pos[i].first] = '#';
    // }

    // for (int i=0; i<tall; i++) {
    //   for (int j=0; j<wide; j++) {
    //     cout<<grid[i][j];
    //   }
    //   cout<<endl;
    // }
    // cout<<"############################################"<<endl;
    // break;
  }
  sort(states.begin(), states.end());
  states.resize(100);
  for (auto x: states) {
    int t = x.second;
    vector<pair<int,int>> pos = opos, vel = ovel;
    int one=0, two=0, three=0, four=0;
    for (int i=0; i<n; i++) {
      pos[i].first += vel[i].first*t;
      pos[i].second += vel[i].second*t;

      pos[i].first %= wide;
      if (pos[i].first<0) pos[i].first += wide;
      pos[i].second %= tall;
      if (pos[i].second<0) pos[i].second += tall;
    }
    cout << "ANS = " << t << endl;
    vector<vector<char>> grid(tall, vector<char>(wide, '.'));
    for (int i=0; i<n; i++) {
      grid[pos[i].second][pos[i].first] = '#';
    }

    for (int i=0; i<tall; i++) {
      for (int j=0; j<wide; j++) {
        cout<<grid[i][j];
      }
      cout<<endl;
    }
    cout<<"############################################"<<endl;
    // break;
  }
}