#include <iostream>
#include <vector> 

using namespace std; // std:: 생략을 위해 사용

int fibo(int n) {
    if (n <= 1) return 1;
    if (n == 2) return 1;

    vector<int> dp(n + 1); 
    
    dp[0] = 1; 
    dp[1] = 1;

    for (int i = 2; i < n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n - 1]; 
}

int main() {
    int n;

    cin >> n;

    int recursion_count = fibo(n);
    
    int dp_count = n - 2;

    cout << recursion_count << " " << dp_count << endl;

    return 0;
}