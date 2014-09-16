#include <iostream>
using namespace std;

bool IsPrime(int input){
	if (input == 2)
		return true;
	if (input % 2 == 0 || input == 1)
		return false;
	for (int i = 2; i < sqrt(input) + 1; i++)
		if (input % i == 0)
			return false;
	return true;
}

int SpiralPrimeRatio(){
	int currentSkip = 1;
	int side = 0;
	int i = 1;
	int primes = 0;
	int nonprimes = 1;
	while (true){
		i += currentSkip;
		i++;
		if (IsPrime(i))
			primes++;
		else
			nonprimes++;
		if (++side == 4){
			side = 0;
			currentSkip += 2;
			if (((double)primes) / ((double)nonprimes + primes) < .1)
				return currentSkip;
		}
	}
}


int main(){
	int i = 7;
	cout << SpiralPrimeRatio();
	while (true){
		if (SpiralPrimeRatio() < .1)
			break;
		i++;
	}
	int in;
	cin >> in;
	return 0;
}