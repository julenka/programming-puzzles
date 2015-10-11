#include <iostream>
#include <cstdio>
#include <map>
#include <queue>
#include <set>
#include <unordered_set>
#include <math.h>   
#include <vector>

using namespace std;

void fail() {
	printf("Danger!! Lucifer will trap you\n");
}

void success() {
	printf("Go on get the Magical Lamp\n");
}


int get_color(int* colors, int n, int &max_color, int &num_colors) {
	// get the color
	int c = colors[n];
	if (c == 0) {
		max_color++;
		c = max_color;
		colors[n] = c;
		num_colors++;
	}
	return c;
}

void merge_colors(int* colors, int N, int a, int b) {
	for(int i = 0; i < N; i++) {
		if(colors[i] == b) {
			colors[i] = a;
		}
	}

}

void process_case() {
	int N, M, num_colors = 0, max_color = 0;
	scanf("%d %d\n", &N, &M);
	std::map<int, int> in_counts, out_counts;
	std::map<int, vector<int> > outgoing_edges;
	int colors[N];


	for(int i = 0; i < N+1; i++) {
		in_counts[i] = 0;
		out_counts[i] = 0;
		colors[i] = 0;
 	}

	for(int i = 0; i < M; i++) {
		int from, to;
		scanf("%d %d\n", &from, &to);
		outgoing_edges[from].push_back(to);
		in_counts[to] += 1;
		out_counts[from] += 1;

	}



	if(out_counts[N] == 0) {
		return fail();
	}
	if(out_counts[1] == 0) {
		return fail();
	}

	for (auto iter : out_counts) {
		int k = iter.first;
		int v = iter.second;
		if (in_counts[k] != v) {
			return fail();
		}
	}

	for (auto iter : outgoing_edges) {
		int from = iter.first;
		auto to_list = iter.second;
		for(auto to : to_list) {
			int from_color = get_color(colors, from - 1, max_color, num_colors);
			int to_color = get_color(colors, to - 1, max_color, num_colors);
			if (from_color != to_color) {
				merge_colors(colors, N, from_color, to_color);
				num_colors--;
			}	
		}
		
	}
	if(num_colors != 1) {
		return fail();
	}

	return success();
}

int main() {
	int T;
	scanf("%d\n", &T);
	for (int i = 0; i < T; i++) {
		process_case();
	}

    return 0;
}
