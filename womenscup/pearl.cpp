#include <iostream>
#include <cstdio>
#include <queue>
#include <math.h>   
#include <vector>

using namespace std;

int main() {
	priority_queue<int, vector<int>, greater<int> >  q;
	int T;
	unsigned long long total_cost, c1, c2, c3;

	long long modulo = pow(10, 9) + 7;
	scanf("%d\n", &T);

	for (int i = 0; i < T; i++) {
		unsigned long long n;
		scanf("%lld ", &n);	
		q.push(n);
	}

	while(q.size() > 1) {
		c1 = q.top() % modulo;
		q.pop();
		c2 = q.top() % modulo;
		q.pop();
		c3 = (c1 + c2) % modulo;
		q.push(c3);
		total_cost += c3;
		// printf("%lld %lld %lld\n", c1, c2, c3);
	}
	// printf("%lld\n", total_cost);
	total_cost %= ( (long long) modulo);
	printf("%lld\n", total_cost);
    // Complete the code.
    return 0;
}
