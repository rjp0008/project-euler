#include <iostream>
using namespace std;

int spiralSum(int gridSize){
	int currentSkip = 1;
	int side = 0;
	int i = 1;
	int output = 1;
	while (currentSkip + 2 <= gridSize){
		i += currentSkip;
		i++;
		output += i;
		if (++side == 4){
			side = 0;
			currentSkip += 2;
		}
	}
	return output;
}

int main(){
	cout << spiralSum(1001);
	int in;
	cin >> in;
	return 0;
}