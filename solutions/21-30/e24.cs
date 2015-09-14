using System;
using System.Collections.Generic;

namespace PE
{
    class e24
    {
        static List<string> permutations = new List<string>();
        static string numbers = "0123456789";

        static void Main(string[] args)
        {
            permutations = perumationGenerator(numbers);
            permutations.Sort();
            Console.WriteLine(permutations[999999].ToString());
        }

        static List<string> perumationGenerator(string initial)
        {
            List<string> output = new List<string>();
            foreach (string jumbled in MakeJumble(initial))
            {
                output.Add(jumbled);
            }
            return output;
        }

        private static IEnumerable<string> MakeJumble(string initial)
        {
            List<string> output = new List<string>();
            if (initial.Length == 1)
            {
                output.Add(initial);
                return output;
            }
            for (int i = 0; i < initial.Length; i++)
            {
                string toJumble = initial.Remove(i, 1);
                foreach (string jumble in MakeJumble(toJumble))
                {
                    output.Add(initial[i] + jumble);
                }

            }
            return output;
        }
    }
}
