#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vt;
typedef vector<vector<int>> vvt;
typedef vector<string> vs;

#define repeat(ix, T) for (int ix = 0; ix < T; ++ix)
#define FOR(ix, s, e) for (int ix = s; ix < e; ++ix)
#define FORR(ix, s, e) for (int ix = s; ix > e; --ix)
#define map(ar, dr, f)                  \
    for (int i = 0; i < dr.size(); ++i) \
        dr[i] = f(ar[i]);

template <class T>
void printarr(const vector<T> &ar)
{
    for (auto iter = ar.begin(); iter < ar.end() - 1; ++iter)
    {
        cout << *iter << " ";
    }
    cout << *(ar.end() - 1);
}

class Solution
{
};
