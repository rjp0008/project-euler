using System;
using System.Collections.Generic;

namespace PE
{
    class e23
    {
        static int GivenUpperLimit = 28123;

        static void Main(string[] args)
        {
            var abundantNumbers = MakeAbundantNumbersList();

            var canSum = CanSumIndexFromTwoAbundantNumbers(abundantNumbers);

            Console.WriteLine(SumFalseIndexes(canSum));
        }

        static bool IsAbundant(int number)
        {
            int sum = 0;
            for (int i = number / 2; i > 0; i--)
            {
                if (number % i == 0)
                {
                    sum += i;
                }
                if (sum > number)
                {
                    return true;
                }
            }

            if (sum > number)
            {
                return true;
            }
            return false;
        }

        static List<int> MakeAbundantNumbersList()
        {
            var list = new List<int>();
            for (int i = 0; i < GivenUpperLimit; i++)
            {
                if (IsAbundant(i))
                {
                    list.Add(i);
                }
            }
            return list;
        }

        static bool[] CanSumIndexFromTwoAbundantNumbers(List<int> abundantNumbers)
        {
            var sumList = new bool[GivenUpperLimit];

            foreach (int firstTerm in abundantNumbers)
            {
                foreach (int secondTerm in abundantNumbers)
                {
                    if (firstTerm + secondTerm >= GivenUpperLimit)
                    {
                        break;
                    }

                    sumList[firstTerm + secondTerm] = true;
                }
            }
            return sumList;
        }

        static int SumFalseIndexes(bool[] input)
        {
            int totalSum = 0;

            for (int i = 0; i < input.Length; i++)
            {
                if (!input[i])
                {
                    totalSum += i;
                }
            }
            return totalSum;
        }
    }
}
