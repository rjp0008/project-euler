
#pragma region Solutions 1-10

int MultiplesOfThreeAndFiveSum(int upperLimit){
	int output = 0;
	for(int i = 0; i < upperLimit;i++){
		if(i%3 == 0 || i%5 == 0){
			output += i;
		}
	}
	return output;
}

int EvenFibNumbers(int upperLimit){
	int littleNumber = 1;
	int bigNumber = 2;
	int output = 0;
	while (bigNumber < upperLimit){
		if(bigNumber%2 == 0){
			output += bigNumber;
		}
		bigNumber = littleNumber + bigNumber;
		littleNumber = bigNumber - littleNumber;
	}
	return output;
}

#pragma endregion
