#include <iostream>
#include "solutions.h"
using namespace std;


int menuScreen(){
	int output = -1;
	cout << "Euler solutions:\nPick a number 1-2 ";
	cin >> output;
	if(output > 0 && output < 3){
		return output;
	}
	else
	{
		cout << "Bad input, try again";
		return -1;
	}
}

int main()
{
	//menuloop for valid solutions
	int eulerSelection = -1;
	do{
		eulerSelection = menuScreen();
	}while(eulerSelection == -1);
	cout << "Answer: ";
	switch(eulerSelection){
		case 1:
			cout << MultiplesOfThreeAndFiveSum(1000);
		case 2:
			cout << EvenFibNumbers(4000000);
		default:
			break;
	}

	cout << "\n0 to quit";
	cin >> eulerSelection;
}